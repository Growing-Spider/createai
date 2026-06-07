# =============================================================
# topology_analysis.py — 血管拓扑特征分析模块
# 功能：骨架提取、拓扑图构建、六大特征自动计算
# =============================================================

import cv2
import numpy as np
import networkx as nx
from skimage import morphology, measure
from scipy import ndimage
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import io
from PIL import Image
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

logger = logging.getLogger(__name__)


class TopologyAnalyzer:
    """视网膜血管拓扑特征分析器"""

    def __init__(self):
        self.graph = None
        self.skeleton = None

    # ─────────────────────────────────────────────────────────
    # 骨架提取
    # ─────────────────────────────────────────────────────────

    def extract_skeleton(self, vessel_mask: np.ndarray) -> np.ndarray:
        """对血管二值掩码进行骨架化"""
        binary = (vessel_mask > 127).astype(np.uint8)
        # 去除小噪声连通域
        labeled = measure.label(binary)
        props = measure.regionprops(labeled)
        clean = np.zeros_like(binary)
        for prop in props:
            if prop.area > 50:
                clean[labeled == prop.label] = 1
        # Lee 骨架算法
        skeleton = morphology.skeletonize(clean.astype(bool)).astype(np.uint8)
        self.skeleton = skeleton
        return skeleton

    # ─────────────────────────────────────────────────────────
    # 构建拓扑图
    # ─────────────────────────────────────────────────────────

    def build_topology_graph(self, skeleton: np.ndarray) -> nx.Graph:
        """从骨架图像构建 NetworkX 拓扑图"""
        G = nx.Graph()
        height, width = skeleton.shape

        # 8-连通邻域偏移
        neighbors_8 = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        # 找到所有骨架像素
        skeleton_points = np.argwhere(skeleton > 0)

        # 添加节点
        for y, x in skeleton_points:
            G.add_node((y, x))

        # 添加边（相邻骨架像素之间）
        for y, x in skeleton_points:
            for dy, dx in neighbors_8:
                ny, nx_ = y + dy, x + dx
                if 0 <= ny < height and 0 <= nx_ < width:
                    if skeleton[ny, nx_] > 0:
                        dist = np.sqrt(dy**2 + dx**2)
                        G.add_edge((y, x), (ny, nx_), weight=dist)

        self.graph = G
        return G

    # ─────────────────────────────────────────────────────────
    # 特征计算
    # ─────────────────────────────────────────────────────────

    def compute_vessel_density(self, vessel_mask: np.ndarray) -> float:
        """血管密度：血管像素占比"""
        total = vessel_mask.size
        vessel_pixels = np.sum(vessel_mask > 127)
        return float(vessel_pixels / total)

    def compute_bifurcation_endpoints(self, skeleton: np.ndarray) -> tuple:
        """
        计算分叉点和终末点数量
        返回：(bifurcation_count, endpoint_count)
        """
        bifurcations = 0
        endpoints = 0
        height, width = skeleton.shape
        neighbors_8 = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                if skeleton[y, x] > 0:
                    count = sum(
                        1 for dy, dx in neighbors_8
                        if skeleton[y+dy, x+dx] > 0
                    )
                    if count == 1:
                        endpoints += 1
                    elif count >= 3:
                        bifurcations += 1

        return bifurcations, endpoints

    def compute_average_vessel_width(self, vessel_mask: np.ndarray,
                                     skeleton: np.ndarray) -> float:
        """
        平均血管宽度：通过距离变换估算
        单位：像素
        """
        binary = (vessel_mask > 127).astype(np.uint8)
        dist_map = ndimage.distance_transform_edt(binary)
        skeleton_dist = dist_map[skeleton > 0]
        if len(skeleton_dist) == 0:
            return 0.0
        # 血管宽度 = 骨架处距离 * 2
        avg_width = float(np.mean(skeleton_dist) * 2)
        return round(avg_width, 2)

    def compute_tortuosity(self, skeleton: np.ndarray) -> float:
        """
        血管迂曲度：实际路径长度 / 端点直线距离
        值越大表示血管越弯曲
        """
        G = self.graph or self.build_topology_graph(skeleton)
        tortuosity_values = []

        # 找终末点（度为1的节点）
        endpoints = [n for n in G.nodes() if G.degree(n) == 1]

        if len(endpoints) < 2:
            return 1.0

        # 对终末点对之间的路径计算迂曲度
        sampled_endpoints = endpoints[:min(50, len(endpoints))]
        for i in range(len(sampled_endpoints) - 1):
            ep1 = sampled_endpoints[i]
            ep2 = sampled_endpoints[i + 1]
            try:
                path = nx.shortest_path(G, ep1, ep2)
                if len(path) < 2:
                    continue
                # 实际路径长度（像素步数）
                actual_length = len(path) - 1
                # 端点间欧式距离
                straight_dist = np.sqrt(
                    (ep1[0]-ep2[0])**2 + (ep1[1]-ep2[1])**2
                )
                if straight_dist > 5:
                    tort = actual_length / straight_dist
                    tortuosity_values.append(tort)
            except nx.NetworkXNoPath:
                continue

        return round(float(np.mean(tortuosity_values)) if tortuosity_values else 1.0, 3)

    def compute_fractal_dimension(self, vessel_mask: np.ndarray) -> float:
        """
        分形维数（盒计数法）
        反映血管网络的复杂度
        """
        binary = (vessel_mask > 127).astype(np.uint8)
        # 调整为正方形（2的幂次）
        min_dim = min(binary.shape)
        size = 2 ** int(np.log2(min_dim))
        img = cv2.resize(binary, (size, size))

        counts = []
        sizes = []
        box_size = 2
        while box_size <= size // 2:
            count = 0
            for i in range(0, size, box_size):
                for j in range(0, size, box_size):
                    block = img[i:i+box_size, j:j+box_size]
                    if block.sum() > 0:
                        count += 1
            counts.append(count)
            sizes.append(box_size)
            box_size *= 2

        # 线性拟合 log(count) ~ log(1/size)
        if len(counts) < 2:
            return 1.5
        log_sizes  = np.log(1.0 / np.array(sizes,  dtype=float))
        log_counts = np.log(np.array(counts, dtype=float) + 1e-8)
        coeffs = np.polyfit(log_sizes, log_counts, 1)
        fd = abs(coeffs[0])
        return round(min(fd, 2.0), 3)

    # ─────────────────────────────────────────────────────────
    # 综合特征提取
    # ─────────────────────────────────────────────────────────

    def extract_all_features(self, vessel_mask: np.ndarray) -> dict:
        """提取全部六大拓扑特征"""
        skeleton = self.extract_skeleton(vessel_mask)
        bifurcations, endpoints = self.compute_bifurcation_endpoints(skeleton)

        features = {
            "vessel_density":     round(self.compute_vessel_density(vessel_mask), 4),
            "bifurcation_count":  bifurcations,
            "endpoint_count":     endpoints,
            "avg_vessel_width":   self.compute_average_vessel_width(vessel_mask, skeleton),
            "tortuosity":         self.compute_tortuosity(skeleton),
            "fractal_dimension":  self.compute_fractal_dimension(vessel_mask),
        }
        return features

    # ─────────────────────────────────────────────────────────
    # 可视化
    # ─────────────────────────────────────────────────────────

    def visualize_skeleton(self, original: np.ndarray,
                           vessel_mask: np.ndarray,
                           skeleton: np.ndarray) -> Image.Image:
        """生成骨架可视化图像（三连图：原图 / 血管叠加 / 骨架叠加）"""
        target_size = (vessel_mask.shape[1], vessel_mask.shape[0])
        if original.shape[:2] != (target_size[1], target_size[0]):
            base = cv2.resize(original, target_size)
        else:
            base = original
        if base.ndim == 2:
            base = cv2.cvtColor(base, cv2.COLOR_GRAY2RGB)

        # 面板1：原始图像
        panel1 = base.copy()

        # 面板2：原图 + 绿色血管标注
        panel2 = base.copy()
        bin_mask = (vessel_mask > 127)
        if np.any(bin_mask):
            panel2[bin_mask, 1] = np.clip(base[bin_mask, 1].astype(int) + 180, 0, 255).astype(np.uint8)
            panel2[bin_mask, 0] = (base[bin_mask, 0] * 0.3).astype(np.uint8)

        # 面板3：原图 + 红色骨架标注
        panel3 = base.copy()
        if skeleton is not None and np.any(skeleton):
            selem = morphology.disk(1)
            skel_dilated = morphology.binary_dilation(skeleton.astype(bool), selem)
            panel3[skel_dilated, 0] = 255
            panel3[skel_dilated, 1] = (panel3[skel_dilated, 1] * 0.3).astype(np.uint8)
            panel3[skel_dilated, 2] = (panel3[skel_dilated, 2] * 0.3).astype(np.uint8)

        fig, axes = plt.subplots(1, 3, figsize=(15, 5), facecolor="#0d1117")
        titles = ["原始图像", "血管分割（绿）", "骨架图（红）"]
        images = [panel1, panel2, panel3]

        for ax, img, title in zip(axes, images, titles):
            ax.imshow(img)
            ax.set_title(title, color="white", fontsize=12, fontproperties=_get_font())
            ax.axis("off")

        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format="png", dpi=100, bbox_inches="tight",
                    facecolor="#0d1117")
        plt.close(fig)
        buf.seek(0)
        return Image.open(buf)

    def visualize_features_chart(self, features: dict) -> Image.Image:
        """生成特征雷达图"""
        labels = ["血管密度", "分叉点", "终末点", "平均宽度", "迂曲度", "分形维数"]
        values = [
            features["vessel_density"] * 100,
            min(features["bifurcation_count"] / 500, 1.0) * 100,
            min(features["endpoint_count"] / 1000, 1.0) * 100,
            min(features["avg_vessel_width"] / 20, 1.0) * 100,
            min(features["tortuosity"] / 2.0, 1.0) * 100,
            features["fractal_dimension"] / 2.0 * 100,
        ]

        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
        angles += angles[:1]
        values_plot = values + values[:1]

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"polar": True},
                               facecolor="#0d1117")
        ax.set_facecolor("#161b22")
        ax.plot(angles, values_plot, color="#58a6ff", linewidth=2)
        ax.fill(angles, values_plot, color="#58a6ff", alpha=0.25)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels, color="white", fontsize=10,
                           fontproperties=_get_font())
        ax.set_ylim(0, 100)
        ax.tick_params(colors="white")
        ax.spines["polar"].set_color("#30363d")
        ax.grid(color="#30363d")
        ax.set_title("血管特征雷达图", color="white", pad=20, fontsize=14,
                     fontproperties=_get_font())

        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format="png", dpi=100, bbox_inches="tight",
                    facecolor="#0d1117")
        plt.close(fig)
        buf.seek(0)
        return Image.open(buf)

    def generate_topology_report(self, vessel_mask: np.ndarray,
                                 original_image: np.ndarray) -> dict:
        """生成完整拓扑分析报告"""
        features = self.extract_all_features(vessel_mask)
        skeleton  = self.skeleton

        skeleton_viz = self.visualize_skeleton(original_image, vessel_mask, skeleton)
        radar_chart  = self.visualize_features_chart(features)

        interpretation = self._interpret_features(features)

        return {
            "features":         features,
            "skeleton":         skeleton,
            "skeleton_viz":     skeleton_viz,
            "radar_chart":      radar_chart,
            "interpretation":   interpretation,
        }

    def _interpret_features(self, features: dict) -> dict:
        """特征解读：给出临床意义说明"""
        interpretation = {}

        vd = features["vessel_density"]
        if vd < 0.05:
            interpretation["vessel_density"] = "血管密度偏低，可能存在血管稀疏，需关注缺血性疾病。"
        elif vd < 0.15:
            interpretation["vessel_density"] = "血管密度正常范围，视网膜血管分布良好。"
        else:
            interpretation["vessel_density"] = "血管密度较高，需结合临床综合评估。"

        bc = features["bifurcation_count"]
        if bc < 50:
            interpretation["bifurcation"] = "分叉点偏少，可能图像质量不佳或血管稀疏。"
        elif bc < 300:
            interpretation["bifurcation"] = "分叉点数量正常，血管网络完整。"
        else:
            interpretation["bifurcation"] = "分叉点丰富，血管网络复杂度较高。"

        tort = features["tortuosity"]
        if tort < 1.1:
            interpretation["tortuosity"] = "血管形态规则，迂曲度正常。"
        elif tort < 1.5:
            interpretation["tortuosity"] = "血管存在轻度迂曲，建议结合病史分析。"
        else:
            interpretation["tortuosity"] = "血管迂曲度明显增高，可能与高血压、糖尿病等相关。"

        fd = features["fractal_dimension"]
        if fd < 1.4:
            interpretation["fractal"] = "分形维数偏低，血管网络简单，可能存在退行性变化。"
        elif fd < 1.7:
            interpretation["fractal"] = "分形维数正常，血管网络自相似性良好。"
        else:
            interpretation["fractal"] = "分形维数较高，血管网络结构复杂。"

        return interpretation


# ─────────────────────────────────────────────────────────────
# 辅助：中文字体
# ─────────────────────────────────────────────────────────────

def _get_font():
    """获取系统中文字体（matplotlib）"""
    import matplotlib.font_manager as fm
    try:
        font_paths = [
            "C:/Windows/Fonts/simhei.ttf",
            "C:/Windows/Fonts/msyh.ttc",
            "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
        ]
        for fp in font_paths:
            if Path(fp).exists():
                return fm.FontProperties(fname=fp)
    except Exception:
        pass
    return fm.FontProperties()
