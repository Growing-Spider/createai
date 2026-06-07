# =============================================================
# modules/__init__.py
# =============================================================
"""
FundusAI-Edu 功能模块包

模块列表：
    fundus_analysis    - 眼底图像智能分析（U-Net血管分割 + 病变识别）
    topology_analysis  - 血管拓扑特征分析（骨架化 + NetworkX图分析）
    rag_chat           - AI科研导师（RAG问答系统）
    topic_generator    - 科研选题生成器
    paper_assistant    - 论文写作辅助
    learning_analytics - 学习行为分析
"""

from .fundus_analysis   import FundusAnalyzer
from .topology_analysis import TopologyAnalyzer
from .rag_chat          import RAGChat, KnowledgeBaseManager
from .topic_generator   import TopicGenerator
from .paper_assistant   import PaperAssistant
from .learning_analytics import LearningAnalytics, init_database

__all__ = [
    "FundusAnalyzer",
    "TopologyAnalyzer",
    "RAGChat",
    "KnowledgeBaseManager",
    "TopicGenerator",
    "PaperAssistant",
    "LearningAnalytics",
    "init_database",
]
