# SEO 优化复盘巡检报告

> 生成日期：2026-08-24
> 对照计划：[2026-08-17 SEO 转化率优化计划](./2026-08-17-optimization-plan.md)
> 数据来源：Google Search Console、GSC URL Inspection、线上页面与 sitemap 实测、Blog 源码检查
> GSC 最新可用日期：2026-08-22（约 2 天延迟）
> 当前结论：**曝光和点击继续增长，但全站 CTR、平均排名与重点词排名未达到计划验收线，需要继续做搜索意图聚合与摘要优化。**

---

## 一、执行摘要

- 全站滚动 15 天展示达到 **37,923**，相对 8/17 计划快照的 21,330 增长 **77.8%**；点击达到 **428**，增长 **55.6%**。
- 增长质量暂未同步：全站 CTR 从计划快照的 **1.3% 降至 1.13%**，平均排名从 **17.2 降至 19.94**（数值越低越好）。
- 等长 7 天对比也显示相同趋势：计划后展示增长 **69.1%**、点击增长 **33.5%**，但 CTR 从 **1.29% 降至 1.02%**，平均排名从 **18.54 降至 21.08**。这表明 Google 正在扩大长尾曝光，但新增曝光集中在较低排名和低点击页面。
- Blog 子域滚动 15 天表现优于全站：**173 点击 / 5,528 展示 / CTR 3.13% / 平均排名 16.09**。核心文章 `deepseek-harness-vs-openclaw-vs-hermes-2026` 贡献 134 点击，但核心查询平均排名已从计划时约 2.9 回落到约 6.0。
- 计划重点页 8/8 URL Inspection 均为 **PASS / Submitted and indexed**，Google canonical 与页面声明一致。
- 日报抽样文章收录为 **7/10**；2 篇处于 `Discovered - currently not indexed`，1 篇存在 `Google chose different canonical`。
- 线上主站和 Blog 的 robots、sitemap 均可访问；但 `sitemap.xml` 与 `sitemap-index.xml` 的 URL 集合明显不一致，需要统一口径。

---

## 二、核心指标复盘

### 2.1 与 8/17 计划快照对比

| 指标 | 8/17 计划快照（8/1~8/15） | 当前滚动 15 天（8/8~8/22） | 变化 | 判断 |
|---|---:|---:|---:|---|
| 点击 | 275 | 428 | +153（+55.6%） | ✅ 增长 |
| 展示 | 21,330 | 37,923 | +16,593（+77.8%） | ✅ 显著增长 |
| CTR | 1.3% | 1.13% | -0.17 个百分点 | ❌ 下降 |
| 平均排名 | 17.2 | 19.94 | 下降 2.74 位 | ❌ 下降 |

> 数据口径说明：重新查询已完成归档的 8/1~8/15 数据得到 270 点击、20,362 展示、CTR 1.33%、平均排名 17.96，与 8/17 文档快照略有差异，属于 GSC 数据最终化和查询时间差异。本报告验收仍以原计划快照为准。

### 2.2 计划前后等长 7 天对比

| 指标 | 计划前 7 天（8/9~8/15） | 计划后 7 天（8/16~8/22） | 变化 |
|---|---:|---:|---:|
| 点击 | 176 | 235 | +33.5% |
| 展示 | 13,675 | 23,129 | +69.1% |
| CTR | 1.29% | 1.02% | -0.27 个百分点 |
| 平均排名 | 18.54 | 21.08 | 下降 2.54 位 |

**判断：** 当前不是流量停滞，而是“曝光扩张快于点击增长”。优化重点应从继续扩量切换为：聚合搜索意图、减少同词多页竞争、改进 Title/Description，并把排名 5~10 的页面推入 Top 5。

---

## 三、8/17 验收目标完成度

| 验收项 | 当前结果 | 状态 |
|---|---|---|
| 整体 CTR 从 1.3% 提升到 2.5%+ | 全站 1.13%；Blog 子域 3.13% | ❌ 全站未达标 |
| Top 3 高展现页面 CTR 各提升 3~5 个百分点 | 重点页 CTR 基本持平或下降 | ❌ 未达标 |
| 排名 5~10 页面至少 3 个进入 Top 5 | 计划跟踪页仍主要位于 6.4~8.3 | ❌ 未达标 |
| DeepSeek Harness 系列关键词 Top 3 | 主词 `deepseek harness vs hermes` 平均排名 5.97 | ❌ 未达标 |
| 重点页面可抓取、canonical 正确 | 抽查 8/8 PASS，canonical 一致 | ✅ 达标 |
| 模型/API 页 SoftwareApplication schema | 抽查页面均存在 | ✅ 达标 |
| 模型/API 页 FAQ + FAQPage schema | 未发现模型页 FAQPage | ❌ 未完成 |

---

