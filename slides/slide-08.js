// slide-08.js
const pptxgen = require("pptxgenjs");
function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fill: { color: theme.accent } });
  slide.addText("实现功能 · 开发过程", { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "0B1D3A", bold: true, align: "center", valign: "middle" });

  slide.addText("借助DeepSeek跨越技术鸿沟", { x: 0.5, y: 0.85, w: 9, h: 0.6, fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });

  slide.addText("生成式AI辅助需求分析,架构设计,编码实现,测试迭代,文档生成全过程", { x: 0.5, y: 1.4, w: 9, h: 0.35, fontSize: 13, fontFace: "Microsoft YaHei", color: "666666" });

  slide.addShape(pres.shapes.RECTANGLE, { x: 1.5, y: 3.0, w: 7, h: 0.03, fill: { color: theme.secondary }, opacity: 0.4 });
  slide.addShape(pres.shapes.OVAL, { x: 1.3, y: 2.85, w: 0.35, h: 0.35, fill: { color: theme.secondary } });
  slide.addText("01", { x: 1.3, y: 2.85, w: 0.35, h: 0.35, fontSize: 10, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  slide.addText("需求分析", { x: 0.8, y: 3.35, w: 1.7, h: 0.35, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center" });
  slide.addText("DeepSeek协助梳理\n医学AI教学痛点\n与功能需求", { x: 0.8, y: 3.7, w: 1.7, h: 0.85, fontSize: 10, fontFace: "Microsoft YaHei", color: "555555", align: "center", lineSpacingMultiple: 1.4 });
  slide.addShape(pres.shapes.OVAL, { x: 3.1500000000000004, y: 2.85, w: 0.35, h: 0.35, fill: { color: theme.secondary } });
  slide.addText("02", { x: 3.1500000000000004, y: 2.85, w: 0.35, h: 0.35, fontSize: 10, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  slide.addText("架构设计", { x: 2.6500000000000004, y: 3.35, w: 1.7, h: 0.35, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center" });
  slide.addText("AI生成三层架构\nU-Net+RAG+LLM\n技术栈选型方案", { x: 2.6500000000000004, y: 3.7, w: 1.7, h: 0.85, fontSize: 10, fontFace: "Microsoft YaHei", color: "555555", align: "center", lineSpacingMultiple: 1.4 });
  slide.addShape(pres.shapes.OVAL, { x: 5.0, y: 2.85, w: 0.35, h: 0.35, fill: { color: theme.accent } });
  slide.addText("03", { x: 5.0, y: 2.85, w: 0.35, h: 0.35, fontSize: 10, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  slide.addText("编码实现", { x: 4.5, y: 3.35, w: 1.7, h: 0.35, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center" });
  slide.addText("DeepSeek辅助编写\n3000+行Python\n全栈代码调试", { x: 4.5, y: 3.7, w: 1.7, h: 0.85, fontSize: 10, fontFace: "Microsoft YaHei", color: "555555", align: "center", lineSpacingMultiple: 1.4 });
  slide.addShape(pres.shapes.OVAL, { x: 6.8500000000000005, y: 2.85, w: 0.35, h: 0.35, fill: { color: theme.secondary } });
  slide.addText("04", { x: 6.8500000000000005, y: 2.85, w: 0.35, h: 0.35, fontSize: 10, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  slide.addText("测试迭代", { x: 6.3500000000000005, y: 3.35, w: 1.7, h: 0.35, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center" });
  slide.addText("Bug修复+UI优化\n7轮反馈改进\n持续打磨细节", { x: 6.3500000000000005, y: 3.7, w: 1.7, h: 0.85, fontSize: 10, fontFace: "Microsoft YaHei", color: "555555", align: "center", lineSpacingMultiple: 1.4 });
  slide.addShape(pres.shapes.OVAL, { x: 8.700000000000001, y: 2.85, w: 0.35, h: 0.35, fill: { color: theme.secondary } });
  slide.addText("05", { x: 8.700000000000001, y: 2.85, w: 0.35, h: 0.35, fontSize: 10, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  slide.addText("文档部署", { x: 8.200000000000001, y: 3.35, w: 1.7, h: 0.35, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center" });
  slide.addText("AI自动生成手册\nPyInstaller EXE打包\npywebview桌面版", { x: 8.200000000000001, y: 3.7, w: 1.7, h: 0.85, fontSize: 10, fontFace: "Microsoft YaHei", color: "555555", align: "center", lineSpacingMultiple: 1.4 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 4.8, w: 9, h: 0.5, fill: { color: theme.primary } });
  slide.addText("Python · Streamlit · PyTorch(U-Net) · DeepSeek(LLM) · ChromaDB(RAG) · NetworkX · pywebview", { x: 0.7, y: 4.8, w: 8.6, h: 0.5, fontSize: 11, fontFace: "Microsoft YaHei", color: "FFFFFF", align: "center", valign: "middle" });
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("8", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  return slide;
}
module.exports = { createSlide };
