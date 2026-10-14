# 正文核读引起的主张修订｜2026-10-14

本文件不是一般局限清单，而是记录本研究室哪些初步判断被原材料具体改变。初稿仍可从 Git 历史追溯；相关入口卡已修订。

| 初版表达或风险 | 本轮原文定位 | 当前修订 | 对后续问题的影响 |
|---|---|---|---|
| CDFP-Net 的方向互换只是建议补做的对照 | [PDF p.8 Table 4(a)](https://papers.miccai.org/miccai-2026/paper/2844_paper.pdf#page=8) | 作者已比较两个查询方向；不再把该对照作为缺失证据或新的贡献 | 研究病例级条件效应、可预测性与预算净收益 |
| MMA-LTS 数量/身份对照尚停留在我们提出的实验 | [PDF p.8 Fig.3](https://papers.miccai.org/miccai-2026/paper/1236_paper.pdf#page=8) | 已有 Count Learnable Token 消融 | 进一步考察区域、统计口径、外部条件和应用终点 |
| Locor 可概括为从全局依赖首次转向局部依赖 | [PDF 引言及 p.4](https://papers.miccai.org/miccai-2025/paper/1747_paper.pdf#page=2) | 局部依赖有前作，具体推进在表示、拟合及计算；可迁移动作不等于历史首创 | 将建模尺度、函数自由度和计算实现分别归因 |
| 概率起点可被读成最终严格联合似然 | [Locor PDF p.4](https://papers.miccai.org/miccai-2025/paper/1747_paper.pdf#page=4) | 作者明确限定汇总目标的概率语义 | 区分设计动机、代理目标和严格概率保证 |
| CAMOS 的流程逆转容易被整体归于本文 | [PDF p.2](https://papers.miccai.org/miccai-2025/paper/1908_paper.pdf#page=2) | 引言已有软组织驱动前作；本文推进具体的条件 3D 预测 | 分开历史归属、论文贡献、本库迁移操作 |
| 目标外观预测与最优/可执行规划仍容易混同 | [CAMOS PDF pp.6–8](https://papers.miccai.org/miccai-2025/paper/1908_paper.pdf#page=6) | 区分术后参照相似性、目标价值与骨移动可行性 | 新实验应先明确要跨越哪一级任务边界 |

## 本轮新增的版本与推理约束

DomainBed 样本实际读取的是 arXiv 2020 v1，不以之后 ICLR 2021 的版本标签替换其设置和结果。Diffusion Policy 使用 RSS 2023 作者公开 PDF，不拼接后续期刊版作者或任务数。Risks of IRM 只核读主文定义、定理及证明思路，没有完整审计附录证明。

正温度保留类别排序、解释图通过必要检查、训练环境上满足不变约束，都不能不经新增证据直接升级为下游决策获益、解释完全忠实或普遍因果恢复。这些是本库的推理边界说明，不是声称相关论文作出了上述越界结论。

## 待 Q/HQ 抽样复核

优先复核 CDFP-Net p.8、MMA-LTS pp.5–8、Locor p.4 与 pp.6–8、CAMOS pp.2/6–8；随后复核新样本的版本、短摘和定理条件。提出实验的条目统一标为未执行，不根据文字完整度提升证据等级。
