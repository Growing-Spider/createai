#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""简化的PPT生成脚本 — 直接写文件,避免f-string嵌套问题"""

import os

SLIDES_DIR = r"F:\demo\slides"
OUTPUT_DIR = os.path.join(SLIDES_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADER = '''// slide-{num}.js
const pptxgen = require("pptxgenjs");
function createSlide(pres, theme) {
  const slide = pres.addSlide();
  slide.background = { color: theme.bg };
'''

BADGE = '''
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: { color: theme.secondary } });
  slide.addText("{pg}", { x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" });
  return slide;
}
module.exports = { createSlide };
'''

NOBADGE = '''
  return slide;
}
module.exports = { createSlide };
'''

T = "theme.primary"
S = "theme.secondary"
A = "theme.accent"
L = "theme.light"
B = "theme.bg"
MY = "Microsoft YaHei"

# helpers as Python functions (returns JS string)
def top_bar():   return f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0, y: 0, w: 10, h: 0.06, fill: {{ color: {A} }} }});\n'
def navy_tag(t): return f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.5, y: 0.3, w: 2.2, h: 0.35, fill: {{ color: {T} }} }});\n  slide.addText("{t}", {{ x: 0.5, y: 0.3, w: 2.2, h: 0.35, fontSize: 12, fontFace: "{MY}", color: "FFFFFF", bold: true, align: "center", valign: "middle" }});\n'
def gold_tag(t): return f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.5, y: 0.3, w: 2.6, h: 0.35, fill: {{ color: {A} }} }});\n  slide.addText("{t}", {{ x: 0.5, y: 0.3, w: 2.6, h: 0.35, fontSize: 12, fontFace: "{MY}", color: "0B1D3A", bold: true, align: "center", valign: "middle" }});\n'
def title_t(t):  return f'  slide.addText("{t}", {{ x: 0.5, y: 0.85, w: 9, h: 0.6, fontSize: 28, fontFace: "{MY}", color: {T}, bold: true }});\n'
def sub(s):      return f'  slide.addText("{s}", {{ x: 0.5, y: 1.4, w: 9, h: 0.35, fontSize: 13, fontFace: "{MY}", color: "666666" }});\n'

def write_slide(name, body_lines, pg=None):
    """body_lines is a list of strings, pg=None means no badge (cover/end)"""
    body = '\n'.join(body_lines)
    if pg:
        footer = BADGE.replace('{pg}', pg)
    else:
        footer = NOBADGE
    header = HEADER.replace('{num}', name)
    content = header + body + footer
    path = os.path.join(SLIDES_DIR, f"slide-{name}.js")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  [OK] slide-{name}.js")


# ═══════════════ SLIDE 01 · 封面 ═══════════════
write_slide("01", [
    f'  slide.background = {{ color: {T} }};',
    f'  slide.addShape(pres.shapes.OVAL, {{ x: -1.5, y: -1.5, w: 5, h: 5, fill: {{ color: {A} }}, opacity: 0.08 }});',
    f'  slide.addShape(pres.shapes.OVAL, {{ x: 8.2, y: 2.8, w: 3.5, h: 3.5, fill: {{ color: {A} }}, opacity: 0.06 }});',
    f'  slide.addShape(pres.shapes.OVAL, {{ x: 7.5, y: -1, w: 4, h: 4, fill: {{ color: {S} }}, opacity: 0.05 }});',
    f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0, y: 0, w: 0.1, h: 5.625, fill: {{ color: {A} }} }});',
    f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.8, y: 0.4, w: 2, h: 0.03, fill: {{ color: {A} }} }});',
    f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.8, y: 0.7, w: 3.2, h: 0.35, fill: {{ color: {A} }}, opacity: 0.15 }});',
    f'  slide.addText("创AI案例征集 · 智能信息系统", {{ x: 0.8, y: 0.7, w: 3.2, h: 0.35, fontSize: 12, fontFace: "{MY}", color: {A}, align: "center", valign: "middle" }});',
    f'  slide.addText("FundusAI-Edu", {{ x: 0.8, y: 1.4, w: 8.5, h: 1.4, fontSize: 56, fontFace: "Arial", color: "FFFFFF", bold: true, align: "left", valign: "bottom" }});',
    f'  slide.addText("眼底图像 AI 教学与科研辅助平台", {{ x: 0.8, y: 2.8, w: 8.5, h: 0.7, fontSize: 26, fontFace: "{MY}", color: "FFFFFF", align: "left", valign: "top" }});',
    f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.8, y: 3.6, w: 2.5, h: 0.04, fill: {{ color: {A} }} }});',
    f'  slide.addText("第一部分：案例概述 · 应用场景与核心问题", {{ x: 0.8, y: 3.9, w: 6.5, h: 0.6, fontSize: 14, fontFace: "{MY}", color: {S}, align: "left" }});',
    f'  slide.addText("2026年6月  |  申报学段: 高等教育  |  案例类别: 智能信息系统", {{ x: 0.8, y: 5.1, w: 5, h: 0.35, fontSize: 11, fontFace: "{MY}", color: "8899AA", align: "left" }});',
], pg=None)


