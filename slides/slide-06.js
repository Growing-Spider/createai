// slide-06.js — 科研选题 + 论文辅助 + 学习分析 (核心功能4-6)
const pptxgen = require("pptxgenjs");

function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.08, fill: { color: theme.accent } });

  slide.addText("科研工具链 — 选题 · 写作 · 学习分析", {
    x: 0.5, y: 0.3, w: 9, h: 0.6,
    fontSize: 26, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });

  // Three horizontal panels
  const panels = [
    {
      icon: "T", title: "科研选题生成器", color: "e76f51",
      items: ["适配 4 个学术层次", "AI 推荐 1-5 个选题", "自动生成研究方案", "实验设计模板输出"],
    },
    {
      icon: "P", title: "论文写作辅助", color: theme.secondary,
      items: ["9 种论文章节类型", "中英双语支持", "框架搭建 + 润色", "参考文献 / 期刊推荐"],
    },
    {
      icon: "L", title: "学习分析", color: "2a9d8f",
      items: ["SQLite 行为记录", "操作频次统计分析", "学习时长趋势图", "个人学习画像报告"],
    },
  ];

  panels.forEach((panel, i) => {
    const x = 0.5 + i * 3.1;
    slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.15, w: 2.9, h: 3.8, fill: { color: "f8fcfe" }, shadow: { type: "outer", blur: 4, offset: 2, color: "000000", opacity: 0.06 } });

    // Icon circle
    slide.addShape(pres.shapes.OVAL, { x: x+0.9, y: 1.3, w: 1.1, h: 1.1, fill: { color: panel.color } });
    slide.addText(panel.icon, { x: x+0.9, y: 1.3, w: 1.1, h: 1.1, fontSize: 28, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

    // Title
    slide.addText(panel.title, { x: x+0.1, y: 2.55, w: 2.7, h: 0.45, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center" });

    // Items
    panel.items.forEach((item, j) => {
      const iy = 3.05 + j * 0.42;
      slide.addText("  " + (j+1) + ". " + item, { x: x+0.2, y: iy, w: 2.5, h: 0.38, fontSize: 10, fontFace: "Microsoft YaHei", color: "555555" });
    });
  });

  // Page badge
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("6", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  return slide;
}

module.exports = { createSlide };
