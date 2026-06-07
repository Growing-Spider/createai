# =============================================================
# rag_chat.py — AI科研导师模块（RAG问答）
# 功能：知识库构建、向量检索、DeepSeek LLM生成回答
# =============================================================

import os
import logging
from pathlib import Path
from typing import Optional
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import (
    DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DEEPSEEK_MODEL,
    DEEPSEEK_MAX_TOKENS, DEEPSEEK_TEMPERATURE,
    CHROMA_PERSIST_DIR, CHUNK_SIZE, CHUNK_OVERLAP, RAG_TOP_K,
    KNOWLEDGE_BASE_DIR, SYSTEM_PROMPT_RAG,
)

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────
# 知识库管理
# ─────────────────────────────────────────────────────────────

class KnowledgeBaseManager:
    """构建和管理本地向量知识库"""

    def __init__(self):
        self.vectorstore = None
        self._init_vectorstore()

    def _init_vectorstore(self):
        """初始化 ChromaDB 向量库"""
        try:
            import chromadb
            from langchain_community.vectorstores import Chroma
            from langchain_community.embeddings import HuggingFaceEmbeddings

            embedding_model = HuggingFaceEmbeddings(
                model_name="BAAI/bge-small-zh-v1.5",
                model_kwargs={"device": "cpu"},
                encode_kwargs={"normalize_embeddings": True},
            )

            self.vectorstore = Chroma(
                persist_directory=CHROMA_PERSIST_DIR,
                embedding_function=embedding_model,
                collection_name="fundus_knowledge",
            )
            logger.info("✅ ChromaDB 知识库初始化成功")
        except Exception as e:
            logger.warning(f"⚠️ ChromaDB 初始化失败，将使用关键词检索：{e}")
            self.vectorstore = None

    def add_documents_from_directory(self, directory: str) -> int:
        """从目录批量导入文档到知识库"""
        try:
            from langchain_community.document_loaders import (
                PyPDFLoader, TextLoader, Docx2txtLoader,
                DirectoryLoader,
            )
            from langchain.text_splitter import RecursiveCharacterTextSplitter

            loaders = {
                "**/*.pdf":  PyPDFLoader,
                "**/*.txt":  TextLoader,
                "**/*.docx": Docx2txtLoader,
            }
            documents = []
            for pattern, loader_cls in loaders.items():
                for file_path in Path(directory).glob(pattern):
                    try:
                        loader = loader_cls(str(file_path))
                        docs = loader.load()
                        documents.extend(docs)
                        logger.info(f"  已加载：{file_path.name}")
                    except Exception as e:
                        logger.error(f"  加载失败 {file_path.name}：{e}")

            if not documents:
                return 0

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP,
                separators=["\n\n", "\n", "。", "！", "？", " ", ""],
            )
            chunks = splitter.split_documents(documents)

            if self.vectorstore:
                self.vectorstore.add_documents(chunks)
                logger.info(f"✅ 已添加 {len(chunks)} 个文本块到知识库")
            return len(chunks)

        except Exception as e:
            logger.error(f"文档导入失败：{e}")
            return 0

    def add_default_knowledge(self):
        """添加内置的眼底医学知识"""
        default_knowledge = [
            {
                "text": """眼底图像（Fundus Image）是通过眼底相机拍摄的视网膜照片，
                是眼科诊断的重要依据。正常眼底包括：视盘（视神经乳头）、视网膜血管、
                黄斑、视杯等结构。眼底检查可发现糖尿病视网膜病变、青光眼、
                年龄相关性黄斑变性等多种眼科疾病。""",
                "metadata": {"source": "眼科学基础", "category": "基础知识"},
            },
            {
                "text": """糖尿病视网膜病变（Diabetic Retinopathy, DR）是糖尿病最常见的
                微血管并发症，也是工作年龄人群首位致盲原因。DR分期：1.无明显视网膜病变；
                2.轻度非增殖性DR（NPDR）：微动脉瘤；3.中度NPDR：出血、渗出；
                4.重度NPDR：广泛出血；5.增殖性DR（PDR）：新生血管形成。
                AI辅助诊断可实现高灵敏度、高特异度的自动分级。""",
                "metadata": {"source": "糖尿病视网膜病变指南", "category": "临床知识"},
            },
            {
                "text": """视网膜血管分割是眼底图像分析的核心任务之一。经典方法包括：
                Frangi滤波器（基于Hessian矩阵）、DRIVE数据集的监督学习方法。
                深度学习方法：U-Net于2015年由Ronneberger等提出，采用编码器-解码器架构，
                是医学图像分割的标准方法。在DRIVE数据集上AUC可达0.9790，
                敏感性0.7811，特异性0.9807。""",
                "metadata": {"source": "医学图像处理", "category": "技术知识"},
            },
            {
                "text": """血管拓扑特征是量化视网膜血管结构的重要指标：
                1.血管密度（Vessel Density）：血管像素占图像总像素的比例；
                2.分叉点（Bifurcation Points）：三条或更多血管交汇处；
                3.终末点（End Points）：血管末端节点；
                4.平均血管宽度（Average Vessel Width）：通过距离变换计算；
                5.血管迂曲度（Tortuosity）：实际路径长度与端点直线距离之比；
                6.分形维数（Fractal Dimension）：盒计数法，反映网络复杂度（正常值约1.5-1.7）。""",
                "metadata": {"source": "血管拓扑分析", "category": "技术知识"},
            },
            {
                "text": """RAG（Retrieval-Augmented Generation）检索增强生成技术是将
                外部知识库与大语言模型结合的方法。工作流程：
                1.文档预处理：分块、向量化嵌入；
                2.向量存储：ChromaDB、Milvus等；
                3.相似度检索：余弦相似度或点积；
                4.提示词构建：将检索内容注入提示词；
                5.LLM生成：基于检索内容生成回答。
                RAG可有效减少大模型幻觉，提升专业领域问答准确性。""",
                "metadata": {"source": "AI技术原理", "category": "技术知识"},
            },
            {
                "text": """青光眼（Glaucoma）是以视神经损害和视野缺损为特征的眼病，
                是全球第二大致盲原因。视盘杯盘比（Cup-to-Disc Ratio, CDR）是诊断青光眼的
                重要指标，CDR > 0.6 高度怀疑青光眼。AI辅助诊断方法主要包括：
                视盘分割、视杯分割、CDR自动测量。常用数据集：ORIGA、DRISHTI、RIM-ONE。""",
                "metadata": {"source": "青光眼诊断指南", "category": "临床知识"},
            },
            {
                "text": """医学图像分割评估指标：
                1.Dice系数（F1分数）= 2|A∩B|/(|A|+|B|)，范围[0,1]；
                2.IoU（Intersection over Union）= |A∩B|/|A∪B|；
                3.敏感性（Sensitivity/Recall）= TP/(TP+FN)；
                4.特异性（Specificity）= TN/(TN+FP)；
                5.AUC（ROC曲线下面积）：综合评价分类器性能。
                优秀的血管分割模型Dice系数通常 > 0.82。""",
                "metadata": {"source": "医学图像评估", "category": "技术知识"},
            },
        ]

        try:
            from langchain.schema import Document
            docs = [
                Document(page_content=item["text"], metadata=item["metadata"])
                for item in default_knowledge
            ]
            if self.vectorstore:
                self.vectorstore.add_documents(docs)
                logger.info(f"✅ 已添加 {len(docs)} 条内置知识")
        except Exception as e:
            logger.error(f"添加默认知识失败：{e}")

    def search(self, query: str, k: int = RAG_TOP_K) -> list:
        """检索相关文档"""
        if self.vectorstore is None:
            return self._keyword_search(query, k)
        try:
            results = self.vectorstore.similarity_search(query, k=k)
            return [{"content": doc.page_content, "metadata": doc.metadata}
                    for doc in results]
        except Exception as e:
            logger.error(f"向量检索失败：{e}")
            return self._keyword_search(query, k)

    def _keyword_search(self, query: str, k: int) -> list:
        """关键词兜底检索（知识库文件直接搜索）"""
        results = []
        keywords = query.split()
        for txt_file in Path(KNOWLEDGE_BASE_DIR).glob("**/*.txt"):
            try:
                content = txt_file.read_text(encoding="utf-8", errors="ignore")
                if any(kw in content for kw in keywords):
                    # 提取匹配段落
                    paragraphs = content.split("\n\n")
                    for para in paragraphs:
                        if any(kw in para for kw in keywords):
                            results.append({
                                "content": para[:500],
                                "metadata": {"source": txt_file.name},
                            })
                            if len(results) >= k:
                                return results
            except Exception:
                continue
        return results