# ═══════════════ SLIDE 02 · 三大痛点 ═══════════════
s02 = [
    top_bar(),
    navy_tag("案例概述 · 应用场景"),
    title_t("医学AI教学中的三大痛点"),
    sub("传统教学中，学生难以接触真实的AI分析工具，理论与实践严重脱节"),
]
# 3 pain cards
pain_data = [
    ("01","工具门槛高","GPU服务器昂贵\\n深度学习框架配置复杂\\n学生难以独立完成实验"),
    ("02","理论脱离实践","以PPT讲授为主\\n缺少动手操作机会\\n无法直观感受AI效果"),
    ("03","科研流程断裂","从选题到论文写作\\n缺乏系统化工具支撑\\n效率低下且方向迷茫"),
]
for j,(num,ptitle,pdesc) in enumerate(pain_data):
    x = 0.5 + j*3.1
    s02.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: {x}, y: 2.0, w: 2.9, h: 2.9, fill: {{ color: {L} }} }});')
    s02.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: {x}, y: 2.0, w: 2.9, h: 0.06, fill: {{ color: {A} }} }});')
    s02.append(f'  slide.addText("{num}", {{ x: {x+0.2}, y: 2.2, w: 0.8, h: 0.5, fontSize: 36, fontFace: "Arial", color: {T}, bold: true }});')
    s02.append(f'  slide.addText("{ptitle}", {{ x: {x+0.2}, y: 2.7, w: 2.5, h: 0.45, fontSize: 17, fontFace: "{MY}", color: {T}, bold: true }});')
    s02.append(f'  slide.addText("{pdesc}", {{ x: {x+0.2}, y: 3.2, w: 2.5, h: 1.4, fontSize: 11, fontFace: "{MY}", color: "555555", lineSpacingMultiple: 1.5 }});')
s02.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.5, y: 5.05, w: 9, h: 0.42, fill: {{ color: {T} }} }});')
s02.append(f'  slide.addText("应用场景: 医学教学课堂演示  ·  学生自主实验  ·  科研起步训练  ·  论文写作辅助", {{ x: 0.7, y: 5.05, w: 8.6, h: 0.42, fontSize: 13, fontFace: "{MY}", color: {A}, bold: true, align: "center", valign: "middle" }});')
write_slide("02", s02, pg="2")


# ═══════════════ SLIDE 03 · 解决方案 ═══════════════
s03 = [
    top_bar(), navy_tag("案例概述 · 解决问题"),
    title_t("借助AI跨越技术鸿沟"),
    sub("对标评分标准: 有效解决问题(40分) + 操作简单易用(40分)"),
]
sol_data = [
    ("工具门槛高,配置复杂","Web浏览器即用,一键启动,无需Python环境"),
    ("理论讲授为主,缺乏动手实践","上传眼底图像即可完成AI分析全流程实验"),
    ("科研选题无从下手","AI智能推荐个性化选题+研究方案+论文辅助"),
    ("学习效果难以量化评估","自动追踪学习行为,生成六维学习画像"),
]
for j,(prob,solu) in enumerate(sol_data):
    y = 2.0 + j*0.85
    s03.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.5, y: {y}, w: 9, h: 0.7, fill: {{ color: {L} }} }});')
    s03.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.5, y: {y}, w: 0.08, h: 0.7, fill: {{ color: "AA3333" }} }});')
    s03.append(f'  slide.addText("{prob}", {{ x: 0.8, y: {y}, w: 3.0, h: 0.7, fontSize: 13, fontFace: "{MY}", color: "AA3333", bold: true, valign: "middle" }});')
    s03.append(f'  slide.addText(">>", {{ x: 3.9, y: {y}, w: 0.4, h: 0.7, fontSize: 18, fontFace: "Arial", color: {A}, bold: true, align: "center", valign: "middle" }});')
    s03.append(f'  slide.addText("{solu}", {{ x: 4.4, y: {y}, w: 4.9, h: 0.7, fontSize: 13, fontFace: "{MY}", color: {T}, bold: true, valign: "middle" }});')
