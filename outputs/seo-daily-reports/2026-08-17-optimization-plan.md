# SEO 转化率优化计划

> 生成日期：2026-08-17
> 数据来源：Google Search Console (2026-08-01 ~ 2026-08-15)
> 当前状态：展示 21,330 / 点击 275 / CTR 1.3% / 平均排名 17.2

---

## 背景数据

- 展示量 30 天增长 10x（200/天 → 2,200/天），说明 Google 在大量展示页面
- 点击增长滞后（5/天 → 30/天），CTR 偏低
- 根因：大部分页面排在第 2 页（排名 10-22），用户看不到

---

## P0：优化高展现低点击页面的 Title/Description（30 分钟）

这些页面已有排名，只需改搜索展示文案就能提升 CTR。

### 修改方式

**模型/API 详情页的 title 和 description** 由后端数据库中的 `display_name` 和 `description` 字段决定。

生成逻辑在 `sandbase-fe/src/features/model-catalog/seo.ts` 的 `buildModelMetadata()` 函数：

```typescript
// 当前逻辑：
const title = `${model.display_name} by ${model.vendor}`
const description = model.description
  ? model.description.slice(0, 160)
  : `${model.display_name} - ${model.type.toUpperCase()} model by ${model.vendor}...`
```

**优化方案 A（推荐，改数据库）：** 在后台管理系统中修改模型的 `display_name` 和 `description` 字段，使其更适合搜索展示。

**优化方案 B（改代码，全局生效）：** 修改 `buildModelMetadata()` 函数的 title 模板，例如：

```typescript
// sandbase-fe/src/features/model-catalog/seo.ts 第 19 行附近
// 修改前：
const title = `${model.display_name} by ${model.vendor}`

// 修改后（加入 "Free API" 和 "SandBase" 品牌词）：
const title = `${model.display_name} — Free API | SandBase`
```

**博客文章的 title 和 description** 在 markdown frontmatter 中直接修改：

```yaml
# 文件：sandbase-blog/src/content/en/xxx.md
---
title: "新标题写在这里"
description: "新描述写在这里，控制在 150 字符内"
---
```

---

### 1. `/model/instagram/v1/media-id-to-shortcode`

- 当前数据：410 展示, 1.0% CTR, 排名 7.8
- **当前 Title**：`Instagram V1 Media Id To Shortcode by Instagram`（自动生成，缺乏吸引力）
- **建议 Title**：`Instagram Media ID to Shortcode Converter — Free Online API | SandBase`
- **建议 Description**：`Convert Instagram media IDs to shortcodes instantly. Free API, no rate limits. One request, structured response. Try it now.`
- **修改方式**：后台修改该模型的 `display_name` 为 `Instagram Media ID to Shortcode Converter`，或用方案 B 改代码模板
- [ ] 已完成

### 2. `/blog/glm-5-3-release-watch-2026`（博客文章）

- 当前数据：286 展示, 0.7% CTR, 排名 7.4
- **当前 Title**：`GLM-5.3 Launches: Frontier Coding and Emergent Cybersecurity`
- **建议 Title**：`GLM 5.3 Release Date: Everything We Know (Updated Aug 2026)`
- **建议 Description**：`When will GLM 5.3 launch? Latest leaks, benchmark predictions, and timeline analysis. Updated weekly.`
- **修改方式**：编辑 `sandbase-blog/src/content/en/glm-5-3-release-watch-2026.md` 的 frontmatter：
  ```yaml
  title: "GLM 5.3 Release Date: Everything We Know (Updated Aug 2026)"
  description: "When will GLM 5.3 launch? Latest leaks, benchmark predictions, and timeline analysis. Updated weekly."
  ```
  同步修改中文版 `sandbase-blog/src/content/zh-CN/glm-5-3-release-watch-2026.md`
- [ ] 已完成

### 3. `/model/instagram/v1/shortcode-to-media-id`

- 当前数据：216 展示, 2.3% CTR, 排名 9.1
- **建议 Title**：`Instagram Shortcode to Media ID — Free Converter API | SandBase`
- **建议 Description**：`Convert any Instagram shortcode to its numeric media ID. Free REST API with instant response. No authentication required.`
- **修改方式**：同 #1，后台修改 `display_name`
- [ ] 已完成

### 4. `/model/douyin/web/all-sec-user-id`

