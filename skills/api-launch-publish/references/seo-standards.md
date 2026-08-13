# SEO 规范 / SEO Standards

> 权威来源。所有博客 SEO 规则以本文件为准。

---

## 1. 标题长度

- **英文标题控制在 60 字符以内**（Google SERP 约 60 字符截断）
- **中文标题控制在 30 个汉字以内**
- 不要用超长副标题。"主标题 — 副标题" 结构里副标题经常被 SERP 截断浪费掉
- 对比类标题用 "vs"（如 "Vector vs Graph vs Episodic"），匹配用户实际搜索词
- 年份放标题里（如 "(2026)"），提升时效性点击率

---

## 2. 关键词策略

- 每篇文章 1 个主关键词 + 2-3 个长尾关键词
- 主关键词出现在：标题、第一段、第一个 H2、meta description
- **第一段前 100 词内必须出现一次精确匹配的主关键词**
  - 开头可以用故事/场景钩子，但第二句就要自然嵌入完整关键词词组
  - 例：开头讲痛点场景，第二句 "Choosing an agent memory architecture is..." 嵌入精确关键词
- 自然分布，不堆砌

---

## 3. 内链策略（每篇必查）

每篇文章至少包含：

- 2-3 个指向权威外部来源的链接（官方文档、GitHub 仓库、研究论文）
- **1-2 个指向其他博客文章的相对链接**（构建 topic cluster，提升站内权重传递）
  - 链接格式：英文 `/{slug}/`，中文 `/zh-CN/{slug}/`（不带 /blog/ 前缀，博客域名是 blog.sandbase.ai）
  - 在提到相关主题/框架/产品时自然插入，不要硬塞
  - 写新文章前先想：站内有没有相关文章可以互链？
- 不要链接到 sandbase.ai（当前阶段不做产品推广）

---

## 4. Meta Description

- 120-160 字符，包含主关键词和 CTA
- **避免在 description 里用 em-dash（—）和特殊 Unicode 符号**：YAML 序列化和 SERP 渲染可能出现编码问题
- 用双引号包裹整个 description 值，避免 YAML 解析歧义
- 示例：`Qwen3-32B is now free on SandBase. Compare pricing, benchmarks, and see code examples to get started in minutes.`

---

## 5. FAQ（利于 Featured Snippet / People Also Ask）

- 每篇文章底部 3-5 个 FAQ 问题
- 用问句式 H2 或加粗问句（"How does X compare to Y?"）
- 问题用用户真实会搜的口语化表达（"Is Mem0 or Zep better?" 而非 "A comparison of Mem0 and Zep"）
- 答案第一句直接给结论再展开（featured snippet 抓第一句）

---

## 6. Featured Snippet 优化

- TL;DR blockquote 放开头，方便摘要抓取
- 对比内容用表格（容易进 featured snippet）

---

## 7. Frontmatter 注意

- `language` 字段保持纯净的 `en` / `zh-CN`，不要带 `\r` 或多余空白
- frontmatter schema 详见 `blog-format.md`

---

## 8. GEO（Generative Engine Optimization）

- 开头 80-120 词回答 what it is、who it is for、when to use it
- 英文含可引用的 `TL;DR` / `Key takeaway`（3-5 条独立事实性 bullets）
- 中文含 `先说结论`
- Provider、API、SandBase Agent Service 等名称全文一致
- 文章明确指出至少一个局限或 trade-off，不制造"万能赢家"
- 重要声明标注来源和日期
- Article JSON-LD 有效；FAQPage JSON-LD 仅用于真正的 FAQ 内容