s03.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.5, y: 5.15, w: 9, h: 0.32, fill: {{ color: {T} }} }});')
s03.append(f'  slide.addText("核心理念: 让每一个医学师生都能亲手操作AI -- 从图像分析到科研全流程智能化", {{ x: 0.7, y: 5.15, w: 8.6, h: 0.32, fontSize: 12, fontFace: "{MY}", color: {A}, align: "center", valign: "middle" }});')
write_slide("03", s03, pg="3")


# ═══════════════ SLIDE 04 · 平台总览 ═══════════════
s04 = [
    top_bar(), navy_tag("案例概述 · 平台总览"),
    title_t("六大功能模块,覆盖医学科研全流程"),
    sub("集成深度学习,图论分析,大语言模型等能力的眼底图像AI教学平台"),
]
mods = [
    ("\U0001f52c","眼底图像智能分析","U-Net血管分割\\n病变识别与可视化"),
    ("\U0001f310","血管拓扑特征分析","六维特征提取\\n雷达图+临床解读"),
    ("\U0001f916","AI科研导师","RAG医学知识问答\\n多轮对话专业指导"),
    ("\U0001f3af","科研选题生成器","AI推荐个性化选题\\n研究方案+实验报告"),
    ("\U0001f4dd","论文写作辅助","框架生成+章节写作\\n润色+期刊推荐"),
    ("\U0001f4ca","学习分析","行为追踪与可视化\\n个人学习画像"),
]
for i,(emoji,mtitle,mdesc) in enumerate(mods):
    x = 0.5 + (i%3)*3.1
    y = 1.95 + (i//3)*1.85
    s04.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: {x}, y: {y}, w: 2.9, h: 1.65, fill: {{ color: {L} }} }});')
    s04.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: {x}, y: {y}, w: 0.08, h: 1.65, fill: {{ color: {A} }} }});')
    s04.append(f'  slide.addText("{emoji}", {{ x: {x+0.25}, y: {y+0.1}, w: 0.6, h: 0.4, fontSize: 24 }});')
    s04.append(f'  slide.addText("{mtitle}", {{ x: {x+0.9}, y: {y+0.1}, w: 1.8, h: 0.4, fontSize: 14, fontFace: "{MY}", color: {T}, bold: true, valign: "middle" }});')
    s04.append(f'  slide.addText("{mdesc}", {{ x: {x+0.25}, y: {y+0.6}, w: 2.4, h: 0.85, fontSize: 10.5, fontFace: "{MY}", color: "555555", lineSpacingMultiple: 1.5 }});')
s04.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.5, y: 5.15, w: 9, h: 0.32, fill: {{ color: {A} }}, opacity: 0.15 }});')
s04.append(f'  slide.addText("案例概述(~2min)  >>>  实现功能(~5min)  >>>  应用情况(~1min)", {{ x: 0.7, y: 5.15, w: 8.6, h: 0.32, fontSize: 11, fontFace: "{MY}", color: {T}, bold: true, align: "center", valign: "middle" }});')
write_slide("04", s04, pg="4")


