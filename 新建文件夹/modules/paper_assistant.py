# =============================================================
# paper_assistant.py — 论文写作辅助模块
# 功能：论文框架生成、章节辅助写作、引言/摘要生成
# =============================================================

import logging
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import (
    DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DEEPSEEK_MODEL,
    DEEPSEEK_MAX_TOKENS, SYSTEM_PROMPT_PAPER,
)

logger = logging.getLogger(__name__)


class PaperAssistant:
    """医学论文写作辅助助手"""

    PAPER_TYPES = {
        "sci_original":    "SCI原著论文",
        "sci_review":      "SCI综述论文",
        "chinese_core":    "中文核心期刊",
        "graduation":      "毕业论文/学位论文",
        "conference":      "学术会议论文",
    }

    SECTION_PROMPTS = {
        "abstract": "请为这篇关于{topic}的论文撰写一个结构化摘要（约250字），包含：研究目的、方法、结果和结论。",
        "introduction": "请撰写关于{topic}的论文引言部分（约600字），包含：研究背景、国内外研究现状、研究空白、本研究目的和意义。",
        "methods": "请撰写关于{topic}的材料与方法部分（约500字），包含：数据来源、图像预处理、模型架构、评价指标、统计分析方法。",
        "results": "请根据以下数据，撰写研究结果部分（约400字），客观描述实验发现，不包含讨论内容。数据：{data}",
        "discussion": "请撰写关于{topic}的讨论部分（约600字），解释研究结果的意义，与既往研究比较，分析局限性，提出未来研究方向。",
        "conclusion": "请为关于{topic}的论文撰写简洁的结论部分（约200字），总结主要发现和贡献。",
    }

    def __init__(self):
        self._client = None

    def _get_client(self):
        if self._client is None:
            try:
                from openai import OpenAI
                self._client = OpenAI(
                    api_key=DEEPSEEK_API_KEY,
                    base_url=DEEPSEEK_BASE_URL,
                )
            except ImportError:
                logger.error("openai SDK 未安装")
        return self._client

    def _call_api(self, messages: list, temperature: float = 0.7) -> str:
        """统一 API 调用"""
        try:
            client = self._get_client()
            if client is None:
                return "⚠️ API 客户端未初始化，请检查 openai 库安装和 API Key 配置。"
            response = client.chat.completions.create(
                model=DEEPSEEK_MODEL,
                messages=messages,
                max_tokens=DEEPSEEK_MAX_TOKENS,
                temperature=temperature,
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"API 调用失败：{e}")
            return f"⚠️ 生成失败：{str(e)}\n请检查 API Key 配置。"

    # ─────────────────────────────────────────────────────────
    # 论文框架生成
    # ─────────────────────────────────────────────────────────

    def generate_paper_outline(self,
                                topic: str,
                                paper_type: str = "sci_original",
                                analysis_results: dict = None) -> str:
        """
        生成完整论文框架

        Args:
            topic: 论文主题/研究课题
            paper_type: 论文类型
            analysis_results: 眼底分析结果（可选，用于数据填充）
        Returns:
            Markdown 格式论文框架
        """
        paper_type_name = self.PAPER_TYPES.get(paper_type, "SCI原著论文")
        results_str = ""
        if analysis_results:
            features = analysis_results.get("topology_features", {})
            lesion   = analysis_results.get("lesion_info", {})
            results_str = f"""
已有实验数据可供参考：
- DR分级：{lesion.get('dr_grade', '待填写')}
- 血管密度：{features.get('vessel_density', '待填写')}
- 分形维数：{features.get('fractal_dimension', '待填写')}
"""

        prompt = f"""请为以下研究主题生成完整的{paper_type_name}论文框架（Markdown格式）：

**研究主题**：{topic}
**论文类型**：{paper_type_name}
{results_str}

框架应包含：
1. 论文标题（中英文）
2. 关键词（中英文，各5个）
3. 摘要结构（结构式摘要）
4. 正文各章节标题及写作要点
5. 图表清单（建议图表数量和类型）
6. 参考文献检索策略（关键词、数据库）
7. 投稿期刊推荐（3个相关期刊）

同时给出各章节字数建议和写作注意事项。"""

        return self._call_api([
            {"role": "system", "content": SYSTEM_PROMPT_PAPER},
            {"role": "user",   "content": prompt},
        ], temperature=0.7)

    # ─────────────────────────────────────────────────────────
    # 章节写作辅助
    # ─────────────────────────────────────────────────────────

    def write_section(self,
                       section: str,
                       topic: str,
                       additional_info: str = "",
                       data: str = "") -> str:
        """
        辅助撰写论文特定章节

        Args:
            section: 章节名称（abstract/introduction/methods/results/discussion/conclusion）
            topic: 研究主题
            additional_info: 补充信息
            data: 结果数据（results 章节需要）
        Returns:
            章节内容（Markdown格式）
        """
        if section not in self.SECTION_PROMPTS:
            return f"⚠️ 未知章节：{section}"

        section_prompt = self.SECTION_PROMPTS[section].format(
            topic=topic, data=data or "请提供具体实验数据"
        )

        full_prompt = section_prompt
        if additional_info:
            full_prompt += f"\n\n补充信息：{additional_info}"

        return self._call_api([
            {"role": "system", "content": SYSTEM_PROMPT_PAPER},
            {"role": "user",   "content": full_prompt},
        ], temperature=0.65)

    # ─────────────────────────────────────────────────────────
    # 语言润色
    # ─────────────────────────────────────────────────────────

    def polish_text(self, text: str, style: str = "academic") -> str:
        """
        论文文本润色

        Args:
            text: 待润色文本
            style: 润色风格（academic/concise/formal）
        Returns:
            润色后文本
        """
        style_desc = {
            "academic":  "学术规范，逻辑严谨，表述精确",
            "concise":   "简洁明了，去除冗余，保留核心信息",
            "formal":    "正式书面语，符合期刊投稿要求",
        }.get(style, "学术规范")

        prompt = f"""请对以下医学论文文本进行润色，风格要求：{style_desc}。
保持原意不变，重点改善表达准确性、逻辑连贯性和学术规范性。
同时指出3-5个主要修改点及原因。

原文：
{text}

请返回：
## 润色后文本
[润色后的文本]

## 主要修改说明
[逐条说明修改原因]"""

        return self._call_api([
            {"role": "system", "content": "你是一位经验丰富的医学论文编辑。"},
            {"role": "user",   "content": prompt},
        ], temperature=0.5)

    # ─────────────────────────────────────────────────────────
    # 参考文献辅助
    # ─────────────────────────────────────────────────────────

    def suggest_references(self, topic: str, num_refs: int = 10) -> str:
        """
        推荐参考文献方向

        Returns:
            参考文献推荐列表（Markdown格式）
        """
        prompt = f"""请为主题「{topic}」推荐{num_refs}篇核心参考文献，包括：
- 3篇经典基础论文（2015年前）
- 5篇近3年高质量SCI论文
- 2篇中文权威综述

对每篇文献请提供：
1. 作者（et al.形式）
2. 标题
3. 期刊名称
4. 发表年份
5. 主要贡献（一句话）
6. 重要性（★★★~★★★★★）

注意：请提供真实存在的文献，或明确标注为"建议检索方向"。"""

        return self._call_api([
            {"role": "system", "content": "你是一位熟悉眼科学和医学AI领域文献的专家。"},
            {"role": "user",   "content": prompt},
        ], temperature=0.6)

    # ─────────────────────────────────────────────────────────
    # 统计方法建议
    # ─────────────────────────────────────────────────────────

    def suggest_statistics(self, research_design: str) -> str:
        """
        根据研究设计推荐统计方法

        Args:
            research_design: 研究设计描述
        Returns:
            统计方法建议（Markdown格式）
        """
        prompt = f"""根据以下研究设计，推荐合适的统计分析方法：

研究设计：{research_design}

请提供：
1. 描述性统计方法
2. 推断性统计方法（含假设检验）
3. 模型性能评估指标
4. 统计软件推荐（SPSS/R/Python）
5. 常见统计错误提示
6. 报告规范（参考CONSORT/STARD等）"""

        return self._call_api([
            {"role": "system", "content": "你是一位医学统计专家。"},
            {"role": "user",   "content": prompt},
        ], temperature=0.5)

    # ─────────────────────────────────────────────────────────
    # 投稿建议
    # ─────────────────────────────────────────────────────────

    def suggest_journals(self, topic: str, quality_level: str = "中等") -> str:
        """推荐适合投稿的期刊"""
        prompt = f"""为主题「{topic}」的眼底AI研究推荐适合投稿的期刊。
研究质量水平：{quality_level}

请推荐：
**SCI期刊（5个）**：
- 期刊名称
- 影响因子（最新）
- 分区（JCR/中科院）
- 审稿周期
- 适合的文章类型

**中文核心期刊（3个）**：
- 期刊名称
- 收录情况（北大核心/CSCD）
- 特色要求

**投稿建议**：投稿顺序和注意事项"""

        return self._call_api([
            {"role": "system", "content": SYSTEM_PROMPT_PAPER},
            {"role": "user",   "content": prompt},
        ], temperature=0.6)
