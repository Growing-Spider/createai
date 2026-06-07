# =============================================================
# app.py — FundusAI-Edu 主应用入口
# 眼底图像AI教学与科研辅助平台
# 运行：streamlit run app.py
# =============================================================

import streamlit as st
import numpy as np
import cv2
from PIL import Image
import io
import sys
import os
import time
import json
from pathlib import Path
import logging

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────────
# 导入本地模块
# ─────────────────────────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))

try:
    from config import APP_TITLE, APP_ICON, THEME_COLOR, RESEARCH_DIRECTIONS
    from modules.fundus_analysis import FundusAnalyzer
    from modules.topology_analysis import TopologyAnalyzer
    from modules.rag_chat import RAGChat
    from modules.topic_generator import TopicGenerator
    from modules.paper_assistant import PaperAssistant
    from modules.learning_analytics import LearningAnalytics, init_database
except ImportError as e:
    st.error(f"模块导入失败：{e}\n请确认已运行 `pip install -r requirements.txt`")
    st.stop()

# ─────────────────────────────────────────────────────────────
# Streamlit 页面配置
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FundusAI-Edu 眼底图像AI教学平台",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": "# FundusAI-Edu\n眼底图像AI教学与科研辅助平台 v1.0",
    },
)

# ─────────────────────────────────────────────────────────────
# 自定义 CSS
# ─────────────────────────────────────────────────────────────
CUSTOM_CSS = """
<style>
/* ── 全局 ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', 'PingFang SC', 'Microsoft YaHei', sans-serif; }

/* ── 布局：确保 Streamlit 不裁剪内容 ── */
header[data-testid="stHeader"] {
    height: auto !important;
    background: transparent !important;
}
div[data-testid="stAppViewContainer"] > section.main {
    padding-top: 2.5rem !important;
    overflow: visible !important;
}
section.main, .main {
    overflow: visible !important;
}
div.block-container {
    padding: 1.5rem 2rem !important;
    overflow: visible !important;
}
div.stMarkdown, div.element-container,
div[data-testid="stVerticalBlock"],
div[data-testid="stMarkdownContainer"] {
    overflow: visible !important;
}
/* emotion-cache 容器 - 仅限 main 内容区 */
section.main div[class*="st-emotion-cache"] {
    overflow: visible !important;
}

/* ── 全局输入组件对比度增强 ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stNumberInput > div > div > input {
    background-color: #1c2333 !important;
    border: 2px solid #30363d !important;
    border-radius: 6px !important;
    color: #f0f6fc !important;
}
.stTextInput > div > div > input::placeholder,
.stTextArea > div > div > textarea::placeholder {
    color: #6e7681 !important;
    opacity: 1 !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus,
.stNumberInput > div > div > input:focus {
    border-color: #58a6ff !important;
    box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.2) !important;
}

/* ── SelectBox 下拉菜单对比度 ── */
.stSelectbox > div > div > div {
    background-color: #1c2333 !important;
    border: 2px solid #30363d !important;
    border-radius: 6px !important;
}
div[data-baseweb="popover"] li {
    background-color: #161b22 !important;
    color: #e6edf3 !important;
}
div[data-baseweb="popover"] li:hover {
    background-color: #1c2b41 !important;
    color: #58a6ff !important;
}

/* ── 侧边栏 ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1117 0%, #161b22 100%);
    border-right: 1px solid #30363d;
}
[data-testid="stSidebar"] * { color: #e6edf3 !important; }

/* ── 侧边栏输入组件高对比度 ── */
[data-testid="stSidebar"] .stTextInput > div > div > input,
[data-testid="stSidebar"] .stTextArea > div > div > textarea,
[data-testid="stSidebar"] .stSelectbox > div > div > div,
[data-testid="stSidebar"] .stNumberInput > div > div > input {
    background-color: #1c2333 !important;
    border: 2px solid #4a5568 !important;
    border-radius: 6px !important;
    color: #f0f6fc !important;
    caret-color: #58a6ff !important;
}
[data-testid="stSidebar"] .stTextInput > div > div > input::placeholder,
[data-testid="stSidebar"] .stTextArea > div > div > textarea::placeholder {
    color: #8b949e !important;
    opacity: 1 !important;
}
[data-testid="stSidebar"] .stTextInput > div > div > input:focus,
[data-testid="stSidebar"] .stTextArea > div > div > textarea:focus,
[data-testid="stSidebar"] .stSelectbox > div > div > div:focus-within,
[data-testid="stSidebar"] .stNumberInput > div > div > input:focus {
    border-color: #58a6ff !important;
    box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.25) !important;
    background-color: #1a2332 !important;
}

/* ── 侧边栏 文件上传 ── */
[data-testid="stSidebar"] [data-testid="stFileUploader"] {
    background-color: #1c2333 !important;
    border: 2px dashed #4a5568 !important;
    border-radius: 8px !important;
    padding: 1rem !important;
}
[data-testid="stSidebar"] [data-testid="stFileUploader"]:hover {
    border-color: #58a6ff !important;
    background-color: #1a2332 !important;
}
[data-testid="stSidebar"] [data-testid="stFileUploader"] small {
    color: #8b949e !important;
}

/* ── 侧边栏 Slider ── */
[data-testid="stSidebar"] .stSlider > div > div > div > div {
    background-color: #58a6ff !important;
}
[data-testid="stSidebar"] .stSlider [data-testid="stThumbValue"] {
    background-color: #58a6ff !important;
    color: #0d1117 !important;
    font-weight: 700 !important;
}

/* ── 侧边栏 Checkbox / Radio ── */
[data-testid="stSidebar"] .stCheckbox label,
[data-testid="stSidebar"] .stRadio label {
    color: #e6edf3 !important;
}

/* ── 侧边栏 Expander ── */
[data-testid="stSidebar"] .streamlit-expanderHeader {
    background-color: #1c2333 !important;
    border: 1px solid #30363d !important;
    border-radius: 6px !important;
    color: #e6edf3 !important;
}
[data-testid="stSidebar"] .streamlit-expanderContent {
    background-color: #161b22 !important;
    border: 1px solid #30363d !important;
    border-top: none !important;
    border-radius: 0 0 6px 6px !important;
}

/* ── 侧边栏 Metrics ── */
[data-testid="stSidebar"] [data-testid="stMetricValue"] {
    color: #58a6ff !important;
    font-weight: 700 !important;
}
[data-testid="stSidebar"] [data-testid="stMetricDelta"] {
    color: #3fb950 !important;
}

/* ── 侧边栏分割线 ── */
[data-testid="stSidebar"] hr {
    border-color: #30363d !important;
    margin: 1.5rem 0 !important;
}

/* ── 侧边栏 Button 高对比度 ── */
[data-testid="stSidebar"] .stButton > button {
    background: linear-gradient(135deg, #1a2332 0%, #1c2b41 100%) !important;
    border: 2px solid #4a5568 !important;
    color: #e6edf3 !important;
    font-weight: 600 !important;
    border-radius: 8px !important;
    transition: all 0.2s !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    border-color: #58a6ff !important;
    background: linear-gradient(135deg, #1c2b41 0%, #1e3458 100%) !important;
    box-shadow: 0 0 12px rgba(88, 166, 255, 0.3) !important;
    transform: translateY(-1px) !important;
}
[data-testid="stSidebar"] .stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #238636 0%, #2ea043 100%) !important;
    border-color: #3fb950 !important;
    color: #fff !important;
}
[data-testid="stSidebar"] .stButton > button[kind="primary"]:hover {
    border-color: #56d364 !important;
    box-shadow: 0 0 16px rgba(63, 185, 80, 0.35) !important;
}

/* ── 侧边栏 Expander 强化 ── */
[data-testid="stSidebar"] .streamlit-expanderHeader {
    background-color: #1c2333 !important;
    border: 2px solid #4a5568 !important;
    border-radius: 8px !important;
    color: #e6edf3 !important;
    font-weight: 600 !important;
    padding: 0.75rem 1rem !important;
}
[data-testid="stSidebar"] .streamlit-expanderHeader:hover {
    border-color: #58a6ff !important;
}
[data-testid="stSidebar"] .streamlit-expanderHeader p {
    color: #e6edf3 !important;
    font-weight: 600 !important;
}
[data-testid="stSidebar"] .streamlit-expanderContent {
    background-color: #0d1117 !important;
    border: 2px solid #4a5568 !important;
    border-top: none !important;
    border-radius: 0 0 8px 8px !important;
    padding: 1rem !important;
}

/* ── 侧边栏 Caption / Small text ── */
[data-testid="stSidebar"] .st-caption,
[data-testid="stSidebar"] small {
    color: #b0b8c4 !important;
}

/* ── 侧边栏 Success/Info/Error 消息盒 ── */
[data-testid="stSidebar"] .stAlert {
    background-color: #1c2333 !important;
    border: 2px solid #4a5568 !important;
    color: #e6edf3 !important;
}

/* ── 全局白色背景强制深色（解决 Streamlit 默认白底问题） ── */
[data-testid="stSidebar"] .st-emotion-cache-1gwvycy,
[data-testid="stSidebar"] .st-emotion-cache-1v0mbdj,
[data-testid="stSidebar"] div[style*="background-color: rgb(255, 255, 255)"],
[data-testid="stSidebar"] div[style*="background: rgb(255, 255, 255)"] {
    background-color: #1c2333 !important;
    color: #e6edf3 !important;
}

/* ── 标题区：使用 Streamlit 原生 h1 渲染 ── */
h1 {
    color: #58a6ff !important;
    font-size: 2.2rem !important;
    font-weight: 700 !important;
    line-height: 1.8 !important;
    padding: 0.5rem 0 !important;
    letter-spacing: 0.02em !important;
}
.hero-title {
    color: #58a6ff;
    font-size: 2.2rem;
    font-weight: 700;
    line-height: 2.2;
    margin-top: 1rem;
    margin-bottom: 0.3rem;
    padding: 0.8rem 0;
    text-shadow: 0 0 20px rgba(88, 166, 255, 0.4);
    letter-spacing: 0.02em;
    min-height: 4.5rem;
}
.hero-subtitle {
    color: #8b949e;
    font-size: 1rem;
    margin-bottom: 1.5rem;
}

/* ── 卡片 ── */
.metric-card {
    background: linear-gradient(135deg, #161b22 0%, #1c2128 100%);
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 1.2rem;
    margin-bottom: 1rem;
    transition: border-color 0.2s, box-shadow 0.2s;
}
.metric-card:hover {
    border-color: #58a6ff;
    box-shadow: 0 0 15px rgba(88, 166, 255, 0.15);
}
.metric-value {
    font-size: 2rem;
    font-weight: 700;
    color: #58a6ff;
}
.metric-label {
    font-size: 0.85rem;
    color: #8b949e;
    margin-top: 0.3rem;
}

/* ── 结果区 ── */
.result-box {
    background: #0d1117;
    border: 1px solid #21262d;
    border-radius: 8px;
    padding: 1rem;
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
    color: #e6edf3;
}

/* ── 警告框 ── */
.info-box {
    background: rgba(88, 166, 255, 0.1);
    border-left: 4px solid #58a6ff;
    border-radius: 0 8px 8px 0;
    padding: 1rem;
    margin: 1rem 0;
}

/* ── 成功框 ── */
.success-box {
    background: rgba(63, 185, 80, 0.1);
    border-left: 4px solid #3fb950;
    border-radius: 0 8px 8px 0;
    padding: 1rem;
    margin: 1rem 0;
}

/* ── 导航按钮 ── */
.stButton > button {
    border-radius: 8px;
    transition: all 0.2s;
    font-weight: 500;
}
.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

/* ── 进度条 ── */
.stProgress > div > div { background: linear-gradient(90deg, #58a6ff, #3fb950); }

/* ── Tab ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: #161b22;
    border-radius: 8px;
    padding: 4px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 6px;
    padding: 8px 16px;
    color: #8b949e;
}
.stTabs [aria-selected="true"] {
    background: #21262d;
    color: #e6edf3 !important;
}

/* ── 分割线 ── */
hr { border-color: #21262d; }

/* ── 文件上传区 ── */
[data-testid="stFileUploader"] {
    border: 2px dashed #30363d;
    border-radius: 12px;
    padding: 1rem;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# Session State 初始化
# ─────────────────────────────────────────────────────────────

def init_session():
    defaults = {
        "username":           "demo_user",
        "initialized":        False,
        "analysis_result":    None,
        "topology_result":    None,
        "current_image":      None,
        "chat_history":       [],
        "rag_chat":           None,
        "topic_generator":    None,
        "paper_assistant":    None,
        "learning_analytics": None,
        "fundus_analyzer":    None,
        "topology_analyzer":  None,
        "kb_initialized":     False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_session()

# ─────────────────────────────────────────────────────────────
# 延迟初始化组件（避免启动过慢）
# ─────────────────────────────────────────────────────────────

@st.cache_resource(show_spinner=False)
def get_fundus_analyzer():
    return FundusAnalyzer()

@st.cache_resource(show_spinner=False)
def get_topology_analyzer():
    return TopologyAnalyzer()

@st.cache_resource(show_spinner=False)
def get_rag_chat():
    chat = RAGChat()
    return chat

@st.cache_resource(show_spinner=False)
def get_topic_generator():
    return TopicGenerator()

@st.cache_resource(show_spinner=False)
def get_paper_assistant():
    return PaperAssistant()

def get_learning_analytics():
    if st.session_state.learning_analytics is None:
        init_database()
        st.session_state.learning_analytics = LearningAnalytics(
            st.session_state.username
        )
    return st.session_state.learning_analytics

# ─────────────────────────────────────────────────────────────
# 辅助函数
# ─────────────────────────────────────────────────────────────

def pil_to_numpy(img: Image.Image) -> np.ndarray:
    """PIL Image → NumPy RGB array"""
    if img.mode != "RGB":
        img = img.convert("RGB")
    return np.array(img)

def numpy_to_pil(arr: np.ndarray) -> Image.Image:
    """NumPy → PIL Image"""
    if arr.max() <= 1.0:
        arr = (arr * 255).astype(np.uint8)
    return Image.fromarray(arr.astype(np.uint8))

def render_metric(label: str, value, icon: str = "") -> str:
    return f"""