# ═══════════════ SLIDE 05 · 眼底图像分析 ═══════════════
s05 = [
    top_bar(), gold_tag("实现功能 · 核心功能演示"),
    title_t("眼底图像智能分析"),
    sub("上传眼底照片,AI自动完成血管分割,病变识别与拓扑特征提取"),
]
feats = [
    ("\U0001fa78 血管分割","U-Net深度学习+多尺度\\nFrangi增强,精准提取"),
    ("\U0001f50e 病变识别","HSV色彩空间规则引擎\\nDR四等级自动分级"),
    ("\U0001f310 拓扑分析","六维特征:密度/分叉/\\n迂曲度/分形维数"),
]
for i,(fn,fdesc) in enumerate(feats):
    x = 0.5 + i*3.1
    s05.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: {x}, y: 1.9, w: 2.9, h: 1.0, fill: {{ color: {L} }} }});')
    s05.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: {x}, y: 1.9, w: 0.06, h: 1.0, fill: {{ color: {A} }} }});')
    s05.append(f'  slide.addText("{fn}", {{ x: {x+0.2}, y: 1.93, w: 2.5, h: 0.35, fontSize: 14, fontFace: "{MY}", color: {T}, bold: true }});')
    s05.append(f'  slide.addText("{fdesc}", {{ x: {x+0.2}, y: 2.28, w: 2.5, h: 0.55, fontSize: 10.5, fontFace: "{MY}", color: "555555", lineSpacingMultiple: 1.3 }});')
# Screenshot
s05.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.5, y: 3.1, w: 5.6, h: 2.2, fill: {{ color: {L} }} }});')
s05.append(f'  slide.addImage({{ path: "imgs/ui_01_upload.png", x: 0.55, y: 3.15, w: 5.5, h: 2.1 }});')
s05.append(f'  slide.addText("▲ 支持JPG/PNG/BMP/TIFF, 左侧上传>>右侧三标签结果切换", {{ x: 0.5, y: 5.3, w: 5.6, h: 0.2, fontSize: 9, fontFace: "{MY}", color: "AAAAAA", italic: true }});')
# Process steps on right
s05.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 6.3, y: 3.1, w: 3.2, h: 2.2, fill: {{ color: {T} }} }});')
s05.append(f'  slide.addText("应用流程", {{ x: 6.5, y: 3.2, w: 2.8, h: 0.35, fontSize: 14, fontFace: "{MY}", color: {A}, bold: true }});')
for i,step in enumerate(["上传眼底图像","点击[开始分析]","查看血管分割掩码","查看DR分级结果","查看六维拓扑特征"]):
    s05.append(f'  slide.addText("{i+1}. {step}", {{ x: 6.5, y: {3.6+i*0.42}, w: 2.8, h: 0.35, fontSize: 11, fontFace: "{MY}", color: "FFFFFF", valign: "middle" }});')
write_slide("05", s05, pg="5")


# ═══════════════ SLIDE 06 · 分析结果 ═══════════════
s06 = [
    top_bar(), gold_tag("实现功能 · 分析结果"),
    title_t("DR分级 + 六维拓扑特征"),
    sub("分析完成后,系统自动生成三标签结果: 血管分割 | 病变识别 | 拓扑特征"),
    f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.5, y: 1.9, w: 4.4, h: 2.8, fill: {{ color: {L} }} }});',
    f'  slide.addText("病变识别结果", {{ x: 0.6, y: 1.95, w: 3, h: 0.35, fontSize: 14, fontFace: "{MY}", color: {T}, bold: true }});',
    f'  slide.addImage({{ path: "imgs/ui_02_lesion.png", x: 0.55, y: 2.35, w: 4.3, h: 2.3 }});',
    f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 5.1, y: 1.9, w: 4.4, h: 2.8, fill: {{ color: {L} }} }});',
    f'  slide.addText("六维拓扑特征", {{ x: 5.2, y: 1.95, w: 3, h: 0.35, fontSize: 14, fontFace: "{MY}", color: {T}, bold: true }});',
    f'  slide.addImage({{ path: "imgs/ui_04_topo2.png", x: 5.15, y: 2.35, w: 4.3, h: 2.3 }});',
    f'  slide.addText("▲ Severe DR分级+出血/渗出风险量化评估", {{ x: 0.5, y: 4.75, w: 4.4, h: 0.25, fontSize: 9, fontFace: "{MY}", color: "AAAAAA", italic: true }});',
    f'  slide.addText("▲ 密度/分叉点/宽度/迂曲度/分形维数+临床参考范围", {{ x: 5.1, y: 4.75, w: 4.4, h: 0.25, fontSize: 9, fontFace: "{MY}", color: "AAAAAA", italic: true }});',
    f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.5, y: 5.05, w: 9, h: 0.42, fill: {{ color: {T} }} }});',
    f'  slide.addText("每个特征均附有正常参考范围,辅助医学教学中的定量分析与病理理解", {{ x: 0.7, y: 5.05, w: 8.6, h: 0.42, fontSize: 12, fontFace: "{MY}", color: "FFFFFF", align: "center", valign: "middle" }});',
]
write_slide("06", s06, pg="6")


