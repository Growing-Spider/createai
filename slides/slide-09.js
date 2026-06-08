// slide-09.js
const pptxgen = require("pptxgenjs");
function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fill: { color: theme.accent } });
  slide.addText("实现功能 · 技术架构", { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "0B1D3A", bold: true, align: "center", valign: "middle" });

  slide.addText("面向教学场景的三层松耦合架构", { x: 0.5, y: 0.85, w: 9, h: 0.6, fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });

  slide.addText("所有核心能力均封装为独立模块,降低学习成本,便于二次开发和教学演示", { x: 0.5, y: 1.4, w: 9, h: 0.35, fontSize: 13, fontFace: "Microsoft YaHei", color: "666666" });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 1.95, w: 8.4, h: 0.95, fill: { color: theme.secondary }, opacity: 0.08 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 1.95, w: 1.3, h: 0.95, fill: { color: theme.secondary } });
  slide.addText("应用层", { x: 0.8, y: 1.95, w: 1.3, h: 0.5, fontSize: 15, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  slide.addText("L3", { x: 0.8, y: 2.45, w: 1.3, h: 0.35, fontSize: 10, fontFace: "Arial", color: "FFFFFF", align: "center", valign: "middle", opacity: 0.7 });
  slide.addText("• Streamlit Web界面", { x: 2.4, y: 2.03, w: 2.3, h: 0.8, fontSize: 10.5, fontFace: "Microsoft YaHei", color: theme.primary, valign: "middle" });
  slide.addText("• 深色主题+侧边栏导航", { x: 4.9, y: 2.03, w: 2.3, h: 0.8, fontSize: 10.5, fontFace: "Microsoft YaHei", color: theme.primary, valign: "middle" });
  slide.addText("• 实时分析进度+结果切换", { x: 7.4, y: 2.03, w: 2.3, h: 0.8, fontSize: 10.5, fontFace: "Microsoft YaHei", color: theme.primary, valign: "middle" });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 3.0700000000000003, w: 8.4, h: 0.95, fill: { color: theme.accent }, opacity: 0.08 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 3.0700000000000003, w: 1.3, h: 0.95, fill: { color: theme.accent } });
  slide.addText("AI层", { x: 0.8, y: 3.0700000000000003, w: 1.3, h: 0.5, fontSize: 15, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  slide.addText("L2", { x: 0.8, y: 3.5700000000000003, w: 1.3, h: 0.35, fontSize: 10, fontFace: "Arial", color: "FFFFFF", align: "center", valign: "middle", opacity: 0.7 });
  slide.addText("• U-Net血管分割", { x: 2.4, y: 3.1500000000000004, w: 2.3, h: 0.8, fontSize: 10.5, fontFace: "Microsoft YaHei", color: theme.primary, valign: "middle" });
  slide.addText("• DeepSeek RAG问答", { x: 4.9, y: 3.1500000000000004, w: 2.3, h: 0.8, fontSize: 10.5, fontFace: "Microsoft YaHei", color: theme.primary, valign: "middle" });
  slide.addText("• LLM选题/论文辅助", { x: 7.4, y: 3.1500000000000004, w: 2.3, h: 0.8, fontSize: 10.5, fontFace: "Microsoft YaHei", color: theme.primary, valign: "middle" });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 4.19, w: 8.4, h: 0.95, fill: { color: theme.primary }, opacity: 0.08 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 4.19, w: 1.3, h: 0.95, fill: { color: theme.primary } });
  slide.addText("数据层", { x: 0.8, y: 4.19, w: 1.3, h: 0.5, fontSize: 15, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  slide.addText("L1", { x: 0.8, y: 4.69, w: 1.3, h: 0.35, fontSize: 10, fontFace: "Arial", color: "FFFFFF", align: "center", valign: "middle", opacity: 0.7 });
  slide.addText("• SQLite学习行为库", { x: 2.4, y: 4.2700000000000005, w: 2.3, h: 0.8, fontSize: 10.5, fontFace: "Microsoft YaHei", color: theme.primary, valign: "middle" });
  slide.addText("• ChromaDB向量知识库", { x: 4.9, y: 4.2700000000000005, w: 2.3, h: 0.8, fontSize: 10.5, fontFace: "Microsoft YaHei", color: theme.primary, valign: "middle" });
  slide.addText("• PyTorch CPU推理", { x: 7.4, y: 4.2700000000000005, w: 2.3, h: 0.8, fontSize: 10.5, fontFace: "Microsoft YaHei", color: theme.primary, valign: "middle" });
  slide.addText("无需GPU · 浏览器即用 · MIT开源 · 完整文档 · 可复现", { x: 0.5, y: 5.15, w: 9, h: 0.32, fontSize: 12, fontFace: "Microsoft YaHei", color: theme.accent, bold: true, align: "center" });
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("9", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  return slide;
}
module.exports = { createSlide };
