// compile.js — FundusAI-Edu 创AI竞赛PPT编译
const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.author = "FundusAI-Edu Team";
pres.title = "FundusAI-Edu 创AI案例展示";

const theme = {
  primary: "0B1D3A",
  secondary: "1E6FCF",
  accent: "F0A500",
  light: "F0F4F8",
  bg: "FFFFFF",
};

// 12 slides for competition video
for (let i = 1; i <= 12; i++) {
  const num = String(i).padStart(2, "0");
  try {
    const mod = require(`./slide-${num}.js`);
    mod.createSlide(pres, theme);
  } catch (e) {
    console.error(`slide-${num}.js error:`, e.message);
  }
}

pres.writeFile({ fileName: "./output/FundusAI-Edu_创AI竞赛.pptx" })
  .then(() => console.log(`[OK] PPT generated: 12 slides → ./output/FundusAI-Edu_创AI竞赛.pptx`))
  .catch(e => console.error("Error:", e));
