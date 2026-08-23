# SandBase SEO Experiment Ledger

This ledger keeps SEO changes measurable. Each experiment must have a pre-change GSC baseline, a single primary change, a production verification run, and a post-change window before the next edit.

## Baseline

- GSC frozen 28-day baseline: 515 site clicks / 44,665 impressions; Blog 168 clicks / 5,578 impressions; non-brand 119 clicks / 9,131 impressions (1.3% CTR).
- Current recurring collection: `.github/workflows/blog-operations.yml` in `sandbase-blog`.
- Primary evidence sources: GSC URL inspection and performance reports; DataForSEO is directional and may differ by location/device.

## Active experiments

| ID | Page | Change | Pre-change evidence | Production run | Measurement gate | Status |
|---|---|---|---|---|---|---|
| CTR-001 | `deepseek-harness-developer-preview-2026` | EN/ZH title and description aligned to review, GitHub setup, plugins, and API limits | 429 impressions, position 6.8, CTR 0.0% | Deploy `32640599737`; Blog PR #178 | Compare after 7–14 days | Running |
| CTR-002 | `glm-5-3-release-watch-2026` | EN/ZH title and description lead with “release date” intent while retaining API/pricing/benchmarks | 341 impressions, position 7.4, CTR 0.6%; query `glm 5.3 release date` had 49 impressions | Deploy `32640900625`; Blog PR #179 | Compare after 7–14 days | Running |

## Decision rules

1. Do not make a second metadata change before the measurement gate unless Google rewrites the snippet or the page has a factual error.
2. Prefer pages ranking 5–20 with at least 50 impressions and CTR below 2%.
3. Treat a CTR lift as provisional until it persists across a comparable 28-day window; do not claim a 100x improvement from a single report.
4. After each gate, record clicks, impressions, CTR, average position, indexed state, and the exact production URL in the daily operations PR.

Last updated: 2026-08-23
