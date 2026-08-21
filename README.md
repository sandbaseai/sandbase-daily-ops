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

## Structure

```text
playbooks/
  seo-geo-daily.md           # SEO/GEO daily ops checklist
scripts/
  cross_post.py              # Cross-channel distribution helper
  daily_hot_topics.py        # Daily topic monitoring
  seo_daily_check.py         # GSC/DataForSEO daily report
  track_rankings.py          # Search ranking checks
  submit_indexing.py         # Google indexing submission
  submit_indexnow.py         # IndexNow submission
skills/
  social-publish/            # LinkedIn, X, Discord, Xiaohongshu skill
outputs/
  seo-daily-reports/         # Daily SEO/indexing reports
```

## Blog operations moved

The canonical copies now live in `sandbase-blog`:

- [`skills/blog/`](https://github.com/sandbaseai/sandbase-blog/tree/main/skills/blog) — the single home for the skill, guides, prompts, references, and helper scripts

Make future Blog workflow changes there so implementation and documentation stay in sync.

Social distribution stays here under `skills/social-publish/`; Blog, Medium, DEV Community, and Zhihu long-form content stay in `sandbase-blog`.
