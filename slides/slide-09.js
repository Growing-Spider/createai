// slide-09.js — Summary / Thank You
const pptxgen = require("pptxgenjs");

function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.primary };

  // Large decorative circles
  slide.addShape(pres.shapes.OVAL, { x: -1, y: 3, w: 4, h: 4, fill: { color: theme.accent }, opacity: 0.05 });
  slide.addShape(pres.shapes.OVAL, { x: 7, y: -1.5, w: 4, h: 4, fill: { color: theme.accent }, opacity: 0.05 });

  slide.addText("谢谢观看", {
    x: 0, y: 1.5, w: 10, h: 1.2,
    fontSize: 52, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center"
  });

  slide.addShape(pres.shapes.RECTANGLE, { x: 4, y: 2.8, w: 2, h: 0.06, fill: { color: theme.accent } });

  slide.addText("FundusAI-Edu — 眼底图像AI教学与科研辅助平台\n让医学AI触手可及", {
    x: 0, y: 3.1, w: 10, h: 1,
    fontSize: 16, fontFace: "Microsoft YaHei", color: "8ecae6", align: "center", lineSpacingMultiple: 1.6
  });

  slide.addText("2026年6月  |  FundusAI-Edu v1.0", {
    x: 0, y: 4.8, w: 10, h: 0.4,
    fontSize: 12, fontFace: "Microsoft YaHei", color: "557585", align: "center"
  });

  return slide;
}

module.exports = { createSlide };
