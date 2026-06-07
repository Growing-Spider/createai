// slide-02.js — 案例概述 (Part 1, ~2 min)
const pptxgen = require("pptxgenjs");

function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };

  // Top accent bar
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.08, fill: { color: theme.accent } });

  // Section label
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 0.3, w: 1.6, h: 0.4, fill: { color: theme.primary }, rectRadius: 0.1 });
  slide.addText("案例概述", { x: 0.5, y: 0.3, w: 1.6, h: 0.4, fontSize: 13, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  // Title
  slide.addText("应用场景与核心问题", {
    x: 0.5, y: 0.9, w: 9, h: 0.7,
    fontSize: 30, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });

  // Left column - 应用场景
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.8, w: 4.3, h: 3.2, fill: { color: "f0f8fc" }, rectRadius: 0.1 });
  slide.addText("应用场景", { x: 0.7, y: 1.9, w: 3.9, h: 0.45, fontSize: 16, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });

  const scenes = [
    { label: "医学教学", desc: "课堂上演示血管分割与拓扑分析，抽象概念可视化" },
    { label: "科研起步", desc: "学生快速生成选题、实验方案，降低科研门槛" },
    { label: "论文写作", desc: "AI 辅助构建框架、润色章节、推荐参考文献" },
    { label: "自主学习", desc: "知识库问答 + 学习行为画像，个性化学习路径" },
  ];
  scenes.forEach((s, i) => {
    const y = 2.45 + i * 0.65;
    slide.addText(s.label + "   ", { x: 0.8, y, w: 1.5, h: 0.5, fontSize: 13, fontFace: "Microsoft YaHei", color: theme.secondary, bold: true, align: "left", valign: "top" });
    slide.addText(s.desc, { x: 2.2, y, w: 2.5, h: 0.5, fontSize: 12, fontFace: "Microsoft YaHei", color: "555555", align: "left", valign: "top" });
  });

  // Right column - 核心问题
  slide.addShape(pres.shapes.RECTANGLE, { x: 5.2, y: 1.8, w: 4.3, h: 3.2, fill: { color: theme.primary }, rectRadius: 0.1 });
  slide.addText("解决的核心问题", { x: 5.4, y: 1.9, w: 3.9, h: 0.45, fontSize: 16, fontFace: "Microsoft YaHei", color: theme.accent, bold: true });

  const problems = [
    "眼底图像分析工具门槛高，学生难以独立完成实验",
    "科研选题缺乏指导，本科生不知道如何切入",
    "血管拓扑特征计算复杂，手工提取耗时且易错",
    "论文写作流程不清晰，效率低下",
  ];
  problems.forEach((p, i) => {
    const y = 2.5 + i * 0.7;
    slide.addText((i+1) + ".", { x: 5.5, y, w: 0.4, h: 0.5, fontSize: 20, fontFace: "Arial", color: theme.accent, bold: true, align: "center", valign: "top" });
    slide.addText(p, { x: 5.9, y, w: 3.4, h: 0.55, fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", valign: "top" });
  });

  // Page badge
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("2", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  return slide;
}

module.exports = { createSlide };