## 四、计划重点页面表现

数据范围：2026-08-08~2026-08-22。

| 页面 | 当前点击 | 当前展示 | 当前 CTR | 当前排名 | 与计划基线相比 |
|---|---:|---:|---:|---:|---|
| `/model/instagram/v1/media-id-to-shortcode` | 3 | 302 | 0.99% | 7.23 | CTR 基本持平；排名改善约 0.6 位；展示 -26% |
| `blog/glm-5-3-release-watch-2026`（英文 canonical） | 2 | 343 | 0.58% | 7.45 | 展示 +20%；CTR -0.12pp；排名基本不变 |
| `/model/instagram/v1/shortcode-to-media-id` | 5 | 239 | 2.09% | 8.25 | 展示 +11%；CTR -0.21pp；排名改善约 0.85 位 |
| `/model/douyin/web/all-sec-user-id` | 2 | 126 | 1.59% | 6.40 | 展示 +21%；CTR -0.31pp；排名基本不变 |
| `/model/instagram/v3/user-id-to-username` | 0 | 81 | 0% | 52.88 | CTR -1.7pp；排名下降约 11 位 |

### 4.1 线上摘要检查

当前模型页已经具备更丰富的接口说明、输入/输出 schema、代码示例、README、Related Models 和 `SoftwareApplication` JSON-LD，页面不再只是简单 playground；但计划中的搜索摘要文案并未完全落地：

| 页面 | 当前 Title | 结论 |
|---|---|---|
| Instagram media ID → shortcode | `Convert media ID to shortcode by Instagram \| SandBase` | 仍偏数据库式命名，缺少 `Instagram`、`Free API` 等强意图词 |
| Instagram shortcode → media ID | `Convert shortcode to media ID by Instagram \| SandBase` | 同上 |
| Douyin sec user ID | `Extract list user id by Douyin \| SandBase` | 未覆盖用户实际搜索的 `sec_user_id lookup/resolve` 意图 |
| GLM 5.3 | `GLM 5.3 Release Date (2026): API, Pricing & Benchmark Results \| SandBase Blog` | ✅ 已明显优化且 canonical 正确 |

### 4.2 Instagram 搜索意图互相竞争

`instagram shortcode media id timestamp algorithm` 等查询同时由 v1、v2、v3 多个 API 页面获得展示：

- v2 media-id-to-shortcode：36 展示，排名 4.64
- v3 media-id-to-shortcode：29 展示，排名 5.41
- v1 shortcode-to-media-id：21 展示，排名 6.48
- v1 media-id-to-shortcode：16 展示，排名 6.13

这些页面都使用近似 Title 和描述，Google 难以判断哪个页面最符合教程/算法类意图。应建立一个权威教程或转换器落地页承接信息型查询，再明确链接到不同 API 版本；API 页 Title 应说明版本和用途差异，而不是全部争夺同一摘要。

---

## 五、当前高展现低点击机会

| 页面 | 展示 | CTR | 排名 | 优先动作 |
|---|---:|---:|---:|---|
| `/model/instagram/v3/media-id-to-shortcode` | 449 | 0.89% | 7.11 | 改 Title/Description；与 v1/v2 做意图区分 |
| `blog/deepseek-harness-developer-preview-2026` | 430 | 0% | 6.82 | 重写摘要并加强到主比较页的链接 |
| `/model/instagram/v2/media-id-to-shortcode` | 394 | 0.25% | 7.74 | 同 Instagram 聚合策略 |
| `/model/tencent/hy3` | 381 | 0% | 6.39 | 核对查询意图并重写摘要 |
| `/model/wechat-mp/v2/article-detail` | 350 | 0% | 4.22 | **排名已进 Top 5，优先修摘要** |
| `blog/glm-5-3-release-watch-2026` | 343 | 0.58% | 7.45 | 保持更新日期、增强 SERP 价值主张 |
| `/model/instagram/v1/media-id-to-shortcode` | 302 | 0.99% | 7.23 | 落实计划中的搜索友好文案 |
| `/model/defillama/chain-stablecoin-market-cap-history` | 264 | 0% | 9.05 | 增加明确用途和免费试用价值 |
| `/deepk-ai/profiles-bundles-patches` | 254 | 1.18% | 5.44 | 加强摘要与站内入口链接 |
| `/model/instagram/v1/shortcode-to-media-id` | 239 | 2.09% | 8.25 | 保持排名提升并测试新 Title |

> 旧 `www.sandbase.ai/blog/*` URL 在当前 15 天窗口仍保留迁移前数据，且线上已 308 到 `blog.sandbase.ai`。做内容决策时应以新 canonical URL 为主，避免把迁移前后 URL 当成两个独立页面。

---

## 六、DeepSeek Harness 专题复盘

### 6.1 当前表现

