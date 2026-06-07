# =============================================================
# launcher.py — PyInstaller 打包入口（处理 exe 内路径）
# =============================================================

import os
import sys
import time
import socket
import subprocess
from pathlib import Path


def get_base_dir():
    """获取真实文件目录（exe 打包后 sys._MEIPASS 是临时解压目录）"""
    if getattr(sys, "frozen", False):
        # PyInstaller 打包后的 exe 运行路径
        return Path(sys.executable).parent.resolve()
    else:
        return Path(__file__).parent.resolve()


BASE_DIR = get_base_dir()


def fix_encoding():
    """修复 Windows GBK 控制台编码问题"""
    if sys.stdout.encoding != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def start_streamlit():
    """后台启动 Streamlit 服务"""
    fix_encoding()

    app_path = BASE_DIR / "app.py"
    if not app_path.exists():
        print(f"[ERROR] 未找到 app.py: {app_path}")
        print("请确保 app.py 与 FundusAI-Edu.exe 在同一目录")
        input("按 Enter 退出...")
        sys.exit(1)

    env = os.environ.copy()
    env["STREAMLIT_HOME"] = str(BASE_DIR / ".streamlit")
    env["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
    env["PYTHONIOENCODING"] = "utf-8"

    subprocess.Popen(
        [
            sys.executable,
            "-m", "streamlit", "run", str(app_path),
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
    fix_encoding()

    # 检查端口占用
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(("127.0.0.1", 8501))
    s.close()
    if result == 0:
        print("[INFO] 端口 8501 已被占用，尝试复用...")

    print("[INFO] 正在启动 FundusAI-Edu 服务...")
    start_streamlit()
    print("[INFO] 等待服务就绪...")

    if not wait_for_server():
        print("[ERROR] 服务启动超时 (30秒)")
        print("可能原因：")
        print("  1. 防火墙阻止了本地连接")
        print("  2. 杀毒软件拦截了 Streamlit")
        print("  3. app.py 启动失败")
        input("按 Enter 退出...")
        sys.exit(1)

    print("[INFO] 服务就绪，打开桌面窗口...")

    import webview
    window = webview.create_window(
        title="FundusAI-Edu - 眼底图像AI教学平台",
        url="http://127.0.0.1:8501",
        width=1400,
        height=900,
        min_size=(1024, 700),
        resizable=True,
        fullscreen=False,
    )
    webview.start(gui="edgechromium" if os.name == "nt" else None)

    print("[INFO] 窗口已关闭，正在停止服务...")
    try:
        import urllib.request
        urllib.request.urlopen("http://127.0.0.1:8501/_stcore/shutdown", timeout=3)
    except Exception:
        pass
    print("[INFO] 服务已停止")


if __name__ == "__main__":
    main()
