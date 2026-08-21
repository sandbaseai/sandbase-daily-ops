---
name: blog-operations
description: Discover and qualify SandBase Blog topics, inspect Google Search Console performance and indexing, track configured Google rankings, and hand approved topics to the sandbase-blog publishing workflow. Use for热点选词、SEO 日报、Google 关键词跟踪、文章发布后巡检、收录检查，或 Blog 与 Daily Ops 的跨仓库自动化。
---

# Blog Operations

Run from the `sandbase-daily-ops` repository root. Read `playbooks/blog-content-loop.md` before changing workflow ownership, secrets, output paths, or the Blog handoff.

## Keep ownership clear

- Maintain topic discovery, GSC, rankings, indexing notifications, reports, and social distribution here.
- Maintain articles, authors, visuals, screenshots, covers, Medium/DEV/Zhihu adaptations, and publication rules in `sandbase-blog/skills/blog/`.
- Never copy one repository's scripts or Skill into the other. Link to its canonical location.

## Choose the operation

### Discover topics

Run `python3 scripts/daily_hot_topics.py`. Require `SANDBASE_API_KEY`. Read the dated JSON in `outputs/seo-daily-reports/`, verify source freshness, and compare candidates against the Blog content index. Search volume is evidence, not permission to publish.

Hand selected candidates to `sandbase-blog/skills/blog/SKILL.md`; the Blog workflow owns research, bilingual drafting, images, three review passes, PR, deployment, and live verification.

### Inspect Google performance

Run `python3 scripts/seo_daily_check.py`. Require a GSC-authorized service account via `GOOGLE_SERVICE_ACCOUNT_FILE` or the documented local default. Use its report for observed clicks, impressions, CTR, average position, and sampled URL Inspection status.

Do not describe GSC's delayed data as live ranking data. Do not describe URL Inspection or the Google Indexing API as a ranking or indexing guarantee.

### Track explicit rankings

Edit `config/blog-keywords.json`, not Python constants. Every record needs a keyword, DataForSEO language code, location code, canonical Blog slug, and last verified volume.

Preview without credentials or cost:

```bash
python3 scripts/track_rankings.py --config config/blog-keywords.json --dry-run
```

Only make live calls after explicit billable approval:

```bash
python3 scripts/track_rankings.py \
  --config config/blog-keywords.json \
  --env-file /absolute/path/to/ignored.env \
  --allow-billable-requests \
  --output outputs/seo-daily-reports/ranking-history.csv
```

### Run automation

Use `.github/workflows/blog-signals.yml` for scheduled and manual runs. Confirm required secrets before starting a task. Ranking runs are manual and must set the billable approval input.

Discover Blog changes from the live sitemap and GSC rather than waiting for a cross-repository event. For an immediate targeted inspection, run `python3 scripts/seo_daily_check.py --slugs <comma-separated-slugs>` in Daily. Do not add a cross-repository token or claim Blog deployment triggered monitoring. Route every DataForSEO model through `https://api.sandbase.ai/v1/run` with `SANDBASE_API_KEY`; never request direct provider credentials.

## Review outputs

Before recommending work:

1. verify dates, source URLs, locale and location;
2. distinguish observed GSC data from DataForSEO samples;
3. check whether an existing Blog page should be updated instead of creating a duplicate;
4. reject topics without a useful SandBase angle or adequate primary evidence;
5. preserve secrets and keep generated local reports out of unrelated commits.
