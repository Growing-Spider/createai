// slide-03.js — Section Divider: 实现功能 (Part 2 intro)
const pptxgen = require("pptxgenjs");

function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.primary };

  // Large decorative circle
  slide.addShape(pres.shapes.OVAL, { x: 6.5, y: -1.5, w: 5, h: 5, fill: { color: theme.accent }, opacity: 0.08 });
  slide.addShape(pres.shapes.OVAL, { x: -1, y: 3, w: 4, h: 4, fill: { color: theme.secondary }, opacity: 0.08 });

  slide.addText("PART 02", { x: 0.8, y: 1.2, w: 3, h: 0.6, fontSize: 18, fontFace: "Arial", color: theme.accent, bold: true, letterSpacing: 8 });
  slide.addText("实现功能", { x: 0.8, y: 1.8, w: 8, h: 1.5, fontSize: 48, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 3.3, w: 2, h: 0.06, fill: { color: theme.accent } });
  slide.addText("六大功能模块 · 从图像分析到科研全流程覆盖", { x: 0.8, y: 3.6, w: 8, h: 0.5, fontSize: 16, fontFace: "Microsoft YaHei", color: "8ecae6" });

  // Page badge
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.accent } });
  slide.addText("3", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  return slide;
}

module.exports = { createSlide };
