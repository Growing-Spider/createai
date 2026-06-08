// slide-06.js
const pptxgen = require("pptxgenjs");
function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fill: { color: theme.accent } });
  slide.addText("实现功能 · 分析结果", { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "0B1D3A", bold: true, align: "center", valign: "middle" });

  slide.addText("DR分级 + 六维拓扑特征", { x: 0.5, y: 0.85, w: 9, h: 0.6, fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });

  slide.addText("分析完成后,系统自动生成三标签结果: 血管分割 | 病变识别 | 拓扑特征", { x: 0.5, y: 1.4, w: 9, h: 0.35, fontSize: 13, fontFace: "Microsoft YaHei", color: "666666" });

  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.9, w: 4.4, h: 2.8, fill: { color: theme.light } });
  slide.addText("病变识别结果", { x: 0.6, y: 1.95, w: 3, h: 0.35, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });
  slide.addImage({ path: "imgs/ui_02_lesion.png", x: 0.55, y: 2.35, w: 4.3, h: 2.3 });
  slide.addShape(pres.shapes.RECTANGLE, { x: 5.1, y: 1.9, w: 4.4, h: 2.8, fill: { color: theme.light } });
  slide.addText("六维拓扑特征", { x: 5.2, y: 1.95, w: 3, h: 0.35, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });
  slide.addImage({ path: "imgs/ui_04_topo2.png", x: 5.15, y: 2.35, w: 4.3, h: 2.3 });
  slide.addText("▲ Severe DR分级+出血/渗出风险量化评估", { x: 0.5, y: 4.75, w: 4.4, h: 0.25, fontSize: 9, fontFace: "Microsoft YaHei", color: "AAAAAA", italic: true });
  slide.addText("▲ 密度/分叉点/宽度/迂曲度/分形维数+临床参考范围", { x: 5.1, y: 4.75, w: 4.4, h: 0.25, fontSize: 9, fontFace: "Microsoft YaHei", color: "AAAAAA", italic: true });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 5.05, w: 9, h: 0.42, fill: { color: theme.primary } });
  slide.addText("每个特征均附有正常参考范围,辅助医学教学中的定量分析与病理理解", { x: 0.7, y: 5.05, w: 8.6, h: 0.42, fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", align: "center", valign: "middle" });
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("6", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  return slide;
}
module.exports = { createSlide };
