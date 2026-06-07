// slide-08.js — 应用情况 (Part 3, ~1 min)
const pptxgen = require("pptxgenjs");

function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.primary };

  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.08, fill: { color: theme.accent } });

  slide.addText("应用成效与影响力", {
    x: 0.5, y: 0.35, w: 9, h: 0.7,
    fontSize: 30, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true
  });

  // Four metric cards
  const metrics = [
    { value: "6", label: "功能模块", sub: "覆盖图像分析到\n科研全流程" },
    { value: "4000+", label: "行代码", sub: "结构清晰\n可维护可扩展" },
    { value: "4", label: "学术层次", sub: "高职高专/本科\n硕士/博士全覆盖" },
    { value: "28", label: "依赖包", sub: "成熟技术栈\n开箱即用" },
  ];

  metrics.forEach((m, i) => {
    const x = 0.5 + i * 2.35;
    slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.3, w: 2.15, h: 2.0, fill: { color: "0a2e4a" }, rectRadius: 0.08 });

    slide.addText(m.value, { x, y: 1.35, w: 2.15, h: 0.8, fontSize: 32, fontFace: "Arial", color: theme.accent, bold: true, align: "center", valign: "middle" });
    slide.addText(m.label, { x: x+0.1, y: 2.15, w: 1.95, h: 0.35, fontSize: 13, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center" });
    slide.addText(m.sub, { x: x+0.1, y: 2.55, w: 1.95, h: 0.6, fontSize: 10, fontFace: "Microsoft YaHei", color: "8ecae6", align: "center", lineSpacingMultiple: 1.4 });
  });

  // Impact section
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 3.6, w: 9, h: 1.3, fill: { color: "0a2e4a" }, rectRadius: 0.08 });

  slide.addText("项目价值", { x: 0.8, y: 3.7, w: 2, h: 0.4, fontSize: 16, fontFace: "Microsoft YaHei", color: theme.accent, bold: true });

  const impacts = [
    "教学创新：将抽象的理论知识转化为可视化交互体验，提升学习效果",
    "科研赋能：AI 辅助选题到论文全流程，降低科研启动门槛",
    "技术普惠：CPU 即可运行，无需 GPU，支持 Windows 桌面和浏览器双模式",
  ];
  impacts.forEach((imp, i) => {
    slide.addText(imp, { x: 0.8, y: 4.1 + i*0.32, w: 8.4, h: 0.3, fontSize: 11, fontFace: "Microsoft YaHei", color: "d0e8f0" });
  });

  // Page badge
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.accent } });
  slide.addText("8", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  return slide;
}

module.exports = { createSlide };
