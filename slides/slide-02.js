// slide-02.js
const pptxgen = require("pptxgenjs");
function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fill: { color: theme.primary } });
  slide.addText("案例概述 · 应用场景", { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  slide.addText("医学AI教学中的三大痛点", { x: 0.5, y: 0.85, w: 9, h: 0.6, fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });

  slide.addText("传统教学中，学生难以接触真实的AI分析工具，理论与实践严重脱节", { x: 0.5, y: 1.4, w: 9, h: 0.35, fontSize: 13, fontFace: "Microsoft YaHei", color: "666666" });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 2.0, w: 2.9, h: 2.9, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 2.0, w: 2.9, h: 0.06, fill: { color: theme.accent } });
  slide.addText("01", { x: 0.7, y: 2.2, w: 0.8, h: 0.5, fontSize: 36, fontFace: "Arial", color: theme.primary, bold: true });
  slide.addText("工具门槛高", { x: 0.7, y: 2.7, w: 2.5, h: 0.45, fontSize: 17, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });
  slide.addText("GPU服务器昂贵\n深度学习框架配置复杂\n学生难以独立完成实验", { x: 0.7, y: 3.2, w: 2.5, h: 1.4, fontSize: 11, fontFace: "Microsoft YaHei", color: "555555", lineSpacingMultiple: 1.5 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 3.6, y: 2.0, w: 2.9, h: 2.9, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 3.6, y: 2.0, w: 2.9, h: 0.06, fill: { color: theme.accent } });
  slide.addText("02", { x: 3.8000000000000003, y: 2.2, w: 0.8, h: 0.5, fontSize: 36, fontFace: "Arial", color: theme.primary, bold: true });
  slide.addText("理论脱离实践", { x: 3.8000000000000003, y: 2.7, w: 2.5, h: 0.45, fontSize: 17, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });
  slide.addText("以PPT讲授为主\n缺少动手操作机会\n无法直观感受AI效果", { x: 3.8000000000000003, y: 3.2, w: 2.5, h: 1.4, fontSize: 11, fontFace: "Microsoft YaHei", color: "555555", lineSpacingMultiple: 1.5 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 6.7, y: 2.0, w: 2.9, h: 2.9, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 6.7, y: 2.0, w: 2.9, h: 0.06, fill: { color: theme.accent } });
  slide.addText("03", { x: 6.9, y: 2.2, w: 0.8, h: 0.5, fontSize: 36, fontFace: "Arial", color: theme.primary, bold: true });
  slide.addText("科研流程断裂", { x: 6.9, y: 2.7, w: 2.5, h: 0.45, fontSize: 17, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });
  slide.addText("从选题到论文写作\n缺乏系统化工具支撑\n效率低下且方向迷茫", { x: 6.9, y: 3.2, w: 2.5, h: 1.4, fontSize: 11, fontFace: "Microsoft YaHei", color: "555555", lineSpacingMultiple: 1.5 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 5.05, w: 9, h: 0.42, fill: { color: theme.primary } });
  slide.addText("应用场景: 医学教学课堂演示  ·  学生自主实验  ·  科研起步训练  ·  论文写作辅助", { x: 0.7, y: 5.05, w: 8.6, h: 0.42, fontSize: 13, fontFace: "Microsoft YaHei", color: theme.accent, bold: true, align: "center", valign: "middle" });
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("2", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  return slide;
}
module.exports = { createSlide };
