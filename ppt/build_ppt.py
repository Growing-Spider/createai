#!/usr/bin/env python
# -*- coding: utf-8 -*-
# build_ppt.py — 生成创AI竞赛优化的瑞士风格Web PPT
# 读取 template-swiss.html，替换标题 + 主题 + 幻灯片内容

import os

TEMPLATE = r"F:\demo\ppt\index.html"
OUTPUT   = r"F:\demo\ppt\index.html"

# ── 主题: IKB 克莱因蓝（默认已匹配，无需改） ──

# ── 幻灯片 HTML ──
SLIDES = r'''
<!-- ============ 01 封面 · Hero Cover ============ -->
<section class="slide accent" data-animate="hero" data-layout="S01">
  <div class="canvas-card">
    <canvas class="ascii-bg" aria-hidden="true"></canvas>
    <div class="chrome-min">
      <div class="l">创AI案例 · 智能信息系统</div>
      <div class="r">01 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr auto;gap:2.6vh">
      <div data-anim="kicker" class="t-meta" style="color:rgba(255,255,255,.78);letter-spacing:.22em">FUNDUSAI-EDU · FIELD NOTE 2026</div>
      <h1 data-anim="title" style="align-self:center;font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(10.4vw,17vh);line-height:.94;letter-spacing:-.025em;color:#fff">
        Fundus<span style="font-style:italic;font-weight:300">AI</span>-Edu<br/>
      </h1>
      <div data-anim="bottom" style="display:grid;grid-template-rows:auto auto;gap:1.6vh;border-top:1px solid rgba(255,255,255,.22);padding-top:2vh">
        <div data-anim="lead" class="lead" style="max-width:52ch;color:rgba(255,255,255,.86);font-weight:300">眼底图像 AI 教学与科研辅助平台 — 从图像分析到科研全流程智能化</div>
        <div style="display:flex;justify-content:space-between;align-items:end">
          <div class="t-meta" style="color:rgba(255,255,255,.6)">案例类别: 智能信息系统 · 高等教育</div>
          <div class="t-meta" style="color:rgba(255,255,255,.6)">2026.06</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ 02 开发背景 · 传统教学痛点 vs AI方案 ============ -->
<section class="slide duo-compare" data-animate="duo-reveal" data-layout="S08">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">开发背景 · BACKGROUND</div>
      <div class="r">02 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:grid;grid-template-columns:1fr 1px 1fr;gap:3.6vw;align-items:start">
      <div data-anim="left" style="display:flex;flex-direction:column;gap:3vh">
        <div class="t-cat" style="color:var(--text-secondary)">BEFORE · 传统教学痛点</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(4.6vw,8.5vh);line-height:1.1;letter-spacing:-.02em;color:var(--text-primary)">高门槛<br/>缺工具<br/>难上手</h2>
        <div style="display:flex;flex-direction:column;gap:2vh;margin-top:1.6vh">
          <div class="card-outlined" style="padding:var(--sp-6);background:var(--grey-1)">
            <div style="font-weight:400;font-size:max(12px,1vw);line-height:1.5;color:var(--text-secondary)">
              <span style="font-weight:600;color:var(--text-primary)">硬件昂贵</span><br/>眼底照相机 + GPU 服务器成本高昂
            </div>
          </div>
          <div class="card-outlined" style="padding:var(--sp-6);background:var(--grey-1)">
            <div style="font-weight:400;font-size:max(12px,1vw);line-height:1.5;color:var(--text-secondary)">
              <span style="font-weight:600;color:var(--text-primary)">软件复杂</span><br/>深度学习框架配置繁琐,依赖管理困难
            </div>
          </div>
          <div class="card-outlined" style="padding:var(--sp-6);background:var(--grey-1)">
            <div style="font-weight:400;font-size:max(12px,1vw);line-height:1.5;color:var(--text-secondary)">
              <span style="font-weight:600;color:var(--text-primary)">教学脱节</span><br/>理论讲授为主,学生缺少动手实践机会
            </div>
          </div>
        </div>
      </div>
      <div class="vrule" style="background:var(--border-subtle);height:100%"></div>
      <div data-anim="right" style="display:flex;flex-direction:column;gap:3vh">
        <div class="t-cat" style="color:var(--accent)">AFTER · AI 赋能解决方案</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(4.6vw,8.5vh);line-height:1.1;letter-spacing:-.02em;color:var(--accent)">一站式<br/>自动化<br/>可复现</h2>
        <div style="display:flex;flex-direction:column;gap:2vh;margin-top:1.6vh">
          <div class="card-accent" style="padding:var(--sp-6);background:var(--accent);color:var(--accent-on)">
            <div style="font-weight:400;font-size:max(12px,1vw);line-height:1.5">
              <span style="font-weight:600">Web 浏览器即用</span><br/>无需 GPU,Streamlit 一键启动
            </div>
          </div>
          <div class="card-accent" style="padding:var(--sp-6);background:var(--accent);color:var(--accent-on)">
            <div style="font-weight:400;font-size:max(12px,1vw);line-height:1.5">
              <span style="font-weight:600">AI 辅助全流程</span><br/>血管分割→病变识别→拓扑分析→科研辅助
            </div>
          </div>
          <div class="card-accent" style="padding:var(--sp-6);background:var(--accent);color:var(--accent-on)">
            <div style="font-weight:400;font-size:max(12px,1vw);line-height:1.5">
              <span style="font-weight:600">完整文档体系</span><br/>代码 + 使用手册 + 安装手册 + 开发记录
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ 03 核心宣言 ============ -->
<section class="slide dark" data-animate="hero" data-layout="S09">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">CORE MANIFESTO</div>
      <div class="r">03 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:flex;flex-direction:column;justify-content:center;gap:4vh">
      <div data-anim="statement" style="display:flex;flex-direction:column;gap:2vh">
        <div class="t-meta" style="color:rgba(255,255,255,.5)">借助生成式 AI 跨越技术门槛</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(7.2vw,12.5vh);line-height:.96;letter-spacing:-.025em;color:#fff">让每一个医学师生<br/>都能<span style="color:var(--accent-bright);font-style:italic;font-weight:300">亲手操作</span> AI</h2>
        <div data-anim="kicker" class="lead" style="color:rgba(255,255,255,.7);font-weight:300;max-width:52ch;margin-top:2vh">
          借助 DeepSeek + ChromaDB + U-Net 构建一站式眼底图像分析教学平台,覆盖从图像处理到科研选题的全流程智能化。
        </div>
      </div>
      <div data-anim="stats" style="display:grid;grid-template-columns:repeat(4,1fr);gap:2vw;margin-top:3vh">
        <div style="border-top:2px solid var(--accent-bright);padding-top:1.6vh">
          <div class="kpi-mid" style="font-size:min(4.8vw,8vh);color:var(--accent-bright)">6</div>
          <div class="body-sm" style="color:rgba(255,255,255,.65)">功能模块</div>
        </div>
        <div style="border-top:2px solid rgba(255,255,255,.25);padding-top:1.6vh">
          <div class="kpi-mid" style="font-size:min(4.8vw,8vh);color:#fff">3</div>
          <div class="body-sm" style="color:rgba(255,255,255,.65)">核心技术</div>
        </div>
        <div style="border-top:2px solid rgba(255,255,255,.25);padding-top:1.6vh">
          <div class="kpi-mid" style="font-size:min(4.8vw,8vh);color:#fff">100%</div>
          <div class="body-sm" style="color:rgba(255,255,255,.65)">开源可复现</div>
        </div>
        <div style="border-top:2px solid rgba(255,255,255,.25);padding-top:1.6vh">
          <div class="kpi-mid" style="font-size:min(4.8vw,8vh);color:#fff">0</div>
          <div class="body-sm" style="color:rgba(255,255,255,.65)">GPU 依赖</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ 04 六大功能全景 ============ -->
<section class="slide light" data-animate="grid-reveal" data-layout="S19">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">功能全景 · FEATURES</div>
      <div class="r">04 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr;gap:3vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:1vh">
        <div class="t-meta">SIX MODULES</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(5.2vw,9vh);line-height:1.05;letter-spacing:-.02em;color:var(--text-primary)">六大功能模块,覆盖<br/>医学科研<span style="color:var(--accent);font-weight:300">全流程</span></h2>
      </div>
      <div data-anim="items" class="grid-3" style="align-items:start;justify-items:stretch">
        <div class="card-fill" style="padding:var(--sp-6);background:var(--grey-1);border-left:3px solid var(--accent)">
          <div style="font-size:2rem;margin-bottom:1vh">🔬</div>
          <h3 style="font-weight:400;font-size:max(15px,1.3vw);color:var(--text-primary);margin-bottom:.6vh">眼底图像智能分析</h3>
          <p class="body-sm" style="color:var(--text-secondary)">U-Net 血管分割 + HSV 病变识别 + 可视化报告</p>
        </div>
        <div class="card-fill" style="padding:var(--sp-6);background:var(--grey-1);border-left:3px solid var(--accent)">
          <div style="font-size:2rem;margin-bottom:1vh">🌐</div>
          <h3 style="font-weight:400;font-size:max(15px,1.3vw);color:var(--text-primary);margin-bottom:.6vh">血管拓扑特征分析</h3>
          <p class="body-sm" style="color:var(--text-secondary)">六维特征提取 + 雷达图 + 临床意义解读</p>
        </div>
        <div class="card-fill" style="padding:var(--sp-6);background:var(--grey-1);border-left:3px solid var(--accent)">
          <div style="font-size:2rem;margin-bottom:1vh">🤖</div>
          <h3 style="font-weight:400;font-size:max(15px,1.3vw);color:var(--text-primary);margin-bottom:.6vh">AI 科研导师</h3>
          <p class="body-sm" style="color:var(--text-secondary)">RAG 医学知识问答 + 多轮对话 + 专业指导</p>
        </div>
        <div class="card-fill" style="padding:var(--sp-6);background:var(--grey-1);border-left:3px solid var(--accent)">
          <div style="font-size:2rem;margin-bottom:1vh">🎯</div>
          <h3 style="font-weight:400;font-size:max(15px,1.3vw);color:var(--text-primary);margin-bottom:.6vh">科研选题生成器</h3>
          <p class="body-sm" style="color:var(--text-secondary)">个性化选题推荐 + 研究方案 + 实验报告</p>
        </div>
        <div class="card-fill" style="padding:var(--sp-6);background:var(--grey-1);border-left:3px solid var(--accent)">
          <div style="font-size:2rem;margin-bottom:1vh">📝</div>
          <h3 style="font-weight:400;font-size:max(15px,1.3vw);color:var(--text-primary);margin-bottom:.6vh">论文写作辅助</h3>
          <p class="body-sm" style="color:var(--text-secondary)">框架生成 + 章节写作 + 润色 + 期刊推荐</p>
        </div>
        <div class="card-fill" style="padding:var(--sp-6);background:var(--grey-1);border-left:3px solid var(--accent)">
          <div style="font-size:2rem;margin-bottom:1vh">📊</div>
          <h3 style="font-weight:400;font-size:max(15px,1.3vw);color:var(--text-primary);margin-bottom:.6vh">学习分析</h3>
          <p class="body-sm" style="color:var(--text-secondary)">行为统计 + 可视化 + 个人学习画像</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ 05 眼底图像分析 · 核心功能展示 ============ -->
<section class="slide light" data-animate="grid-reveal" data-layout="S22">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">核心功能 · CORE FEATURE</div>
      <div class="r">05 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr auto;gap:2.4vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:1vh">
        <div class="t-meta">IMAGE ANALYSIS</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(5vw,8.8vh);line-height:1.05;letter-spacing:-.02em;color:var(--text-primary)">眼底图像智能分析</h2>
        <p class="lead" style="color:var(--text-secondary);max-width:64ch">上传眼底照片,AI 自动完成<span style="color:var(--accent);font-weight:500">血管分割</span>、<span style="color:var(--accent);font-weight:500">病变识别</span>与<span style="color:var(--accent);font-weight:500">拓扑特征</span>提取,一站式分析报告</p>
      </div>
      <div data-anim="image" style="position:relative;overflow:hidden;border:1px solid var(--border-subtle)">
        <img src="images/ui_01_upload.png" style="width:100%;height:100%;object-fit:contain;object-position:center" alt="眼底图像智能分析界面">
      </div>
      <div data-anim="caption" style="display:flex;justify-content:space-between;align-items:center">
        <div class="body-sm" style="color:var(--text-helper)">▲ 支持 JPG/PNG/BMP/TIFF 格式,左侧上传,右侧实时查看分析结果</div>
        <div class="t-meta" style="color:var(--text-helper)">U-Net + HSV 色彩空间规则引擎</div>
      </div>
    </div>
  </div>
</section>

<!-- ============ 06 技术架构 · AI 赋能开发 ============ -->
<section class="slide dark" data-animate="grid-reveal" data-layout="S17">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">技术架构 · ARCHITECTURE</div>
      <div class="r">06 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr auto;gap:3vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:1.2vh">
        <div class="t-meta" style="color:rgba(255,255,255,.5)">AI-POWERED DEVELOPMENT</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(5vw,8.8vh);line-height:1.05;letter-spacing:-.02em;color:#fff">借助<span style="color:var(--accent-bright);font-style:italic;font-weight:300">生成式 AI</span>跨越技术鸿沟</h2>
      </div>
      <div data-anim="layers" style="display:flex;flex-direction:column;gap:0">
        <div style="display:grid;grid-template-columns:auto 1fr;gap:3vw;align-items:center;padding:2.4vh 0;border-top:1px solid rgba(255,255,255,.12);border-bottom:1px solid rgba(255,255,255,.12)">
          <div style="font-family:var(--mono);font-size:min(3.2vw,5.6vh);font-weight:200;color:var(--accent-bright);letter-spacing:-.03em">L3</div>
          <div>
            <h3 style="font-weight:400;font-size:max(15px,1.3vw);color:#fff;margin-bottom:.4vh">应用层 · Streamlit Web 界面</h3>
            <p class="body-sm" style="color:rgba(255,255,255,.6)">深色主题 · 侧边栏导航 · 实时分析进度 · 三标签结果切换</p>
          </div>
        </div>
        <div style="display:grid;grid-template-columns:auto 1fr;gap:3vw;align-items:center;padding:2.4vh 0;border-bottom:1px solid rgba(255,255,255,.12)">
          <div style="font-family:var(--mono);font-size:min(3.2vw,5.6vh);font-weight:200;color:var(--accent-bright);letter-spacing:-.03em">L2</div>
          <div>
            <h3 style="font-weight:400;font-size:max(15px,1.3vw);color:#fff;margin-bottom:.4vh">AI 层 · 深度学习 + 大语言模型</h3>
            <p class="body-sm" style="color:rgba(255,255,255,.6)">U-Net 血管分割 · 多尺度 Frangi 增强 · DeepSeek RAG 问答 · 选题/写作 LLM</p>
          </div>
        </div>
        <div style="display:grid;grid-template-columns:auto 1fr;gap:3vw;align-items:center;padding:2.4vh 0;border-bottom:1px solid rgba(255,255,255,.12)">
          <div style="font-family:var(--mono);font-size:min(3.2vw,5.6vh);font-weight:200;color:var(--accent-bright);letter-spacing:-.03em">L1</div>
          <div>
            <h3 style="font-weight:400;font-size:max(15px,1.3vw);color:#fff;margin-bottom:.4vh">数据层 · 存储与向量检索</h3>
            <p class="body-sm" style="color:rgba(255,255,255,.6)">SQLite 学习行为库 · ChromaDB 向量知识库 · PyTorch CPU 推理</p>
          </div>
        </div>
      </div>
      <div data-anim="footnote" style="display:grid;grid-template-columns:repeat(3,1fr);gap:2vw;border-top:1px solid rgba(255,255,255,.15);padding-top:2vh">
        <div class="body-sm" style="color:rgba(255,255,255,.5)"><span style="color:var(--accent-bright)">Python</span> 核心语言</div>
        <div class="body-sm" style="color:rgba(255,255,255,.5)"><span style="color:var(--accent-bright)">DeepSeek</span> 辅助编码</div>
        <div class="body-sm" style="color:rgba(255,255,255,.5)"><span style="color:var(--accent-bright)">MIT</span> 开源协议</div>
      </div>
    </div>
  </div>
</section>

<!-- ============ 07 分析结果展示 ============ -->
<section class="slide light" data-animate="grid-reveal" data-layout="S15">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">分析结果 · RESULTS</div>
      <div class="r">07 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr;gap:2.8vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:1vh">
        <div class="t-meta">LESION DETECTION & TOPOLOGY</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(4.8vw,8.5vh);line-height:1.05;letter-spacing:-.02em;color:var(--text-primary)">病变识别 + 拓扑特征</h2>
      </div>
      <div data-anim="images" style="display:grid;grid-template-columns:1fr 1fr;gap:1.6vw">
        <div style="display:flex;flex-direction:column;gap:1vh">
          <img src="images/ui_02_lesion.png" style="width:100%;height:auto;object-fit:contain;border:1px solid var(--border-subtle)" alt="病变识别结果">
          <div class="body-sm" style="color:var(--text-helper)">▲ DR 分级 · 出血/渗出风险评估</div>
        </div>
        <div style="display:flex;flex-direction:column;gap:1vh">
          <img src="images/ui_04_topo2.png" style="width:100%;height:auto;object-fit:contain;border:1px solid var(--border-subtle)" alt="拓扑特征分析">
          <div class="body-sm" style="color:var(--text-helper)">▲ 六维拓扑特征 · 临床参考范围</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ 08 AI 科研辅助 · 选题 + 学习 ============ -->
<section class="slide light" data-animate="grid-reveal" data-layout="S16">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">AI 科研辅助 · RESEARCH</div>
      <div class="r">08 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr;gap:2.4vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:1vh">
        <div class="t-meta">RAG + LLM</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(4.8vw,8.5vh);line-height:1.05;letter-spacing:-.02em;color:var(--text-primary)">从<span style="color:var(--accent);font-weight:300">知识问答</span>到<span style="color:var(--accent);font-weight:300">论文写作</span></h2>
      </div>
      <div data-anim="cards" class="grid-3" style="gap:1.6vw">
        <div style="display:flex;flex-direction:column;gap:1vh">
          <img src="images/ui_07_topic.png" style="width:100%;aspect-ratio:16/10;object-fit:cover;border:1px solid var(--border-subtle)" alt="科研选题生成器">
          <div class="body-sm" style="color:var(--text-helper)">▲ AI 选题生成 + 研究方案</div>
        </div>
        <div style="display:flex;flex-direction:column;gap:1vh">
          <img src="images/ui_05_api.png" style="width:100%;aspect-ratio:16/10;object-fit:cover;border:1px solid var(--border-subtle)" alt="API 配置">
          <div class="body-sm" style="color:var(--text-helper)">▲ DeepSeek API 接入配置</div>
        </div>
        <div style="display:flex;flex-direction:column;gap:1vh">
          <img src="images/ui_06_learning.png" style="width:100%;aspect-ratio:16/10;object-fit:cover;border:1px solid var(--border-subtle)" alt="学习分析">
          <div class="body-sm" style="color:var(--text-helper)">▲ 学习画像 + 行为雷达图</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ 09 AI 赋能开发过程 ============ -->
<section class="slide dark" data-animate="timeline" data-layout="S02">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">开发过程 · DEV PROCESS</div>
      <div class="r">09 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr;gap:3vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:1.2vh">
        <div class="t-meta" style="color:rgba(255,255,255,.5)">AI-DRIVEN DEVELOPMENT</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(5vw,8.8vh);line-height:1.05;letter-spacing:-.02em;color:#fff">生成式 AI 辅助<span style="color:var(--accent-bright);font-style:italic;font-weight:300">全栈开发</span></h2>
      </div>
      <div data-anim="timeline" class="timeline-h" style="--cols:5;display:grid;grid-template-columns:repeat(5,1fr);gap:1.4vw">
        <div class="tl-h-node" style="display:flex;flex-direction:column;gap:1vh">
          <div style="font-family:var(--mono);font-size:min(3vw,5.2vh);font-weight:200;color:var(--accent-bright)">01</div>
          <div class="tl-h-axis"></div>
          <h3 style="font-weight:400;font-size:max(13px,1.1vw);color:#fff">需求分析</h3>
          <p class="body-sm" style="color:rgba(255,255,255,.55)">DeepSeek 协助梳理医学AI教学痛点与功能需求</p>
        </div>
        <div class="tl-h-node" style="display:flex;flex-direction:column;gap:1vh">
          <div style="font-family:var(--mono);font-size:min(3vw,5.2vh);font-weight:200;color:var(--accent-bright)">02</div>
          <div class="tl-h-axis"></div>
          <h3 style="font-weight:400;font-size:max(13px,1.1vw);color:#fff">架构设计</h3>
          <p class="body-sm" style="color:rgba(255,255,255,.55)">AI 生成三层架构方案,U-Net+RAG 技术栈选型</p>
        </div>
        <div class="tl-h-node" style="display:flex;flex-direction:column;gap:1vh">
          <div style="font-family:var(--mono);font-size:min(3vw,5.2vh);font-weight:200;color:var(--accent-bright)">03</div>
          <div class="tl-h-axis"></div>
          <h3 style="font-weight:400;font-size:max(13px,1.1vw);color:#fff">编码实现</h3>
          <p class="body-sm" style="color:rgba(255,255,255,.55)">DeepSeek 辅助编写 3000+ 行 Python 代码,调试纠错</p>
        </div>
        <div class="tl-h-node" style="display:flex;flex-direction:column;gap:1vh">
          <div style="font-family:var(--mono);font-size:min(3vw,5.2vh);font-weight:200;color:var(--accent-bright)">04</div>
          <div class="tl-h-axis"></div>
          <h3 style="font-weight:400;font-size:max(13px,1.1vw);color:#fff">文档生成</h3>
          <p class="body-sm" style="color:rgba(255,255,255,.55)">AI 自动生成使用手册、安装手册、开发记录</p>
        </div>
        <div class="tl-h-node" style="display:flex;flex-direction:column;gap:1vh">
          <div style="font-family:var(--mono);font-size:min(3vw,5.2vh);font-weight:200;color:var(--accent-bright)">05</div>
          <div class="tl-h-axis"></div>
          <h3 style="font-weight:400;font-size:max(13px,1.1vw);color:#fff">打包部署</h3>
          <p class="body-sm" style="color:rgba(255,255,255,.55)">PyInstaller 打包 EXE,pywebview 桌面窗口</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ 10 应用成效 · 四组对比 ============ -->
<section class="slide light" data-animate="stat-enter" data-layout="S06">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">应用成效 · IMPACT</div>
      <div class="r">10 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr;gap:3vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:1.2vh">
        <div class="t-meta">BEFORE & AFTER</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(4.8vw,8.5vh);line-height:1.05;letter-spacing:-.02em;color:var(--text-primary)">从<span style="color:var(--accent);font-weight:300">理论授课</span>到<span style="color:var(--accent);font-weight:300">动手实践</span>的跨越</h2>
      </div>
      <div data-anim="tower" class="kpi-tower-row" style="display:grid;grid-template-columns:repeat(4,1fr);gap:2vw;align-items:end">
        <div style="display:flex;flex-direction:column;align-items:center;gap:1vh">
          <div style="font-family:var(--sans);font-weight:200;font-size:min(5.6vw,9.5vh);line-height:.9;color:var(--accent)">5 min</div>
          <div class="bar-tower" style="width:80%;height:28vh;background:rgba(0,47,167,.18);border:1px solid var(--accent)"></div>
          <div class="body-sm" style="color:var(--text-primary);font-weight:500">上手时间</div>
          <div class="body-sm" style="color:var(--text-helper)">从安装到首次分析</div>
        </div>
        <div style="display:flex;flex-direction:column;align-items:center;gap:1vh">
          <div style="font-family:var(--sans);font-weight:200;font-size:min(5.6vw,9.5vh);line-height:.9;color:var(--text-primary)">6</div>
          <div class="bar-tower" style="width:80%;height:22vh;background:rgba(0,47,167,.12);border:1px solid var(--border-strong)"></div>
          <div class="body-sm" style="color:var(--text-primary);font-weight:500">功能模块</div>
          <div class="body-sm" style="color:var(--text-helper)">覆盖全链条科研</div>
        </div>
        <div style="display:flex;flex-direction:column;align-items:center;gap:1vh">
          <div style="font-family:var(--sans);font-weight:200;font-size:min(5.6vw,9.5vh);line-height:.9;color:var(--text-primary)">0</div>
          <div class="bar-tower" style="width:80%;height:18vh;background:rgba(0,47,167,.08);border:1px solid var(--border-subtle)"></div>
          <div class="body-sm" style="color:var(--text-primary);font-weight:500">GPU 依赖</div>
          <div class="body-sm" style="color:var(--text-helper)">CPU 即可运行</div>
        </div>
        <div style="display:flex;flex-direction:column;align-items:center;gap:1vh">
          <div style="font-family:var(--sans);font-weight:200;font-size:min(5.6vw,9.5vh);line-height:.9;color:var(--text-primary)">100%</div>
          <div class="bar-tower" style="width:80%;height:24vh;background:rgba(0,47,167,.12);border:1px solid var(--border-strong)"></div>
          <div class="body-sm" style="color:var(--text-primary);font-weight:500">开源可复现</div>
          <div class="body-sm" style="color:var(--text-helper)">完整代码+文档</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ 11 三大创新点 ============ -->
<section class="slide dark" data-animate="grid-reveal" data-layout="S13">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">创新点 · INNOVATION</div>
      <div class="r">11 / 12</div>
    </div>
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr;gap:3vh">
      <div data-anim="head" style="display:flex;flex-direction:column;gap:1.2vh">
        <div class="t-meta" style="color:rgba(255,255,255,.5)">THREE FORCES</div>
        <h2 style="font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(4.8vw,8.5vh);line-height:1.05;letter-spacing:-.02em;color:#fff">三大创新,<span style="color:var(--accent-bright);font-style:italic;font-weight:300">重新定义</span>医学 AI 教学</h2>
      </div>
      <div data-anim="forces" class="three-forces" style="display:grid;grid-template-columns:repeat(3,1fr);gap:3vw">
        <div style="display:flex;flex-direction:column;gap:2vh;border-top:3px solid var(--accent-bright);padding-top:2vh">
          <div style="font-family:var(--mono);font-size:min(3.6vw,6vh);font-weight:200;color:var(--accent-bright);line-height:.9">01</div>
          <h3 style="font-family:var(--sans),var(--sans-zh);font-weight:300;font-size:max(15px,1.4vw);color:#fff;letter-spacing:-.01em">多学科交叉融合</h3>
          <p class="body-sm" style="color:rgba(255,255,255,.6);line-height:1.6">眼科医学 × 深度学习<br/>× 图论拓扑学</p>
          <div class="body-sm" style="color:rgba(255,255,255,.5)">将 U-Net 分割、Frangi 滤波器、NetworkX 图论分析集成在同一平台,打破学科壁垒</div>
        </div>
        <div style="display:flex;flex-direction:column;gap:2vh;border-top:3px solid var(--accent-bright);padding-top:2vh">
          <div style="font-family:var(--mono);font-size:min(3.6vw,6vh);font-weight:200;color:var(--accent-bright);line-height:.9">02</div>
          <h3 style="font-family:var(--sans),var(--sans-zh);font-weight:300;font-size:max(15px,1.4vw);color:#fff;letter-spacing:-.01em">AI 赋能全流程</h3>
          <p class="body-sm" style="color:rgba(255,255,255,.6);line-height:1.6">生成式 AI 辅助<br/>开发 · 教学 · 科研</p>
          <div class="body-sm" style="color:rgba(255,255,255,.5)">DeepSeek 辅助编码 + RAG 知识问答 + LLM 选题论文,形成完整 AI 辅助闭环</div>
        </div>
        <div style="display:flex;flex-direction:column;gap:2vh;border-top:3px solid var(--accent-bright);padding-top:2vh">
          <div style="font-family:var(--mono);font-size:min(3.6vw,6vh);font-weight:200;color:var(--accent-bright);line-height:.9">03</div>
          <h3 style="font-family:var(--sans),var(--sans-zh);font-weight:300;font-size:max(15px,1.4vw);color:#fff;letter-spacing:-.01em">零门槛落地</h3>
          <p class="body-sm" style="color:rgba(255,255,255,.6);line-height:1.6">CPU 运行 · EXE 打包<br/>· 完整文档</p>
          <div class="body-sm" style="color:rgba(255,255,255,.5)">无需 GPU/Python 环境,双击 EXE 即可启动;使用手册+安装手册+开发记录齐全</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ 12 收束 · 开源落地 ============ -->
<section class="slide split" data-animate="split-statement" data-layout="S10">
  <div class="canvas-card">
    <div class="split-half">
      <div class="half b-accent" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between;position:relative;overflow:hidden">
        <canvas class="ascii-bg" aria-hidden="true"></canvas>
        <div class="chrome-min" style="margin-bottom:0;position:relative;z-index:1">
          <div class="l">12 / 12</div>
          <div class="r">OPEN SOURCE</div>
        </div>
        <div data-anim="manifesto" style="display:flex;flex-direction:column;gap:2vh;position:relative;z-index:1">
          <div class="t-meta" style="color:rgba(255,255,255,.78);letter-spacing:.22em;margin-bottom:1.6vh">DELIVERABLES</div>
          <h2 style="font-family:var(--sans),var(--sans-zh);font-size:min(6.4vw,12vh);line-height:.96;letter-spacing:-.025em;font-weight:200;color:#fff">
            开源<br/>可复现<br/><span style="font-style:italic;font-weight:300">可落地</span>
          </h2>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(13px,1vw);line-height:1.6;color:rgba(255,255,255,.82);font-weight:300;max-width:36ch;margin-top:1.4vh">完整代码 + 使用手册 + 安装手册 + 开发记录 + 演示视频<br/>一键部署,即刻上手</div>
        </div>
        <div data-anim="signature" style="display:flex;justify-content:space-between;align-items:end;border-top:1px solid rgba(255,255,255,.22);padding-top:2vh;position:relative;z-index:1">
          <div class="t-meta" style="color:rgba(255,255,255,.62)">FundusAI-Edu · 智能信息系统</div>
          <div class="t-meta" style="color:rgba(255,255,255,.62)">2026.06</div>
        </div>
      </div>
      <div class="half" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between">
        <div class="chrome-min">
          <div class="l">TARGET SCORE</div>
          <div class="r">EVALUATION</div>
        </div>
        <div data-anim="rules" style="display:flex;flex-direction:column;gap:0">
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:2.4vh 0;border-top:1px solid var(--border-subtle)">
            <div style="font-family:var(--sans);font-weight:200;font-size:min(4vw,6.8vh);line-height:.9;color:var(--text-primary)">40</div>
            <div>
              <h3 style="font-weight:400;font-size:max(15px,1.3vw);color:var(--text-primary);margin-bottom:.4vh">有效解决问题</h3>
              <p style="font-family:var(--sans),var(--sans-zh);font-size:max(12px,.85vw);line-height:1.5;color:var(--text-secondary);font-weight:300">真实医学教学痛点 → AI 驱动的全流程工具</p>
            </div>
          </div>
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:2.4vh 0;border-top:1px solid var(--border-subtle)">
            <div style="font-family:var(--sans);font-weight:200;font-size:min(4vw,6.8vh);line-height:.9;color:var(--text-primary)">40</div>
            <div>
              <h3 style="font-weight:400;font-size:max(15px,1.3vw);color:var(--text-primary);margin-bottom:.4vh">操作简单易用</h3>
              <p style="font-family:var(--sans),var(--sans-zh);font-size:max(12px,.85vw);line-height:1.5;color:var(--text-secondary);font-weight:300">Web 界面 · 一键分析 · CPU 运行 · 桌面版 EXE</p>
            </div>
          </div>
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:2.4vh 0;border-top:1px solid var(--border-subtle);border-bottom:3px solid var(--accent)">
            <div style="font-family:var(--sans);font-weight:200;font-size:min(4vw,6.8vh);line-height:.9;color:var(--accent)">40</div>
            <div>
              <h3 style="font-weight:400;font-size:max(15px,1.3vw);color:var(--accent);margin-bottom:.4vh">AI 赋能 + 开源分享</h3>
              <p style="font-family:var(--sans),var(--sans-zh);font-size:max(12px,.85vw);line-height:1.5;color:var(--text-secondary);font-weight:300">DeepSeek 辅助全栈开发 · MIT 开源 · 完整文档</p>
            </div>
          </div>
        </div>
        <div data-anim="foot" class="t-meta" style="color:var(--text-helper);text-align:right">→ END · FundusAI-Edu 创AI案例展示</div>
      </div>
    </div>
  </div>
</section>
'''

