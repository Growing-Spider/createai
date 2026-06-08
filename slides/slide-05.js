// slide-05.js
const pptxgen = require("pptxgenjs");
function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fill: { color: theme.accent } });
  slide.addText("实现功能 · 核心功能演示", { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "0B1D3A", bold: true, align: "center", valign: "middle" });

  slide.addText("眼底图像智能分析", { x: 0.5, y: 0.85, w: 9, h: 0.6, fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });

  slide.addText("上传眼底照片,AI自动完成血管分割,病变识别与拓扑特征提取", { x: 0.5, y: 1.4, w: 9, h: 0.35, fontSize: 13, fontFace: "Microsoft YaHei", color: "666666" });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.9, w: 2.9, h: 1.0, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.9, w: 0.06, h: 1.0, fill: { color: theme.accent } });
  slide.addText("🩸 血管分割", { x: 0.7, y: 1.93, w: 2.5, h: 0.35, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });
  slide.addText("U-Net深度学习+多尺度\nFrangi增强,精准提取", { x: 0.7, y: 2.28, w: 2.5, h: 0.55, fontSize: 10.5, fontFace: "Microsoft YaHei", color: "555555", lineSpacingMultiple: 1.3 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 3.6, y: 1.9, w: 2.9, h: 1.0, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 3.6, y: 1.9, w: 0.06, h: 1.0, fill: { color: theme.accent } });
  slide.addText("🔎 病变识别", { x: 3.8000000000000003, y: 1.93, w: 2.5, h: 0.35, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });
  slide.addText("HSV色彩空间规则引擎\nDR四等级自动分级", { x: 3.8000000000000003, y: 2.28, w: 2.5, h: 0.55, fontSize: 10.5, fontFace: "Microsoft YaHei", color: "555555", lineSpacingMultiple: 1.3 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 6.7, y: 1.9, w: 2.9, h: 1.0, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 6.7, y: 1.9, w: 0.06, h: 1.0, fill: { color: theme.accent } });
  slide.addText("🌐 拓扑分析", { x: 6.9, y: 1.93, w: 2.5, h: 0.35, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });
  slide.addText("六维特征:密度/分叉/\n迂曲度/分形维数", { x: 6.9, y: 2.28, w: 2.5, h: 0.55, fontSize: 10.5, fontFace: "Microsoft YaHei", color: "555555", lineSpacingMultiple: 1.3 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 3.1, w: 5.6, h: 2.2, fill: { color: theme.light } });
  slide.addImage({ path: "imgs/ui_01_upload.png", x: 0.55, y: 3.15, w: 5.5, h: 2.1 });
  slide.addText("▲ 支持JPG/PNG/BMP/TIFF, 左侧上传>>右侧三标签结果切换", { x: 0.5, y: 5.3, w: 5.6, h: 0.2, fontSize: 9, fontFace: "Microsoft YaHei", color: "AAAAAA", italic: true });
  slide.addShape(pres.shapes.RECTANGLE, { x: 6.3, y: 3.1, w: 3.2, h: 2.2, fill: { color: theme.primary } });
  slide.addText("应用流程", { x: 6.5, y: 3.2, w: 2.8, h: 0.35, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.accent, bold: true });
  slide.addText("1. 上传眼底图像", { x: 6.5, y: 3.6, w: 2.8, h: 0.35, fontSize: 11, fontFace: "Microsoft YaHei", color: "FFFFFF", valign: "middle" });
  slide.addText("2. 点击[开始分析]", { x: 6.5, y: 4.0200000000000005, w: 2.8, h: 0.35, fontSize: 11, fontFace: "Microsoft YaHei", color: "FFFFFF", valign: "middle" });
  slide.addText("3. 查看血管分割掩码", { x: 6.5, y: 4.44, w: 2.8, h: 0.35, fontSize: 11, fontFace: "Microsoft YaHei", color: "FFFFFF", valign: "middle" });
  slide.addText("4. 查看DR分级结果", { x: 6.5, y: 4.86, w: 2.8, h: 0.35, fontSize: 11, fontFace: "Microsoft YaHei", color: "FFFFFF", valign: "middle" });
  slide.addText("5. 查看六维拓扑特征", { x: 6.5, y: 5.28, w: 2.8, h: 0.35, fontSize: 11, fontFace: "Microsoft YaHei", color: "FFFFFF", valign: "middle" });
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("5", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  return slide;
}
module.exports = { createSlide };
