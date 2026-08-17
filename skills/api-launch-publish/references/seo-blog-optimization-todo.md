# 博客 SEO 优化待办（2026-08-17 巡检）

> 写新文章或更新旧文章时，顺手完成以下优化。每完成一个打勾。

---

## 一、现有文章 Title/Description 优化

以下文章排名已进 Top 10 但 CTR 偏低，需要优化标题吸引力。

### 1. `glm-5-3-release-watch-2026`（EN + ZH）

**当前 Title：** `GLM-5.3 Launches: Frontier Coding and Emergent Cybersecurity`
**问题：** 286 展示, 0.7% CTR, 排名 7.4 — 用户搜 "GLM 5.3 release date" 看到这个标题没有点击动力

**修改 EN 文件** `sandbase-blog/src/content/en/glm-5-3-release-watch-2026.md`：
```yaml
title: "GLM 5.3 Release Date: Everything We Know (Updated Aug 2026)"
description: "When will GLM 5.3 launch? Latest leaks, benchmark predictions, and timeline analysis for the next GLM frontier model."
```

**修改 ZH 文件** `sandbase-blog/src/content/zh-CN/glm-5-3-release-watch-2026.md`：
```yaml
title: "GLM 5.3 发布时间：我们所知的一切（2026年8月更新）"
description: "GLM 5.3 何时发布？最新爆料、基准预测和时间线分析。"
```

- [ ] EN 已修改
- [ ] ZH 已修改

---

## 二、现有文章内链补充

写新文章或路过这些旧文章时，加入以下内链。

### 1. `instagram-user-id-api-tutorial-2026`（EN + ZH）

在正文中提到 ID 转换时，加入：
```markdown
For bulk conversions, see the [Media ID to Shortcode API](https://www.sandbase.ai/model/instagram/v1/media-id-to-shortcode) and [Shortcode to Media ID API](https://www.sandbase.ai/model/instagram/v1/shortcode-to-media-id).
```

- [ ] EN 已加
- [ ] ZH 已加

### 2. `deepseek-harness-vs-openclaw-vs-hermes-2026`（EN + ZH）

在文章底部 Related 区块或正文中加入：
```markdown
Try DeepSeek V4 Pro on SandBase: [DeepSeek V4 Pro](/model/deepseek/deepseek-v4-pro) | [DeepSeek V4 Flash](/model/deepseek/deepseek-v4-flash)
```

- [ ] EN 已加
- [ ] ZH 已加

### 3. `glm-5-3-release-watch-2026`（EN + ZH）

加入指向 vendor 页和相关模型的链接：
```markdown
See all GLM models on SandBase: [Z.ai Vendor Page](/vendor/z-ai) | [GLM 5.2](/model/z-ai/glm-5.2)
```

- [ ] EN 已加
- [ ] ZH 已加

### 4. `best-open-source-ai-agent-frameworks-2026`（EN + ZH）

在文章底部加入：
```markdown
Browse ready-made Agents built with these frameworks: [SandBase Agent Store](/agents)
```

- [ ] EN 已加
- [ ] ZH 已加

---

## 三、Dify 文章排名提升

`dify-ai-platform-explained-2026` 有 781 展示但排名 13.4（第 2 页），需要从相关对比文章给它加内链。

### 在 `n8n-vs-dify-2026` 中加入

```markdown
For a full guide to Dify's architecture and self-hosting, see [What Is Dify?](/dify-ai-platform-explained-2026/).
```

### 在 `dify-vs-langgraph-2026` 中加入

```markdown
New to Dify? Start with our [complete Dify platform guide](/dify-ai-platform-explained-2026/).
```

- [ ] n8n-vs-dify EN 已加
- [ ] n8n-vs-dify ZH 已加
- [ ] dify-vs-langgraph EN 已加
- [ ] dify-vs-langgraph ZH 已加

---

## 四、新文章选题（基于 GSC 数据）

以下关键词有展示但缺少专门内容，适合作为近期选题：

| 关键词 | 当前展示 | 当前排名 | 建议文章 |
|--------|---------|---------|----------|
| instagram media id to shortcode | 410 | 7.8 | 教程："How to Convert Instagram Media ID to Shortcode via API" |
| douyin sec user id | 104 | 6.5 | 教程："Douyin Sec User ID: What It Is and How to Resolve" |
| instagram user id to username | 119 | 41.7 | 教程（已有，需优化内容丰富度） |
| glm 5.3 release date | 48 | 7.7 | 已有文章，优化 title（见上方 #1） |
| deepseek harness vs hermes | 17 | 2.9 | 已有文章，继续扩写系列 |

---

## 五、写作时的 SEO Checklist（每篇必查）

写完一篇文章后，对照检查：

- [ ] Title ≤ 60 字符（EN）/ ≤ 30 汉字（ZH），包含主关键词 + 年份
- [ ] Description 120-160 字符，包含主关键词和行动号召
- [ ] 第一段前 100 词内出现精确匹配的主关键词
- [ ] 至少 2 个内链指向其他博客文章
- [ ] 至少 1 个链接指向 SandBase 模型/API 页（如相关）
- [ ] 底部 3-5 个 FAQ（问句式，答案第一句给结论）
- [ ] TL;DR blockquote 在开头
- [ ] 有对比表格（容易进 Featured Snippet）
- [ ] 文章 > 1500 词（EN）/ > 2000 字（ZH）
- [ ] `updatedDate` 已设为今天日期
