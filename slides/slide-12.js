// slide-12.js — 科研选题生成器 + 侧边栏API配置展示 (ui_05 + ui_07)
const pptxgen = require("pptxgenjs");
const path = require("path");

function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.08, fill: { color: theme.accent } });

  slide.addText("科研选题 & 侧边栏配置 — 操作界面", {
    x: 0.5, y: 0.2, w: 9, h: 0.55,
    fontSize: 24, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });

  // 左图：科研选题生成器
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.3, y: 0.9, w: 4.6, h: 4.3, fill: { color: "f0f4f8" }, rectRadius: 0.08 });
  slide.addText("科研选题生成器", { x: 0.4, y: 0.9, w: 4.4, h: 0.32, fontSize: 11, fontFace: "Microsoft YaHei", color: "e76f51", bold: true, align: "center" });
  try {
    slide.addImage({ path: path.join(__dirname, "imgs/ui_07_topic.png"), x: 0.45, y: 1.28, w: 4.3, h: 3.8 });
  } catch(e) {}

  // 右图：API配置
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 5.1, y: 0.9, w: 4.6, h: 4.3, fill: { color: "f0f4f8" }, rectRadius: 0.08 });
  slide.addText("侧边栏 API 配置 + 知识库管理", { x: 5.2, y: 0.9, w: 4.4, h: 0.32, fontSize: 11, fontFace: "Microsoft YaHei", color: theme.secondary, bold: true, align: "center" });
  try {
    slide.addImage({ path: path.join(__dirname, "imgs/ui_05_api.png"), x: 5.25, y: 1.28, w: 4.3, h: 3.8 });
  } catch(e) {}

  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("12", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  return slide;
}
module.exports = { createSlide };
