# SandBase Growth Operations Ledger

`sandbase-daily-ops` is the canonical record for all ongoing growth operations. Code and content remain in the repository that owns the production surface; this repository records why work was done, what changed, whether it shipped, and how it performed.

## What must be recorded

Record every material action involving:

- Google SEO, technical SEO, GSC, indexing, sitemaps, canonical URLs, structured data, or internal links;
- Blog articles, refreshes, topic clusters, translations, and editorial experiments;
- GitHub README, release, example, directory, issue, and contributor-growth work;
- DEV, Medium, Hacker News, Reddit, directory, newsletter, partner, or other third-party distribution;
- conversion-path changes from organic landing page to signup, API key, CLI install, first call, or paid usage.

## Source-of-truth boundary

| Information | Canonical location |
|---|---|
| Product or Blog implementation | Owning code/content repository |
| Workflow code | Owning repository, for example `sandbase-blog/scripts/operations/` |
| Operational decision and experiment history | `sandbase-daily-ops` |
| GSC snapshot and interpretation | Dated file under `outputs/seo-daily-reports/` |
| Credentials and tokens | Secret manager or CI; never this repository |

## Required fields

Every dated operation entry must include:

1. **Objective** — the query, audience, funnel stage, or technical problem.
2. **Evidence** — GSC values, crawl output, user behavior, or primary-source research.
3. **Action** — exact pages, repositories, or channels changed.
4. **Implementation location** — repository and file paths or pull request.
5. **Validation** — build, tests, rendered HTML, live URL, sitemap, or structured-data evidence.
6. **Deployment state** — drafted, local, pull request, merged, deployed, indexed, or measured.
7. **Baseline** — clicks, impressions, CTR, position, conversion, or “not yet available.”
8. **Review date** — normally 14 and 28 days for SEO experiments.
9. **Result** — pending, win, neutral, loss, reverted, or superseded.
10. **Next action** — the single next operational step.

## Experiment template

```markdown
## Experiment: <short name>

- Objective:
- Evidence:
- Action:
- Implementation:
- Validation:
- Deployment state:
- Baseline:
- Review dates:
- Result: pending
- Next action:
```

## Measurement rules for the 100× SEO goal

- North star: Google organic clicks across SandBase properties, rolling 28 days.
- Primary proof: like-for-like Google Search Console comparison.
- Report brand and non-brand queries separately.
- Preserve the property set, country/device filters, search type, and delay window.
- A code build, published article, or index notification is progress, not proof of traffic growth.
- Do not claim 100× until a rolling 28-day GSC comparison verifies it.

