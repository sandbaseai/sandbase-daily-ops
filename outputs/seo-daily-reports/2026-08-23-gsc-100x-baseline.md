# SandBase Google SEO 100× baseline

Baseline frozen on 2026-08-23 from Google Search Console's rolling 28-day window, with the standard two-day reporting delay. Source workflow: [sandbase-blog Actions run 32611196712](https://github.com/sandbaseai/sandbase-blog/actions/runs/32611196712). The unedited generated report is stored beside this file as `2026-08-23-gsc-28d-baseline-raw.md`.

## North-star definition

The 100× target is defined as **rolling 28-day non-brand organic Google clicks**. This isolates discoverability beyond people already searching for SandBase by name and is the closest measurable match to the growth objective.

| Metric | Baseline | 100× target |
| --- | ---: | ---: |
| Non-brand Google clicks | 119 | 11,900 |
| Blog Google clicks | 168 | 16,800 |
| Whole-site Google clicks | 515 | 51,500 |

The first row is the primary success criterion. Blog and whole-site clicks are supporting indicators and must not be substituted for the primary metric.

## Baseline diagnostics

| Metric | Value |
| --- | ---: |
| Whole-site impressions | 44,665 |
| Blog impressions | 5,578 |
| Non-brand impressions | 9,131 |
| Non-brand CTR | 1.3% |
| Brand clicks | 111 |
| Brand impressions | 307 |
| Brand CTR | 36.2% |
| Sitemap articles with GSC data | 232 |
| Tracked new articles indexed | 7/10 |

## Immediate opportunity queue

Pages already ranking 5–20 with at least 50 impressions and CTR below 2% offer the fastest measurable gains. The first three are:

1. `deepseek-harness-developer-preview-2026`: 429 impressions, position 6.8, 0 clicks.
2. `glm-5-3-release-watch-2026`: 341 impressions, position 7.4, 2 clicks.
3. `claude-opus-5-deep-dive-2026`: 236 impressions, position 10.5, 1 click.

## Measurement rules

- Compare equivalent rolling 28-day windows from the same Search Console property and report implementation.
- Keep the two-day GSC delay unchanged.
- Record absolute clicks, impressions, CTR, and average position; do not report percentage growth alone.
- Annotate major releases, migrations, incidents, and tracking changes.
- Review at 14 and 28 days; do not claim 100× until non-brand clicks reach 11,900 in a comparable window.
