// slide-11.js
const pptxgen = require("pptxgenjs");
function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.background = { color: theme.primary };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fill: { color: theme.accent } });
  slide.addText("应用情况 · 创新与影响力", { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "0B1D3A", bold: true, align: "center", valign: "middle" });

  slide.addText("三个维度,重新定义医学AI教学", { x: 0.5, y: 0.85, w: 9, h: 0.6, fontSize: 28, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 1.65, w: 8.4, h: 1.02, fill: { color: "FFFFFF" }, opacity: 0.07 });
  slide.addText("01", { x: 1.0, y: 1.65, w: 1.0, h: 0.45, fontSize: 28, fontFace: "Arial", color: theme.accent, bold: true, valign: "middle" });
  slide.addText("多学科交叉融合", { x: 2.0, y: 1.65, w: 3.0, h: 0.45, fontSize: 18, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, valign: "middle" });
  slide.addText("眼科医学 x 深度学习 x 图论拓扑学 -- U-Net + Frangi + NetworkX协同创新", { x: 1.0, y: 2.2, w: 8.0, h: 0.45, fontSize: 11, fontFace: "Microsoft YaHei", color: "CCCCCC" });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 2.8, w: 8.4, h: 1.02, fill: { color: "FFFFFF" }, opacity: 0.07 });
  slide.addText("02", { x: 1.0, y: 2.8, w: 1.0, h: 0.45, fontSize: 28, fontFace: "Arial", color: theme.accent, bold: true, valign: "middle" });
  slide.addText("AI赋能全流程开发", { x: 2.0, y: 2.8, w: 3.0, h: 0.45, fontSize: 18, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, valign: "middle" });
  slide.addText("DeepSeek全程辅助需求>架构>编码>测试>文档,跨越技能限制,体现终身学习", { x: 1.0, y: 3.3499999999999996, w: 8.0, h: 0.45, fontSize: 11, fontFace: "Microsoft YaHei", color: "CCCCCC" });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 3.9499999999999997, w: 8.4, h: 1.02, fill: { color: "FFFFFF" }, opacity: 0.07 });
  slide.addText("03", { x: 1.0, y: 3.9499999999999997, w: 1.0, h: 0.45, fontSize: 28, fontFace: "Arial", color: theme.accent, bold: true, valign: "middle" });
  slide.addText("零门槛可复现", { x: 2.0, y: 3.9499999999999997, w: 3.0, h: 0.45, fontSize: 18, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, valign: "middle" });
  slide.addText("CPU运行+浏览器即用+EXE桌面版+三份完整文档+MIT开源协议", { x: 1.0, y: 4.5, w: 8.0, h: 0.45, fontSize: 11, fontFace: "Microsoft YaHei", color: "CCCCCC" });
  slide.addText("对标评分: 导向性(40)+实用性(80)+影响力(40)+创新性(10)+完整性(10)=180分", { x: 0.5, y: 5.05, w: 9, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: theme.accent, bold: true, align: "center" });
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.accent } });
  slide.addText("11", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "0B1D3A", bold: true, align: "center", valign: "middle" });
  return slide;
}
module.exports = { createSlide };