<div class="metric-card">
    <div class="metric-value">{icon} {value}</div>
    <div class="metric-label">{label}</div>
</div>"""

# ─────────────────────────────────────────────────────────────
# 侧边栏
# ─────────────────────────────────────────────────────────────

def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div style="text-align:center; padding: 1rem 0;">
            <div style="font-size:3rem;">👁️</div>
            <div style="font-size:1.1rem; font-weight:700; color:#58a6ff;">FundusAI-Edu</div>
            <div style="font-size:0.75rem; color:#8b949e; margin-top:4px;">眼底图像AI教学平台 v1.0</div>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # 用户设置
        with st.expander("👤 用户设置", expanded=False):
            username = st.text_input("用户名", value=st.session_state.username,
                                     key="sidebar_username")
            if st.button("确认", use_container_width=True):
                st.session_state.username = username
                st.success(f"欢迎，{username}！")

        st.divider()

        # API 配置
        with st.expander("🔑 API 配置", expanded=False):
            api_key = st.text_input("DeepSeek API Key",
                                    type="password",
                                    placeholder="sk-...",
                                    help="访问 https://platform.deepseek.com 获取")
            if api_key:
                os.environ["DEEPSEEK_API_KEY"] = api_key
                st.success("✅ API Key 已设置")

        st.divider()

        # 知识库管理
        with st.expander("📚 知识库管理", expanded=False):
            st.caption("上传文档以扩充知识库")
            kb_files = st.file_uploader(
                "上传文档（PDF/TXT/DOCX）",
                type=["pdf", "txt", "docx"],
                accept_multiple_files=True,
                key="kb_uploader",
            )
            if kb_files:
                kb_dir = Path("knowledge_base")
                kb_dir.mkdir(exist_ok=True)
                for f in kb_files:
                    (kb_dir / f.name).write_bytes(f.read())
                st.success(f"✅ 已上传 {len(kb_files)} 个文件")

            if st.button("🔄 重建知识库", use_container_width=True):
                with st.spinner("正在初始化知识库..."):
                    chat = get_rag_chat()
                    chat.initialize_knowledge_base()
                st.success("✅ 知识库已更新")

        st.divider()

        # 快速统计
        analytics = get_learning_analytics()
        stats = analytics.get_user_stats()
        col1, col2 = st.columns(2)
        with col1:
            st.metric("📊 操作次数", stats.get("total_actions", 0))
        with col2:
            st.metric("🔬 分析次数", stats.get("analysis_count", 0))

        st.divider()
        st.caption("© 2026 FundusAI-Edu | 医学AI教育平台")


# ─────────────────────────────────────────────────────────────
# 模块 1：眼底图像智能分析
# ─────────────────────────────────────────────────────────────

def page_fundus_analysis():
    st.title("🔬 眼底图像智能分析")
    st.markdown('<div class="hero-subtitle">上传眼底图像，自动完成血管分割与病变识别</div>', unsafe_allow_html=True)

    analytics = get_learning_analytics()

    # ── 上传计数 key，用于强制刷新 file_uploader ──
    if "upload_key_counter" not in st.session_state:
        st.session_state.upload_key_counter = 0

    col_upload, col_result = st.columns([1, 1], gap="large")

    with col_upload:
        st.subheader("📤 图像上传")

        # 不限制 type，改用手动校验，避免大小写导致红色感叹号
        uploaded_file = st.file_uploader(
            "选择眼底图像（支持 jpg / png / bmp / tiff 等常见格式）",
            type=None,  # 接受所有文件，自己校验
            key=f"fundus_uploader_{st.session_state.upload_key_counter}",
            help="支持彩色眼底照片，建议分辨率 ≥ 512×512",
        )

        # ── 校验文件类型 ──
        if uploaded_file is not None:
            name_lower = uploaded_file.name.lower()
            allowed_exts = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif", ".webp")
            if not name_lower.endswith(allowed_exts):
                st.error(f"不支持的文件格式：{uploaded_file.name}")
                st.info("请上传 JPG / PNG / BMP / TIFF 格式的图片。")
                # 让用户重新上传
                if st.button("🔄 重新选择", key="retry_upload"):
                    st.session_state.upload_key_counter += 1
                    st.rerun()
            else:
                # ── 读取并显示图片 ──
                try:
                    img_pil = Image.open(uploaded_file)
                    img_pil.verify()  # 快速校验图片完整性
                    uploaded_file.seek(0)  # verify() 后需要重置指针
                    img_pil = Image.open(uploaded_file)
                    img_np = pil_to_numpy(img_pil)
                    st.session_state.current_image = img_np

                    st.image(img_pil, caption=f"原始图像：{uploaded_file.name}",
                             use_container_width=True)

                    col_meta1, col_meta2 = st.columns(2)
                    with col_meta1:
                        st.caption(f"📐 尺寸：{img_np.shape[1]} × {img_np.shape[0]} px")
                    with col_meta2:
                        size_mb = uploaded_file.size / 1024 / 1024
                        st.caption(f"📦 大小：{size_mb:.2f} MB")

                    # ── 操作按钮 ──
                    col_btn1, col_btn2 = st.columns(2)
                    with col_btn1:
                        if st.button("🚀 开始分析", type="primary", use_container_width=True):
                            with st.spinner("AI分析中，请稍候..."):
                                try:
                                    analyzer = get_fundus_analyzer()
                                    topo = get_topology_analyzer()
                                    progress = st.progress(0, text="初始化...")

                                    progress.progress(20, "正在进行血管分割...")
                                    vessel_mask = analyzer.segment_vessels(img_np)

                                    progress.progress(50, "正在进行病变识别...")
                                    lesion_info = analyzer.detect_lesions(img_np)

                                    progress.progress(70, "正在提取拓扑特征...")
                                    topo_report = topo.generate_topology_report(vessel_mask, img_np)

                                    progress.progress(90, "正在生成可视化...")
                                    overlay = analyzer.overlay_vessels(img_np, vessel_mask)
                                    progress.progress(100, "分析完成！")

                                    st.session_state.analysis_result = {
                                        "vessel_mask": vessel_mask,
                                        "lesion_info": lesion_info,
                                        "overlay": overlay,
                                        "image_name": uploaded_file.name,
                                    }
                                    st.session_state.topology_result = topo_report

                                    analytics.log_analysis(
                                        uploaded_file.name,
                                        topo_report["features"],
                                        lesion_info,
                                    )
                                    st.success("✅ 分析完成！")
                                    st.rerun()

                                except Exception as proc_err:
                                    import traceback
                                    traceback.print_exc()
                                    st.error(f"❌ 分析过程出错：{proc_err}")
                                    st.info("请尝试重新上传或更换一张图片。")
                    with col_btn2:
                        if st.button("🗑️ 清除", use_container_width=True):
                            st.session_state.current_image = None
                            st.session_state.analysis_result = None
                            st.session_state.topology_result = None
                            st.session_state.upload_key_counter += 1
                            st.rerun()

                except Exception as img_err:
                    import traceback
                    traceback.print_exc()
                    st.error(f"❌ 图片读取失败：{img_err}")
                    st.info("文件可能已损坏或不是有效的图片格式，请尝试其他图片。")
                    if st.button("🔄 重新选择", key="retry_bad_img"):
                        st.session_state.upload_key_counter += 1
                        st.rerun()

    with col_result:
        st.subheader("📊 分析结果")

        if st.session_state.analysis_result:
            result = st.session_state.analysis_result
            lesion = result["lesion_info"]
            topo   = st.session_state.topology_result

            tab1, tab2, tab3 = st.tabs(["🔍 血管分割", "📈 病变识别", "🌐 拓扑特征"])

            with tab1:
                col_a, col_b = st.columns(2)
                with col_a:
                    # 血管掩码：黑底绿色血管，直观显示
                    mask_disp = result["vessel_mask"].copy()
                    show_mask = (mask_disp > 127).astype(np.uint8)
                    mask_colored = np.zeros((*mask_disp.shape, 3), dtype=np.uint8)
                    mask_colored[:, :, 1] = (show_mask * 255).astype(np.uint8)  # 绿=血管
                    st.image(mask_colored, caption="血管分割掩码（绿色=血管，黑色=背景）",
                             use_container_width=True)
                with col_b:
                    st.image(numpy_to_pil(result["overlay"]),
                             caption="血管叠加图", use_container_width=True)
                if topo and "skeleton_viz" in topo:
                    st.image(topo["skeleton_viz"], caption="骨架可视化",
                             use_container_width=True)

            with tab2:
                # DR 分级
                dr_grade = lesion.get("dr_grade", "未知")
                dr_conf  = lesion.get("dr_confidence", 0)
                dr_colors = {
                    "No DR": "#3fb950",
                    "Mild DR": "#ffa657",
                    "Moderate DR": "#f78166",
                    "Severe DR": "#ff7b72",
                }
                color = dr_colors.get(dr_grade, "#8b949e")

                st.markdown(f"""
                <div class="metric-card" style="text-align:center;">
                    <div style="font-size:2.5rem; font-weight:700; color:{color};">{dr_grade}</div>
                    <div style="color:#8b949e; margin-top:0.5rem;">糖尿病视网膜病变分级</div>
                    <div style="color:{color}; font-size:1.2rem;">置信度：{dr_conf:.0%}</div>
                </div>
                """, unsafe_allow_html=True)

                col_r1, col_r2, col_r3 = st.columns(3)
                with col_r1:
                    q = lesion.get("overall_quality", "未知")
                    st.metric("图像质量", q)
                with col_r2:
                    hr = lesion.get("hemorrhage_risk", 0)
                    st.metric("出血风险", f"{hr:.3f}")
                with col_r3:
                    er = lesion.get("hard_exudate_risk", 0)
                    st.metric("渗出风险", f"{er:.3f}")

                # 风险进度条
                st.markdown("**病变风险评估**")
                st.progress(lesion.get("hemorrhage_risk", 0),
                            text=f"出血风险：{lesion.get('hemorrhage_risk',0):.1%}")
                st.progress(lesion.get("hard_exudate_risk", 0),
                            text=f"硬性渗出：{lesion.get('hard_exudate_risk',0):.1%}")

            with tab3:
                if topo:
                    features = topo["features"]
                    col_f1, col_f2 = st.columns(2)
                    feature_items = [
                        ("血管密度",    f"{features.get('vessel_density',0):.4f}"),
                        ("分叉点数量",  features.get("bifurcation_count", 0)),
                        ("终末点数量",  features.get("endpoint_count", 0)),
                        ("平均血管宽度", f"{features.get('avg_vessel_width',0):.2f} px"),
                        ("血管迂曲度",  f"{features.get('tortuosity',0):.3f}"),
                        ("分形维数",    f"{features.get('fractal_dimension',0):.3f}"),
                    ]
                    for i, (label, value) in enumerate(feature_items):
                        with (col_f1 if i % 2 == 0 else col_f2):
                            st.metric(label, value)

                    if "radar_chart" in topo:
                        st.image(topo["radar_chart"], caption="特征雷达图",
                                 use_container_width=True)

                    # 特征解读
                    if topo.get("interpretation"):
                        st.subheader("📋 特征解读")
                        for key, text in topo["interpretation"].items():
                            st.markdown(f"- {text}")
        else:
            st.markdown("""
            <div class="info-box">
                <strong>💡 使用提示</strong><br>
                请在左侧上传眼底图像后，点击「开始分析」按钮。<br>
                支持彩色眼底照片，建议使用高质量图像以获得最佳分析效果。
            </div>
            """, unsafe_allow_html=True)

            # 演示说明
            st.markdown("### 🎯 功能说明")
            features_info = [
                ("🩸 血管分割", "基于 U-Net 深度学习模型，自动提取视网膜血管区域"),
                ("🔎 病变识别", "检测出血点、硬性渗出等糖尿病视网膜病变特征"),
                ("🌐 拓扑分析", "计算血管密度、分叉点、迂曲度等六项量化特征"),
            ]
            for icon_title, desc in features_info:
                st.markdown(f"**{icon_title}**：{desc}")


# ─────────────────────────────────────────────────────────────
# 模块 2：血管拓扑特征分析（独立展示）
# ─────────────────────────────────────────────────────────────

def page_topology_analysis():
    st.title("🌐 血管拓扑特征分析")
    st.markdown('<div class="hero-subtitle">深度解析视网膜血管网络的结构特征</div>', unsafe_allow_html=True)

    if st.session_state.topology_result:
        topo = st.session_state.topology_result
        features = topo["features"]

        st.subheader("📊 六大拓扑特征")
        cols = st.columns(3)
        feature_configs = [
            ("血管密度", f"{features['vessel_density']:.4f}", "正常范围：0.08~0.18", "📐"),
            ("分叉点数量", features["bifurcation_count"], "反映血管网络复杂度", "🔱"),
            ("终末点数量", features["endpoint_count"],  "血管末端节点数", "⚫"),
            ("平均血管宽度", f"{features['avg_vessel_width']:.2f} px", "正常：3~8像素", "📏"),
            ("血管迂曲度",  f"{features['tortuosity']:.3f}", "正常范围：1.0~1.3", "〰️"),
            ("分形维数",    f"{features['fractal_dimension']:.3f}", "正常范围：1.5~1.7", "🔢"),
        ]
        for i, (label, value, hint, icon) in enumerate(feature_configs):
            with cols[i % 3]:
                st.markdown(render_metric(f"{icon} {label}", value), unsafe_allow_html=True)
                st.caption(hint)

        st.divider()

        col_viz, col_interp = st.columns([1, 1], gap="large")
        with col_viz:
            if "radar_chart" in topo:
                st.image(topo["radar_chart"], caption="特征雷达图",
                         use_container_width=True)
            if "skeleton_viz" in topo:
                st.image(topo["skeleton_viz"], caption="骨架可视化（原图/分割/骨架）",
                         use_container_width=True)

        with col_interp:
            st.subheader("🩺 临床意义解读")
            interp = topo.get("interpretation", {})
            interp_labels = {
                "vessel_density": "血管密度",
                "bifurcation":    "分叉点",
                "tortuosity":     "迂曲度",
                "fractal":        "分形维数",
            }
            for key, text in interp.items():
                label = interp_labels.get(key, key)
                st.markdown(f"""
                <div class="info-box">
                    <strong>{label}</strong><br>{text}
                </div>
                """, unsafe_allow_html=True)

            st.subheader("📚 参考价值")
            st.markdown("""
            | 特征 | 升高提示 | 降低提示 |
            |------|---------|---------|
            | 血管密度 | 血管增生 | 缺血/萎缩 |
            | 迂曲度 | 高血压/DR | 正常 |
            | 分形维数 | 血管复杂 | 血管稀疏 |
            | 分叉点 | 新生血管 | 血管减少 |
            """)
    else:
        st.info("⚠️ 请先在「眼底图像分析」模块上传并分析图像，才能查看详细拓扑特征。")


# ─────────────────────────────────────────────────────────────
# 模块 3：AI 科研导师
# ─────────────────────────────────────────────────────────────

def page_rag_chat():
    st.title("🤖 AI 科研导师")
    st.markdown('<div class="hero-subtitle">基于 RAG 的专业医学知识问答，随时解答您的科研疑问</div>', unsafe_allow_html=True)

    analytics = get_learning_analytics()
    chat_engine = get_rag_chat()

    # 控制区
    col_ctrl1, col_ctrl2, col_ctrl3 = st.columns([2, 1, 1])
    with col_ctrl1:
        use_rag = st.toggle("📚 启用知识库检索（RAG）", value=True,
                            help="开启后将基于知识库内容回答，减少幻觉")
    with col_ctrl2:
        if st.button("🗑️ 清空对话", use_container_width=True):
            st.session_state.chat_history = []
            chat_engine.clear_history()
            st.rerun()
    with col_ctrl3:
        if st.button("💡 示例问题", use_container_width=True):
            st.session_state["example_question"] = True

    # 示例问题快捷按钮
    example_questions = [
        "什么是糖尿病视网膜病变？如何分级？",
        "U-Net模型的结构是什么？在眼底分析中有哪些应用？",
        "视网膜血管分形维数的临床意义是什么？",
        "如何设计一个眼底图像AI诊断研究？",
        "RAG技术的原理是什么？如何减少LLM幻觉？",
    ]

    if st.session_state.get("example_question"):
        st.markdown("**💬 快速提问：**")
        cols = st.columns(len(example_questions))
        for i, q in enumerate(example_questions):
            with cols[i]:
                if st.button(q[:12] + "...", key=f"eq_{i}",
                             use_container_width=True):
                    st.session_state.chat_history.append(
                        {"role": "user", "content": q}
                    )
                    with st.spinner("AI思考中..."):
                        answer = chat_engine.chat(q, with_rag=use_rag)
                    st.session_state.chat_history.append(
                        {"role": "assistant", "content": answer}
                    )
                    analytics.log_chat(q, answer)
                    st.session_state["example_question"] = False
                    st.rerun()

    st.divider()

    # 对话历史
    chat_container = st.container(height=450)
    with chat_container:
        if not st.session_state.chat_history:
            st.markdown("""
            <div style="text-align:center; padding:3rem; color:#8b949e;">
                <div style="font-size:3rem; margin-bottom:1rem;">🤖</div>
                <div style="font-size:1.1rem;">你好！我是你的AI科研导师。</div>
                <div style="margin-top:0.5rem;">你可以问我关于眼底图像、视网膜疾病、深度学习医学应用等任何问题。</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            for msg in st.session_state.chat_history:
                with st.chat_message(msg["role"],
                                     avatar="🧑‍🎓" if msg["role"]=="user" else "🤖"):
                    st.markdown(msg["content"])

    # 输入框
    user_input = st.chat_input("向AI科研导师提问...", key="chat_input")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.spinner("AI思考中..."):
            answer = chat_engine.chat(user_input, with_rag=use_rag)
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        analytics.log_chat(user_input, answer)
        analytics.log_action("rag_chat", "question_asked",
                             {"question_len": len(user_input)})
        st.rerun()


