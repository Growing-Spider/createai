// slide-01.js — Cover Page: FundusAI-Edu
const pptxgen = require("pptxgenjs");

const slideConfig = { type: 'cover', index: 1, title: 'FundusAI-Edu Cover' };

function createSlide(pres, theme) {
  const slide = pres.addSlide();
  // Dark navy background
  slide.background = { color: theme.primary };

  // Decorative circles top-right
  slide.addShape(pres.shapes.OVAL, { x: 7.5, y: -1.2, w: 3.5, h: 3.5, fill: { color: theme.accent }, opacity: 0.15 });
  slide.addShape(pres.shapes.OVAL, { x: 8.8, y: 0.3, w: 2, h: 2, fill: { color: theme.accent }, opacity: 0.10 });

  // Left accent bar
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.12, h: 5.625, fill: { color: theme.accent } });

  // Eye icon representation (simple circle + circle)
  slide.addShape(pres.shapes.OVAL, { x: 0.8, y: 0.6, w: 1.3, h: 1.3, fill: { color: theme.secondary }, opacity: 0.3 });
  slide.addShape(pres.shapes.OVAL, { x: 1.1, y: 0.9, w: 0.7, h: 0.7, fill: { color: theme.accent }, opacity: 0.5 });

  // Main title
  slide.addText("FundusAI-Edu", {
    x: 2.5, y: 0.5, w: 6.5, h: 1.5,
    fontSize: 54, fontFace: "Arial",
    color: "FFFFFF", bold: true, align: "left", valign: "bottom"
  });

  // Subtitle
  slide.addText("眼底图像AI教学与科研辅助平台", {
    x: 2.5, y: 2.0, w: 6.5, h: 0.8,
    fontSize: 24, fontFace: "Microsoft YaHei",
    color: "FFFFFF", align: "left", valign: "top"
  });

  // Yellow accent line
  slide.addShape(pres.shapes.RECTANGLE, { x: 2.5, y: 2.9, w: 2.5, h: 0.05, fill: { color: theme.accent } });

  // Description
  slide.addText("让医学AI触手可及 — 从图像分析到科研全流程智能化", {
    x: 2.5, y: 3.2, w: 6.5, h: 0.6,
    fontSize: 16, fontFace: "Microsoft YaHei",
    color: "8ecae6", align: "left"
  });

  // Bottom info
  slide.addText("2026年6月  |  项目开发案例展示", {
    x: 0.8, y: 5.0, w: 5, h: 0.4,
    fontSize: 13, fontFace: "Microsoft YaHei",
    color: "8ecae6", align: "left"
  });

  return slide;
}

if (require.main === module) {
  const pres = new pptxgen(); pres.layout = 'LAYOUT_16x9';
  const theme = { primary: "023047", secondary: "219ebc", accent: "ffb703", light: "8ecae6", bg: "ffffff" };
  createSlide(pres, theme);
  pres.writeFile({ fileName: "slide-01-preview.pptx" });
}

module.exports = { createSlide, slideConfig };
