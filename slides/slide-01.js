// slide-01.js
const pptxgen = require("pptxgenjs");
function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.background = { color: theme.primary };
  slide.addShape(pres.shapes.OVAL, { x: -1.5, y: -1.5, w: 5, h: 5, fill: { color: theme.accent }, opacity: 0.08 });
  slide.addShape(pres.shapes.OVAL, { x: 8.2, y: 2.8, w: 3.5, h: 3.5, fill: { color: theme.accent }, opacity: 0.06 });
  slide.addShape(pres.shapes.OVAL, { x: 7.5, y: -1, w: 4, h: 4, fill: { color: theme.secondary }, opacity: 0.05 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.1, h: 5.625, fill: { color: theme.accent } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 0.4, w: 2, h: 0.03, fill: { color: theme.accent } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 0.7, w: 3.2, h: 0.35, fill: { color: theme.accent }, opacity: 0.15 });
  slide.addText("创AI案例征集 · 智能信息系统", { x: 0.8, y: 0.7, w: 3.2, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: theme.accent, align: "center", valign: "middle" });
  slide.addText("FundusAI-Edu", { x: 0.8, y: 1.4, w: 8.5, h: 1.4, fontSize: 56, fontFace: "Arial", color: "FFFFFF", bold: true, align: "left", valign: "bottom" });
  slide.addText("眼底图像 AI 教学与科研辅助平台", { x: 0.8, y: 2.8, w: 8.5, h: 0.7, fontSize: 26, fontFace: "Microsoft YaHei", color: "FFFFFF", align: "left", valign: "top" });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 3.6, w: 2.5, h: 0.04, fill: { color: theme.accent } });
  slide.addText("第一部分：案例概述 · 应用场景与核心问题", { x: 0.8, y: 3.9, w: 6.5, h: 0.6, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.secondary, align: "left" });
  slide.addText("2026年6月  |  申报学段: 高等教育  |  案例类别: 智能信息系统", { x: 0.8, y: 5.1, w: 5, h: 0.35, fontSize: 11, fontFace: "Microsoft YaHei", color: "8899AA", align: "left" });
  return slide;
}
module.exports = { createSlide };