- 主比较文章：**134 点击 / 1,950 展示 / CTR 6.87% / 平均排名 6.86**。
- 核心查询 `deepseek harness vs hermes`：**47 点击 / 478 展示 / CTR 9.83% / 排名 5.97**。
- `deepseek harness vs hermes agent`：16 点击 / 151 展示 / CTR 10.60% / 排名 6.24。
- `deepseek harness vs openclaw`：3 点击 / 47 展示 / CTR 6.38% / 排名 5.74。
- 与 8/17 记录的 CTR 17.6%、排名 2.9 相比，主词排名和 CTR 均回落，Top 3 目标未达成。

### 6.2 内容落地情况

- 计划指定的 3 个精确文章 slug 未创建，但当前英文目录已有 **8 篇** DeepSeek Harness/DSH 相关文章，专题覆盖已明显扩大。
- 主比较文章到 DeepSeek V4 Pro/Flash 的内链已在中英文版本落地。
- 当前主词绝大多数展示仍集中在主比较文章，不是严重的多篇互相竞争；问题更接近排名回落和摘要点击率下降。
- `deepseek harness` 泛词由主站 `/deepk-ai/what-is-deepseek-harness` 承接，但当前仅 11 展示、平均排名 70.55，应加强该文档页与 Blog 专题之间的双向内链，并明确“官方介绍/教程”和“框架对比”的搜索意图边界。

---

## 七、收录与 canonical

### 7.1 日报抽样

当前 canonical 巡检脚本抽样 10 篇 Blog 文章：

- 已收录：**7/10（70%）**
- `agent-harness-performance-variable-2026`：Discovered - currently not indexed
- `agent-plugins-1-portable-coding-agent-standard-2026`：Discovered - currently not indexed
- `agent-observability-logging-tracing-debugging`：Duplicate, Google chose different canonical than user

建议先处理重复 canonical 页面；另外两篇先检查内链、内容差异化和 sitemap 更新时间，再通过 GSC URL Inspection 手动请求，不使用普通文章不适用的 Google Indexing API。

### 7.2 重点页抽查

以下 8 个页面全部为 `PASS / Submitted and indexed / INDEXING_ALLOWED`，Google canonical 与 user canonical 一致：

- `/models`
- `/apis`
- 4 个计划重点模型/API 页面
- GLM 5.3 Blog canonical
- DeepSeek Harness 主比较文章 canonical

旧主站 Blog URL 到新 Blog 子域使用 308 永久重定向，迁移路径有效。

---

## 八、技术 SEO 与 GEO 检查

### 8.1 正常项

- 主站与 Blog `robots.txt`：HTTP 200，允许公开内容抓取。
- `/models`、`/apis` 和抽查页面：HTTP 200，SSR HTML 体积充足，Title、Description、canonical 均存在。
- 模型/API 页 JSON-LD：存在 `SoftwareApplication`、`BreadcrumbList`、`Organization`。
- Blog 页 JSON-LD：存在 `BlogPosting`、`WebPage`、`BreadcrumbList`、`Organization`。
- `sitemap-models.xml`：2,349 URL，HTTP 200。
- `sitemap-vendors.xml`：125 URL，HTTP 200。
- Blog sitemap：344 URL，HTTP 200。

### 8.2 需处理项

#### A. 两套 sitemap 口径不一致

- `robots.txt` 声明的 `https://www.sandbase.ai/sitemap.xml`：4,862 个唯一 URL。
- `https://www.sandbase.ai/sitemap-index.xml` 的 7 个子 sitemap：3,230 条记录、3,229 个唯一 URL。
- 两者交集仅 2,481 URL；仅 monolithic sitemap 存在 2,381 URL，仅 index 子 sitemap 存在 748 URL。
- 差异主要来自 model docs、plugins、Blog 中英文、docs 与新页面集合。

两者当前都返回 200，但搜索引擎收到的是不同 URL 清单。应确定唯一 canonical sitemap 入口，或者保证两套内容一致；同时找出 index 子 sitemap 中的 1 条重复 URL。

#### B. 模型页 FAQ schema 未落地

抽查模型/API 页有 SoftwareApplication，但未发现 `FAQPage`；计划 P3/P5 的 FAQ 展示和 FAQ JSON-LD 尚未完成。应先在高展现页面试点，不建议直接对全站生成低质量重复 FAQ。

#### C. 巡检脚本口径标注错误

当前 `sandbase-blog/scripts/operations/gsc_report.py`：

- 页面查询已限定 Blog URL，但报告“总体数据”仍标为“全站 / 博客”，导致两列完全相同。
- 日期计算为 `today-9` 至 `today-2`，包含首尾共 8 天，但报告写“过去 7 天”。

本报告没有使用该错误的“全站”数字，而是另行调用 GSC 无维度聚合获取准确全站数据。建议修正脚本标签和日期窗口。

