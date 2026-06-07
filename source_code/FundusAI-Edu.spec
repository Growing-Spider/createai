# -*- mode: python ; coding: utf-8 -*-
# FundusAI-Edu.spec — PyInstaller 打包配置
# 打包命令: pyinstaller FundusAI-Edu.spec

import sys
from pathlib import Path

BASE_DIR = Path(SPECPATH)  # spec 文件所在目录

a = Analysis(
    [str(BASE_DIR / "launcher.py")],
    pathex=[str(BASE_DIR)],
    binaries=[],
    datas=[
        # app.py 和模块文件随 exe 一起分发到输出目录
        (str(BASE_DIR / "app.py"), "."),
        (str(BASE_DIR / "config.py"), "."),
        (str(BASE_DIR / "modules"), "modules"),
        (str(BASE_DIR / "knowledge_base"), "knowledge_base"),
        (str(BASE_DIR / "models"), "models"),
        (str(BASE_DIR / ".streamlit"), ".streamlit"),
    ],
    hiddenimports=[
        "streamlit",
        "streamlit.runtime",
        "streamlit.web",
        "streamlit.web.bootstrap",
        "streamlit.web.server",
        "streamlit.runtime.scriptrunner",
        "streamlit.runtime.app_session",
        "streamlit.elements",
        "streamlit.commands",
        "cv2",
        "torch",
        "numpy",
        "PIL",
        "PIL.Image",
        "scipy",
        "skimage",
        "skimage.filters",
        "skimage.morphology",
        "skimage.measure",
        "networkx",
        "pandas",
        "matplotlib",
        "plotly",
        "tornado",
        "uvicorn",
        "pywebview",
        "chromadb",
        "sentence_transformers",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["tkinter", "IPython", "jupyter", "notebook"],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="FundusAI-Edu",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,           # 窗口应用（不显示控制台）
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
