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
- Deployment state: merged in `sandbase-blog#11` and deployed to production on 2026-08-23 at approximately 01:23 UTC; live URL returned HTTP 200 with the updated title and canonical. Google indexing/measurement remains pending.
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
- Deployment state: merged in `sandbase-blog#11` and deployed to production on 2026-08-23. The corrected workflow has not yet been run with production GSC credentials.
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
- Deployment state: merged in `sandbase-blog#11` and deployed to production on 2026-08-23; the live URL returned HTTP 200, has the intended canonical, and appears in the live sitemap. Indexing and measurement remain pending.
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
- Deployment state: merged in `sandbase-blog#11` and deployed to production on 2026-08-23. The production build and live sitemap passed the new link checks.
- Baseline: 369 malformed legacy link targets and six unresolved internal image paths.
- Review dates: immediately after deployment; crawl/index review after 14 and 28 days.
- Result: pending.
- Next action: push the Blog branch, create a pull request, deploy, and verify representative repaired links on the live site.

## GitHub authentication state

- `denial123789`: currently authenticated in GitHub CLI with repository access, but intentionally not used because the requested identity is `lybing315`.
- `liyangbing`: authenticated through GitHub device authorization and active in GitHub CLI. The browser explicitly displayed `Signed in as liyangbing`; the user confirmed use of the displayed account.
- `lybing315`: was not a GitHub account available in the credential store; it was superseded by the browser-confirmed `liyangbing` identity.
- Blog pull request: https://github.com/sandbaseai/sandbase-blog/pull/11
- Operations-ledger pull request: https://github.com/sandbaseai/sandbase-daily-ops/pull/6
- Current state: both pull requests merged. The Blog deployed successfully through GitHub Actions run `32610190549`; the production GSC run and Google index verification remain pending.

## Experiment 5: OpenAI API alternatives commercial-intent hub

- Objective: capture searches from developers actively evaluating an OpenAI replacement and route qualified readers toward SandBase's unified model and API surface.
- Evidence: the existing corpus covered OpenRouter, LiteLLM, routing, and LLM pricing, but had no page directly targeting “OpenAI API alternatives.” The new page is intentionally separated from “OpenRouter alternatives” to avoid conflating direct model providers, managed aggregators, and self-hosted gateways.
- Action: created a six-option comparison covering Anthropic, Google Gemini, SandBase, OpenRouter, LiteLLM, and Portkey; added an OpenAI SDK migration example, compatibility caveats, production checklist, FAQ, and links to SandBase Docs; added contextual cluster links from the OpenRouter alternatives and LLM API pricing pages.
- Implementation: `sandbase-blog/src/content/en/openai-api-alternatives-2026.md` plus two cluster backlinks.
- Source verification: current official OpenAI API compatibility guidance, Google Gemini OpenAI compatibility documentation, and the SandBase model/first-call documentation in the Docs repository.
- Validation: Blog tests passed (25 tests); production build passed with 1,120 pages; the internal-link checker inspected 1,119 rendered HTML files and found zero unresolved paths; rendered title, description, canonical, H1, structured data, and cluster links were inspected.
- Deployment state: merged in `sandbase-blog#11` and deployed to production on 2026-08-23; the live URL returned HTTP 200, has the intended canonical, and appears in the live sitemap. Indexing and measurement remain pending.
- Baseline: no GSC data yet.
- Review dates: 14 and 28 days after deployment.
- Result: pending.
- Next action: push the Blog branch after `lybing315` authorization, create a pull request, deploy, submit the URL for crawling, and track non-brand impressions/clicks separately.

## Experiment 6: sitemap and hreflang release gate

- Objective: prevent deploys that advertise nonexistent, duplicated, or unflattened URLs to Google through the sitemap and hreflang graph.
- Evidence: the live `robots.txt` and sitemap endpoints both return HTTP 200; the live sitemap currently contains 334 URLs. The pending build contains 336 URLs after adding the two English commercial-intent hubs. The existing build gate checked rendered links but did not verify sitemap targets.
- Action: extended the rendered-build link checker to require `sitemap-0.xml`, validate every same-origin `<loc>` and hreflang target against generated files, reject duplicate `<loc>` entries, and reject leaked `/en/` URLs because English is served at the root.
- Implementation: `sandbase-blog/scripts/check-internal-links.mjs`.
- Validation: production build passed with 1,120 pages; the release gate inspected 1,119 HTML files, 336 sitemap URLs, and 668 hreflang targets with zero unresolved paths, duplicates, or default-locale leaks.
- Deployment state: merged in `sandbase-blog#11` and active in production. Live sitemap verification found 336 URLs, both new hubs, and zero pagination URLs.
- Baseline: live sitemap 334 URLs; pending sitemap 336 valid URLs.
- Review dates: every build; live verification immediately after deployment.
- Result: release gate active; Google crawl effects pending.
- Next action: push and merge, then compare the live sitemap URL count and fetch representative English/Chinese alternates.