# ═══════════════ SLIDE 07 · AI科研辅助 ═══════════════
s07 = [
    top_bar(), gold_tag("实现功能 · AI科研辅助"),
    title_t("从知识问答到选题论文,AI全链路赋能"),
    sub("基于DeepSeek大语言模型+ChromaDB向量知识库,提供RAG增强的科研智能服务"),
]
imgs = [
    ("imgs/ui_07_topic.png","科研选题生成器","个性化选题推荐\\n研究方案+实验报告"),
    ("imgs/ui_05_api.png","AI科研导师","RAG医学知识问答\\n多轮对话+文献引用"),
    ("imgs/ui_06_learning.png","论文写作辅助","框架生成+章节写作\\n润色+期刊推荐"),
]
for i,(img,ctitle,cdesc) in enumerate(imgs):
    x = 0.5 + i*3.2
    s07.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: {x}, y: 1.95, w: 3.0, h: 3.0, fill: {{ color: {L} }} }});')
    s07.append(f'  slide.addImage({{ path: "{img}", x: {x+0.05}, y: 1.98, w: 2.9, h: 1.95 }});')
    s07.append(f'  slide.addText("{ctitle}", {{ x: {x+0.1}, y: 4.05, w: 2.8, h: 0.35, fontSize: 13, fontFace: "{MY}", color: {T}, bold: true, align: "center" }});')
    s07.append(f'  slide.addText("{cdesc}", {{ x: {x+0.1}, y: 4.35, w: 2.8, h: 0.5, fontSize: 10, fontFace: "{MY}", color: "666666", align: "center", lineSpacingMultiple: 1.3 }});')
s07.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.5, y: 5.1, w: 9, h: 0.35, fill: {{ color: {T} }} }});')
s07.append(f'  slide.addText("所有AI功能均需配置DeepSeek API Key(侧边栏即可完成)", {{ x: 0.7, y: 5.1, w: 8.6, h: 0.35, fontSize: 12, fontFace: "{MY}", color: "FFFFFF", align: "center", valign: "middle" }});')
write_slide("07", s07, pg="7")


# ═══════════════ SLIDE 08 · AI赋能开发 ═══════════════
s08 = [
    top_bar(), gold_tag("实现功能 · 开发过程"),
    title_t("借助DeepSeek跨越技术鸿沟"),
    sub("生成式AI辅助需求分析,架构设计,编码实现,测试迭代,文档生成全过程"),
    f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 1.5, y: 3.0, w: 7, h: 0.03, fill: {{ color: {S} }}, opacity: 0.4 }});',
]
steps = [
    ("01","需求分析","DeepSeek协助梳理\\n医学AI教学痛点\\n与功能需求"),
    ("02","架构设计","AI生成三层架构\\nU-Net+RAG+LLM\\n技术栈选型方案"),
    ("03","编码实现","DeepSeek辅助编写\\n3000+行Python\\n全栈代码调试"),
    ("04","测试迭代","Bug修复+UI优化\\n7轮反馈改进\\n持续打磨细节"),
    ("05","文档部署","AI自动生成手册\\nPyInstaller EXE打包\\npywebview桌面版"),
]
for i,(sn,stitle,sdesc) in enumerate(steps):
    xx = 0.8 + i*1.85
    c = A if i==2 else S
    s08.append(f'  slide.addShape(pres.shapes.OVAL, {{ x: {xx+0.5}, y: 2.85, w: 0.35, h: 0.35, fill: {{ color: {c} }} }});')
    s08.append(f'  slide.addText("{sn}", {{ x: {xx+0.5}, y: 2.85, w: 0.35, h: 0.35, fontSize: 10, fontFace: "Arial", color: "FFFFFF", bold: true, align: "center", valign: "middle" }});')
    s08.append(f'  slide.addText("{stitle}", {{ x: {xx}, y: 3.35, w: 1.7, h: 0.35, fontSize: 14, fontFace: "{MY}", color: {T}, bold: true, align: "center" }});')
    s08.append(f'  slide.addText("{sdesc}", {{ x: {xx}, y: 3.7, w: 1.7, h: 0.85, fontSize: 10, fontFace: "{MY}", color: "555555", align: "center", lineSpacingMultiple: 1.4 }});')
