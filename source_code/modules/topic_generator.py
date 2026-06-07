# =============================================================
# topic_generator.py — 科研选题生成器模块
# 功能：根据学生兴趣自动生成研究课题、方案及论文框架
# =============================================================

import json
import logging
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from config import (
    DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DEEPSEEK_MODEL,
    DEEPSEEK_MAX_TOKENS, SYSTEM_PROMPT_TOPIC, RESEARCH_DIRECTIONS,
)

logger = logging.getLogger(__name__)


class TopicGenerator:
    """科研选题智能生成器"""

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

    # ─────────────────────────────────────────────────────────
    # 选题推荐
    # ─────────────────────────────────────────────────────────

    def generate_topics(self,
                        interest_area: str,
                        academic_level: str = "本科生",
                        num_topics: int = 3,
                        custom_requirements: str = "") -> dict:
        """
        生成科研选题推荐

        Args:
            interest_area: 研究兴趣方向
            academic_level: 学术层次（本科生/硕士生/博士生）
            num_topics: 生成选题数量
            custom_requirements: 自定义要求

        Returns:
            包含选题列表的字典
        """
        prompt = self._build_topic_prompt(
            interest_area, academic_level, num_topics, custom_requirements
        )

        try:
            client = self._get_client()
            if client is None:
                return self._offline_topics(interest_area, num_topics)

            response = client.chat.completions.create(
                model=DEEPSEEK_MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT_TOPIC},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=DEEPSEEK_MAX_TOKENS,
                temperature=0.8,
                response_format={"type": "json_object"},
            )
            result_text = response.choices[0].message.content
            result = json.loads(result_text)
            return result

        except json.JSONDecodeError:
            # 如果JSON解析失败，返回原始文本
            return {"raw_text": result_text, "topics": []}
        except Exception as e:
            logger.error(f"选题生成失败：{e}")
            return self._offline_topics(interest_area, num_topics)

    def _build_topic_prompt(self, interest_area: str, academic_level: str,
                             num_topics: int, custom_requirements: str) -> str:
        req_part = f"\n额外要求：{custom_requirements}" if custom_requirements else ""
        return f"""请为一名{academic_level}生成{num_topics}个眼底图像AI方向的科研选题。

研究兴趣方向：{interest_area}
学术层次：{academic_level}{req_part}

请以JSON格式返回，结构如下：
{{
  "topics": [
    {{
      "title": "选题标题",
      "background": "研究背景（150字以内）",
      "objective": "研究目标（100字以内）",
      "methods": ["方法1", "方法2", "方法3"],
      "innovation": "创新点（100字以内）",
      "difficulty": "难度等级（初级/中级/高级）",
      "expected_outcome": "预期成果",
      "references_direction": ["参考文献方向1", "参考文献方向2"]
    }}
  ]
}}"""

    def _offline_topics(self, interest_area: str, num_topics: int) -> dict:
        """离线模式：返回预设选题模板"""
        templates = [
            {
                "title": f"基于深度学习的{interest_area}自动检测研究",
                "background": f"随着深度学习技术的快速发展，{interest_area}的自动化检测成为研究热点。现有方法在准确性和泛化能力方面仍有提升空间。",
                "objective": f"构建高效的{interest_area}自动检测模型，实现准确分级诊断。",
                "methods": ["U-Net血管分割", "ResNet特征提取", "多尺度注意力机制", "迁移学习"],
                "innovation": "引入多尺度注意力机制，提升模型对细小血管的检测能力。",
                "difficulty": "中级",
                "expected_outcome": "在公开数据集上AUC > 0.95",
                "references_direction": ["Nature Medicine AI诊断系列", "IEEE TMI血管分割综述"],
            },
            {
                "title": f"视网膜血管拓扑特征在{interest_area}预测中的应用",
                "background": "血管拓扑特征能定量描述视网膜血管网络的结构特性，与多种全身疾病密切相关。",
                "objective": "提取并分析血管拓扑特征，建立疾病预测模型。",
                "methods": ["图像预处理", "骨架提取", "NetworkX拓扑分析", "机器学习分类"],
                "innovation": "系统性整合六维拓扑特征，构建新型疾病预测指标体系。",
                "difficulty": "初级",
                "expected_outcome": "预测准确率 > 80%，发表学术论文1篇",
                "references_direction": ["血管分形维数研究", "视网膜拓扑与高血压关联研究"],
            },
            {
                "title": f"多模态眼底图像融合分析用于{interest_area}诊断",
                "background": "单模态眼底图像信息有限，多模态融合可提供更全面的诊断依据。",
                "objective": "融合彩色眼底照、OCT等多模态信息，提升诊断准确性。",
                "methods": ["多模态特征融合", "注意力机制", "跨模态学习", "模型可解释性分析"],
                "innovation": "首次在该疾病中探索多模态融合诊断方法。",
                "difficulty": "高级",
                "expected_outcome": "SCI论文1篇，参加学术会议",
                "references_direction": ["多模态医学影像综述", "眼底OCT融合研究"],
            },
        ]
        return {"topics": templates[:num_topics]}

    # ─────────────────────────────────────────────────────────
    # 研究方案扩展
    # ─────────────────────────────────────────────────────────

    def expand_research_plan(self, topic_title: str, topic_info: dict) -> str:
        """
        将选题扩展为完整研究方案

        Returns:
            研究方案文本（Markdown格式）
        """
        prompt = f"""请基于以下选题，生成完整的研究方案（Markdown格式，约800-1000字）：

选题：{topic_title}
研究背景：{topic_info.get('background', '')}
研究目标：{topic_info.get('objective', '')}
拟用方法：{', '.join(topic_info.get('methods', []))}
创新点：{topic_info.get('innovation', '')}

研究方案应包含：
1. 研究背景与意义（含国内外研究现状）
2. 研究目标与科学假设
3. 技术路线图
4. 主要研究内容
5. 可行性分析
6. 时间安排（按季度）
7. 预期成果
8. 参考文献方向"""

        try:
            client = self._get_client()
            if client is None:
                return f"# {topic_title}\n\n请配置DeepSeek API以获取完整研究方案。"

            response = client.chat.completions.create(
                model=DEEPSEEK_MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT_TOPIC},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=DEEPSEEK_MAX_TOKENS,
                temperature=0.7,
            )
            return response.choices[0].message.content

        except Exception as e:
            logger.error(f"研究方案生成失败：{e}")
            return f"# {topic_title}\n\n研究方案生成失败，错误：{str(e)}"

    # ─────────────────────────────────────────────────────────
    # 实验报告生成
    # ─────────────────────────────────────────────────────────

    def generate_experiment_report(self,
                                    image_analysis: dict,
                                    topology_features: dict,
                                    topic: str = "") -> str:
        """
        根据分析结果自动生成实验报告

        Args:
            image_analysis: 图像分析结果
            topology_features: 拓扑特征
            topic: 研究主题

        Returns:
            Markdown格式实验报告
        """
        lesion_info = image_analysis.get("lesion_info", {})
        topic_str = topic or "眼底图像血管特征分析"

        prompt = f"""请根据以下眼底图像分析数据，生成一份规范的实验报告（Markdown格式）：

**研究主题**：{topic_str}

**图像分析结果**：
- 图像质量：{lesion_info.get('overall_quality', '未知')}
- DR分级：{lesion_info.get('dr_grade', '未知')}（置信度：{lesion_info.get('dr_confidence', 0):.0%}）
- 出血风险评分：{lesion_info.get('hemorrhage_risk', 0):.3f}
- 硬性渗出风险评分：{lesion_info.get('hard_exudate_risk', 0):.3f}

**血管拓扑特征**：
- 血管密度：{topology_features.get('vessel_density', 0):.4f}
- 分叉点数量：{topology_features.get('bifurcation_count', 0)}
- 终末点数量：{topology_features.get('endpoint_count', 0)}
- 平均血管宽度：{topology_features.get('avg_vessel_width', 0):.2f} 像素
- 血管迂曲度：{topology_features.get('tortuosity', 0):.3f}
- 分形维数：{topology_features.get('fractal_dimension', 0):.3f}

报告应包含：
1. 摘要
2. 实验目的
3. 材料与方法
4. 实验结果（含数据解读）
5. 讨论（结合临床意义）
6. 结论
7. 参考文献（列举3-5篇相关文献）"""

        try:
            client = self._get_client()
            if client is None:
                return self._offline_report(topic_str, lesion_info, topology_features)

            response = client.chat.completions.create(
                model=DEEPSEEK_MODEL,
                messages=[
                    {"role": "system", "content": "你是一位医学实验报告撰写专家。"},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=DEEPSEEK_MAX_TOKENS,
                temperature=0.6,
            )
            return response.choices[0].message.content

        except Exception as e:
            logger.error(f"实验报告生成失败：{e}")
            return self._offline_report(topic_str, lesion_info, topology_features)

    def _offline_report(self, topic: str, lesion_info: dict,
                         features: dict) -> str:
        """离线模式实验报告"""
        return f"""# 实验报告：{topic}

## 摘要
本次实验对眼底图像进行了血管分割和拓扑特征分析，采用基于深度学习的U-Net模型完成血管自动分割，并提取了六项拓扑特征。

## 实验目的
通过眼底图像自动分析，学习视网膜血管结构特征及其临床意义。

## 材料与方法
- 分析工具：FundusAI-Edu平台
- 血管分割：U-Net深度学习模型
- 特征提取：骨架化算法 + NetworkX拓扑分析

## 实验结果

### 图像质量评估
- 图像质量：{lesion_info.get('overall_quality', '未评估')}
- DR分级：{lesion_info.get('dr_grade', '未评估')}

### 血管拓扑特征
| 特征 | 数值 |
|------|------|
| 血管密度 | {features.get('vessel_density', 0):.4f} |
| 分叉点数量 | {features.get('bifurcation_count', 0)} |
| 终末点数量 | {features.get('endpoint_count', 0)} |
| 平均血管宽度 | {features.get('avg_vessel_width', 0):.2f} px |
| 血管迂曲度 | {features.get('tortuosity', 0):.3f} |
| 分形维数 | {features.get('fractal_dimension', 0):.3f} |

## 讨论
血管拓扑特征能够定量描述视网膜微血管的结构特性，与全身性疾病（如高血压、糖尿病）密切相关。

## 结论
本实验成功完成眼底图像自动分析，提取了六项拓扑特征，为进一步科研分析奠定了基础。

## 参考文献
1. Ronneberger O, et al. U-Net: Convolutional Networks for Biomedical Image Segmentation. MICCAI 2015.
2. Staal J, et al. Ridge-based vessel segmentation in color images of the retina. IEEE TMI 2004.
3. Fraz MM, et al. Blood vessel segmentation methodologies in retinal images. CMPB 2012.
"""

    @staticmethod
    def get_research_directions() -> list:
        """获取预设研究方向列表"""
        return RESEARCH_DIRECTIONS
