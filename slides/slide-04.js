// slide-04.js — 眼底图像智能分析 (核心功能1)
const pptxgen = require("pptxgenjs");

function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.08, fill: { color: theme.accent } });

  // Title
  slide.addText("眼底图像智能分析 — 血管分割与病变识别", {
    x: 0.5, y: 0.3, w: 9, h: 0.7,
    fontSize: 26, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });

  // === Three column cards ===
  const cards = [
    { title: "1. 上传图像", desc: "支持 JPG/PNG/BMP/TIFF\n等 7 种常见格式\n自动校验图片完整性\n实时预览 + 元数据", color: theme.secondary, y: 1.3 },
    { title: "2. AI 分析", desc: "多尺度黑帽变换\nFrangi 血管增强滤波\nOtsu 自适应阈值\nMorphology 后处理", color: theme.primary, y: 1.3 },
    { title: "3. 结果呈现", desc: "血管分割掩码（绿标）\n血管叠加图\nDR 四级分级\n六维拓扑特征", color: "e76f51", y: 1.3 },
  ];

  cards.forEach((c, i) => {
    const x = 0.5 + i * 3.1;
    // Card background
    slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: c.y, w: 2.9, h: 2.7, fill: { color: "f8fcfe" }, shadow: { type: "outer", blur: 6, offset: 2, color: "000000", opacity: 0.08 } });
    // Top color stripe
    slide.addShape(pres.shapes.RECTANGLE, { x, y: c.y, w: 2.9, h: 0.06, fill: { color: c.color } });
    // Step number + title
    slide.addText(c.title, { x: x+0.15, y: c.y+0.15, w: 2.6, h: 0.45, fontSize: 15, fontFace: "Microsoft YaHei", color: c.color, bold: true });
    // Description
    slide.addText(c.desc, { x: x+0.15, y: c.y+0.7, w: 2.6, h: 1.8, fontSize: 11, fontFace: "Microsoft YaHei", color: "444444", lineSpacingMultiple: 1.5 });
  });

  // Bottom note
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 4.25, w: 9, h: 0.8, fill: { color: "fef3e0" }, rectRadius: 0.08 });
  slide.addText("演示模式：无需 GPU 或预训练权重，Frangi 滤波器自动切换，平台完全可用。加载 U-Net 权重后精度更高。", {
    x: 0.7, y: 4.25, w: 8.6, h: 0.8, fontSize: 11, fontFace: "Microsoft YaHei", color: "555555", valign: "middle"
  });

  // Page badge
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("4", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  return slide;
}

module.exports = { createSlide };