# ── 读取模板 ──
with open(TEMPLATE, 'r', encoding='utf-8') as f:
    html = f.read()

# ── 替换标题 ──
html = html.replace(
    '<title>[必填] 替换为 PPT 标题 · Deck Title</title>',
    '<title>FundusAI-Edu · 创AI案例展示 · 眼底图像AI教学与科研辅助平台</title>'
)

# ── 找到 SLIDES_HERE 区域并替换 ──
import re
# 从 <!-- SLIDES_HERE 到最后的 </div> 之前 -->
pattern = r'(<!-- SLIDES_HERE.*?)(<!-- ============ 示例:.*?</section>\s*)(</div>\s*\n\s*<div id="nav">)'
replacement = r'\1\n' + SLIDES + r'\n\3'

# 更简单的方法: 找到 "SLIDES_HERE" 注释到 "</div>" + "<div id=\"nav\">" 之间
slide_marker = '<!-- SLIDES_HERE'
nav_marker = '<div id="nav">'
slide_start = html.find(slide_marker)
nav_start = html.find(nav_marker, slide_start)

# 找到示例结束的 </section>
example_end_pattern = r'<!-- ============ 示例:.*?</section>\s*'
import re
# 找最后一个示例节
example_match = re.search(r'<!-- ============ 示例:最后一页.*?</section>\s*', html, re.DOTALL)
if example_match:
    replace_start = slide_start
    replace_end = example_match.end()
    # 在示例结束后插入新幻灯片
    html = html[:replace_start] + SLIDES + '\n' + html[replace_end:]

