# =============================================================
# learning_analytics.py — 学习分析模块
# 功能：记录学习行为、统计使用数据、生成学习画像
# =============================================================

import sqlite3
import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
import sys

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import io
from PIL import Image

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import DATABASE_PATH

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────
# 数据库初始化
# ─────────────────────────────────────────────────────────────

def init_database():
    """初始化 SQLite 数据库，创建所需表"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.executescript("""
    -- 用户表
    CREATE TABLE IF NOT EXISTS users (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        username    TEXT UNIQUE NOT NULL,
        display_name TEXT,
        student_id  TEXT,
        department  TEXT,
        created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    -- 学习记录表
    CREATE TABLE IF NOT EXISTS learning_records (
        id           INTEGER PRIMARY KEY AUTOINCREMENT,
        username     TEXT NOT NULL,
        session_id   TEXT,
        module       TEXT NOT NULL,       -- 功能模块
        action       TEXT NOT NULL,       -- 操作类型
        detail       TEXT,                -- 详情（JSON）
        duration_sec INTEGER DEFAULT 0,   -- 停留时长（秒）
        created_at   DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    -- 图像分析记录
    CREATE TABLE IF NOT EXISTS analysis_records (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        username        TEXT NOT NULL,
        image_name      TEXT,
        vessel_density  REAL,
        bifurcation_count INTEGER,
        endpoint_count  INTEGER,
        avg_vessel_width REAL,
        tortuosity      REAL,
        fractal_dimension REAL,
        dr_grade        TEXT,
        dr_confidence   REAL,
        image_quality   TEXT,
        created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    -- 问答记录
    CREATE TABLE IF NOT EXISTS chat_records (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        username    TEXT NOT NULL,
        question    TEXT NOT NULL,
        answer      TEXT,
        module      TEXT DEFAULT 'rag_chat',
        created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    -- 选题记录
    CREATE TABLE IF NOT EXISTS topic_records (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        username        TEXT NOT NULL,
        interest_area   TEXT,
        generated_topics TEXT,            -- JSON
        selected_topic  TEXT,
        created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    conn.close()
    logger.info("✅ 数据库初始化完成")


# ─────────────────────────────────────────────────────────────
# 学习分析器
# ─────────────────────────────────────────────────────────────

class LearningAnalytics:
    """学习行为分析与可视化"""

    def __init__(self, username: str = "anonymous"):
        self.username = username
        self.session_id = datetime.now().strftime("%Y%m%d%H%M%S")
        init_database()

    # ─────────────────────────────────────────────────────────
    # 数据记录
    # ─────────────────────────────────────────────────────────

    def log_action(self, module: str, action: str,
                   detail: dict = None, duration_sec: int = 0):
        """记录用户操作"""
        try:
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO learning_records
                   (username, session_id, module, action, detail, duration_sec)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (self.username, self.session_id, module, action,
                 json.dumps(detail or {}, ensure_ascii=False), duration_sec)
            )
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"记录操作失败：{e}")

    def log_analysis(self, image_name: str, features: dict, lesion_info: dict):
        """记录图像分析结果"""
        try:
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO analysis_records
                   (username, image_name, vessel_density, bifurcation_count,
                    endpoint_count, avg_vessel_width, tortuosity, fractal_dimension,
                    dr_grade, dr_confidence, image_quality)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    self.username, image_name,
                    features.get("vessel_density", 0),
                    features.get("bifurcation_count", 0),
                    features.get("endpoint_count", 0),
                    features.get("avg_vessel_width", 0),
                    features.get("tortuosity", 0),
                    features.get("fractal_dimension", 0),
                    lesion_info.get("dr_grade", ""),
                    lesion_info.get("dr_confidence", 0),
                    lesion_info.get("overall_quality", ""),
                )
            )
            conn.commit()
            conn.close()
            self.log_action("fundus_analysis", "image_analyzed",
                            {"image": image_name})
        except Exception as e:
            logger.error(f"记录分析结果失败：{e}")

    def log_chat(self, question: str, answer: str, module: str = "rag_chat"):
        """记录问答记录"""
        try:
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO chat_records (username, question, answer, module)
                   VALUES (?, ?, ?, ?)""",
                (self.username, question, answer, module)
            )
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"记录问答失败：{e}")

    def log_topic(self, interest_area: str, topics: list,
                  selected: str = ""):
        """记录选题记录"""
        try:
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO topic_records
                   (username, interest_area, generated_topics, selected_topic)
                   VALUES (?, ?, ?, ?)""",
                (self.username, interest_area,
                 json.dumps(topics, ensure_ascii=False), selected)
            )
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"记录选题失败：{e}")

    # ─────────────────────────────────────────────────────────
    # 统计分析
    # ─────────────────────────────────────────────────────────

    def get_user_stats(self, username: str = None) -> dict:
        """获取用户学习统计数据"""
        uname = username or self.username
        try:
            conn = sqlite3.connect(DATABASE_PATH)

            # 总操作次数
            total_actions = pd.read_sql_query(
                "SELECT COUNT(*) as cnt FROM learning_records WHERE username=?",
                conn, params=(uname,)
            )["cnt"][0]

            # 各模块使用次数
            module_stats = pd.read_sql_query(
                """SELECT module, COUNT(*) as cnt
                   FROM learning_records WHERE username=?
                   GROUP BY module ORDER BY cnt DESC""",
                conn, params=(uname,)
            )

            # 图像分析次数
            analysis_count = pd.read_sql_query(
                "SELECT COUNT(*) as cnt FROM analysis_records WHERE username=?",
                conn, params=(uname,)
            )["cnt"][0]

            # 问答次数
            chat_count = pd.read_sql_query(
                "SELECT COUNT(*) as cnt FROM chat_records WHERE username=?",
                conn, params=(uname,)
            )["cnt"][0]

            # 最近7天活跃度
            week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
            daily_activity = pd.read_sql_query(
                """SELECT DATE(created_at) as date, COUNT(*) as cnt
                   FROM learning_records
                   WHERE username=? AND created_at >= ?
                   GROUP BY DATE(created_at)
                   ORDER BY date""",
                conn, params=(uname, week_ago)
            )

            # 最近分析的特征均值
            feature_means = pd.read_sql_query(
                """SELECT
                   AVG(vessel_density) as avg_density,
                   AVG(bifurcation_count) as avg_bifurcation,
                   AVG(tortuosity) as avg_tortuosity,
                   AVG(fractal_dimension) as avg_fractal
                   FROM analysis_records WHERE username=?""",
                conn, params=(uname,)
            )

            conn.close()

            return {
                "total_actions":    int(total_actions),
                "analysis_count":   int(analysis_count),
                "chat_count":       int(chat_count),
                "module_stats":     module_stats.to_dict("records"),
                "daily_activity":   daily_activity.to_dict("records"),
                "feature_means":    feature_means.iloc[0].to_dict() if not feature_means.empty else {},
            }
        except Exception as e:
            logger.error(f"获取统计数据失败：{e}")
            return {}

    def get_all_users_stats(self) -> pd.DataFrame:
        """获取所有用户统计（管理员视图）"""
        try:
            conn = sqlite3.connect(DATABASE_PATH)
            df = pd.read_sql_query(
                """SELECT
                   username,
                   COUNT(*) as total_actions,
                   MIN(created_at) as first_active,
                   MAX(created_at) as last_active
                   FROM learning_records
                   GROUP BY username
                   ORDER BY total_actions DESC""",
                conn
            )
            conn.close()
            return df
        except Exception as e:
            logger.error(f"获取全局统计失败：{e}")
            return pd.DataFrame()

    # ─────────────────────────────────────────────────────────
    # 可视化
    # ─────────────────────────────────────────────────────────

    def plot_activity_heatmap(self, username: str = None) -> Image.Image:
        """绘制学习活跃度折线图"""
        uname = username or self.username
        stats  = self.get_user_stats(uname)
        daily  = stats.get("daily_activity", [])

        fig, ax = plt.subplots(figsize=(10, 4), facecolor="#0d1117")
        ax.set_facecolor("#161b22")

        if daily:
            dates  = [d["date"] for d in daily]
            counts = [d["cnt"]  for d in daily]
            ax.plot(dates, counts, color="#58a6ff", linewidth=2, marker="o",
                    markersize=6, markerfacecolor="#58a6ff")
            ax.fill_between(dates, counts, alpha=0.2, color="#58a6ff")
        else:
            ax.text(0.5, 0.5, "暂无活动记录", ha="center", va="center",
                    color="gray", fontsize=14, transform=ax.transAxes)

        ax.set_title("近7天学习活跃度", color="white", fontsize=13,
                     fontproperties=_get_font())
        ax.set_xlabel("日期", color="gray", fontproperties=_get_font())
        ax.set_ylabel("操作次数", color="gray", fontproperties=_get_font())
        ax.tick_params(colors="white")
        ax.spines[:].set_color("#30363d")
        ax.grid(color="#21262d", linestyle="--", alpha=0.5)
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format="png", dpi=100, bbox_inches="tight",
                    facecolor="#0d1117")
        plt.close(fig)
        buf.seek(0)
        return Image.open(buf)

    def plot_module_usage(self, username: str = None) -> Image.Image:
        """绘制功能模块使用分布饼图"""
        uname = username or self.username
        stats  = self.get_user_stats(uname)
        module_stats = stats.get("module_stats", [])

        module_labels_cn = {
            "fundus_analysis":   "图像分析",
            "topology_analysis": "拓扑分析",
            "rag_chat":          "AI导师",
            "topic_generator":   "选题生成",
            "paper_assistant":   "论文辅助",
            "learning_analytics":"学习分析",
        }

        fig, ax = plt.subplots(figsize=(7, 7), facecolor="#0d1117")
        ax.set_facecolor("#0d1117")

        if module_stats:
            labels = [module_labels_cn.get(m["module"], m["module"])
                      for m in module_stats]
            sizes  = [m["cnt"] for m in module_stats]
            colors = ["#58a6ff", "#3fb950", "#f78166", "#d2a8ff",
                      "#ffa657", "#79c0ff"][:len(labels)]
            wedges, texts, autotexts = ax.pie(
                sizes, labels=labels, colors=colors,
                autopct="%1.1f%%", startangle=140,
                textprops={"color": "white", "fontproperties": _get_font()},
            )
            for at in autotexts:
                at.set_color("white")
        else:
            ax.text(0.5, 0.5, "暂无使用记录", ha="center", va="center",
                    color="gray", fontsize=14, transform=ax.transAxes)

        ax.set_title("功能模块使用分布", color="white", fontsize=13,
                     fontproperties=_get_font(), pad=20)
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format="png", dpi=100, bbox_inches="tight",
                    facecolor="#0d1117")
        plt.close(fig)
        buf.seek(0)
        return Image.open(buf)

    # ─────────────────────────────────────────────────────────
    # 学习画像生成
    # ─────────────────────────────────────────────────────────

    def generate_learning_portrait(self, username: str = None) -> dict:
        """生成学习画像"""
        uname = username or self.username
        stats = self.get_user_stats(uname)

        portrait = {
            "username":       uname,
            "generated_at":   datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "summary": {},
            "strengths":      [],
            "suggestions":    [],
            "progress_level": "初学者",
        }

        total = stats.get("total_actions", 0)
        analysis_cnt = stats.get("analysis_count", 0)
        chat_cnt     = stats.get("chat_count", 0)

        # 进度等级
        if total > 100:
            portrait["progress_level"] = "熟练用户"
        elif total > 30:
            portrait["progress_level"] = "进阶用户"
        else:
            portrait["progress_level"] = "初学者"

        portrait["summary"] = {
            "total_operations": total,
            "images_analyzed":  analysis_cnt,
            "questions_asked":  chat_cnt,
            "progress_level":   portrait["progress_level"],
        }

        # 优势分析
        if analysis_cnt > 5:
            portrait["strengths"].append("图像分析实践积极，动手能力强")
        if chat_cnt > 10:
            portrait["strengths"].append("善于利用AI导师，学习主动性高")
        if total > 50:
            portrait["strengths"].append("使用频率高，学习持续性好")

        # 建议
        if analysis_cnt < 3:
            portrait["suggestions"].append("建议多进行眼底图像分析练习，加深对血管结构的理解")
        if chat_cnt < 5:
            portrait["suggestions"].append("建议充分利用AI科研导师功能，提出更多专业问题")
        if stats.get("feature_means", {}).get("avg_density") is None:
            portrait["suggestions"].append("建议分析更多图像，积累数据以了解正常值范围")

        return portrait

    def export_report_csv(self, username: str = None) -> str:
        """导出学习记录为 CSV"""
        uname = username or self.username
        try:
            conn = sqlite3.connect(DATABASE_PATH)
            df = pd.read_sql_query(
                "SELECT * FROM learning_records WHERE username=? ORDER BY created_at DESC",
                conn, params=(uname,)
            )
            conn.close()
            csv_path = Path(DATABASE_PATH).parent / f"{uname}_learning_report.csv"
            df.to_csv(csv_path, index=False, encoding="utf-8-sig")
            return str(csv_path)
        except Exception as e:
            logger.error(f"导出CSV失败：{e}")
            return ""


# ─────────────────────────────────────────────────────────────
# 辅助函数
# ─────────────────────────────────────────────────────────────

def _get_font():
    import matplotlib.font_manager as fm
    try:
        for fp in ["C:/Windows/Fonts/simhei.ttf",
                   "C:/Windows/Fonts/msyh.ttc",
                   "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"]:
            if Path(fp).exists():
                return fm.FontProperties(fname=fp)
    except Exception:
        pass
    return fm.FontProperties()
