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

- `denial123789`: currently authenticated in GitHub CLI with repository access, but intentionally not used because the requested identity is `lybing315`.
- `lybing315`: not present in the current GitHub CLI credential store (`gh auth switch` returned `not logged in`).
- Local commits remain possible. Push and pull-request creation are paused until the user confirms the GitHub device authorization for `lybing315`.

## Experiment 5: OpenAI API alternatives commercial-intent hub

- Objective: capture searches from developers actively evaluating an OpenAI replacement and route qualified readers toward SandBase's unified model and API surface.
- Evidence: the existing corpus covered OpenRouter, LiteLLM, routing, and LLM pricing, but had no page directly targeting “OpenAI API alternatives.” The new page is intentionally separated from “OpenRouter alternatives” to avoid conflating direct model providers, managed aggregators, and self-hosted gateways.
- Action: created a six-option comparison covering Anthropic, Google Gemini, SandBase, OpenRouter, LiteLLM, and Portkey; added an OpenAI SDK migration example, compatibility caveats, production checklist, FAQ, and links to SandBase Docs; added contextual cluster links from the OpenRouter alternatives and LLM API pricing pages.
- Implementation: `sandbase-blog/src/content/en/openai-api-alternatives-2026.md` plus two cluster backlinks.
- Source verification: current official OpenAI API compatibility guidance, Google Gemini OpenAI compatibility documentation, and the SandBase model/first-call documentation in the Docs repository.
- Validation: Blog tests passed (25 tests); production build passed with 1,120 pages; the internal-link checker inspected 1,119 rendered HTML files and found zero unresolved paths; rendered title, description, canonical, H1, structured data, and cluster links were inspected.
- Deployment state: committed locally on `seo/100x-foundation-20260823`; not yet pushed, merged, deployed, indexed, or measured.
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
- Deployment state: committed locally on `seo/100x-foundation-20260823`; not yet pushed or deployed.
- Baseline: live sitemap 334 URLs; pending sitemap 336 valid URLs.
- Review dates: every build; live verification immediately after deployment.
- Result: pending deployment.
- Next action: push and merge, then compare the live sitemap URL count and fetch representative English/Chinese alternates.
