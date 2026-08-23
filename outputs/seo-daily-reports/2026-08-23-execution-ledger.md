# SandBase SEO 100× Execution Ledger — 2026-08-23

## Objective

Build and operate a durable Google SEO growth system for SandBase, with a verified target of 100× organic search clicks. The target is not yet achieved.

## Evidence reviewed

- Latest stored GSC report: seven days, 310 whole-site clicks, 9,304 impressions, 500 pages with data.
- Blog subset: three clicks, 1,286 impressions, and 35 pages with data.
- Dify article: 816 impressions, one click, 0.1% CTR, average position 15.1.
- Existing public assets: main site, Docs, Blog, GitHub organization, CLI, Skills, Harness, and growth repositories.
- Existing Blog corpus already covers hundreds of English and Chinese pages; raw content volume is not the main constraint.

The stored values are provisional. During implementation review, the current Blog GSC script was found to query Blog URLs only while labeling one aggregate “whole site.” The reporting implementation has been corrected locally, but a new production run is required before freezing the 28-day baseline.

## Experiment 1: Dify high-impression CTR refresh

- Objective: improve CTR and ranking for a page already receiving substantial non-brand impressions.
- Evidence: 816 impressions, one click, 0.1% CTR, position 15.1 in the 2026-08-21 stored report.
- Action: changed the title to match pricing, self-hosting, and alternatives intent; rewrote the description; added a direct-answer section; added contextual links to the SandBase LLM gateway and first-call guide.
- Implementation: `sandbase-blog/src/content/en/dify-ai-platform-explained-2026.md`.
- Validation: Blog tests passed; production build passed; rendered title, description, canonical, `dateModified`, structured data, heading, and links were inspected.
- Deployment state: local change; not yet pushed, merged, deployed, or indexed.
- Baseline: 816 impressions / 1 click / 0.1% CTR / position 15.1 over the stored seven-day report.
- Review dates: 14 and 28 days after deployment.
- Result: pending.
- Next action: create a Blog pull request, deploy, then annotate the deployment date here.

## Experiment 2: correct the 100× measurement system

- Objective: make 100× measurable and prevent Blog-only data from being reported as whole-site performance.
- Evidence: current `gsc_report.py` applied the Blog URL filter in `fetch_page_data`, while the report displayed a whole-site column; it used a seven-day window and did not split brand/non-brand traffic.
- Action: changed the report to fetch whole-site and Blog page/query data independently; changed the window to 28 days; added brand/non-brand query totals; added an automatic opportunity queue for pages with at least 50 impressions, position 5–20, and CTR below 2%; added a click-gap estimate to 2% CTR.
- Implementation: `sandbase-blog/scripts/operations/gsc_report.py`.
- Validation: Python compilation passed; deterministic smoke test passed; Blog test suite passed (25 tests).
- Deployment state: local change; not yet pushed or run with production GSC credentials.
- Baseline: provisional until the corrected job runs in CI.
- Review dates: immediately after merge, then weekly.
- Result: pending.
- Next action: merge the script, run the GSC workflow with production credentials, and store the first corrected 28-day report here.

## Experiment 3: OpenRouter alternatives commercial-intent hub

- Objective: create a central page for “OpenRouter alternatives,” “self-hosted LLM gateway,” “OpenAI-compatible API,” and multimodal API intent.
- Evidence: the Blog already had individual LiteLLM/OpenRouter/Google routing pages but no central alternatives hub, leaving the cluster fragmented.
- Action: created a neutral comparison of OpenRouter, SandBase, LiteLLM, Portkey, and Cloudflare; documented fit and trade-offs; added a runnable OpenAI SDK example, migration checklist, FAQ, and SandBase Docs links; added contextual backlinks from four existing cluster pages.
- Implementation: `sandbase-blog/src/content/en/openrouter-alternatives-2026.md` plus updates to the LiteLLM vs OpenRouter, LiteLLM gateway, Google routing, and LLM API pricing articles.
- Source verification: OpenRouter provider-routing and fee documentation; Portkey gateway and guardrail documentation; Cloudflare AI Gateway documentation; SandBase Docs and configured SandBase catalog discovery.
- Validation: production build passed with 1,118 generated pages; title, description, canonical, and all four cluster backlinks were verified in rendered HTML.
- Deployment state: local change; not yet pushed, merged, deployed, indexed, or measured.
- Baseline: no GSC data yet.
- Review dates: 14 and 28 days after deployment.
- Result: pending.
- Next action: create a Blog pull request and add the live URL to the deployment record.

## 100× milestone definition

The temporary weekly reference is 310 Google clicks. Its arithmetic 100× equivalent is 31,000 weekly clicks, but the official baseline will be the first corrected rolling 28-day GSC report. Brand and non-brand growth must be shown separately.

## Repository policy adopted

All future SEO, Blog, GitHub, and third-party distribution operations will be recorded in `sandbase-daily-ops`. Implementation remains in the repository that owns the affected production surface.

## Experiment 4: repair the Blog internal-link graph

- Objective: remove broken legacy paths that prevent crawlers and users from reaching related content, then make broken internal links fail CI.
- Evidence: repository scan found 331 malformed `((//blog/...))` Markdown targets, 20 `/en/blog/...` paths, 18 `/zh-CN/blog/...` paths, and six references to image files that were absent from the repository and production build.
- Action: normalized legacy article links to current root and `/zh-CN/` routes; preserved valid `/blog/evidence/` static asset paths; removed six references to nonexistent editorial images; added a rendered-build internal link checker; attached it to the production build command.
- Implementation: 140 English/Chinese content files, `sandbase-blog/scripts/check-internal-links.mjs`, and `sandbase-blog/package.json`.
- Validation: all 369 known legacy path patterns reduced to zero; Blog tests passed (25 tests); production build passed with 1,118 pages; the new checker inspected 1,117 rendered HTML files and found zero unresolved internal paths.
- Deployment state: local change; not yet pushed, merged, or deployed because GitHub CLI authentication is unavailable.
- Baseline: 369 malformed legacy link targets and six unresolved internal image paths.
- Review dates: immediately after deployment; crawl/index review after 14 and 28 days.
- Result: pending.
- Next action: push the Blog branch, create a pull request, deploy, and verify representative repaired links on the live site.

## GitHub authentication state

- `denial123789`: configured but token invalid.
- `lybing315`: not present in the current GitHub CLI credential store (`gh auth switch` returned `not logged in`).
- Local commits remain possible; push and pull-request creation require `gh auth login -h github.com` for an authorized account.
