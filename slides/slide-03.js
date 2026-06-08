// slide-03.js
const pptxgen = require("pptxgenjs");
function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fill: { color: theme.primary } });
  slide.addText("案例概述 · 解决问题", { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  slide.addText("借助AI跨越技术鸿沟", { x: 0.5, y: 0.85, w: 9, h: 0.6, fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });

  slide.addText("对标评分标准: 有效解决问题(40分) + 操作简单易用(40分)", { x: 0.5, y: 1.4, w: 9, h: 0.35, fontSize: 13, fontFace: "Microsoft YaHei", color: "666666" });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 2.0, w: 9, h: 0.7, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 2.0, w: 0.08, h: 0.7, fill: { color: "AA3333" } });
  slide.addText("工具门槛高,配置复杂", { x: 0.8, y: 2.0, w: 3.0, h: 0.7, fontSize: 13, fontFace: "Microsoft YaHei", color: "AA3333", bold: true, valign: "middle" });
  slide.addText(">>", { x: 3.9, y: 2.0, w: 0.4, h: 0.7, fontSize: 18, fontFace: "Arial", color: theme.accent, bold: true, align: "center", valign: "middle" });
  slide.addText("Web浏览器即用,一键启动,无需Python环境", { x: 4.4, y: 2.0, w: 4.9, h: 0.7, fontSize: 13, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, valign: "middle" });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 2.85, w: 9, h: 0.7, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 2.85, w: 0.08, h: 0.7, fill: { color: "AA3333" } });
  slide.addText("理论讲授为主,缺乏动手实践", { x: 0.8, y: 2.85, w: 3.0, h: 0.7, fontSize: 13, fontFace: "Microsoft YaHei", color: "AA3333", bold: true, valign: "middle" });
  slide.addText(">>", { x: 3.9, y: 2.85, w: 0.4, h: 0.7, fontSize: 18, fontFace: "Arial", color: theme.accent, bold: true, align: "center", valign: "middle" });
  slide.addText("上传眼底图像即可完成AI分析全流程实验", { x: 4.4, y: 2.85, w: 4.9, h: 0.7, fontSize: 13, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, valign: "middle" });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 3.7, w: 9, h: 0.7, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 3.7, w: 0.08, h: 0.7, fill: { color: "AA3333" } });
  slide.addText("科研选题无从下手", { x: 0.8, y: 3.7, w: 3.0, h: 0.7, fontSize: 13, fontFace: "Microsoft YaHei", color: "AA3333", bold: true, valign: "middle" });
  slide.addText(">>", { x: 3.9, y: 3.7, w: 0.4, h: 0.7, fontSize: 18, fontFace: "Arial", color: theme.accent, bold: true, align: "center", valign: "middle" });
  slide.addText("AI智能推荐个性化选题+研究方案+论文辅助", { x: 4.4, y: 3.7, w: 4.9, h: 0.7, fontSize: 13, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, valign: "middle" });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 4.55, w: 9, h: 0.7, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 4.55, w: 0.08, h: 0.7, fill: { color: "AA3333" } });
  slide.addText("学习效果难以量化评估", { x: 0.8, y: 4.55, w: 3.0, h: 0.7, fontSize: 13, fontFace: "Microsoft YaHei", color: "AA3333", bold: true, valign: "middle" });
  slide.addText(">>", { x: 3.9, y: 4.55, w: 0.4, h: 0.7, fontSize: 18, fontFace: "Arial", color: theme.accent, bold: true, align: "center", valign: "middle" });
  slide.addText("自动追踪学习行为,生成六维学习画像", { x: 4.4, y: 4.55, w: 4.9, h: 0.7, fontSize: 13, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, valign: "middle" });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 5.15, w: 9, h: 0.32, fill: { color: theme.primary } });
  slide.addText("核心理念: 让每一个医学师生都能亲手操作AI -- 从图像分析到科研全流程智能化", { x: 0.7, y: 5.15, w: 8.6, h: 0.32, fontSize: 12, fontFace: "Microsoft YaHei", color: theme.accent, align: "center", valign: "middle" });
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("3", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  return slide;
}
module.exports = { createSlide };
