# SandBase SEO 下一步执行清单

更新时间：2026-08-23

## 已在自动运行

- Blog 每日 UTC 01:20 运行热点与 GSC 巡检。
- Blog 合并后自动部署 Cloudflare Pages。
- 每次内容变更前后运行 `npm run check`、`npm run build` 和 sitemap/hreflang 检查。
- 每日运营结果统一记录在 `outputs/seo-daily-reports/2026-08-23.md`。

## 等待外部状态

- Claude Agent SDK、GitHub MCP 新文章：HTTP 200、sitemap、canonical、hreflang 均正常；等待 Google 收录窗口。
- CTR 实验 1–6：至少 14 天后再比较，避免把数据延迟当成 uplift。
- GSC 当前博客基线：168 clicks / 5,578 impressions；非品牌词 119 clicks / 9,131 impressions / 1.3% CTR。

## 需要配置后才能执行

- `sandbase-blog` GitHub Actions Secret `SANDBASE_API_KEY` 尚未存在；因此 DataForSEO 自动排名任务会在请求前安全停止，未产生费用。
- 配置后运行 Blog operations → `rankings`，再把排名历史写入本日志并与 GSC 页面数据交叉验证。

## 下一轮优先级

1. 复核新文章是否进入 GSC 页面数据和 `site:` 结果。
2. 14 天窗口到期后评估 CTR 实验 1–6，保留有效变更、回滚无效变更。
3. 用排名历史选择下一批排名 5–20、CTR <2% 的页面做 metadata 实验。
4. 继续建设 MCP、Agent SDK、LLM/API、视频 API 主题集群和高流量入口内链。