# ── 替换 [必填] 占位符 ──
html = html.replace('[必填] Deck 标题 · Issue/Field Note 编号', 'FundusAI-Edu 创AI智能信息系统案例')
html = html.replace('[必填] 章节英文 / Section En', 'CREATIVE AI · FIELD NOTE')
html = html.replace('[必填] 中文主标题<br/>(≤ 12 字,可在某字加 <span style="font-style:italic;font-weight:300">italic</span> 微强调)', 
                     'Fundus<span style="font-style:italic;font-weight:300">AI</span>-Edu<br/>眼底图像AI教学平台')
html = html.replace('[必填] 一段 1-2 行的副标 / 引子,定调全场.', 
                     '从图像分析到科研全流程智能化 — 让每一个医学师生都能亲手操作 AI')
html = html.replace('[选填] 作者 · 日期 · 出处', '创AI案例 · 智能信息系统 · 2026')
html = html.replace('SS · 25.05.10 · 01 / NN', '创AI · 2026.06 · 01 / 12')

# ── 写回 ──
with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'[OK] PPT generated: {OUTPUT}')
print(f'[OK] Slides: 12 pages (S01-S22 layouts)')
print(f'[OK] Theme: IKB International Klein Blue')
print(f'[OK] Strategy: Aligned with competition evaluation criteria')
