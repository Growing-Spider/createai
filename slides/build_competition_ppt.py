#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate all slide JS files for 创AI competition video PPTX."""

import os

SLIDES_DIR = r"F:\demo\slides"
OUTPUT_DIR = os.path.join(SLIDES_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

THEME = {
    "primary": "0B1D3A",    # 深海蓝 - 标题/深色背景
    "secondary": "1E6FCF",  # 专业蓝 - 次要强调
    "accent": "F0A500",     # 金色 - 高亮
    "light": "F0F4F8",      # 浅蓝灰 - 卡片背景
    "bg": "FFFFFF",          # 白色
}

HEADER = '''// slide-{num}.js — {desc}
const pptxgen = require("pptxgenjs");

const slideConfig = {{ type: "{type}", index: {idx}, title: "{title}" }};

function createSlide(pres, theme) {{
  const slide = pres.addSlide();
  slide.background = {{ color: theme.bg }};
'''

FOOTER_PAGE = '''
  // Page badge
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("PGNUM", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  return slide;
}

module.exports = { createSlide, slideConfig };
'''

FOOTER_NOPAGE = '''
  return slide;
}

module.exports = { createSlide, slideConfig };
'''

def write_slide(num, desc, slide_type, title, idx, body_code, with_page_badge=True):
    h = HEADER.format(num=num, desc=desc, type=slide_type, idx=idx, title=title)
    f = FOOTER_PAGE.replace("PGNUM", str(idx)) if with_page_badge else FOOTER_NOPAGE
    content = h + body_code + f
    filepath = os.path.join(SLIDES_DIR, f"slide-{num}.js")
    with open(filepath, 'w', encoding='utf-8') as fh:
        fh.write(content)
    print(f"  [OK] slide-{num}.js — {desc}")

# ══════════════════════════════════════════
# SLIDE 01 — 封面 (无页码)
# ══════════════════════════════════════════
write_slide("01", "封面", "cover", "FundusAI-Edu 创AI案例", 1, '''
  // Full deep navy background
  slide.background = { color: theme.primary };

  // Decorative gold elements - large circles
  slide.addShape(pres.shapes.OVAL, { x: -1.5, y: -1.5, w: 5, h: 5, fill: { color: theme.accent }, opacity: 0.08 });
  slide.addShape(pres.shapes.OVAL, { x: 8.2, y: 2.8, w: 3.5, h: 3.5, fill: { color: theme.accent }, opacity: 0.06 });
  slide.addShape(pres.shapes.OVAL, { x: 7.5, y: -1, w: 4, h: 4, fill: { color: theme.secondary }, opacity: 0.05 });

  // Left gold bar
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.1, h: 5.625, fill: { color: theme.accent } });

  // Top decorative line
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 0.4, w: 2, h: 0.03, fill: { color: theme.accent } });

  // Case label
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 0.7, w: 2.8, h: 0.35, fill: { color: theme.accent }, opacity: 0.15 });
  slide.addText("创AI案例征集 · 智能信息系统", {
    x: 0.8, y: 0.7, w: 2.8, h: 0.35,
    fontSize: 12, fontFace: "Microsoft YaHei", color: theme.accent,
    align: "center", valign: "middle"
  });

  // Main title
  slide.addText("FundusAI-Edu", {
    x: 0.8, y: 1.4, w: 8.5, h: 1.4,
    fontSize: 56, fontFace: "Arial", color: "FFFFFF", bold: true, align: "left", valign: "bottom"
  });

  // Subtitle line 1
  slide.addText("眼底图像 AI 教学与科研辅助平台", {
    x: 0.8, y: 2.8, w: 8.5, h: 0.7,
    fontSize: 26, fontFace: "Microsoft YaHei", color: "FFFFFF", align: "left", valign: "top"
  });

  // Gold separator
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 3.6, w: 2.5, h: 0.04, fill: { color: theme.accent } });

  // Description
  slide.addText("从图像分析到科研全流程智能化 — 让每一个医学师生都能亲手操作 AI", {
    x: 0.8, y: 3.9, w: 6.5, h: 0.6,
    fontSize: 14, fontFace: "Microsoft YaHei", color: theme.secondary, align: "left"
  });

  // Bottom info
  slide.addText("2026年6月  |  申报学段: 高等教育  |  案例类别: 智能信息系统", {
    x: 0.8, y: 5.1, w: 5, h: 0.35,
    fontSize: 11, fontFace: "Microsoft YaHei", color: "8899AA", align: "left"
  });
''', with_page_badge=False)

# ══════════════════════════════════════════
# SLIDE 02 — 开发背景：痛点与方案
# ══════════════════════════════════════════
write_slide("02", "开发背景", "content", "痛点与方案", 2, '''
  // Top accent bar
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });

  // Section tag
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 1.8, h: 0.35, fill: { color: theme.primary } });
  slide.addText("开发背景", { x: 0.5, y: 0.3, w: 1.8, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  // Title
  slide.addText("医学 AI 教学的三大痛点", {
    x: 0.5, y: 0.85, w: 9, h: 0.6,
    fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });

  // Three pain-point cards
  const pains = [
    { num: "01", title: "工具门槛高", desc: "GPU 服务器昂贵\\n深度学习框架配置繁琐\\n依赖管理复杂", icon: "x" },
    { num: "02", title: "理论脱离实践", desc: "以 PPT 讲授为主\\n学生缺少动手机会\\n无法直观感受 AI 效果", icon: "x" },
    { num: "03", title: "科研流程断裂", desc: "从选题到论文\\n缺乏系统化工具支撑\\n效率低下", icon: "x" },
  ];
  pains.forEach((p, i) => {
    const x = 0.5 + i * 3.1;
    // Card background
    slide.addShape(pres.shapes.RECTANGLE, { x, y: 1.7, w: 2.9, h: 2.8, fill: { color: theme.light } });
    // Card top accent
    slide.addShape(pres.shapes.RECTANGLE, { x, y: 1.7, w: 2.9, h: 0.06, fill: { color: theme.accent } });
    // Number
    slide.addText(p.num, { x: x + 0.2, y: 1.9, w: 0.8, h: 0.5, fontSize: 32, fontFace: "Arial", color: theme.primary, bold: true });
    // Title
    slide.addText(p.title, { x: x + 0.2, y: 2.4, w: 2.5, h: 0.5, fontSize: 17, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });
    // Desc
    slide.addText(p.desc, { x: x + 0.2, y: 3.0, w: 2.5, h: 1.3, fontSize: 12, fontFace: "Microsoft YaHei", color: "555555", lineSpacingMultiple: 1.5 });
  });

  // Bottom banner - AI 方案
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 4.7, w: 9, h: 0.55, fill: { color: theme.primary } });
  slide.addText("借助生成式 AI 跨越技术鸿沟 → FundusAI-Edu 提供一站式 AI 教学辅助平台", {
    x: 0.7, y: 4.7, w: 8.6, h: 0.55,
    fontSize: 14, fontFace: "Microsoft YaHei", color: theme.accent, bold: true, align: "center", valign: "middle"
  });
''')

# ══════════════════════════════════════════
# SLIDE 03 — 平台总览 (六大模块)
# ══════════════════════════════════════════
write_slide("03", "平台总览", "content", "六大功能模块", 3, '''
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 1.8, h: 0.35, fill: { color: theme.primary } });
  slide.addText("平台总览", { x: 0.5, y: 0.3, w: 1.8, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  slide.addText("六大功能模块，覆盖医学科研全流程", {
    x: 0.5, y: 0.85, w: 9, h: 0.6,
    fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });

  const modules = [
    ["🔬", "眼底图像智能分析", "U-Net 血管分割\\n病变识别与可视化"],
    ["🌐", "血管拓扑特征分析", "六维特征提取\\n雷达图与临床解读"],
    ["🤖", "AI 科研导师", "RAG 医学问答\\n多轮对话指导"],
    ["🎯", "科研选题生成器", "个性化选题推荐\\n研究方案与报告"],
    ["📝", "论文写作辅助", "框架生成 + 章节写作\\n润色 + 期刊推荐"],
    ["📊", "学习分析", "行为追踪与可视化\\n个人学习画像"],
  ];

  modules.forEach((m, i) => {
    const col = i % 3;
    const row = Math.floor(i / 3);
    const x = 0.5 + col * 3.1;
    const y = 1.7 + row * 1.9;

    slide.addShape(pres.shapes.RECTANGLE, { x, y, w: 2.9, h: 1.7, fill: { color: theme.light } });
    slide.addShape(pres.shapes.RECTANGLE, { x, y, w: 0.08, h: 1.7, fill: { color: theme.accent } });

    slide.addText(m[0], { x: x + 0.25, y: y + 0.15, w: 0.6, h: 0.45, fontSize: 24 });
    slide.addText(m[1], { x: x + 0.9, y: y + 0.15, w: 1.8, h: 0.45, fontSize: 15, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, valign: "middle" });
    slide.addText(m[2], { x: x + 0.25, y: y + 0.7, w: 2.4, h: 0.8, fontSize: 11, fontFace: "Microsoft YaHei", color: "666666", lineSpacingMultiple: 1.5 });
  });
''')

# ══════════════════════════════════════════
# SLIDE 04 — 眼底图像智能分析 + 截图
# ══════════════════════════════════════════
write_slide("04", "眼底图像分析", "content", "眼底图像智能分析", 4, '''
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fill: { color: theme.primary } });
  slide.addText("核心功能演示", { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  slide.addText("眼底图像智能分析", {
    x: 0.5, y: 0.85, w: 5, h: 0.6,
    fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });
  slide.addText("上传眼底照片，AI 自动完成血管分割、病变识别与拓扑特征提取", {
    x: 0.5, y: 1.35, w: 9, h: 0.4,
    fontSize: 14, fontFace: "Microsoft YaHei", color: "555555"
  });

  // Screenshot
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.9, w: 5.6, h: 3.3, fill: { color: theme.light } });
  slide.addImage({ path: "imgs/ui_01_upload.png", x: 0.55, y: 1.95, w: 5.5, h: 3.2 });

  // Feature cards on right
  const features = [
    ["🩸 血管分割", "U-Net 深度学习 + 多尺度\\nFrangi 增强，精准提取"],
    ["🔎 病变识别", "HSV 色彩空间规则引擎\\nDR 四等级自动分级"],
    ["🌐 拓扑分析", "六维特征量化\\n密度/分叉/迂曲/分形"],
  ];
  features.forEach((f, i) => {
    const y = 1.9 + i * 1.15;
    slide.addShape(pres.shapes.RECTANGLE, { x: 6.3, y, w: 3.2, h: 1.0, fill: { color: theme.light } });
    slide.addShape(pres.shapes.RECTANGLE, { x: 6.3, y, w: 0.06, h: 1.0, fill: { color: theme.accent } });
    slide.addText(f[0], { x: 6.5, y: y + 0.08, w: 2.8, h: 0.35, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });
    slide.addText(f[1], { x: 6.5, y: y + 0.45, w: 2.8, h: 0.5, fontSize: 10.5, fontFace: "Microsoft YaHei", color: "555555", lineSpacingMultiple: 1.3 });
  });

  // Caption
  slide.addText("▲ 支持 JPG/PNG/BMP/TIFF，左侧上传 → 右侧三标签结果切换", {
    x: 0.5, y: 5.25, w: 5.6, h: 0.25,
    fontSize: 9, fontFace: "Microsoft YaHei", color: "AAAAAA", italic: true
  });
''')

# ══════════════════════════════════════════
# SLIDE 05 — 分析结果：病变 + 拓扑
# ══════════════════════════════════════════
write_slide("05", "分析结果", "content", "病变识别与拓扑分析", 5, '''
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fill: { color: theme.primary } });
  slide.addText("分析结果", { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  slide.addText("DR 分级 + 六维拓扑特征", {
    x: 0.5, y: 0.85, w: 9, h: 0.6,
    fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });

  // Left: Lesion
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.6, w: 4.4, h: 3.1, fill: { color: theme.light } });
  slide.addText("病变识别结果", { x: 0.6, y: 1.65, w: 3, h: 0.35, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });
  slide.addImage({ path: "imgs/ui_02_lesion.png", x: 0.55, y: 2.05, w: 4.3, h: 2.6 });
  slide.addText("▲ Severe DR · 出血/渗出风险量化评估", {
    x: 0.5, y: 4.75, w: 4.4, h: 0.25,
    fontSize: 9, fontFace: "Microsoft YaHei", color: "AAAAAA", italic: true
  });

  // Right: Topology
  slide.addShape(pres.shapes.RECTANGLE, { x: 5.1, y: 1.6, w: 4.4, h: 3.1, fill: { color: theme.light } });
  slide.addText("六维拓扑特征", { x: 5.2, y: 1.65, w: 3, h: 0.35, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true });
  slide.addImage({ path: "imgs/ui_04_topo2.png", x: 5.15, y: 2.05, w: 4.3, h: 2.6 });
  slide.addText("▲ 密度/分叉点/终末点/宽度/迂曲度/分形维数", {
    x: 5.1, y: 4.75, w: 4.4, h: 0.25,
    fontSize: 9, fontFace: "Microsoft YaHei", color: "AAAAAA", italic: true
  });

  // Bottom key insight
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 5.1, w: 9, h: 0.35, fill: { color: theme.primary } });
  slide.addText("每个特征均附有临床参考范围，辅助医学教学中的定量分析与病理理解", {
    x: 0.7, y: 5.1, w: 8.6, h: 0.35,
    fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", align: "center", valign: "middle"
  });
''')

# ══════════════════════════════════════════
# SLIDE 06 — AI 赋能开发过程
# ══════════════════════════════════════════
write_slide("06", "AI赋能开发", "content", "生成式AI辅助全栈开发", 6, '''
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });
  // Highlight tag
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fill: { color: theme.accent } });
  slide.addText("AI 赋能开发", { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center", valign: "middle" });
  slide.addText("借助 DeepSeek 跨越技术鸿沟", {
    x: 0.5, y: 0.85, w: 9, h: 0.6,
    fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });
  slide.addText("生成式 AI 辅助需求分析、架构设计、编码实现、文档生成全过程", {
    x: 0.5, y: 1.35, w: 9, h: 0.35,
    fontSize: 14, fontFace: "Microsoft YaHei", color: "555555"
  });

  // 5-step timeline
  const steps = [
    { num: "01", title: "需求分析", desc: "DeepSeek 辅助\\n梳理教学痛点\\n定义功能边界" },
    { num: "02", title: "架构设计", desc: "AI 生成三层架构\\n技术栈选型\\n模块划分" },
    { num: "03", title: "编码实现", desc: "3000+ 行代码\\nU-Net + RAG +\\nNetworkX 集成" },
    { num: "04", title: "测试迭代", desc: "Bug 修复 + UI 优化\\n7 轮用户反馈\\n持续改进" },
    { num: "05", title: "文档与部署", desc: "自动生成文档\\nPyInstaller 打包\\n桌面版 EXE" },
  ];

  // Timeline line
  slide.addShape(pres.shapes.RECTANGLE, { x: 1.5, y: 2.95, w: 7, h: 0.03, fill: { color: theme.secondary }, opacity: 0.4 });

  steps.forEach((s, i) => {
    const x = 0.8 + i * 1.85;
    // Circle node
    slide.addShape(pres.shapes.OVAL, { x: x + 0.5, y: 2.8, w: 0.35, h: 0.35, fill: { color: i === 2 ? theme.accent : theme.secondary } });
    slide.addText(s.num, { x: x + 0.5, y: 2.8, w: 0.35, h: 0.35, fontSize: 11, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
    // Title
    slide.addText(s.title, { x, y: 3.3, w: 1.7, h: 0.4, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center" });
    // Description
    slide.addText(s.desc, { x, y: 3.7, w: 1.7, h: 0.9, fontSize: 10, fontFace: "Microsoft YaHei", color: "555555", align: "center", lineSpacingMultiple: 1.4 });
  });

  // Bottom tech stack banner
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 4.8, w: 9, h: 0.5, fill: { color: theme.primary } });
  const techs = ["Python", "Streamlit", "PyTorch (U-Net)", "DeepSeek (LLM)", "ChromaDB (RAG)", "NetworkX", "pywebview"];
  slide.addText(techs.join("  ·  "), {
    x: 0.7, y: 4.8, w: 8.6, h: 0.5,
    fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", align: "center", valign: "middle"
  });
''')

# ══════════════════════════════════════════
# SLIDE 07 — 技术架构
# ══════════════════════════════════════════
write_slide("07", "技术架构", "content", "三层技术架构", 7, '''
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fill: { color: theme.primary } });
  slide.addText("技术架构", { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  slide.addText("面向教学场景的三层系统架构", {
    x: 0.5, y: 0.85, w: 9, h: 0.6,
    fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });

  const layers = [
    { label: "应用层", color: theme.secondary, techs: ["Streamlit Web 界面", "侧边栏导航 · 深色主题", "实时分析进度 · 三标签结果"], opacity: 1.0 },
    { label: "AI 层", color: theme.accent, techs: ["U-Net 血管分割 · 多尺度 Frangi", "DeepSeek RAG 知识问答", "LLM 选题推荐 · 论文辅助"], opacity: 0.9 },
    { label: "数据层", color: theme.primary, techs: ["SQLite 学习行为数据库", "ChromaDB 向量知识库", "PyTorch CPU 模型推理"], opacity: 0.85 },
  ];

  layers.forEach((l, i) => {
    const y = 1.6 + i * 1.3;
    // Layer background
    slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y, w: 8.4, h: 1.1, fill: { color: l.color }, opacity: 0.08 });
    // Left label
    slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y, w: 1.4, h: 1.1, fill: { color: l.color } });
    slide.addText(l.label, { x: 0.8, y, w: 1.4, h: 0.55, fontSize: 16, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
    slide.addText("Level " + (3-i), { x: 0.8, y: y + 0.55, w: 1.4, h: 0.45, fontSize: 11, fontFace: "Arial", color: "FFFFFF", align: "center", valign: "middle", opacity: 0.7 });

    // Tech items
    l.techs.forEach((t, j) => {
      slide.addText("• " + t, { x: 2.4 + j * 2.5, y: y + 0.15, w: 2.4, h: 0.85, fontSize: 11, fontFace: "Microsoft YaHei", color: theme.primary, valign: "middle" });
    });
  });

  // Footer
  slide.addText("🎯 核心理念：无需 GPU · 浏览器即用 · 完整开源 · 可复现", {
    x: 0.5, y: 5.2, w: 9, h: 0.3,
    fontSize: 12, fontFace: "Microsoft YaHei", color: theme.secondary, bold: true, align: "center"
  });
''')

# ══════════════════════════════════════════
# SLIDE 08 — 科研辅助模块
# ══════════════════════════════════════════
write_slide("08", "科研辅助", "content", "AI科研辅助", 8, '''
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fill: { color: theme.primary } });
  slide.addText("AI 科研辅助", { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  slide.addText("从知识问答到选题生成，AI 全链路赋能", {
    x: 0.5, y: 0.85, w: 9, h: 0.6,
    fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });

  // Three screenshots in a row
  const cards = [
    { img: "imgs/ui_07_topic.png", title: "科研选题生成器", desc: "个性化选题推荐\\n研究方案与实验报告", w: 3.0 },
    { img: "imgs/ui_05_api.png", title: "API 配置面板", desc: "DeepSeek 大模型接入\\n一键配置即开即用", w: 3.0 },
    { img: "imgs/ui_06_learning.png", title: "学习行为分析", desc: "操作统计 + 活跃图表\\n六维学习画像", w: 3.0 },
  ];
  cards.forEach((c, i) => {
    const x = 0.5 + i * 3.2;
    slide.addShape(pres.shapes.RECTANGLE, { x, y: 1.6, w: c.w, h: 3.4, fill: { color: theme.light } });
    slide.addImage({ path: c.img, x: x + 0.05, y: 1.63, w: c.w - 0.1, h: 2.3 });
    slide.addText(c.title, { x: x + 0.1, y: 4.05, w: c.w - 0.2, h: 0.35, fontSize: 13, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center" });
    slide.addText(c.desc, { x: x + 0.1, y: 4.4, w: c.w - 0.2, h: 0.5, fontSize: 10, fontFace: "Microsoft YaHei", color: "666666", align: "center", lineSpacingMultiple: 1.3 });
  });
''')

# ══════════════════════════════════════════
# SLIDE 09 — 应用成效
# ══════════════════════════════════════════
write_slide("09", "应用成效", "content", "应用成效", 9, '''
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fill: { color: theme.primary } });
  slide.addText("应用成效", { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  slide.addText("从理论教学到动手实践的跨越", {
    x: 0.5, y: 0.85, w: 9, h: 0.6,
    fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });

  const metrics = [
    { value: "5 min", label: "上手时间", desc: "从安装到首次分析", color: theme.accent },
    { value: "6", label: "功能模块", desc: "覆盖全链条科研", color: theme.secondary },
    { value: "0", label: "GPU 依赖", desc: "CPU 即可运行", color: theme.primary },
    { value: "100%", label: "开源可复现", desc: "完整代码 + 文档", color: theme.accent },
  ];

  metrics.forEach((m, i) => {
    const x = 0.8 + i * 2.3;
    slide.addShape(pres.shapes.RECTANGLE, { x, y: 1.7, w: 2.0, h: 3.2, fill: { color: theme.light } });
    slide.addShape(pres.shapes.RECTANGLE, { x, y: 1.7, w: 2.0, h: 0.06, fill: { color: m.color } });

    // Big number
    slide.addText(m.value, { x, y: 2.0, w: 2.0, h: 1.2, fontSize: 36, fontFace: "Arial", color: m.color, bold: true, align: "center", valign: "middle" });
    // Label
    slide.addText(m.label, { x, y: 3.3, w: 2.0, h: 0.5, fontSize: 16, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center", valign: "middle" });
    // Desc
    slide.addText(m.desc, { x, y: 3.8, w: 2.0, h: 0.4, fontSize: 11, fontFace: "Microsoft YaHei", color: "777777", align: "center" });
  });

  // Bottom insight
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 5.1, w: 9, h: 0.35, fill: { color: theme.primary } });
  slide.addText("对比传统方案：无需配置 Python 环境、无需 GPU、双击 EXE 即可启动", {
    x: 0.7, y: 5.1, w: 8.6, h: 0.35,
    fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", align: "center", valign: "middle"
  });
''')

# ══════════════════════════════════════════
# SLIDE 10 — 创新点
# ══════════════════════════════════════════
write_slide("10", "创新点", "content", "三大创新", 10, '''
  slide.background = { color: theme.primary };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fill: { color: theme.accent } });
  slide.addText("创新亮点", { x: 0.5, y: 0.3, w: 2.2, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center", valign: "middle" });
  slide.addText("三个维度，重新定义医学AI教学", {
    x: 0.5, y: 0.85, w: 9, h: 0.6,
    fontSize: 28, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true
  });

  const innovations = [
    { num: "01", title: "多学科交叉融合", desc: "眼科医学 × 深度学习 × 图论拓扑学\\nU-Net 分割 + Frangi 增强 + NetworkX 分析\\n在同一平台完成跨学科实验", highlight: "创新点一" },
    { num: "02", title: "AI 赋能全流程", desc: "从需求分析到文档生成，DeepSeek 全程辅助\\n教师借助生成式 AI 跨越编码技能限制\\n体现终身学习与自主开发的核心理念", highlight: "创新点二" },
    { num: "03", title: "零门槛 · 可复现", desc: "CPU 运行、浏览器即用、EXE 桌面版\\n完整的代码 + 使用手册 + 安装手册 + 开发记录\\n他人可在一小时内完成环境搭建与复现", highlight: "创新点三" },
  ];

  innovations.forEach((inv, i) => {
    const y = 1.7 + i * 1.25;
    slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y, w: 8.4, h: 1.1, fill: { color: "FFFFFF" }, opacity: 0.07 });
    // Number
    slide.addText(inv.num, { x: 1.0, y: y + 0.05, w: 1.0, h: 0.5, fontSize: 28, fontFace: "Arial", color: theme.accent, bold: true, align: "left", valign: "middle" });
    // Title
    slide.addText(inv.title, { x: 2.0, y: y + 0.05, w: 3.0, h: 0.5, fontSize: 18, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, valign: "middle" });
    // Desc
    slide.addText(inv.desc, { x: 1.0, y: y + 0.6, w: 8.2, h: 0.5, fontSize: 11, fontFace: "Microsoft YaHei", color: "CCCCCC", lineSpacingMultiple: 1.3 });
  });

  slide.addText("匹配竞赛评价标准：开发角度新颖(10分) + AI赋能开发(20分) + 开源分享(20分)", {
    x: 0.5, y: 5.1, w: 9, h: 0.35,
    fontSize: 11, fontFace: "Microsoft YaHei", color: theme.accent, align: "center"
  });
  // Page badge 用金色
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.accent } });
  slide.addText("10", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: theme.primary, bold: true, align: "center", valign: "middle" });
''', with_page_badge=False)  # already have custom badge

# ══════════════════════════════════════════
# SLIDE 11 — 解决方案总结
# ══════════════════════════════════════════
write_slide("11", "解决方案", "content", "解决的教学问题", 11, '''
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.06, fill: { color: theme.accent } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fill: { color: theme.primary } });
  slide.addText("解决的教学问题", { x: 0.5, y: 0.3, w: 2.6, h: 0.35, fontSize: 12, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  slide.addText("对标评价标准：有效解决问题 + 操作简单易用", {
    x: 0.5, y: 0.85, w: 9, h: 0.6,
    fontSize: 28, fontFace: "Microsoft YaHei", color: theme.primary, bold: true
  });

  // Left: Problems solved
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.6, w: 4.5, h: 3.3, fill: { color: theme.light } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.6, w: 4.5, h: 0.45, fill: { color: theme.primary } });
  slide.addText("核心问题 → 解决方案", { x: 0.6, y: 1.6, w: 4.3, h: 0.45, fontSize: 14, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "center", valign: "middle" });

  const solutions = [
    ["工具门槛高", "→", "Web 浏览器即用，零环境配置"],
    ["理论脱离实践", "→", "上传图像即可开始 AI 分析实验"],
    ["科研流程断裂", "→", "从选题到论文一站式辅助"],
    ["学习效果难量化", "→", "学习行为追踪 + 个人画像"],
    ["硬件成本高", "→", "CPU 运行，无需 GPU"],
    ["文档不完备", "→", "三份手册 + 完整代码"],
  ];
  solutions.forEach((s, i) => {
    const y = 2.15 + i * 0.48;
    slide.addText(s[0], { x: 0.7, y, w: 1.5, h: 0.4, fontSize: 11, fontFace: "Microsoft YaHei", color: "AA3333", bold: true, valign: "middle" });
    slide.addText(s[1], { x: 2.1, y, w: 0.3, h: 0.4, fontSize: 11, fontFace: "Arial", color: theme.accent, bold: true, align: "center", valign: "middle" });
    slide.addText(s[2], { x: 2.4, y, w: 2.4, h: 0.4, fontSize: 11, fontFace: "Microsoft YaHei", color: "226644", bold: true, valign: "middle" });
  });

  // Right: File listing
  slide.addShape(pres.shapes.RECTANGLE, { x: 5.3, y: 1.6, w: 4.2, h: 3.3, fill: { color: theme.primary } });
  slide.addShape(pres.shapes.RECTANGLE, { x: 5.3, y: 1.6, w: 4.2, h: 0.45, fill: { color: theme.accent } });
  slide.addText("配套资源清单", { x: 5.4, y: 1.6, w: 4.0, h: 0.45, fontSize: 14, fontFace: "Microsoft YaHei", color: theme.primary, bold: true, align: "center", valign: "middle" });

  const files = [
    ["\u2705 完整源代码", "3000+ 行 Python"],
    ["\u2705 用户使用手册", "含 8 张 UI 截图"],
    ["\u2705 安装部署手册", "一键环境搭建"],
    ["\u2705 开发记录", "含架构图与流程图"],
    ["\u2705 演示视频", "MP4 1080p 高清"],
    ["\u2705 桌面版 EXE", "PyInstaller 打包"],
  ];
  files.forEach((f, i) => {
    const y = 2.2 + i * 0.48;
    slide.addText(f[0], { x: 5.6, y, w: 2.0, h: 0.4, fontSize: 11, fontFace: "Microsoft YaHei", color: theme.accent, bold: true, valign: "middle" });
    slide.addText(f[1], { x: 7.6, y, w: 1.7, h: 0.4, fontSize: 11, fontFace: "Microsoft YaHei", color: "CCCCCC", valign: "middle" });
  });
''')

# ══════════════════════════════════════════
# SLIDE 12 — 感谢页
# ══════════════════════════════════════════
write_slide("12", "感谢页", "summary", "感谢观看", 12, '''
  slide.background = { color: theme.primary };

  // Decorative circles
  slide.addShape(pres.shapes.OVAL, { x: -1.5, y: 3.5, w: 5, h: 5, fill: { color: theme.accent }, opacity: 0.06 });
  slide.addShape(pres.shapes.OVAL, { x: 7.5, y: -1.5, w: 4, h: 4, fill: { color: theme.secondary }, opacity: 0.05 });

  // Left gold bar
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.1, h: 5.625, fill: { color: theme.accent } });

  // Thank you text
  slide.addText("谢谢观看", {
    x: 0.8, y: 1.0, w: 8.5, h: 1.2,
    fontSize: 52, fontFace: "Microsoft YaHei", color: "FFFFFF", bold: true, align: "left", valign: "bottom"
  });

  // Gold separator
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: 2.3, w: 2.5, h: 0.04, fill: { color: theme.accent } });

  // Subtitle
  slide.addText("FundusAI-Edu · 眼底图像AI教学与科研辅助平台", {
    x: 0.8, y: 2.6, w: 8.5, h: 0.6,
    fontSize: 22, fontFace: "Microsoft YaHei", color: theme.secondary, align: "left"
  });

  // Contact info / notes
  slide.addText([
    { text: "案例类别：智能信息系统", options: { fontSize: 14, color: "AAAAAA" } },
    { text: "  |  ", options: { fontSize: 14, color: "666666" } },
    { text: "申报学段：高等教育", options: { fontSize: 14, color: "AAAAAA" } },
  ], { x: 0.8, y: 3.5, w: 8.5, h: 0.4, align: "left" });

  slide.addText("MIT 开源许可 · 完整代码与文档提供 · 支持复现验证", {
    x: 0.8, y: 4.0, w: 8.5, h: 0.4,
    fontSize: 14, fontFace: "Microsoft YaHei", color: "888888", align: "left"
  });

  // Bottom note
  slide.addText("2026年6月  |  创AI案例征集  |  FundusAI-Edu", {
    x: 0.8, y: 5.1, w: 5, h: 0.35,
    fontSize: 11, fontFace: "Microsoft YaHei", color: "667788", align: "left"
  });

  // Page badge - gold for final slide
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.accent } });
  slide.addText("12", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: theme.primary, bold: true, align: "center", valign: "middle" });
''', with_page_badge=False)

print("\n[DONE] All 12 slide files generated.")
print(f"[INFO] Output: {SLIDES_DIR}/")
