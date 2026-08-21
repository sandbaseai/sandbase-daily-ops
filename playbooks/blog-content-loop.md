# Blog 内容与搜索闭环

这是 `sandbase-daily-ops` 与 `sandbase-blog` 的跨仓库操作契约。Daily 是监控和分发的唯一实现仓库；Blog 是文章、视觉、SEO 编辑规则和发布的唯一实现仓库。不要在两个仓库复制脚本或 Skill。

## 完整流程

1. Daily 运行 `scripts/daily_hot_topics.py`，输出 `outputs/seo-daily-reports/hot-topics-YYYYMMDD.json`。
2. 编辑或自动代理读取最新热点报告，并在 Blog 的 `scripts/ai-content-generator/content-index.md` 与 `src/content/` 中查重。
3. 在 Blog 按 `skills/blog/SKILL.md` 研究、写 EN/ZH、生成截图和封面、三轮校验并提交 PR。
4. Blog 合并到 `main` 后独立部署 Cloudflare Pages，不调用 Daily 仓库。
5. Daily 按自己的定时任务读取线上 sitemap 和 GSC；需要立即检查时，用户在 Daily 手动传入文章 slug。
6. 需要付费 SERP 排名时，由操作员手动运行 Daily workflow，并明确打开 billable 开关。
7. 社交分发读取已经发布的 canonical Blog URL，按 `skills/social-publish/SKILL.md` 生成 LinkedIn、X、Discord 或小红书内容。

## 自动任务入口

Daily workflow：`.github/workflows/blog-signals.yml`

- `schedule`：每日热点与 GSC；每周排名默认关闭。
- `workflow_dispatch`：人工选择 `daily`、`hot-topics`、`gsc` 或 `rankings`。

需要的 GitHub Secrets：

- `SANDBASE_API_KEY`：热点、搜索量和显式批准的 SERP 排名；所有 DataForSEO 模型均经 SandBase API。
- `GOOGLE_SERVICE_ACCOUNT_JSON`：GSC 只读与 URL Inspection。

两个仓库之间不配置 token、不发送 repository dispatch。联动依靠稳定的线上接口（Blog sitemap、canonical URL、GSC）和文档契约。不要使用 DataForSEO 直连账号。

## 数据契约

| 数据 | 生产者 | 消费者 | 稳定位置 |
|---|---|---|---|
| 热点候选、来源、搜索量 | Daily | Blog 选题 | `outputs/seo-daily-reports/hot-topics-YYYYMMDD.json` |
| GSC 点击、展示、CTR、排名、收录 | Daily | 编辑/SEO | `outputs/seo-daily-reports/YYYY-MM-DD.md` |
| 指定词 SERP 历史 | Daily | 编辑/SEO | `outputs/seo-daily-reports/ranking-history.csv` |
| 跟踪词、语言、地区、目标 slug | Daily | ranking job | `config/blog-keywords.json` |
| 已有文章和 canonical slug | Blog | Daily/编辑 | `scripts/ai-content-generator/content-index.md`、Blog sitemap |

热点和排名是选题证据，不是写作指令。先判断读者意图、是否已有覆盖、SandBase 是否有可信角度，再决定新写、更新旧文或放弃。

## 人工运行

```bash
python3 scripts/track_rankings.py --config config/blog-keywords.json --dry-run

python3 scripts/track_rankings.py \
  --config config/blog-keywords.json \
  --env-file /absolute/path/to/ignored.env \
  --allow-billable-requests \
  --output outputs/seo-daily-reports/ranking-history.csv
```

Google Indexing API 不是普通 Blog 文章的通用收录保证。Blog 发布后优先保证 sitemap、canonical、内链和 GSC URL Inspection 正常；IndexNow 仅作为支持该协议的搜索引擎通知。