# ─────────────────────────────────────────────────────────────
# 模块 4：科研选题生成器
# ─────────────────────────────────────────────────────────────

def page_topic_generator():
    st.title("🎯 科研选题生成器")
    st.markdown('<div class="hero-subtitle">AI 智能推荐个性化研究课题，助力科研起步</div>', unsafe_allow_html=True)

    analytics  = get_learning_analytics()
    topic_gen  = get_topic_generator()

    col_form, col_result = st.columns([1, 1.5], gap="large")

    with col_form:
        st.subheader("⚙️ 选题配置")
        with st.form("topic_form"):
            interest_area = st.selectbox(
                "研究兴趣方向",
                options=RESEARCH_DIRECTIONS,
                help="选择最感兴趣的研究方向",
            )
            custom_interest = st.text_input(
                "自定义兴趣方向（可选）",
                placeholder="如：高血压与视网膜血管关系",
            )
            academic_level = st.selectbox(
                "学术层次",
                ["高职高专", "本科生", "硕士研究生", "博士研究生"],
            )
            num_topics = st.slider("生成选题数量", 1, 5, 3)
            custom_req = st.text_area(
                "其他要求（可选）",
                placeholder="如：希望有公开数据集可用；侧重算法创新...",
                height=80,
            )
            submitted = st.form_submit_button("🚀 生成选题", type="primary",
                                              use_container_width=True)

        if submitted:
            final_interest = custom_interest or interest_area
            with st.spinner(f"AI正在为您生成 {num_topics} 个选题..."):
                result = topic_gen.generate_topics(
                    interest_area=final_interest,
                    academic_level=academic_level,
                    num_topics=num_topics,
                    custom_requirements=custom_req,
                )
            st.session_state["generated_topics"] = result
            analytics.log_action("topic_generator", "topics_generated",
                                 {"interest": final_interest, "count": num_topics})

    with col_result:
        st.subheader("📋 生成的研究选题")

        if "generated_topics" in st.session_state and st.session_state["generated_topics"]:
            result = st.session_state["generated_topics"]
            topics = result.get("topics", [])

            if result.get("raw_text"):
                st.markdown(result["raw_text"])
            elif topics:
                for i, topic in enumerate(topics, 1):
                    with st.expander(f"📌 选题 {i}：{topic.get('title', '未命名')}", expanded=(i==1)):
                        st.markdown(f"**背景**：{topic.get('background', '')}")
                        st.markdown(f"**目标**：{topic.get('objective', '')}")
                        st.markdown(f"**创新点**：{topic.get('innovation', '')}")
                        st.markdown(f"**预期成果**：{topic.get('expected_outcome', '')}")

                        diff = topic.get("difficulty", "中级")
                        diff_colors = {"初级": "🟢", "中级": "🟡", "高级": "🔴"}
                        st.markdown(f"**难度**：{diff_colors.get(diff, '⚪')} {diff}")

                        if topic.get("methods"):
                            st.markdown("**研究方法**：" + " → ".join(topic["methods"]))

                        col_expand, col_export = st.columns(2)
                        with col_expand:
                            if st.button(f"📝 生成研究方案", key=f"expand_{i}",
                                         use_container_width=True):
                                with st.spinner("生成研究方案..."):
                                    plan = topic_gen.expand_research_plan(
                                        topic.get("title", ""), topic
                                    )
                                st.markdown(plan)

                        with col_export:
                            if st.session_state.analysis_result and st.session_state.topology_result:
                                if st.button(f"📄 生成实验报告", key=f"report_{i}",
                                             use_container_width=True):
                                    with st.spinner("生成实验报告..."):
                                        report = topic_gen.generate_experiment_report(
                                            st.session_state.analysis_result,
                                            st.session_state.topology_result.get("features", {}),
                                            topic.get("title", ""),
                                        )
                                    st.download_button(
                                        "⬇️ 下载实验报告",
                                        data=report.encode("utf-8"),
                                        file_name=f"experiment_report_{i}.md",
                                        mime="text/markdown",
                                    )
        else:
            st.markdown("""
            <div class="info-box">
                <strong>💡 使用说明</strong><br>
                1. 在左侧选择研究兴趣方向<br>
                2. 设置学术层次和生成数量<br>
                3. 点击「生成选题」获取个性化推荐<br>
                4. 点击「生成研究方案」获取完整研究计划
            </div>
            """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# 模块 5：论文写作辅助
# ─────────────────────────────────────────────────────────────

def page_paper_assistant():
    st.title("📝 论文写作辅助")
    st.markdown('<div class="hero-subtitle">AI 辅助构建论文框架，逐章节精准写作指导</div>', unsafe_allow_html=True)

    analytics = get_learning_analytics()
    paper_ast = get_paper_assistant()

    tab_outline, tab_section, tab_polish, tab_refs, tab_journal = st.tabs([
        "📋 论文框架", "✍️ 章节写作", "💎 文本润色", "📚 参考文献", "📰 期刊推荐"
    ])

    with tab_outline:
        st.subheader("生成论文框架")
        col1, col2 = st.columns([2, 1])
        with col1:
            topic = st.text_input("论文研究主题",
                                  placeholder="如：基于U-Net的糖尿病视网膜病变自动分级")
            paper_type = st.selectbox(
                "论文类型",
                options=list(PaperAssistant.PAPER_TYPES.keys()),
                format_func=lambda x: PaperAssistant.PAPER_TYPES[x],
            )
        with col2:
            use_analysis = st.checkbox("结合已有分析数据",
                                       value=bool(st.session_state.analysis_result))
            st.caption("勾选后将分析结果纳入框架")

        if st.button("生成框架", type="primary", use_container_width=True):
            if not topic:
                st.warning("请输入论文主题")
            else:
                analysis_data = None
                if use_analysis and st.session_state.analysis_result:
                    analysis_data = {
                        "topology_features": st.session_state.topology_result.get("features", {}),
                        "lesion_info": st.session_state.analysis_result.get("lesion_info", {}),
                    }
                with st.spinner("生成论文框架中..."):
                    outline = paper_ast.generate_paper_outline(topic, paper_type, analysis_data)
                st.markdown(outline)
                st.download_button("⬇️ 下载论文框架",
                                   data=outline.encode("utf-8"),
                                   file_name="paper_outline.md",
                                   mime="text/markdown")
                analytics.log_action("paper_assistant", "outline_generated",
                                     {"topic": topic})

    with tab_section:
        st.subheader("章节辅助写作")
        sec_topic = st.text_input("研究主题", key="sec_topic",
                                   placeholder="您的论文主题")
        section = st.selectbox("选择章节", options=list(PaperAssistant.SECTION_PROMPTS.keys()),
                                format_func=lambda x: {
                                    "abstract": "摘要",
                                    "introduction": "引言",
                                    "methods": "材料与方法",
                                    "results": "结果",
                                    "discussion": "讨论",
                                    "conclusion": "结论",
                                }[x])
        add_info = st.text_area("补充信息（可选）", height=80,
                                 placeholder="如：样本量、数据集名称、特殊说明...")
        data_str = ""
        if section == "results" and st.session_state.topology_result:
            features = st.session_state.topology_result.get("features", {})
            data_str = str(features)
            st.info("ℹ️ 将自动结合当前图像分析数据生成结果部分")

        if st.button("生成章节内容", type="primary"):
            if not sec_topic:
                st.warning("请输入研究主题")
            else:
                with st.spinner(f"生成{section}章节..."):
                    content = paper_ast.write_section(section, sec_topic, add_info, data_str)
                st.markdown(content)
                st.download_button("⬇️ 下载章节内容",
                                   data=content.encode("utf-8"),
                                   file_name=f"section_{section}.md",
                                   mime="text/markdown")

    with tab_polish:
        st.subheader("学术文本润色")
        raw_text = st.text_area("粘贴需要润色的文本", height=200,
                                 placeholder="请粘贴论文段落...")
        polish_style = st.radio("润色风格", ["academic", "concise", "formal"],
                                 format_func=lambda x: {
                                     "academic": "学术规范",
                                     "concise": "简洁明了",
                                     "formal": "正式书面",
                                 }[x], horizontal=True)
        if st.button("✨ 开始润色", type="primary"):
            if not raw_text:
                st.warning("请输入待润色文本")
            else:
                with st.spinner("润色中..."):
                    polished = paper_ast.polish_text(raw_text, polish_style)
                st.markdown(polished)

    with tab_refs:
        st.subheader("参考文献推荐")
        ref_topic = st.text_input("研究主题", key="ref_topic",
                                   placeholder="如：视网膜血管分割深度学习")
        num_refs  = st.slider("参考文献数量", 5, 20, 10)
        if st.button("🔍 推荐文献", type="primary"):
            if not ref_topic:
                st.warning("请输入研究主题")
            else:
                with st.spinner("检索参考文献..."):
                    refs = paper_ast.suggest_references(ref_topic, num_refs)
                st.markdown(refs)

    with tab_journal:
        st.subheader("投稿期刊推荐")
        jnl_topic = st.text_input("研究主题", key="jnl_topic",
                                   placeholder="您的研究方向")
        quality = st.select_slider("研究质量水平",
                                   options=["初级", "中等", "较高", "高水平"],
                                   value="中等")
        if st.button("📰 推荐期刊", type="primary"):
            if not jnl_topic:
                st.warning("请输入研究主题")
            else:
                with st.spinner("分析推荐中..."):
                    journals = paper_ast.suggest_journals(jnl_topic, quality)
                st.markdown(journals)


# ─────────────────────────────────────────────────────────────
# 模块 6：学习分析
# ─────────────────────────────────────────────────────────────

def page_learning_analytics():
    st.title("📊 学习分析")
    st.markdown('<div class="hero-subtitle">可视化学习行为，生成个人学习画像</div>', unsafe_allow_html=True)

    analytics = get_learning_analytics()
    username  = st.session_state.username
    stats     = analytics.get_user_stats(username)

    # 顶部概览
    cols = st.columns(4)
    overview_items = [
        ("总操作次数", stats.get("total_actions", 0),    "📊"),
        ("图像分析次数", stats.get("analysis_count", 0), "🔬"),
        ("提问次数",    stats.get("chat_count", 0),       "💬"),
        ("学习等级",    analytics.generate_learning_portrait()["progress_level"], "🏆"),
    ]
    for col, (label, value, icon) in zip(cols, overview_items):
        with col:
            st.markdown(render_metric(label, f"{icon} {value}"),
                        unsafe_allow_html=True)

    st.divider()

    col_chart1, col_chart2 = st.columns(2, gap="large")

    with col_chart1:
        st.subheader("📅 学习活跃度（近7天）")
        activity_img = analytics.plot_activity_heatmap(username)
        st.image(activity_img, use_container_width=True)

    with col_chart2:
        st.subheader("🍩 功能模块使用分布")
        module_img = analytics.plot_module_usage(username)
        st.image(module_img, use_container_width=True)

    st.divider()

    # 学习画像
    st.subheader("🎭 个人学习画像")
    portrait = analytics.generate_learning_portrait(username)

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown(f"**用户**：{portrait['username']}")
        st.markdown(f"**学习等级**：{portrait['progress_level']}")
        st.markdown(f"**生成时间**：{portrait['generated_at']}")

        if portrait["strengths"]:
            st.markdown("**💪 学习优势：**")
            for s in portrait["strengths"]:
                st.markdown(f"  ✅ {s}")
        else:
            st.info("继续使用平台，系统将分析您的学习优势")

    with col_p2:
        if portrait["suggestions"]:
            st.markdown("**💡 提升建议：**")
            for suggestion in portrait["suggestions"]:
                st.markdown(f"""
                <div class="info-box">{suggestion}</div>
                """, unsafe_allow_html=True)

    # 导出报告
    st.divider()
    col_export1, col_export2 = st.columns(2)
    with col_export1:
        if st.button("📥 导出学习记录（CSV）", use_container_width=True):
            csv_path = analytics.export_report_csv(username)
            if csv_path and Path(csv_path).exists():
                with open(csv_path, "rb") as f:
                    st.download_button(
                        "⬇️ 下载CSV",
                        data=f.read(),
                        file_name=f"{username}_learning_report.csv",
                        mime="text/csv",
                    )

    with col_export2:
        portrait_json = json.dumps(portrait, ensure_ascii=False, indent=2)
        st.download_button(
            "📄 导出学习画像（JSON）",
            data=portrait_json.encode("utf-8"),
            file_name=f"{username}_portrait.json",
            mime="application/json",
            use_container_width=True,
        )


# ─────────────────────────────────────────────────────────────
# 首页
# ─────────────────────────────────────────────────────────────

def page_home():
    st.markdown("""
    <div style="text-align:center; padding: 2rem 0 1rem;">
        <div style="font-size:4rem;">👁️</div>
        <div class="hero-title" style="font-size:2.5rem; text-align:center;">FundusAI-Edu</div>
        <div class="hero-subtitle" style="text-align:center; font-size:1.1rem;">
            眼底图像AI教学与科研辅助平台 · 让医学AI触手可及
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # 功能模块卡片
    modules = [
        ("🔬", "眼底图像智能分析", "U-Net血管分割 + 病变识别 + 可视化报告"),
        ("🌐", "血管拓扑特征分析", "六维特征提取 + 雷达图 + 临床意义解读"),
        ("🤖", "AI科研导师",       "RAG知识问答 + 多轮对话 + 专业指导"),
        ("🎯", "科研选题生成器",   "个性化选题推荐 + 研究方案 + 实验报告"),
        ("📝", "论文写作辅助",     "框架生成 + 章节写作 + 润色 + 期刊推荐"),
        ("📊", "学习分析",         "行为统计 + 可视化 + 个人学习画像"),
    ]
    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(modules):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size:2rem; margin-bottom:0.5rem;">{icon}</div>
                <div style="font-weight:700; color:#e6edf3; margin-bottom:0.3rem;">{title}</div>
                <div style="color:#8b949e; font-size:0.85rem;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    # 技术栈
    st.subheader("🛠️ 技术架构")
    tech_cols = st.columns(5)
    tech_stack = [
        ("🐍", "Python", "核心语言"),
        ("⚡", "Streamlit", "Web界面"),
        ("🔥", "PyTorch", "深度学习"),
        ("🧠", "DeepSeek", "大语言模型"),
        ("🗄️", "ChromaDB", "向量知识库"),
    ]
    for col, (icon, name, desc) in zip(tech_cols, tech_stack):
        with col:
            st.markdown(f"""
            <div style="text-align:center; padding:1rem; background:#161b22;
                        border-radius:8px; border:1px solid #30363d;">
                <div style="font-size:1.8rem;">{icon}</div>
                <div style="font-weight:600; color:#e6edf3;">{name}</div>
                <div style="font-size:0.75rem; color:#8b949e;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.caption("📌 快速开始：左侧选择功能模块 → 上传眼底图像 → 开始AI分析")


# ─────────────────────────────────────────────────────────────
# 主导航
# ─────────────────────────────────────────────────────────────

PAGES = {
    "🏠 首页":             page_home,
    "🔬 眼底图像分析":    page_fundus_analysis,
    "🌐 血管拓扑分析":    page_topology_analysis,
    "🤖 AI科研导师":       page_rag_chat,
    "🎯 科研选题生成器":  page_topic_generator,
    "📝 论文写作辅助":    page_paper_assistant,
    "📊 学习分析":         page_learning_analytics,
}


def main():
    render_sidebar()

    # 导航菜单
    with st.sidebar:
        st.subheader("📌 功能导航")
        selected_page = st.radio(
            "选择功能模块",
            options=list(PAGES.keys()),
            label_visibility="collapsed",
        )

    # 渲染页面
    PAGES[selected_page]()

    # 记录页面访问
    try:
        analytics = get_learning_analytics()
        module_name = selected_page.split(" ", 1)[-1].replace(" ", "_")
        analytics.log_action(module_name, "page_visit")
    except Exception:
        pass


if __name__ == "__main__":
    main()
