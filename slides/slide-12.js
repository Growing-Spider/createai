// slide-12.js
const pptxgen = require("pptxgenjs");
function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.background = { color: theme.primary };
  slide.addShape(pres.shapes.OVAL, { x: -1.5, y: 3.5, w: 5, h: 5, fill: { color: theme.accent }, opacity: 0.06 });
  slide.addShape(pres.shapes.OVAL, { x: 7.5, y: -1.5, w: 4, h: 4, fill: { color: theme.secondary }, opacity: 0.05 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.1, h: 5.625, fill: { color: theme.accent } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 0.7, w: 2.2, h: 0.35, fill: { color: theme.accent }, opacity: 0.15 });
  slide.addText("创AI案例征集 · 智能信息系统", { x: 0.8, y: 0.7, w: 2.2, h: 0.35, fontSize: 11, fontFace: "Microsoft YaHei", color: theme.accent, align: "center", valign: "middle" });
  slide.addText("谢谢观看", { x: 0.8, y: 1.2, w: 8.5, h: 1.0, fontSize: 52, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "left", valign: "bottom" });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 2.3, w: 2.5, h: 0.04, fill: { color: theme.accent } });
  slide.addText("FundusAI-Edu · 眼底图像AI教学与科研辅助平台", { x: 0.8, y: 2.6, w: 8.5, h: 0.55, fontSize: 22, fontFace: "Microsoft YaHei", color: theme.secondary, align: "left" });
  slide.addText("案例类别: 智能信息系统  |  申报学段: 高等教育  |  适用: 高职高专/本科/硕士/博士", { x: 0.8, y: 3.4, w: 8.5, h: 0.35, fontSize: 13, fontFace: "Microsoft YaHei", color: "AAAAAA", align: "left" });
  slide.addText("配套资源: 完整代码 + 使用手册 + 安装手册 + 开发记录 + 演示视频", { x: 0.8, y: 3.85, w: 8.5, h: 0.35, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.accent, bold: true, align: "left" });
  slide.addText("借助生成式人工智能赋能开发,跨越自身专业与技能限制,体现终身学习", { x: 0.8, y: 4.4, w: 6.5, h: 0.4, fontSize: 12, fontFace: "Microsoft YaHei", color: "888888", italic: true, align: "left" });
  slide.addText("MIT开源许可  ·  支持复现验证  ·  2026年6月", { x: 0.8, y: 5.1, w: 5, h: 0.35, fontSize: 11, fontFace: "Microsoft YaHei", color: "667788", align: "left" });
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.accent } });
  slide.addText("12", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "0B1D3A", bold: true, align: "center", valign: "middle" });
  return slide;
}
module.exports = { createSlide };