## Experiment 7: remove duplicate pagination pages from the index

- Objective: keep Google focused on article and language-homepage canonicals instead of 36 repetitive archive-pagination pages and the 404 document.
- Evidence: rendered metadata audit found 373 indexable HTML pages but only 336 sitemap URLs. The 37-page gap consisted of `/2/` through `/19/`, their `/zh-CN/` counterparts, and `/404/`. Pagination was excluded from the sitemap but did not carry the `noindex, follow` directive claimed by the repository's technical SEO comments.
- Action: added `noindex, follow` to pagination pages after page one and to the 404 page; expanded the sitemap release gate so every indexable same-origin canonical must appear in the sitemap and every noindex canonical must stay out.
- Implementation: `sandbase-blog/src/pages/[locale]/[...page].astro`, `sandbase-blog/src/pages/404.astro`, and `sandbase-blog/scripts/check-internal-links.mjs`.
- Validation: production build passed; rendered audit now reports exactly 336 indexable HTML pages and 336 sitemap URLs, with 783 supporting/noindex HTML pages; representative English pagination, Chinese pagination, and 404 output all contain `noindex, follow`.
- Deployment state: merged in `sandbase-blog#11` and active in production. `/2/` and `/zh-CN/19/` both returned HTTP 200 with `noindex, follow`; neither pagination pattern appears in the live sitemap.
- Baseline: 37 unintended indexable pages outside the sitemap.
- Review dates: immediately after deployment; GSC “Crawled - currently not indexed” and duplicate-page trends after 14 and 28 days.
- Result: technical fix live; GSC de-indexing trend pending.
- Next action: deploy, request recrawl of representative pagination URLs, and verify Google recognizes the directives.

## Experiment 8: indexable metadata integrity gate

- Objective: prevent indexable pages from shipping with missing or duplicated search-result identity signals.
- Evidence: the rendered audit found no current duplicate titles or canonicals among indexable pages, but this invariant was not enforced in CI. The repository contains more than 1,100 rendered HTML files, so manual review cannot reliably prevent regressions.
- Action: extended the SEO release checker to require an H1, title, description, and canonical on every indexable same-origin HTML page and to reject duplicate indexable titles, descriptions, or canonicals.
- Implementation: `sandbase-blog/scripts/check-internal-links.mjs`.
- Validation: the gate passed across 1,119 HTML files, 336 indexable/sitemap URLs, and 668 hreflang targets with unique indexable metadata and zero unresolved paths.
- Deployment state: merged in `sandbase-blog#11` and enforced in the production Cloudflare build workflow.
- Baseline: metadata integrity was manually auditable but not release-enforced.
- Review dates: every production build.
- Result: release gate active.
- Next action: deploy and keep the check mandatory in the Cloudflare build workflow.

## Production deployment record

- Blog pull request: https://github.com/sandbaseai/sandbase-blog/pull/11 — merged at 2026-08-23 01:22:13 UTC, merge commit `7957a7cfb9d7b566cfd0bedec4504655c8536850`.
- Operations pull request: https://github.com/sandbaseai/sandbase-daily-ops/pull/6 — merged at 2026-08-23 01:22:22 UTC, merge commit `9a1263f276e5b33ca1b09dab9d92857bf7dc6de3`.
- Deployment workflow: https://github.com/sandbaseai/sandbase-blog/actions/runs/32610190549 — completed successfully in 1m12s.
- Production verification:
  - `https://blog.sandbase.ai/openrouter-alternatives-2026/`: HTTP 200, correct title and canonical.
  - `https://blog.sandbase.ai/openai-api-alternatives-2026/`: HTTP 200, correct title and canonical.
  - `https://blog.sandbase.ai/dify-ai-platform-explained-2026/`: HTTP 200 with the updated pricing/self-hosting/alternatives title and correct canonical.
  - `https://blog.sandbase.ai/2/` and `/zh-CN/19/`: HTTP 200 with `noindex, follow`.
  - live sitemap: 336 URLs, both new hubs present, zero numeric pagination URLs.
- Remaining measurement work: run the corrected production GSC job, freeze the official rolling 28-day baseline, then review CTR, position, index coverage, and non-brand clicks at 14 and 28 days.
