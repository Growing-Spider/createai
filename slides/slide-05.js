// slide-05.js — 拓扑分析 + RAG 问答 (核心功能2+3)
const pptxgen = require("pptxgenjs");

function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.08, fill: { color: theme.accent } });

  slide.addText("血管拓扑分析 & AI 智能问答", {
    x: 0.5, y: 0.3, w: 9, h: 0.6,
    fontSize: 26, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });

  // === Left: 拓扑分析 ===
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.15, w: 4.5, h: 0.4, fill: { color: theme.primary } });
  slide.addText("血管拓扑特征分析", { x: 0.5, y: 1.15, w: 4.5, h: 0.4, fontSize: 14, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  // Six features grid (3x2)
  const features = [
    ["血管密度", "密度", "反映视网膜血管覆盖率"],
    ["分叉点数量", "计数", "血管网络复杂度指标"],
    ["终末点数量", "计数", "血管末梢生长状况"],
    ["平均血管宽度", "像素", "CAD 辅助诊断依据"],
    ["血管迂曲度", "比值", "弯曲度异常提示病变"],
    ["分形维数", "1-2", "血管空间填充效率"],
  ];
  features.forEach((f, i) => {
    const col = i % 3;
    const row = Math.floor(i / 3);
    const x = 0.55 + col * 1.47;
    const y = 1.7 + row * 1.4;
    slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: 1.4, h: 1.2, fill: { color: "f0f8fc" }, rectRadius: 0.08 });
    slide.addText(f[0], { x: x+0.05, y: y+0.05, w: 1.3, h: 0.4, fontSize: 13, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center" });
    slide.addText(f[1], { x: x+0.05, y: y+0.45, w: 1.3, h: 0.3, fontSize: 16, fontFace: "Arial", color: theme.accent, bold: true, align: "center" });
    slide.addText(f[2], { x: x+0.05, y: y+0.75, w: 1.3, h: 0.35, fontSize: 9, fontFace: "Microsoft YaHei", color: "777777", align: "center" });
  });

  // === Right: RAG 问答 ===
  slide.addShape(pres.shapes.RECTANGLE, { x: 5.3, y: 1.15, w: 4.2, h: 0.4, fill: { color: theme.primary } });
  slide.addText("AI 科研导师 (RAG 问答)", { x: 5.3, y: 1.15, w: 4.2, h: 0.4, fontSize: 14, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 5.3, y: 1.7, w: 4.2, h: 3.4, fill: { color: "f8fcfe" }, rectRadius: 0.08 });

  const ragItems = [
    { hdr: "知识库检索", txt: "ChromaDB 向量数据库存储\n眼底医学知识文档" },
    { hdr: "多轮对话", txt: "DeepSeek 大模型 + 检索\n上下文增强回答质量" },
    { hdr: "离线兜底", txt: "无 API Key 时自动切换\n关键词搜索，功能不中断" },
    { hdr: "文档扩充", txt: "上传 PDF/TXT/DOCX\n一键重建知识库" },
  ];
  ragItems.forEach((item, i) => {
    const y = 1.85 + i * 0.82;
    slide.addText(item.hdr, { x: 5.5, y, w: 3.8, h: 0.3, fontSize: 13, fontFace: "Microsoft YaHei", color: theme.secondary, bold: true });
    slide.addText(item.txt, { x: 5.5, y: y+0.3, w: 3.8, h: 0.45, fontSize: 10, fontFace: "Microsoft YaHei", color: "666666" });
  });

  // Page badge
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("5", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  return slide;
}

module.exports = { createSlide };
