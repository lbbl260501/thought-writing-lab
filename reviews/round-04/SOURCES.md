# R04｜来源与实际核读范围

核对日期：2026-10-18。以下六项是本轮采用的来源，不声称都是总库新来源。只有标为引文的短语是原文；实验四格、反例、改写段落与迁移设计均为原创教学内容。完整机读元数据随会话研究包交付。

| 来源 | 固定版本与原文入口 | 实际检查 |
|---|---|---|
| Shaker et al., UNETR++ | [arXiv:2212.04497v3](https://arxiv.org/html/2212.04497v3)；关联TMI 2024 | §1贡献段、§3.2 Q/K/V设置与公式；不是完整实验重审 |
| Isensee et al., nnU-Net Revisited | [MICCAI 2024官方PDF，2847](https://papers.miccai.org/miccai-2024/paper/2847_paper.pdf) | §1、§2.1 P1/P2、§3.1；PDF第3、5页页面核对 |
| Gulrajani & Lopez-Paz, In Search of Lost Domain Generalization | [arXiv:2007.01434v1](https://arxiv.org/pdf/2007.01434v1)，2020-07-02 | §3–3.1，PDF第3–4页；§4.3–5.1相关文字；未将ICLR最终版当成本次原文 |
| Adebayo et al., Sanity Checks for Saliency Maps | [NeurIPS 2018官方PDF](https://papers.neurips.cc/paper/8160-sanity-checks-for-saliency-maps.pdf) | 引言、参数/标签随机化设置、§3.1–3.2及§4；PDF第5页图文核对 |
| Mehta et al., CF-Seg: Counterfactuals meet Segmentation | [MICCAI 2025官方PDF，4597](https://papers.miccai.org/miccai-2025/paper/4597_paper.pdf) | §1–4干预与评价；重点§3.2、§4.2、§4.4；PDF第7页Table 1/Fig 5核对 |
| Gentner, Structure-Mapping: A Theoretical Framework for Analogy | [作者存档，1983](https://groups.psych.northwestern.edu/gentner/papers/Gentner83.2b.pdf) | 印刷页156–161，对应PDF第2–4页双页扫描；已查看原始页面，未依赖错乱文字层复原引文 |

## 应保留的具体区别

UNETR++中共享查询/键投影、独立值投影是设置事实；互补性是另一层机制判断。nnU-Net Revisited的同显存边界不等于所有训练时间、预训练条件完全相同。DomainBed v1中的oracle使用目标域验证信息，不等于直接在最终测试标签上挑选；其表现也不是保证的上界。

Saliency的标签随机化涉及重新训练，不能写成只打乱评估标签。CF-Seg Table 1说明右肺与双肺比较的p值不大于0.05，左肺不是同样结论；不可将所有点估计改善写成所有区域显著。该方法固定分割器，不等于整条流程免训练。Gentner的理论用于构造关系映射，不构成本课程效果的实验证据。

## 未采用的来源与边界

Platt的Strong Inference只取得元数据与检索线索，全文访问未成功，因此没有纳入已核读来源。未以聚合摘要网站替代原文。没有复制论文全文、表格图像、书籍页面或字体；没有实施算法复现、重训、理论独立证明或真实学习者测试。
