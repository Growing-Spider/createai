// slide-10.js — 眼底图像分析操作界面展示 (ui_01 + ui_02)
const pptxgen = require("pptxgenjs");
const path = require("path");

function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.08, fill: { color: theme.accent } });

  slide.addText("眼底图像分析 — 操作界面", {
    x: 0.5, y: 0.2, w: 9, h: 0.55,
    fontSize: 24, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });

  // 左图：上传 + 图像预览
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.3, y: 0.9, w: 4.6, h: 4.3, fill: { color: "f0f4f8" }, rectRadius: 0.08 });
  slide.addText("图像上传与预览", { x: 0.4, y: 0.9, w: 4.4, h: 0.32, fontSize: 11, fontFace: "Microsoft YaHei", color: theme.secondary, bold: true, align: "center" });
  try {
    slide.addImage({ path: path.join(__dirname, "imgs/ui_01_upload.png"), x: 0.45, y: 1.28, w: 4.3, h: 3.8 });
  } catch(e) {}

  // 右图：病变识别结果
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 5.1, y: 0.9, w: 4.6, h: 4.3, fill: { color: "f0f4f8" }, rectRadius: 0.08 });
  slide.addText("病变识别与DR分级", { x: 5.2, y: 0.9, w: 4.4, h: 0.32, fontSize: 11, fontFace: "Microsoft YaHei", color: theme.secondary, bold: true, align: "center" });
  try {
    slide.addImage({ path: path.join(__dirname, "imgs/ui_02_lesion.png"), x: 5.25, y: 1.28, w: 4.3, h: 3.8 });
  } catch(e) {}

  // Page badge
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("10", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  return slide;
}
module.exports = { createSlide };
