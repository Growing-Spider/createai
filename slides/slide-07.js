// slide-07.js
const pptxgen = require("pptxgenjs");
function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fill: { color: theme.accent } });
  slide.addText("实现功能 · AI科研辅助", { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "0B1D3A", bold: true, align: "center", valign: "middle" });

  slide.addText("从知识问答到选题论文,AI全链路赋能", { x: 0.5, y: 0.85, w: 9, h: 0.6, fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });

  slide.addText("基于DeepSeek大语言模型+ChromaDB向量知识库,提供RAG增强的科研智能服务", { x: 0.5, y: 1.4, w: 9, h: 0.35, fontSize: 13, fontFace: "Microsoft YaHei", color: "666666" });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.95, w: 3.0, h: 3.0, fill: { color: theme.light } });
  slide.addImage({ path: "imgs/ui_07_topic.png", x: 0.55, y: 1.98, w: 2.9, h: 1.95 });
  slide.addText("科研选题生成器", { x: 0.6, y: 4.05, w: 2.8, h: 0.35, fontSize: 13, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center" });
  slide.addText("个性化选题推荐\n研究方案+实验报告", { x: 0.6, y: 4.35, w: 2.8, h: 0.5, fontSize: 10, fontFace: "Microsoft YaHei", color: "666666", align: "center", lineSpacingMultiple: 1.3 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 3.7, y: 1.95, w: 3.0, h: 3.0, fill: { color: theme.light } });
  slide.addImage({ path: "imgs/ui_05_api.png", x: 3.75, y: 1.98, w: 2.9, h: 1.95 });
  slide.addText("AI科研导师", { x: 3.8000000000000003, y: 4.05, w: 2.8, h: 0.35, fontSize: 13, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center" });
  slide.addText("RAG医学知识问答\n多轮对话+文献引用", { x: 3.8000000000000003, y: 4.35, w: 2.8, h: 0.5, fontSize: 10, fontFace: "Microsoft YaHei", color: "666666", align: "center", lineSpacingMultiple: 1.3 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 6.9, y: 1.95, w: 3.0, h: 3.0, fill: { color: theme.light } });
  slide.addImage({ path: "imgs/ui_06_learning.png", x: 6.95, y: 1.98, w: 2.9, h: 1.95 });
  slide.addText("论文写作辅助", { x: 7.0, y: 4.05, w: 2.8, h: 0.35, fontSize: 13, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center" });
  slide.addText("框架生成+章节写作\n润色+期刊推荐", { x: 7.0, y: 4.35, w: 2.8, h: 0.5, fontSize: 10, fontFace: "Microsoft YaHei", color: "666666", align: "center", lineSpacingMultiple: 1.3 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 5.1, w: 9, h: 0.35, fill: { color: theme.primary } });
  slide.addText("所有AI功能均需配置DeepSeek API Key(侧边栏即可完成)", { x: 0.7, y: 5.1, w: 8.6, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", align: "center", valign: "middle" });
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("7", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  return slide;
}
module.exports = { createSlide };
