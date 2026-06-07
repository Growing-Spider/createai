# =============================================================
# build.py — FundusAI-Edu exe 打包脚本
# 使用: python build.py
# 输出: F:\demo\dist\FundusAI-Edu.exe
# =============================================================

import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
DIST_DIR = BASE_DIR.parent / "dist"

print(f"项目路径: {BASE_DIR}")
print(f"输出路径: {DIST_DIR}")
print()

# 直接用 spec 文件打包（配置在 FundusAI-Edu.spec 中）
cmd = [
    sys.executable, "-m", "PyInstaller",
    str(BASE_DIR / "FundusAI-Edu.spec"),
    "--clean",
    "--noconfirm",
]

result = subprocess.run(cmd, cwd=str(BASE_DIR))
if result.returncode != 0:
    print("\n[ERROR] 打包失败，请检查错误信息")
    sys.exit(1)

exe = DIST_DIR / "FundusAI-Edu.exe"
if exe.exists():
    size = exe.stat().st_size / (1024 * 1024)
    print(f"\n[OK] 打包成功: {exe} ({size:.1f} MB)")
else:
    print("\n[ERROR] 未找到生成的 exe 文件")
