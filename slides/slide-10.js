// slide-10.js
const pptxgen = require("pptxgenjs");
function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fill: { color: theme.primary } });
  slide.addText("应用情况 · 应用成效", { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  slide.addText("从理论教学到动手实践的跨越", { x: 0.5, y: 0.85, w: 9, h: 0.6, fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });

  slide.addText("安装简单,上手快,覆盖全流程,开源可复现 -- 四大维度衡量应用价值", { x: 0.5, y: 1.4, w: 9, h: 0.35, fontSize: 13, fontFace: "Microsoft YaHei", color: "666666" });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.7, y: 1.95, w: 2.0, h: 2.6, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.7, y: 1.95, w: 2.0, h: 0.06, fill: { color: theme.accent } });
  slide.addText("5 min", { x: 0.7, y: 2.15, w: 2.0, h: 1.1, fontSize: 36, fontFace: "Arial", color: theme.accent, bold: true, align: "center", valign: "middle" });
  slide.addText("上手时间", { x: 0.7, y: 3.3, w: 2.0, h: 0.45, fontSize: 16, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center", valign: "middle" });
  slide.addText("安装到首次分析", { x: 0.7, y: 3.8, w: 2.0, h: 0.4, fontSize: 11, fontFace: "Microsoft YaHei", color: "777777", align: "center" });
  slide.addShape(pres.shapes.RECTANGLE, { x: 3.0, y: 1.95, w: 2.0, h: 2.6, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 3.0, y: 1.95, w: 2.0, h: 0.06, fill: { color: theme.secondary } });
  slide.addText("6", { x: 3.0, y: 2.15, w: 2.0, h: 1.1, fontSize: 36, fontFace: "Arial", color: theme.secondary, bold: true, align: "center", valign: "middle" });
  slide.addText("功能模块", { x: 3.0, y: 3.3, w: 2.0, h: 0.45, fontSize: 16, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center", valign: "middle" });
  slide.addText("覆盖全链条科研", { x: 3.0, y: 3.8, w: 2.0, h: 0.4, fontSize: 11, fontFace: "Microsoft YaHei", color: "777777", align: "center" });
  slide.addShape(pres.shapes.RECTANGLE, { x: 5.3, y: 1.95, w: 2.0, h: 2.6, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 5.3, y: 1.95, w: 2.0, h: 0.06, fill: { color: theme.primary } });
  slide.addText("0", { x: 5.3, y: 2.15, w: 2.0, h: 1.1, fontSize: 36, fontFace: "Arial", color: theme.primary, bold: true, align: "center", valign: "middle" });
  slide.addText("GPU依赖", { x: 5.3, y: 3.3, w: 2.0, h: 0.45, fontSize: 16, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center", valign: "middle" });
  slide.addText("CPU即可运行", { x: 5.3, y: 3.8, w: 2.0, h: 0.4, fontSize: 11, fontFace: "Microsoft YaHei", color: "777777", align: "center" });
  slide.addShape(pres.shapes.RECTANGLE, { x: 7.6, y: 1.95, w: 2.0, h: 2.6, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 7.6, y: 1.95, w: 2.0, h: 0.06, fill: { color: theme.accent } });
  slide.addText("100%", { x: 7.6, y: 2.15, w: 2.0, h: 1.1, fontSize: 36, fontFace: "Arial", color: theme.accent, bold: true, align: "center", valign: "middle" });
  slide.addText("开源可复现", { x: 7.6, y: 3.3, w: 2.0, h: 0.45, fontSize: 16, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center", valign: "middle" });
  slide.addText("代码+文档齐全", { x: 7.6, y: 3.8, w: 2.0, h: 0.4, fontSize: 11, fontFace: "Microsoft YaHei", color: "777777", align: "center" });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 4.75, w: 9, h: 0.6, fill: { color: theme.primary } });
  slide.addText("对软硬件要求低,安装容易;操作简单,使用门槛低 -- 创AI评价标准 操作简单易用(40分)", { x: 0.7, y: 4.75, w: 8.6, h: 0.6, fontSize: 13, fontFace: "Microsoft YaHei", color: "FFFFFF", align: "center", valign: "middle" });
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("10", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  return slide;
}
module.exports = { createSlide };