- 当前数据：104 展示, 1.9% CTR, 排名 6.5
- **建议 Title**：`Douyin Sec User ID Lookup — Batch Resolve API | SandBase`
- **建议 Description**：`Resolve Douyin sec_user_id from share URLs or usernames in batch. Structured JSON response, ready for agent workflows.`
- **修改方式**：后台修改 `display_name`
- [ ] 已完成

### 5. `/model/instagram/v3/user-id-to-username`

- 当前数据：119 展示, 1.7% CTR, 排名 41.7
- 排名太靠后，暂不优先做 title 优化，先通过内链提升排名
- [ ] 跳过 / 已完成

### 6. 全局 Title 模板优化（方案 B，可选）

如果不想逐个改数据库，可以修改代码模板让所有模型页的 title 都更适合搜索：

**文件：** `sandbase-monorepo/sandbase-fe/src/features/model-catalog/seo.ts`

```typescript
// 修改前（第 19 行）：
const title = `${model.display_name} by ${model.vendor}`

// 修改后：
const title = `${model.display_name} — Free API | SandBase`
```

**注意：** 改模板会影响所有 5000+ 模型页的 title，部署前确认效果。

---

---

## P1：内链加强，推 Top 10 页面进 Top 5（2 小时）

排名 5-10 的页面进 top 5 后 CTR 会从 1-2% 跳到 5-15%。

### 修改方式

**博客文章加内链：** 在相关文章的正文或底部 "Related" 区块加入链接。

示例 — 在 `sandbase-blog/src/content/en/instagram-user-id-api-tutorial-2026.md` 正文中加入：
```markdown
To convert between media IDs and shortcodes, see our
[Media ID to Shortcode API](/model/instagram/v1/media-id-to-shortcode).
```

**模型页互链（需研发支持）：** 在模型详情页底部加一个 "Related APIs" 组件。

文件：`sandbase-fe/src/features/model-catalog/components/RelatedModels.tsx`（已存在）

如果需要跨 vendor 推荐，可在 `LLMDetailView.tsx` 底部加一段硬编码的快速链接，或者让后端返回 `related_models` 字段。

### 操作清单

- [ ] 在博客 `instagram-user-id-api-tutorial-2026` 文章正文中加内链到：
  - `/model/instagram/v1/media-id-to-shortcode`
  - `/model/instagram/v1/shortcode-to-media-id`
  - `/model/instagram/v3/user-id-to-username`
- [ ] 在博客 `best-open-source-ai-agent-frameworks-2026` 底部加内链到 `/agents`
- [ ] 在博客 `deepseek-harness-vs-openclaw-vs-hermes-2026` 加内链到：
  - `/model/deepseek/deepseek-v4-pro`
  - `/model/deepseek/deepseek-v4-flash`
- [ ] 在博客 `glm-5-3-release-watch-2026` 加内链到：
  - `/vendor/z-ai`
  - `/model/z-ai/glm-5.2`
- [ ] 首页 FAQ 区块或 footer "Learn" 栏考虑加一个 "Popular APIs" 链接（指向 `/apis`）
- [ ] （研发）模型详情页底部评估加 "Same Vendor" 推荐区块

---

## P2：为高展现 API 写教程博客（1 天）

围绕已有搜索需求写长尾内容，形成 topic cluster。

### 待写文章

- [ ] `instagram-media-id-shortcode-api-guide-2026` — "How to Convert Instagram Media ID to Shortcode in Python (2026)"
  - 内链目标：`/model/instagram/v1/media-id-to-shortcode`、`/model/instagram/v1/shortcode-to-media-id`
- [ ] `douyin-sec-user-id-batch-lookup-2026` — "Douyin Sec User ID: What It Is and How to Resolve It via API"
  - 内链目标：`/model/douyin/web/all-sec-user-id`、`/model/douyin/web/sec-user-id`
- [ ] `instagram-api-tools-compared-2026` — "Instagram API Tools Comparison: SandBase vs RapidAPI vs Direct"
  - 内链目标：所有 Instagram 相关模型页

---

## P3：模型页加 FAQ + Schema 增强（半天）

### 修改方式

**方案 A（快速，改模板）：** 在模型详情页组件中，根据模型类型自动生成 FAQ 区块。

文件：`sandbase-fe/src/features/model-catalog/components/LLMDetailView.tsx`

在页面底部渲染前，加入 FAQ section：

