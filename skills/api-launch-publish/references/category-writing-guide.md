# 分类写作指南 / Category Writing Guide

> 权威来源。每个 category 的文章结构和写作侧重以本文件为准。

---

## model-introduction（模型介绍）

- **核心**: 一个模型的深度介绍
- **必须包含**: 规格表、价格对比、代码示例、benchmark
- **标题模式**: "Introducing {Model} on SandBase: ..."

---

## model-comparison（模型对比）

- **核心**: 2-4 个模型的横向对比
- **必须包含**: 对比表格（至少 5 个维度）、场景推荐、代码示例
- **标题模式**: "{Model A} vs {Model B}: Which is Better for {Use Case}?"

---

## best-of（最佳推荐）

- **核心**: 某个场景下的 Top N 推荐
- **必须包含**: 排名表格、每个推荐的理由、价格对比
- **标题模式**: "Best {N} {Category} in 2026"

---

## agent-best-picks（Agent 最佳选择）

- **核心**: 特定 Agent 场景下的模型推荐
- **必须包含**: 场景描述、模型对比、成本分析、代码示例
- **标题模式**: "Best Models for {Agent Scenario} on SandBase"

---

## agent-use-cases（Agent 场景介绍）

- **核心**: Agent 架构和工作流介绍
- **必须包含**: 架构图（用 Mermaid）、代码示例、模型推荐
- **标题模式**: "Building {Agent Type} with SandBase: A Complete Guide"

---

## agent-daily-news（Agent 生态新闻）

- **核心**: AI/LLM Agent 生态动态分析
- **必须包含**: 事件摘要、架构影响分析、SandBase 生态相关性
- **写作侧重**: 从 agent 构建者角度分析，不是泛新闻转述

---

## tutorials（教程）

- **核心**: 手把手教程
- **必须包含**: 完整代码、步骤编号、预期输出
- **标题模式**: "How to {Action} with SandBase API"

---

## product-updates（产品更新）

- **核心**: SandBase 平台更新公告
- **必须包含**: 新功能列表、使用方法、迁移指南（如需）
- **标题模式**: "SandBase Update: {Feature} Now Available"

---

## industry-insights（行业洞察）

- **核心**: AI/LLM 行业趋势深度分析
- **必须包含**: 数据支撑的趋势观点、对开发者的实际影响、行动建议
- **标题模式**: "{Trend}: What It Means for Developers"

---

## pricing-guides（价格指南）

- **核心**: 成本优化和价格分析
- **必须包含**: 价格对比表、成本计算示例、省钱技巧
- **标题模式**: "LLM API Pricing Guide: How to Save {X}% with SandBase"

---

## developer-tools（开发者工具）

- **核心**: 工具和框架集成指南
- **必须包含**: 安装步骤、配置代码、集成示例
- **标题模式**: "Using {Tool} with SandBase: Integration Guide"

---

## 通用文章结构（所有分类适用）

```markdown
# 标题（包含主关键词，60字符以内）

> **TL;DR** — 3-4 个要点的 blockquote 摘要

## 引言段落（100字以内，包含主关键词，用 hook 开头）

## 核心内容 H2（至少 5 个 H2 段落）

### 每个 H2 下可以有 H3 子段落

## 实战代码示例

## 对比表格（至少一个）

## FAQ（3-5 个问题）

## Key Takeaways
```

### 字数要求

- **最低**: 1500 词（英文）/ 2000 字（中文）
- **理想**: 1800-2500 词
- **上限**: 3500 词（超过则考虑拆分为系列文章）

---

## 选题去重工作流（每次写文章前必做）

> **铁律：写任何新文章前，先读 `sandbase-blog/content-index.md`，避免与历史文章重复。**

**选题流程：**

1. 选定候选 topic 后，**先打开 `content-index.md`** 扫一遍已有标题和 slug
2. 如果候选 topic 与已有文章主题重复或高度相似，**换一个角度或换一个 topic**
3. 相近主题可以写，但**必须有新角度/新数据/新结论**，并在文中内链到已有的相关文章

**写完后必做：**
- 把新文章追加到 `content-index.md`
- 格式见文件表头：`| date | title | slug | type | category | tags | description | locale | words | cover |`

---

## 数据来源优先级

1. **SandBase 本地 Registry** — 最权威，优先使用
2. **OpenRouter API** — 实时数据，用于补充
3. **HuggingFace** — 模型信息和社区数据
4. **LMSYS Arena** — 排名和 ELO 评分
5. **Artificial Analysis** — 性能基准测试
6. **Open LLM Leaderboard** — 开源模型评测
7. **HackerNews / arXiv** — 新闻和论文

### 数据规则

- **真实性第一**：只写你有来源支撑的内容，宁可少写也不编造
- 价格数据标注日期：`According to SandBase pricing as of {date}...`
- Benchmark 数据标注来源：`根据 LMSYS Arena 排名`
- 不要改变数字精度（$3.00/M tokens 就是 $3.00，不是 "about $3"）
- **禁止编造 URL**

### 价格展示格式

```markdown
| 模型 | 输入价格 ($/M tokens) | 输出价格 ($/M tokens) | Context Window |
|------|----------------------|----------------------|----------------|
| qwen3-32b | $0.00 | $0.00 | 131,072 |
| gpt-4o | $2.50 | $10.00 | 128,000 |
```