s08.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.5, y: 4.8, w: 9, h: 0.5, fill: {{ color: {T} }} }});')
s08.append(f'  slide.addText("Python · Streamlit · PyTorch(U-Net) · DeepSeek(LLM) · ChromaDB(RAG) · NetworkX · pywebview", {{ x: 0.7, y: 4.8, w: 8.6, h: 0.5, fontSize: 11, fontFace: "{MY}", color: "FFFFFF", align: "center", valign: "middle" }});')
write_slide("08", s08, pg="8")


# ═══════════════ SLIDE 09 · 技术架构 ═══════════════
s09 = [
    top_bar(), gold_tag("实现功能 · 技术架构"),
    title_t("面向教学场景的三层松耦合架构"),
    sub("所有核心能力均封装为独立模块,降低学习成本,便于二次开发和教学演示"),
]
layers = [
    ("应用层", S, ["Streamlit Web界面","深色主题+侧边栏导航","实时分析进度+结果切换"]),
    ("AI层", A, ["U-Net血管分割","DeepSeek RAG问答","LLM选题/论文辅助"]),
    ("数据层", T, ["SQLite学习行为库","ChromaDB向量知识库","PyTorch CPU推理"]),
]
for i,(lname,lc,ltechs) in enumerate(layers):
    y = 1.95 + i*1.12
    s09.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.8, y: {y}, w: 8.4, h: 0.95, fill: {{ color: {lc} }}, opacity: 0.08 }});')
    s09.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.8, y: {y}, w: 1.3, h: 0.95, fill: {{ color: {lc} }} }});')
    s09.append(f'  slide.addText("{lname}", {{ x: 0.8, y: {y}, w: 1.3, h: 0.5, fontSize: 15, fontFace: "{MY}", color: "FFFFFF", bold: true, align: "center", valign: "middle" }});')
    s09.append(f'  slide.addText("L{3-i}", {{ x: 0.8, y: {y+0.5}, w: 1.3, h: 0.35, fontSize: 10, fontFace: "Arial", color: "FFFFFF", align: "center", valign: "middle", opacity: 0.7 }});')
    for j,t in enumerate(ltechs):
        s09.append(f'  slide.addText("• {t}", {{ x: {2.4+j*2.5}, y: {y+0.08}, w: 2.3, h: 0.8, fontSize: 10.5, fontFace: "{MY}", color: {T}, valign: "middle" }});')
s09.append(f'  slide.addText("无需GPU · 浏览器即用 · MIT开源 · 完整文档 · 可复现", {{ x: 0.5, y: 5.15, w: 9, h: 0.32, fontSize: 12, fontFace: "{MY}", color: {A}, bold: true, align: "center" }});')
write_slide("09", s09, pg="9")