```tsx
{/* FAQ for SEO - 加在页面底部 return 之前 */}
<section className="mt-12 border-t pt-8">
  <h2 className="text-lg font-semibold mb-4">FAQ</h2>
  <details className="mb-3">
    <summary className="cursor-pointer font-medium">
      What is {model.display_name}?
    </summary>
    <p className="mt-2 text-sm text-muted-foreground">
      {model.description?.slice(0, 200)}
    </p>
  </details>
  <details className="mb-3">
    <summary className="cursor-pointer font-medium">
      How much does {model.display_name} cost?
    </summary>
    <p className="mt-2 text-sm text-muted-foreground">
      Input: ${model.model_card?.prompt_token_price}/M tokens,
      Output: ${model.model_card?.completion_token_price}/M tokens.
      See full pricing on this page.
    </p>
  </details>
  <details className="mb-3">
    <summary className="cursor-pointer font-medium">
      How do I call {model.display_name} via API?
    </summary>
    <p className="mt-2 text-sm text-muted-foreground">
      Use the SandBase unified API with your API key. See the Docs tab for request/response examples.
    </p>
  </details>
</section>
```

**方案 B（Schema 增强）：** 在 `sandbase-fe/src/features/model-catalog/json-ld.ts` 中的 `serializeJsonLd()` 增加 FAQPage schema：

```typescript
// 在现有 JSON-LD 的 @graph 数组中追加：
{
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": `What is ${model.display_name}?`,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": model.description?.slice(0, 200) || ""
      }
    },
    {
      "@type": "Question",
      "name": `How much does ${model.display_name} cost?`,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": `Input: $${model.model_card?.prompt_token_price}/M tokens, Output: $${model.model_card?.completion_token_price}/M tokens.`
      }
    }
  ]
}
```

**方案 C（SoftwareApplication schema，针对免费 API 工具页）：**

在 `json-ld.ts` 中，对 type 为 `connector` 或非 LLM 类型的模型加入：

```typescript
{
  "@type": "SoftwareApplication",
  "name": model.display_name,
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Web",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  }
}
```

这可能在搜索结果中触发 "Free" 价格标注，提升 CTR。

### 操作清单

- [ ] Instagram 相关模型页加 FAQ（优先 media-id-to-shortcode、shortcode-to-media-id）
- [ ] Douyin 相关模型页加 FAQ（优先 all-sec-user-id、user-search）
- [ ] 评估是否全局为 model 详情页模板加 FAQ 组件
- [ ] 评估 SoftwareApplication schema 对 API 工具页的效果

---

## P4：乘胜追击 DeepSeek Harness 系列（2-3 天）

"deepseek harness vs hermes" 已获得 17.6% CTR + 排名 2.9，是已验证的高价值主题。

### 待写文章

- [ ] `deepseek-harness-quickstart-tutorial-2026` — "DeepSeek Harness Tutorial: Build Your First Agent in 10 Minutes"
- [ ] `deepseek-harness-vs-langchain-crewai-2026` — "DeepSeek Harness vs LangChain vs CrewAI: Which Agent Framework?"
- [ ] `deepseek-harness-architecture-internals-2026` — "DeepSeek Harness Architecture: How the Agent Loop Works"

每篇互相内链 + 链回已有的 `deepseek-harness-vs-openclaw-vs-hermes-2026`。

---

## P5：技术优化（按开发排期）

| 项目 | 说明 | 优先级 |
|------|------|--------|
| 模型页 SSR | `/models` 列表页是 CSR，初始 HTML 只有 "Loading..."。改 SSR 可加速收录 | 中 |
| PageSpeed | 用 PageSpeed Insights 测 `/models` 和模型详情页，优化 LCP | 中 |
| 模型页互链 | 详情页底部加 "Similar Models"、"Same Vendor" 推荐 | 低 |
| OG Image | 制作 1200x630 品牌 OG 图，放 `sandbase-fe/public/og-image.png` | 低 |

---

## 验收标准

完成上述优化后，预期 2-4 周内观察到：

- [ ] 整体 CTR 从 1.3% 提升到 2.5%+
- [ ] Top 3 高展现页面 CTR 各提升 3-5 个百分点
- [ ] 排名 5-10 的页面中至少 3 个进入 Top 5
- [ ] DeepSeek Harness 系列关键词占据 Top 3

---

## 参考

- SEO 巡检 playbook：`sandbase-daily-ops/playbooks/seo-geo-daily.md`
- 每日自动报告：`sandbase-daily-ops/outputs/seo-daily-reports/`
- Google 服务账号（GSC API）：`/root/.config/sandbase/google-service-account.json`
