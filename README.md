# SandBase Daily Ops

Daily operating system for SandBase SEO monitoring, content distribution, and community updates.

This repo keeps daily monitoring, distribution, community playbooks, and operational reports. Blog authoring and publication assets now live with the site code in [sandbase-blog](https://github.com/sandbaseai/sandbase-blog).

- Blog
- LinkedIn
- X / Twitter
- Discord
- Medium
- Zhihu

More channels can be added later (DEV Community, Xiaohongshu, WeChat Channels), but the
first version stays focused on company-facing global distribution plus Chinese long-form.

Blog 热点选词、GSC、排名、发布和社交分发如何跨仓库串联，统一以 `playbooks/blog-content-loop.md` 为准。自动任务入口是 `.github/workflows/blog-signals.yml`。

## Structure

```text
playbooks/
  blog-content-loop.md       # Blog/Daily 跨仓库契约与完整闭环
  seo-geo-daily.md           # SEO/GEO daily ops checklist
scripts/
  cross_post.py              # Cross-channel distribution helper
  daily_hot_topics.py        # Daily topic monitoring
  seo_daily_check.py         # GSC/DataForSEO daily report
  track_rankings.py          # Search ranking checks
  submit_indexing.py         # Google indexing submission
  submit_indexnow.py         # IndexNow submission
skills/
  blog-operations/           # 热点、GSC、排名与 Blog 交接 skill
  social-publish/            # LinkedIn, X, Discord, Xiaohongshu skill
outputs/
  seo-daily-reports/         # Daily SEO/indexing reports
```

关键词跟踪配置位于 `config/blog-keywords.json`；不要把关键词继续写死在 Python，也不要把 Blog 文章内容复制到 Daily。

## Blog operations moved

The canonical copies now live in `sandbase-blog`:

- [`skills/blog/`](https://github.com/sandbaseai/sandbase-blog/tree/main/skills/blog) — the single home for the skill, guides, prompts, references, and helper scripts

Make future Blog workflow changes there so implementation and documentation stay in sync.

Social distribution stays here under `skills/social-publish/`; Blog, Medium, DEV Community, and Zhihu long-form content stay in `sandbase-blog`.
