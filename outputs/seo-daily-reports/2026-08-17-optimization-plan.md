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

### 1. `/model/instagram/v1/media-id-to-shortcode`

- 当前数据：410 展示, 1.0% CTR, 排名 7.8
- 建议 Title：`Instagram Media ID to Shortcode Converter — Free Online API | SandBase`
- 建议 Description：`Convert Instagram media IDs to shortcodes instantly. Free API, no rate limits. One request, structured response. Try it now.`
- [ ] 已完成

### 2. `/blog/glm-5-3-release-watch-2026`（博客文章）

- 当前数据：286 展示, 0.7% CTR, 排名 7.4
- 建议 Title：`GLM 5.3 Release Date: Everything We Know (Updated Aug 2026)`
- 建议 Description：`When will GLM 5.3 launch? Latest leaks, benchmark predictions, and timeline analysis. Updated weekly.`
- [ ] 已完成

### 3. `/model/instagram/v1/shortcode-to-media-id`

- 当前数据：216 展示, 2.3% CTR, 排名 9.1
- 建议 Title：`Instagram Shortcode to Media ID — Free Converter API | SandBase`
- 建议 Description：`Convert any Instagram shortcode to its numeric media ID. Free REST API with instant response. No authentication required.`
- [ ] 已完成

### 4. `/model/douyin/web/all-sec-user-id`

- 当前数据：104 展示, 1.9% CTR, 排名 6.5
- 建议 Title：`Douyin Sec User ID Lookup — Batch Resolve API | SandBase`
- 建议 Description：`Resolve Douyin sec_user_id from share URLs or usernames in batch. Structured JSON response, ready for agent workflows.`
- [ ] 已完成

### 5. `/model/instagram/v3/user-id-to-username`

- 当前数据：119 展示, 1.7% CTR, 排名 41.7
- 排名太靠后，暂不优先做 title 优化，先通过内链提升排名
- [ ] 跳过 / 已完成

---

## P1：内链加强，推 Top 10 页面进 Top 5（2 小时）

排名 5-10 的页面进 top 5 后 CTR 会从 1-2% 跳到 5-15%。

### 操作清单

- [ ] 从首页 FAQ 或 footer 加链接到 Instagram API 工具页（`/model/instagram/...`）
- [ ] 从博客 `instagram-user-id-api-tutorial-2026` 加内链到 `/model/instagram/v1/media-id-to-shortcode`
- [ ] 从博客 `best-open-source-ai-agent-frameworks-2026` 加内链到 `/agents`
- [ ] 从 `deepseek-harness-vs-openclaw-vs-hermes-2026` 加内链到相关模型详情页
- [ ] 从 `glm-5-3-release-watch-2026` 加内链到 `/vendor/z-ai` 和 `/model/z-ai/glm-5.2`
- [ ] 模型详情页底部加 "Similar Models" 或 "Same Vendor" 区块（如开发资源允许）

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

### FAQ 段落

为高展现模型页添加 FAQ 区块（HTML `<details>` 或独立 section），示例：

```
Q: What is an Instagram media ID?
A: A numeric identifier (e.g., 2987654321098765432) that uniquely identifies a post on Instagram...

Q: How do I convert a shortcode to a media ID?
A: Call the SandBase API at /v1/model/instagram/v1/shortcode-to-media-id with the shortcode parameter...
```

### Schema.org 增强

为免费 API 工具页添加 SoftwareApplication schema：

```json
{
  "@type": "SoftwareApplication",
  "name": "Instagram Media ID to Shortcode API",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Web",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}
```

- [ ] Instagram 相关模型页加 FAQ
- [ ] Douyin 相关模型页加 FAQ
- [ ] 评估是否全局为 model 详情页模板加 SoftwareApplication schema

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