# ─────────────────────────────────────────────────────────────
# AI科研导师（RAG + LLM）
# ─────────────────────────────────────────────────────────────

class RAGChat:
    """基于RAG的AI科研导师对话系统"""

    def __init__(self):
        self.kb_manager = KnowledgeBaseManager()
        self.conversation_history = []
        self._client = None

    def _get_client(self):
        """获取 DeepSeek API 客户端（懒加载）"""
        if self._client is None:
            try:
                from openai import OpenAI
                self._client = OpenAI(
                    api_key=DEEPSEEK_API_KEY,
                    base_url=DEEPSEEK_BASE_URL,
                )
            except ImportError:
                logger.error("openai SDK 未安装，请运行：pip install openai")
        return self._client

    def chat(self, user_message: str,
             with_rag: bool = True,
             stream: bool = False) -> str:
        """
        与AI科研导师对话
        
        Args:
            user_message: 用户问题
            with_rag: 是否启用知识库检索
            stream: 是否流式输出
        Returns:
            助手回答
        """
        # RAG 检索
        context = ""
        retrieved_docs = []
        if with_rag:
            retrieved_docs = self.kb_manager.search(user_message)
            if retrieved_docs:
                context_parts = [
                    f"【参考资料{i+1}】（来源：{doc.get('metadata',{}).get('source','未知')}）\n{doc['content']}"
                    for i, doc in enumerate(retrieved_docs)
                ]
                context = "\n\n".join(context_parts)

        # 构建消息
        messages = [{"role": "system", "content": SYSTEM_PROMPT_RAG}]

        # 添加对话历史（保留最近6轮）
        for msg in self.conversation_history[-12:]:
            messages.append(msg)

        # 用户消息（含检索内容）
        if context:
            augmented_message = (
                f"以下是与问题相关的参考资料，请基于这些内容回答：\n\n"
                f"{context}\n\n"
                f"---\n用户问题：{user_message}"
            )
        else:
            augmented_message = user_message

        messages.append({"role": "user", "content": augmented_message})

        # 调用 DeepSeek API
        try:
            client = self._get_client()
            if client is None:
                return self._fallback_answer(user_message, retrieved_docs)

            response = client.chat.completions.create(
                model=DEEPSEEK_MODEL,
                messages=messages,
                max_tokens=DEEPSEEK_MAX_TOKENS,
                temperature=DEEPSEEK_TEMPERATURE,
            )
            answer = response.choices[0].message.content

            # 更新对话历史
            self.conversation_history.append({
                "role": "user", "content": user_message
            })
            self.conversation_history.append({
                "role": "assistant", "content": answer
            })

            return answer

        except Exception as e:
            logger.error(f"API调用失败：{e}")
            return self._fallback_answer(user_message, retrieved_docs)

    def _fallback_answer(self, question: str, docs: list) -> str:
        """API不可用时的兜底回答（基于知识库内容）"""
        if not docs:
            return (
                "抱歉，当前无法连接AI服务，且知识库中未找到相关内容。"
                "请检查API配置或稍后重试。"
            )
        answer_parts = [
            "**（离线模式：以下为知识库检索结果）**\n",
            f"关于您的问题「{question}」，知识库中有以下相关内容：\n",
        ]
        for i, doc in enumerate(docs[:3], 1):
            src = doc.get("metadata", {}).get("source", "知识库")
            answer_parts.append(f"\n**参考{i}**（来源：{src}）\n{doc['content']}\n")
        return "\n".join(answer_parts)

    def clear_history(self):
        """清空对话历史"""
        self.conversation_history = []

    def initialize_knowledge_base(self) -> bool:
        """初始化知识库（添加内置知识 + 目录文档）"""
        try:
            self.kb_manager.add_default_knowledge()
            count = self.kb_manager.add_documents_from_directory(
                str(KNOWLEDGE_BASE_DIR)
            )
            logger.info(f"✅ 知识库初始化完成，外部文档数：{count}")
            return True
        except Exception as e:
            logger.error(f"知识库初始化失败：{e}")
            return False
