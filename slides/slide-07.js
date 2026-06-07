// slide-07.js — 技术架构与数据管线
const pptxgen = require("pptxgenjs");

function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.08, fill: { color: theme.accent } });

  slide.addText("技术架构与数据处理管线", {
    x: 0.5, y: 0.3, w: 9, h: 0.6,
    fontSize: 26, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });

  // === Architecture stacks ===
  const layers = [
    { label: "展示层", tech: "Streamlit + pywebview + Custom CSS", color: theme.accent, y: 1.2 },
    { label: "业务层", tech: "6 个 Python 模块 (4080 行代码)", color: theme.secondary, y: 2.0 },
    { label: "AI 层", tech: "PyTorch U-Net + DeepSeek LLM + ChromaDB", color: theme.primary, y: 2.8 },
    { label: "数据层", tech: "SQLite + 知识库文件 + 眼底图像", color: "e76f51", y: 3.6 },
  ];

  layers.forEach((layer) => {
    slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: layer.y, w: 1.6, h: 0.6, fill: { color: layer.color }, rectRadius: 0.05 });
    slide.addText(layer.label, { x: 0.5, y: layer.y, w: 1.6, h: 0.6, fontSize: 14, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
    slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 2.2, y: layer.y, w: 3, h: 0.6, fill: { color: "f0f8fc" }, rectRadius: 0.05 });
    slide.addText(layer.tech, { x: 2.3, y: layer.y, w: 2.8, h: 0.6, fontSize: 11, fontFace: "Microsoft YaHei", color: "555555", valign: "middle" });
  });

  // === Pipeline on right ===
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 5.5, y: 1.1, w: 4.2, h: 0.4, fill: { color: theme.primary } });
  slide.addText("血管分割算法管线", { x: 5.5, y: 1.1, w: 4.2, h: 0.4, fontSize: 13, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  const steps = [
    { label: "图像输入", desc: "灰度化 + 缩放到 512x512", t: 1.75 },
    { label: "CLAHE增强", desc: "局部对比度增强 + 反转", t: 2.35 },
    { label: "多尺度滤波", desc: "BlackHat(7/15/31) + Frangi", t: 2.95 },
    { label: "自适应阈值", desc: "百分位阈值 + 形态学清理", t: 3.55 },
    { label: "骨架提取", desc: "Lee 骨架化 + 拓扑分析", t: 4.15 },
  ];

  steps.forEach((s, i) => {
    const y = s.t;
    slide.addText((i+1) + ". " + s.label, { x: 5.6, y, w: 1.8, h: 0.4, fontSize: 12, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });
    slide.addText(s.desc, { x: 7.5, y, w: 2, h: 0.4, fontSize: 10, fontFace: "Microsoft YaHei", color: "777777", valign: "middle" });
    if (i < steps.length - 1) {
      slide.addText("v", { x: 6.3, y: y+0.32, w: 0.5, h: 0.3, fontSize: 12, fontFace: "Arial", color: theme.accent, bold: true, align: "center" });
    }
  });

  // Bottom: technology tags
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 4.5, w: 9, h: 0.55, fill: { color: "f0f8fc" }, rectRadius: 0.06 });
  const tags = ["Streamlit", "PyTorch", "OpenCV", "scikit-image", "LangChain", "ChromaDB", "DeepSeek", "NetworkX", "SQLite", "pywebview"];
  const tagWidth = 9 / tags.length;
  tags.forEach((tag, i) => {
    slide.addText(tag, { x: 0.5 + i*tagWidth, y: 4.5, w: tagWidth, h: 0.55, fontSize: 10, fontFace: "Arial", color: theme.secondary, bold: true, align: "center", valign: "middle" });
  });

  // Page badge
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("7", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  return slide;
}

module.exports = { createSlide };
