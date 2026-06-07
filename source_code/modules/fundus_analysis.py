# =============================================================
# fundus_analysis.py — 眼底图像智能分析模块
# 功能：图像预处理、U-Net血管分割、病变识别、特征提取
# =============================================================

import cv2
import numpy as np
from PIL import Image
from pathlib import Path
import torch
import torch.nn as nn
import torch.nn.functional as F
from scipy import ndimage
from skimage import morphology, measure, filters
import logging
import sys
import os

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import UNET_MODEL_PATH, MODEL_INPUT_SIZE, VESSEL_THRESHOLD, USE_GPU

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────
# U-Net 模型定义
# ─────────────────────────────────────────────────────────────

class DoubleConv(nn.Module):
    """U-Net 双卷积块"""
    def __init__(self, in_channels, out_channels, mid_channels=None):
        super().__init__()
        mid_channels = mid_channels or out_channels
        self.double_conv = nn.Sequential(
            nn.Conv2d(in_channels, mid_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(mid_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(mid_channels, out_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
        )

    def forward(self, x):
        return self.double_conv(x)


class Down(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.maxpool_conv = nn.Sequential(
            nn.MaxPool2d(2),
            DoubleConv(in_channels, out_channels),
        )

    def forward(self, x):
        return self.maxpool_conv(x)


class Up(nn.Module):
    def __init__(self, in_channels, out_channels, bilinear=True):
        super().__init__()
        if bilinear:
            self.up = nn.Upsample(scale_factor=2, mode="bilinear", align_corners=True)
            self.conv = DoubleConv(in_channels, out_channels, in_channels // 2)
        else:
            self.up = nn.ConvTranspose2d(in_channels, in_channels // 2, kernel_size=2, stride=2)
            self.conv = DoubleConv(in_channels, out_channels)

    def forward(self, x1, x2):
        x1 = self.up(x1)
        diff_y = x2.size(2) - x1.size(2)
        diff_x = x2.size(3) - x1.size(3)
        x1 = F.pad(x1, [diff_x // 2, diff_x - diff_x // 2,
                        diff_y // 2, diff_y - diff_y // 2])
        x = torch.cat([x2, x1], dim=1)
        return self.conv(x)


class OutConv(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=1)

    def forward(self, x):
        return self.conv(x)


class UNet(nn.Module):
    """标准 U-Net，用于视网膜血管分割"""
    def __init__(self, n_channels=3, n_classes=1, bilinear=True):
        super().__init__()
        self.n_channels = n_channels
        self.n_classes = n_classes
        self.bilinear = bilinear
        factor = 2 if bilinear else 1

        self.inc   = DoubleConv(n_channels, 64)
        self.down1 = Down(64, 128)
        self.down2 = Down(128, 256)
        self.down3 = Down(256, 512)
        self.down4 = Down(512, 1024 // factor)
        self.up1   = Up(1024, 512 // factor, bilinear)
        self.up2   = Up(512, 256 // factor, bilinear)
        self.up3   = Up(256, 128 // factor, bilinear)
        self.up4   = Up(128, 64, bilinear)
        self.outc  = OutConv(64, n_classes)

    def forward(self, x):
        x1 = self.inc(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
        x  = self.up1(x5, x4)
        x  = self.up2(x, x3)
        x  = self.up3(x, x2)
        x  = self.up4(x, x1)
        return self.outc(x)


# ─────────────────────────────────────────────────────────────
# 图像分析器
# ─────────────────────────────────────────────────────────────

class FundusAnalyzer:
    """眼底图像智能分析器"""

    def __init__(self):
        self.device = torch.device(
            "cuda" if USE_GPU and torch.cuda.is_available() else "cpu"
        )
        self.model = None
        self._load_model()

    def _load_model(self):
        """加载 U-Net 模型（若权重文件不存在则使用随机权重演示）"""
        try:
            self.model = UNet(n_channels=3, n_classes=1).to(self.device)
            if Path(UNET_MODEL_PATH).exists():
                state_dict = torch.load(UNET_MODEL_PATH, map_location=self.device)
                self.model.load_state_dict(state_dict)
                logger.info("[OK] U-Net 模型加载成功")
            else:
                logger.warning("[WARN] 未找到预训练权重，使用随机权重（演示模式）")
            self.model.eval()
        except Exception as e:
            logger.error(f"模型加载失败：{e}")
            self.model = None

    # ── 图像预处理 ───────────────────────────────────────────

    def preprocess_image(self, image: np.ndarray) -> np.ndarray:
        """图像预处理：调整尺寸 + CLAHE 增强 + 归一化"""
        img = cv2.resize(image, MODEL_INPUT_SIZE)
        # 绿通道对视网膜血管对比度最优
        if img.ndim == 3:
            green = img[:, :, 1]
        else:
            green = img
        # CLAHE 对比度限制自适应直方图均衡化
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(green)
        # 转回 RGB（重复三通道）
        enhanced_rgb = cv2.merge([enhanced, enhanced, enhanced])
        normalized = enhanced_rgb.astype(np.float32) / 255.0
        return normalized

    def preprocess_tensor(self, image: np.ndarray) -> torch.Tensor:
        """转换为 PyTorch Tensor"""
        preprocessed = self.preprocess_image(image)
        tensor = torch.from_numpy(preprocessed).permute(2, 0, 1).unsqueeze(0)
        return tensor.to(self.device)

    # ── 血管分割 ─────────────────────────────────────────────

    def segment_vessels(self, image: np.ndarray) -> np.ndarray:
        """使用 U-Net 进行视网膜血管分割，返回与输入同尺寸的二值掩码"""
        if self.model is None:
            return self._demo_segment(image)

        original_size = (image.shape[1], image.shape[0])  # (w, h)

        with torch.no_grad():
            tensor = self.preprocess_tensor(image)
            output = self.model(tensor)
            prob_map = torch.sigmoid(output).squeeze().cpu().numpy()

        # 二值化
        binary_mask = (prob_map > VESSEL_THRESHOLD).astype(np.uint8) * 255
        # 形态学后处理：去除噪声
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        cleaned = cv2.morphologyEx(binary_mask, cv2.MORPH_OPEN, kernel)
        cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernel)
        # 缩放回原始尺寸
        cleaned = cv2.resize(cleaned, original_size)
        return cleaned

    def _demo_segment(self, image: np.ndarray) -> np.ndarray:
        """演示模式：多尺度血管增强 + 自适应阈值"""
        import traceback
        original_size = (image.shape[1], image.shape[0])

        if image.ndim == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image

        # 缩小加速
        resized = cv2.resize(gray, MODEL_INPUT_SIZE)
        h, w = resized.shape

        # 1) CLAHE 增强
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(resized)

        # 2) 多尺度形态学黑帽
        results = []
        for ksize in [7, 15, 31]:
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ksize, ksize))
            bh = cv2.morphologyEx(enhanced, cv2.MORPH_BLACKHAT, kernel)
            bh_norm = bh.astype(np.float32) / 255.0
            results.append(bh_norm)

        # 3) Frangi 辅助
        try:
            norm = enhanced.astype(np.float32) / 255.0
            inv = 1.0 - norm
            f = filters.frangi(inv, sigmas=range(1, 5), black_ridges=False)
            fn = (f - f.min()) / (f.max() - f.min() + 1e-8)
            results.append(fn)
        except Exception:
            pass

        # 加权融合
        combined = np.zeros_like(results[0])
        for r in results:
            combined += r
        combined /= len(results)

        # 4) 全局百分位阈值
        combined_flat = combined.flatten()
        nonzero = combined_flat[combined_flat > combined_flat.mean() * 0.5]
        if len(nonzero) == 0:
            nonzero = combined_flat

        p90 = np.percentile(nonzero, 90)
        p50 = np.percentile(nonzero, 50)

        # 保守阈值：取 50% 和 90% 分位数之间的安全点
        threshold = p50 + 0.30 * (p90 - p50)

        binary = (combined > threshold).astype(np.uint8) * 255

        # 5) 形态学清理
        kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
        binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel3)
        binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel3)

        # 6) 显著性检查 — 确保检测到合理比例的血管
        vr = np.count_nonzero(binary) / binary.size
        if vr < 0.005:
            # 太少了，逐步降阈值
            for factor in [0.20, 0.12, 0.06, 0.03]:
                t2 = p50 + factor * (p90 - p50)
                b2 = (combined > t2).astype(np.uint8) * 255
                vr2 = np.count_nonzero(b2) / b2.size
                if 0.005 <= vr2 <= 0.50:
                    binary = b2
                    break
                if factor == 0.03:
                    binary = b2  # 最后兜底
        elif vr > 0.45:
            t3 = p50 + 0.50 * (p90 - p50)
            binary = (combined > t3).astype(np.uint8) * 255

        # 最终清理
        binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel3)

        # 缩放回原始尺寸
        result = cv2.resize(binary, original_size)
        return result

    # ── 病变识别 ─────────────────────────────────────────────

    def detect_lesions(self, image: np.ndarray) -> dict:
        """
        眼底病变识别（规则 + 色彩特征分析）
        返回：病变类型及置信度
        """
        if image.ndim != 3:
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        img_rgb = cv2.resize(image, MODEL_INPUT_SIZE)
        results = {}

        # 1. 视盘区域检测（亮区）
        gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        _, bright_mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        bright_ratio = bright_mask.sum() / (255 * bright_mask.size)
        results["optic_disc_detected"] = bright_ratio > 0.005

        # 2. 出血点 / 微动脉瘤（暗红色区域）
        img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
        red_mask1 = cv2.inRange(img_hsv, np.array([0, 50, 30]), np.array([10, 255, 200]))
        red_mask2 = cv2.inRange(img_hsv, np.array([160, 50, 30]), np.array([180, 255, 200]))
        hemorrhage_mask = red_mask1 | red_mask2
        hemorrhage_ratio = hemorrhage_mask.sum() / (255 * hemorrhage_mask.size)
        results["hemorrhage_risk"] = min(hemorrhage_ratio * 50, 1.0)

        # 3. 硬性渗出（黄白色亮区）
        yellow_mask = cv2.inRange(img_hsv, np.array([15, 30, 150]), np.array([40, 255, 255]))
        exudate_ratio = yellow_mask.sum() / (255 * yellow_mask.size)
        results["hard_exudate_risk"] = min(exudate_ratio * 30, 1.0)

        # 4. 整体 DR 风险评估
        dr_score = (results["hemorrhage_risk"] * 0.6 + results["hard_exudate_risk"] * 0.4)
        if dr_score < 0.1:
            results["dr_grade"] = "No DR"
            results["dr_confidence"] = 0.85
        elif dr_score < 0.3:
            results["dr_grade"] = "Mild DR"
            results["dr_confidence"] = 0.70
        elif dr_score < 0.6:
            results["dr_grade"] = "Moderate DR"
            results["dr_confidence"] = 0.65
        else:
            results["dr_grade"] = "Severe DR"
            results["dr_confidence"] = 0.60

        results["overall_quality"] = self._assess_image_quality(gray)
        return results

    def _assess_image_quality(self, gray_image: np.ndarray) -> str:
        """评估图像质量"""
        laplacian_var = cv2.Laplacian(gray_image, cv2.CV_64F).var()
        mean_brightness = gray_image.mean()
        if laplacian_var > 100 and 50 < mean_brightness < 200:
            return "优"
        elif laplacian_var > 50 and 30 < mean_brightness < 220:
            return "良"
        else:
            return "差"

    # ── 可视化 ───────────────────────────────────────────────

    def overlay_vessels(self, original: np.ndarray, mask: np.ndarray) -> np.ndarray:
        """将血管分割结果叠加到原图（绿色标注血管）"""
        if original.ndim == 2:
            overlay = cv2.cvtColor(original, cv2.COLOR_GRAY2RGB)
        else:
            overlay = original.copy()

        # 将 mask 缩放到与 original 相同尺寸
        if mask.shape[:2] != overlay.shape[:2]:
            mask = cv2.resize(mask, (overlay.shape[1], overlay.shape[0]))

        # 二值化掩码确保只有血管区域
        binary_mask = (mask > 127).astype(np.uint8)

        # 只在血管位置标注绿色
        vessel_colored = np.zeros_like(overlay)
        vessel_colored[:, :, 1] = binary_mask * 255  # 绿通道只在血管处激活
        result = cv2.addWeighted(overlay, 0.7, vessel_colored, 0.3, 0)
        return result

    def generate_analysis_report(self, image: np.ndarray) -> dict:
        """生成完整分析报告"""
        vessel_mask = self.segment_vessels(image)
        lesion_info = self.detect_lesions(image)

        return {
            "vessel_mask": vessel_mask,
            "lesion_info": lesion_info,
            "overlay_image": self.overlay_vessels(image, vessel_mask),
            "image_size": image.shape[:2],
        }