# ═══════════════ SLIDE 10 · 应用成效 ═══════════════
s10 = [
    top_bar(), navy_tag("应用情况 · 应用成效"),
    title_t("从理论教学到动手实践的跨越"),
    sub("安装简单,上手快,覆盖全流程,开源可复现 -- 四大维度衡量应用价值"),
]
metrics = [
    ("5 min","上手时间","安装到首次分析",A),
    ("6","功能模块","覆盖全链条科研",S),
    ("0","GPU依赖","CPU即可运行",T),
    ("100%","开源可复现","代码+文档齐全",A),
]
for i,(mv,ml,md,mc) in enumerate(metrics):
    x = 0.7 + i*2.3
    s10.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: {x}, y: 1.95, w: 2.0, h: 2.6, fill: {{ color: {L} }} }});')
    s10.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: {x}, y: 1.95, w: 2.0, h: 0.06, fill: {{ color: {mc} }} }});')
    s10.append(f'  slide.addText("{mv}", {{ x: {x}, y: 2.15, w: 2.0, h: 1.1, fontSize: 36, fontFace: "Arial", color: {mc}, bold: true, align: "center", valign: "middle" }});')
    s10.append(f'  slide.addText("{ml}", {{ x: {x}, y: 3.3, w: 2.0, h: 0.45, fontSize: 16, fontFace: "{MY}", color: {T}, bold: true, align: "center", valign: "middle" }});')
    s10.append(f'  slide.addText("{md}", {{ x: {x}, y: 3.8, w: 2.0, h: 0.4, fontSize: 11, fontFace: "{MY}", color: "777777", align: "center" }});')
s10.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.5, y: 4.75, w: 9, h: 0.6, fill: {{ color: {T} }} }});')
s10.append(f'  slide.addText("对软硬件要求低,安装容易;操作简单,使用门槛低 -- 创AI评价标准 操作简单易用(40分)", {{ x: 0.7, y: 4.75, w: 8.6, h: 0.6, fontSize: 13, fontFace: "{MY}", color: "FFFFFF", align: "center", valign: "middle" }});')
write_slide("10", s10, pg="10")


# ═══════════════ SLIDE 11 · 创新亮点 ═══════════════
s11 = [
    f'  slide.background = {{ color: {T} }};',
    top_bar(),
    gold_tag("应用情况 · 创新与影响力"),
    f'  slide.addText("三个维度,重新定义医学AI教学", {{ x: 0.5, y: 0.85, w: 9, h: 0.6, fontSize: 28, fontFace: "{MY}", color: "FFFFFF", bold: true }});',
]
inno = [
    ("01","多学科交叉融合","眼科医学 x 深度学习 x 图论拓扑学 -- U-Net + Frangi + NetworkX协同创新"),
    ("02","AI赋能全流程开发","DeepSeek全程辅助需求>架构>编码>测试>文档,跨越技能限制,体现终身学习"),
    ("03","零门槛可复现","CPU运行+浏览器即用+EXE桌面版+三份完整文档+MIT开源协议"),
]
for i,(num,intitle,indesc) in enumerate(inno):
    y = 1.65 + i*1.15
    s11.append(f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.8, y: {y}, w: 8.4, h: 1.02, fill: {{ color: "FFFFFF" }}, opacity: 0.07 }});')
    s11.append(f'  slide.addText("{num}", {{ x: 1.0, y: {y}, w: 1.0, h: 0.45, fontSize: 28, fontFace: "Arial", color: {A}, bold: true, valign: "middle" }});')
    s11.append(f'  slide.addText("{intitle}", {{ x: 2.0, y: {y}, w: 3.0, h: 0.45, fontSize: 18, fontFace: "{MY}", color: "FFFFFF", bold: true, valign: "middle" }});')
    s11.append(f'  slide.addText("{indesc}", {{ x: 1.0, y: {y+0.55}, w: 8.0, h: 0.45, fontSize: 11, fontFace: "{MY}", color: "CCCCCC" }});')
s11.append(f'  slide.addText("对标评分: 导向性(40)+实用性(80)+影响力(40)+创新性(10)+完整性(10)=180分", {{ x: 0.5, y: 5.05, w: 9, h: 0.35, fontSize: 12, fontFace: "{MY}", color: {A}, bold: true, align: "center" }});')
s11.append(f'  slide.addShape(pres.shapes.OVAL, {{ x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: {{ color: {A} }} }});')
s11.append(f'  slide.addText("11", {{ x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "0B1D3A", bold: true, align: "center", valign: "middle" }});')
s11.append(f'  return slide;')
s11.append(f'}}')
s11.append(f'module.exports = {{ createSlide }};')
# s11 has custom badge, write directly
path11 = os.path.join(SLIDES_DIR, "slide-11.js")
header11 = HEADER.replace('{num}', "11")
with open(path11, 'w', encoding='utf-8') as f:
    f.write(header11 + '\n'.join(s11))
