// slide-04.js
const pptxgen = require("pptxgenjs");
function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fill: { color: theme.primary } });
  slide.addText("案例概述 · 平台总览", { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  slide.addText("六大功能模块,覆盖医学科研全流程", { x: 0.5, y: 0.85, w: 9, h: 0.6, fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });

  slide.addText("集成深度学习,图论分析,大语言模型等能力的眼底图像AI教学平台", { x: 0.5, y: 1.4, w: 9, h: 0.35, fontSize: 13, fontFace: "Microsoft YaHei", color: "666666" });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.95, w: 2.9, h: 1.65, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.95, w: 0.08, h: 1.65, fill: { color: theme.accent } });
  slide.addText("🔬", { x: 0.75, y: 2.05, w: 0.6, h: 0.4, fontSize: 24 });
  slide.addText("眼底图像智能分析", { x: 1.4, y: 2.05, w: 1.8, h: 0.4, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, valign: "middle" });
  slide.addText("U-Net血管分割\n病变识别与可视化", { x: 0.75, y: 2.55, w: 2.4, h: 0.85, fontSize: 10.5, fontFace: "Microsoft YaHei", color: "555555", lineSpacingMultiple: 1.5 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 3.6, y: 1.95, w: 2.9, h: 1.65, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 3.6, y: 1.95, w: 0.08, h: 1.65, fill: { color: theme.accent } });
  slide.addText("🌐", { x: 3.85, y: 2.05, w: 0.6, h: 0.4, fontSize: 24 });
  slide.addText("血管拓扑特征分析", { x: 4.5, y: 2.05, w: 1.8, h: 0.4, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, valign: "middle" });
  slide.addText("六维特征提取\n雷达图+临床解读", { x: 3.85, y: 2.55, w: 2.4, h: 0.85, fontSize: 10.5, fontFace: "Microsoft YaHei", color: "555555", lineSpacingMultiple: 1.5 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 6.7, y: 1.95, w: 2.9, h: 1.65, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 6.7, y: 1.95, w: 0.08, h: 1.65, fill: { color: theme.accent } });
  slide.addText("🤖", { x: 6.95, y: 2.05, w: 0.6, h: 0.4, fontSize: 24 });
  slide.addText("AI科研导师", { x: 7.6000000000000005, y: 2.05, w: 1.8, h: 0.4, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, valign: "middle" });
  slide.addText("RAG医学知识问答\n多轮对话专业指导", { x: 6.95, y: 2.55, w: 2.4, h: 0.85, fontSize: 10.5, fontFace: "Microsoft YaHei", color: "555555", lineSpacingMultiple: 1.5 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 3.8, w: 2.9, h: 1.65, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 3.8, w: 0.08, h: 1.65, fill: { color: theme.accent } });
  slide.addText("🎯", { x: 0.75, y: 3.9, w: 0.6, h: 0.4, fontSize: 24 });
  slide.addText("科研选题生成器", { x: 1.4, y: 3.9, w: 1.8, h: 0.4, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, valign: "middle" });
  slide.addText("AI推荐个性化选题\n研究方案+实验报告", { x: 0.75, y: 4.3999999999999995, w: 2.4, h: 0.85, fontSize: 10.5, fontFace: "Microsoft YaHei", color: "555555", lineSpacingMultiple: 1.5 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 3.6, y: 3.8, w: 2.9, h: 1.65, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 3.6, y: 3.8, w: 0.08, h: 1.65, fill: { color: theme.accent } });
  slide.addText("📝", { x: 3.85, y: 3.9, w: 0.6, h: 0.4, fontSize: 24 });
  slide.addText("论文写作辅助", { x: 4.5, y: 3.9, w: 1.8, h: 0.4, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, valign: "middle" });
  slide.addText("框架生成+章节写作\n润色+期刊推荐", { x: 3.85, y: 4.3999999999999995, w: 2.4, h: 0.85, fontSize: 10.5, fontFace: "Microsoft YaHei", color: "555555", lineSpacingMultiple: 1.5 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 6.7, y: 3.8, w: 2.9, h: 1.65, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 6.7, y: 3.8, w: 0.08, h: 1.65, fill: { color: theme.accent } });
  slide.addText("📊", { x: 6.95, y: 3.9, w: 0.6, h: 0.4, fontSize: 24 });
  slide.addText("学习分析", { x: 7.6000000000000005, y: 3.9, w: 1.8, h: 0.4, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, valign: "middle" });
  slide.addText("行为追踪与可视化\n个人学习画像", { x: 6.95, y: 4.3999999999999995, w: 2.4, h: 0.85, fontSize: 10.5, fontFace: "Microsoft YaHei", color: "555555", lineSpacingMultiple: 1.5 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 5.15, w: 9, h: 0.32, fill: { color: theme.accent }, opacity: 0.15 });
  slide.addText("案例概述(~2min)  >>>  实现功能(~5min)  >>>  应用情况(~1min)", { x: 0.7, y: 5.15, w: 8.6, h: 0.32, fontSize: 11, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center", valign: "middle" });
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("4", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  return slide;
}
module.exports = { createSlide };
