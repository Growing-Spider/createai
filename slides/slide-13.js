// slide-13.js — 学习分析展示 (ui_06)
const pptxgen = require("pptxgenjs");
const path = require("path");

function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.primary };

  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.08, fill: { color: theme.accent } });

  slide.addText("学习分析 — 个人画像", {
    x: 0.5, y: 0.2, w: 9, h: 0.55,
    fontSize: 24, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true
  });

  // 全宽展示
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 0.9, w: 9, h: 4.3, fill: { color: "0a2e4a" }, rectRadius: 0.08 });
  try {
    slide.addImage({ path: path.join(__dirname, "imgs/ui_06_learning.png"), x: 0.65, y: 1.05, w: 8.7, h: 4.0 });
  } catch(e) {}

  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.accent } });
  slide.addText("13", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  return slide;
}
module.exports = { createSlide };
