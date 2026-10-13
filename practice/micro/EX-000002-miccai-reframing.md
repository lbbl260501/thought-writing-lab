# EX-000002 — From Contrast to Scientific Reframing

- 来源：MICCAI 2025–2026 的原创分析与自行编写的英文练习句，**不是逐字复制论文**。
- 相关文献：[PAPER-000003 Locor](../../corpora/miccai/pilot/PAPER-000003-Locor.md)、[PAPER-000004 MMA-LTS](../../corpora/miccai/pilot/PAPER-000004-MMA-LTS.md)
- 目标：`RECOGNIZE_CAPABILITY`、`QUESTION_ASSUMPTION`、`REFRAME_PROBLEM`
- 时长建议：25–35 分钟；内容适合学术英语/英语考试论证技能之间的迁移。

## A. 句法与命题结构

分析下面这句自行编写的英文示例：

> Although additional imaging sequences may improve overall segmentation performance, their contribution to prediction reliability can differ across anatomical regions.

指出：主句主体、动作与客体；让步从句承担何种叙事功能？哪些词限定了论断的确定程度？

改写任务：用 `whereas` 重写，并说明它与 `although` 的信息重心有何差异。

## B. 从问题分类到科学疑问

材料：一组 MRI 模态存在不同缺失组合。传统报告方式只比较“缺失 1 种 / 2 种”。你怀疑不同模态的贡献并不完全等价。

用英文写出三句：
1. 承认已有“缺失模态”模型能处理的问题；
2. 指出 **which modalities** 与 **how many modalities** 的区别；
3. 提出可以通过实验区分两种解释的科学问题。

不得把尚未验证的假设写成普遍事实。

## C. 一段更紧凑的科学叙事

写 100–130 词，将“输入信息变化”逐渐转入“局部校准”的研究问题。要求：
- 不以抽象模板句 `However, existing methods have limitations.` 结束；
- 至少有一个句子以清楚的科学主体和动词承担实质内容；
- 全段只提出一个核心研究问题；
- 最后一句能够自然接入实验设计。

## 参考答案与解释（A）

主句：`their contribution` → `can differ` → `across anatomical regions`，表达对象间可能存在局部差异。让步从句承认增加序列可能改善整体分割表现，但不等价于局部可靠性一致提升。

改写示例：

> Additional imaging sequences may improve overall segmentation performance, whereas their effects on prediction reliability can vary across anatomical regions.

`although` 更显式地设置“承认已有优势，然后突出主张”的层级；`whereas` 则更侧重对比两个并列判断。二者并非完全可互换，作者需选择符合论证目的的关系。

## B 的示例思路（非唯一答案）

An incomplete set of MRI sequences can still support tumor segmentation. Yet two subsets containing the same number of sequences may not provide equivalent evidence for each tumor region. This raises the question of whether calibration errors are driven primarily by the number of available modalities or by their identities and spatial contributions.

## 评价维度
科学语义准确性；语法与词语精度；主从句信息关系；问题可检验性；结论强度。
