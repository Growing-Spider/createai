// compile.js — FundusAI-Edu PPT 编译（含UI截图）

const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.author = "FundusAI-Edu Team";
pres.title = "FundusAI-Edu 项目展示（含UI截图）";

const theme = {
  primary: "023047",
  secondary: "219ebc",
  accent: "ffb703",
  light: "8ecae6",
  bg: "ffffff",
};

// 幻灯片顺序：
// 1-封面  2-案例概述  3-分区  4-眼底分析  10-UI截图(上传+病变)
// 5-拓扑+RAG  11-UI截图(拓扑)  6-选题+论文+学习  12-UI截图(选题+API)
// 13-UI截图(学习分析)  7-技术架构  8-应用成效  9-谢谢

const slideOrder = [1, 2, 3, 4, 10, 5, 11, 6, 12, 13, 7, 8, 9];

slideOrder.forEach(n => {
  const num = String(n).padStart(2, "0");
  try {
    const mod = require(`./slide-${num}.js`);
    mod.createSlide(pres, theme);
  } catch (e) {
    console.error(`slide-${num}.js error:`, e.message);
  }
});

pres.writeFile({ fileName: "./output/FundusAI-Edu_项目展示_v2.pptx" })
  .then(() => console.log("PPT generated: " + slideOrder.length + " slides"))
  .catch(e => console.error("Error:", e));