print(f"  [OK] slide-11.js  [应用情况]  创新与影响力")


# ═══════════════ SLIDE 12 · 感谢页 ═══════════════
s12 = [
    f'  slide.background = {{ color: {T} }};',
    f'  slide.addShape(pres.shapes.OVAL, {{ x: -1.5, y: 3.5, w: 5, h: 5, fill: {{ color: {A} }}, opacity: 0.06 }});',
    f'  slide.addShape(pres.shapes.OVAL, {{ x: 7.5, y: -1.5, w: 4, h: 4, fill: {{ color: {S} }}, opacity: 0.05 }});',
    f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0, y: 0, w: 0.1, h: 5.625, fill: {{ color: {A} }} }});',
    f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.8, y: 0.7, w: 2.2, h: 0.35, fill: {{ color: {A} }}, opacity: 0.15 }});',
    f'  slide.addText("创AI案例征集 · 智能信息系统", {{ x: 0.8, y: 0.7, w: 2.2, h: 0.35, fontSize: 11, fontFace: "{MY}", color: {A}, align: "center", valign: "middle" }});',
    f'  slide.addText("谢谢观看", {{ x: 0.8, y: 1.2, w: 8.5, h: 1.0, fontSize: 52, fontFace: "{MY}", color: "FFFFFF", bold: true, align: "left", valign: "bottom" }});',
    f'  slide.addShape(pres.shapes.RECTANGLE, {{ x: 0.8, y: 2.3, w: 2.5, h: 0.04, fill: {{ color: {A} }} }});',
    f'  slide.addText("FundusAI-Edu · 眼底图像AI教学与科研辅助平台", {{ x: 0.8, y: 2.6, w: 8.5, h: 0.55, fontSize: 22, fontFace: "{MY}", color: {S}, align: "left" }});',
    f'  slide.addText("案例类别: 智能信息系统  |  申报学段: 高等教育  |  适用: 高职高专/本科/硕士/博士", {{ x: 0.8, y: 3.4, w: 8.5, h: 0.35, fontSize: 13, fontFace: "{MY}", color: "AAAAAA", align: "left" }});',
    f'  slide.addText("配套资源: 完整代码 + 使用手册 + 安装手册 + 开发记录 + 演示视频", {{ x: 0.8, y: 3.85, w: 8.5, h: 0.35, fontSize: 14, fontFace: "{MY}", color: {A}, bold: true, align: "left" }});',
    f'  slide.addText("借助生成式人工智能赋能开发,跨越自身专业与技能限制,体现终身学习", {{ x: 0.8, y: 4.4, w: 6.5, h: 0.4, fontSize: 12, fontFace: "{MY}", color: "888888", italic: true, align: "left" }});',
    f'  slide.addText("MIT开源许可  ·  支持复现验证  ·  2026年6月", {{ x: 0.8, y: 5.1, w: 5, h: 0.35, fontSize: 11, fontFace: "{MY}", color: "667788", align: "left" }});',
    f'  slide.addShape(pres.shapes.OVAL, {{ x: 9.3, y: 5.1, w: 0.4, h: 0.4, fill: {{ color: {A} }} }});',
    f'  slide.addText("12", {{ x: 9.3, y: 5.1, w: 0.4, h: 0.4, fontSize: 12, fontFace: "Arial", color: "0B1D3A", bold: true, align: "center", valign: "middle" }});',
    f'  return slide;',
    f'}}',
    f'module.exports = {{ createSlide }};',
]
path12 = os.path.join(SLIDES_DIR, "slide-12.js")
header12 = HEADER.replace('{num}', "12")
with open(path12, 'w', encoding='utf-8') as f:
    f.write(header12 + '\n'.join(s12))
print(f"  [OK] slide-12.js  [应用情况]  感谢页")


print(f"\n[DONE] 12 slides generated with 3-part competition video structure.")
print(f"Part 1: 案例概述 (Slides 1-4)  ~2 min")
print(f"Part 2: 实现功能 (Slides 5-9)  ~5 min")
print(f"Part 3: 应用情况 (Slides 10-12) ~1 min")
