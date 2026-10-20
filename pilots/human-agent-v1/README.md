# 人读 / Agent 分离试点 · 可运行整合版

关联任务 #33、PR #31。源码接续2026-10-19交付包，2026-10-20整合。没有自动合并或部署。

## 直接使用

在仓库根目录执行：

```sh
python -m pip install -r pilots/human-agent-v1/requirements.txt
python pilots/human-agent-v1/build.py
python -m unittest discover -s pilots/human-agent-v1 -p 'test_*.py' -v
```

打开 `dist/human/lesson.html` 学习《不再罗列模块，把研究关系写清楚》，或打开 `dist/human/report.html` 阅读《系统收益与机制解释，需要分开回答》。路径相对于本目录。生成的 HTML 自包含，不需要本地服务器，不下载外部脚本。原文入口需联网。

## 三类材料分离

- `records.json`：原有17条公开候选记录，来源、论文结果、分析、语言动作和练习身份分开。不是17项新研究成果。
- `lesson.html.in`、`report.html.in`、`assets/`：给人的讲解、版式和交互。浏览器不加载后台JSON、任务状态或审核日志。
- `build.py`：数据校验、关系引用解析、数值生成、上下文裁剪。输出 `dist/agent/` 和 `dist/editorial/` 不混入人读正文。

A–F的任务方向不变。Q改为两阶段：`Q.json`只提供4项来源和定位，先提交独立事实清单；`Q_compare.json`再提供已有主张、解释和答案用于比较。共7个角色、8份包。两阶段是交接约定，不是运行时权限隔离。所有包保持 `not_launched`，没有独立Agent运行、审稿通过或学习者成绩。

## 版本兼容与边界

旧的 `knowledge-base/schemas/knowledge-record.schema.json` 保持原状。生成器仅引用新的 `knowledge-record.v0.2.schema.json`。新版更严格，面向当前论文结果试点，不兼容所有旧记录；禁止直接重命名后全库替换，也不进行自动迁移。已有各组PR不被重写。

原31项测试保留，新增9项版本、审核材料分阶段、页面标题与非有限数值的回归，合计40项。测试检查工程约束，不证明解释正确、实验已复现或教学有效。

## 并行工程检查

```sh
python -m pip install -r pilots/human-agent-v1/requirements-browser.txt
python -m playwright install chromium
python pilots/human-agent-v1/parallel_check.py
```

此命令实际并发运行回归、构建和浏览器三个子进程；它们不是AI子智能体。输出目录各自独立，不竞争写入。浏览器默认检查真实文件导航、同一浏览器上下文内刷新后的草稿保存、实际下载内容，以及桌面和手机版式。

本次对话环境的 `file://` 导航被管理员策略阻止，因此本地使用显式 `--render-only` 复核渲染和交互；不会把它登记成导航、持久化或下载通过。GitHub工作流在独立runner中使用完整模式，不自动降级。跨会话持久化、线上部署、真实学习者效果仍不在验证范围内。

`.github/workflows/human-agent-pilot.yml` 配置Python 3.10/3.12回归和浏览器任务并行运行；只声明 `contents: read`，只上传构建产物、不部署网站、不访问模型API或私人记录。配置存在不等于Actions已经通过，验收以具体head的运行日志为准。

## 来源继承与复核

输入包 `TWL_Human_Agent_Pilot_v01.zip` SHA256：`5180f7dae1b4f3bf360c82adf56ba8d9a835ae842932590894fa27d6eceffc43`。记录身份、创建时间和既有阅读范围保留；本轮未将它们升级为独立审查。

2026-10-20另行访问UNETR++的 arXiv:2212.04497v3，核对§3.2共享关系及Table 2的九项数值。本包不含原论文全文、书籍、字体或学习者作答。其余来源沿用记录中的既有读取范围，不宣称本轮重新通读。

实现依据：JSON Schema官方说明 `format` 默认是注释，本生成器显式使用FormatChecker；条件规则强制相应类型载荷；GitHub Actions官方权限文档支持在工作流明确限制token范围。

- https://json-schema.org/understanding-json-schema/reference/type
- https://json-schema.org/understanding-json-schema/reference/conditionals
- https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax

源码可以重建两个HTML、两个未执行Quarto的qmd和八份Agent包。`dist/`、运行日志、截图与浏览器临时输入不提交到源码树，避免把生成物和个人记录变成新的事实副本。
