# =============================================================
# run.py — FundusAI-Edu 桌面窗口启动器
# 双击运行此文件，以原生窗口模式启动平台
# =============================================================

import os
import sys
import time
import threading
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()


def start_streamlit():
    """后台启动 Streamlit 服务"""
    env = os.environ.copy()
    env["STREAMLIT_HOME"] = str(BASE_DIR / ".streamlit")
    env["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"

    subprocess.Popen(
        [
            sys.executable,
            "-m", "streamlit", "run", str(BASE_DIR / "app.py"),
            "--server.port", "8501",
            "--server.address", "127.0.0.1",
            "--server.headless", "true",
            "--server.fileWatcherType", "none",
            "--server.enableXsrfProtection", "false",
            "--server.enableCORS", "true",
            "--global.developmentMode", "false",
            "--browser.gatherUsageStats", "false",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env=env,
        cwd=str(BASE_DIR),
    )


def wait_for_server(timeout=30):
    """等待 Streamlit 启动就绪"""
    import urllib.request
    start = time.time()
    while time.time() - start < timeout:
        try:
            urllib.request.urlopen("http://127.0.0.1:8501/_stcore/health", timeout=2)
            return True
        except Exception:
            time.sleep(0.5)
    return False


def main():
    # 先杀掉可能残留的旧进程
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(("127.0.0.1", 8501))
    s.close()
    if result == 0:
        print("[run.py] 端口 8501 已被占用，尝试复用...")

    # 启动 Streamlit
    print("[run.py] 正在启动服务...")
    start_streamlit()
    print("[run.py] 等待服务就绪...")
    if not wait_for_server():
        print("[run.py] ❌ 服务启动超时，请检查 app.py 是否可以正常运行")
        sys.exit(1)

    print("[run.py] 服务就绪，打开桌面窗口...")

    # 打开原生桌面窗口
    import webview
    window = webview.create_window(
        title="FundusAI-Edu 眼底图像AI教学平台",
        url="http://127.0.0.1:8501",
        width=1400,
        height=900,
        min_size=(1024, 700),
        resizable=True,
        fullscreen=False,
        easy_drag=False,
    )
    webview.start(gui="edgechromium" if os.name == "nt" else None)

    # 窗口关闭后清理
    print("[run.py] 窗口已关闭，正在停止服务...")
    try:
        import requests
        requests.post("http://127.0.0.1:8501/_stcore/shutdown", timeout=3)
    except Exception:
        pass
    print("[run.py] 服务已停止")


if __name__ == "__main__":
    main()