### 8.3 GEO 边界

本次已验证结构化数据和可抓取性；未对 ChatGPT、Perplexity、Google AI Overview 的实时引用结果做可重复、可归因的登录态测试，因此不把 AI 搜索引用列为本次已验证指标。

---

## 九、8/17 计划实施状态

| 计划项 | 当前状态 | 证据/备注 |
|---|---|---|
| P0 模型/API Title/Description 优化 | 部分完成 | 模板已有品牌词，但计划重点页仍是数据库式命名，CTR 无明显改善 |
| P0 GLM 5.3 标题优化 | 已完成 | live Title、Description 已更新 |
| P1 Instagram 教程加 3 个模型页内链 | 未完成 | 当前文章只出现 API 调用路径，未发现计划中的模型详情页链接 |
| P1 DeepSeek 主文加 V4 Pro/Flash 内链 | 已完成 | 中英文均已存在 |
| P1 GLM 文章加 Z.ai/GLM 5.2 内链 | 已完成 | 中英文均已存在 |
| P1 开源 Agent 框架文章链接 `/agents` | 未发现 | 建议补充 |
| P2 3 篇高展现 API 教程 | 未按计划 slug 创建 | Instagram 主题当前最需要聚合页 |
| P3/P5 SoftwareApplication schema | 已完成 | live 页面可见 |
| P3/P5 模型页 FAQ + FAQPage | 未完成 | live 与源码抽查均未发现 |
| P4 DeepSeek Harness 内容集群 | 部分完成/替代完成 | 精确计划 slug 未建，但已有 8 篇相关英文内容 |
| P5 API 详情页内容丰富化 | 大部分已完成 | 已有 schema、示例、README、Related Models |

---

## 十、下一轮优先级

### P0：本周立即处理

1. **重写 5 个高展现 API 页摘要**：Instagram v1/v2/v3 media ID/shortcode、Douyin all-sec-user-id、Wechat article-detail。标题必须明确平台、操作方向、API/Converter 价值，不再只用数据库 display name。
2. **创建 Instagram media ID ↔ shortcode 权威教程/工具页**：解释算法、timestamp、encode/decode，并链接 v1/v2/v3 API；各 API 页反向链接该权威页，降低同词多页竞争。
3. **恢复 DeepSeek 主词 Top 3**：更新主比较文的开头直接答案、比较表和更新时间；从现有 8 篇集群内容统一加强到主比较文的描述性内链。
4. **处理重复 canonical**：检查 `agent-observability-logging-tracing-debugging` 的语言版本、旧主站 URL、尾斜杠和 canonical 目标。

### P1：技术与数据质量

5. **统一 sitemap**：确定 `sitemap.xml` 或 `sitemap-index.xml` 为唯一权威入口，核对 2,381/748 条差异和 1 条重复记录。
6. **修正 GSC 日报脚本**：Blog-only 报告不再标“全站”，并把日期窗口改成真正 7 天；如需全站指标，增加独立无维度聚合查询。
7. **为高展现模型页试点 FAQ**：先做 Instagram、Douyin、Wechat 各 1~2 页，确保 FAQ 与页面数据和真实搜索问题相关，再加入 FAQPage schema。

### P2：继续观察

8. 每周用固定 15 天窗口复查全站 CTR；下一次关键观察日建议为 **2026-08-31**。
9. 单独追踪 Blog 子域迁移后的 canonical URL，避免旧 `www.sandbase.ai/blog/*` 数据干扰判断。
10. 对 `agent-harness-performance-variable-2026`、`agent-plugins-1-portable-coding-agent-standard-2026` 补内链后再检查收录，不反复无差异提交。

---

## 十一、下轮验收线

- 全站滚动 15 天 CTR：先恢复到 **1.3%+**，再向原计划 2.5% 推进。
- Instagram media ID/shortcode 相关页面：至少 1 个权威页进入 Top 5，相关 API 页 CTR 达到 **2%+**。
- Wechat article-detail：保持 Top 5，CTR 从 0 提升到 **3%+**。
- DeepSeek Harness 主词：平均排名恢复到 **Top 3**，CTR 恢复到 **12%+**。
- sitemap：robots 声明入口与拆分 sitemap URL 集合一致，无重复 URL。
- Blog 抽样收录：恢复到 **9/10+**，重复 canonical 问题清零。

---

## 附：本次产物

- 当前 canonical 自动巡检报告：`sandbase-blog/outputs/blog-operations/2026-08-24.md`
- 本复盘报告：`sandbase-daily-ops/outputs/seo-daily-reports/2026-08-24-optimization-review.md`
- 对照计划：`sandbase-daily-ops/outputs/seo-daily-reports/2026-08-17-optimization-plan.md`
