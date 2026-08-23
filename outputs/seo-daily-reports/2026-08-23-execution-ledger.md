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

## GSC baseline run attempt

- Workflow run: https://github.com/sandbaseai/sandbase-blog/actions/runs/32610327525
- Trigger: manual `Blog operations` run with `task=gsc` on `main`, immediately after the production deployment.
- Result: failed at the credential preflight before any Search Console request was made.
- Root cause: the `sandbase-blog` repository does not have the required `GOOGLE_SERVICE_ACCOUNT_JSON` Actions secret configured.
- Local credential check: no matching GSC/service-account environment variable or credential file was found in the current workspace/configuration paths; no secret content was read or exposed.
- Required remediation: add a Google service-account JSON credential as the repository Actions secret `GOOGLE_SERVICE_ACCOUNT_JSON`, and grant that service-account email read access to the relevant Search Console property.
- Verification after remediation: rerun workflow `32610327525`'s workflow definition with `task=gsc`, download the generated artifact, freeze its rolling 28-day totals as the official baseline, and copy the report into this ledger repository.
- Measurement status: blocked on credential configuration; the 100× outcome is not yet measurable from the corrected job.

## Experiment 9: canonical third-party long-form distribution readiness

- Objective: earn qualified referral traffic and external discovery from DEV Community and Medium without creating duplicate canonical competition for the SandBase Blog.
- Evidence: `sandbase-blog` already contained a cross-posting client with DEV/Medium canonical support, but its dry-run mode incorrectly required live API credentials before it could preview a payload. No `DEVTO_API_KEY`, `MEDIUM_TOKEN`, or `MEDIUM_AUTHOR_ID` is configured in the current environment.
- Action: moved credential checks behind dry-run payload generation while keeping credentials mandatory for real draft/live API calls; generated DEV and Medium previews for the production OpenAI API alternatives hub.
- Implementation: `sandbase-blog/scripts/operations/publish_long_form.py`, merged through https://github.com/sandbaseai/sandbase-blog/pull/12.
- Validation: Python compilation passed; DEV preview selected four tags, draft state, 9,201-character body, and canonical `https://blog.sandbase.ai/openai-api-alternatives-2026/`; Medium preview selected three tags, draft state, the same canonical, and the same body.
- Deployment state: merged to `sandbase-blog` main on 2026-08-23. No third-party draft or public post was created because platform credentials are not configured.
- Baseline: zero third-party placements for the two new alternatives hubs in this execution cycle.
- Review dates: immediately after credential setup and publication, then referral/backlink review after 14 and 28 days.
- Result: publishing path validated; external distribution pending credentials and account authorization.
- Next action: configure DEV/Medium credentials for an approved SandBase publishing identity, create drafts first, verify canonical tags on the rendered drafts, then publish on a staggered schedule.

## Continuous execution schedule

- Automation: `SandBase SEO 100× 日更` (`sandbase-seo-100`).
- Status: active.
- Cadence: daily at 09:30 in the user's local timezone.
- Scope: inspect Blog, operations ledger, production site, GitHub Actions, GSC/index evidence, and the next highest-impact SEO/content/GitHub/distribution opportunity; implement and deploy safe changes; record every operation here.
- Measurement guardrail: the automation must not claim 100× without corrected GSC evidence and must freeze the first successful rolling 28-day report as the official baseline.
- Credential behavior: retry the GSC workflow when `GOOGLE_SERVICE_ACCOUNT_JSON` becomes available, while continuing other executable work if it remains absent.

## Experiment 10: unified AI API commercial-intent hub

- Objective: capture “unified AI API,” “one API for LLM/image/video,” and multimodal API architecture intent that directly matches SandBase's differentiated model-plus-tool surface.
- Evidence: the production sitemap contained 336 indexable URLs but no dedicated page for this topic. The OpenAI/OpenRouter alternatives hubs and image/video API comparisons discussed pieces of the problem without owning the unified intent.
- Action: created an architecture-first comparison of SandBase, fal, Replicate, and OpenRouter; documented OpenAI-compatible LLM calls versus asynchronous media jobs, webhooks, normalization boundaries, selection criteria, and production checks; added contextual links from four relevant cluster pages; corrected an existing statement that inaccurately described video generation as OpenAI-compatible.
- Implementation: `sandbase-blog/src/content/en/unified-ai-api-llm-image-video-2026.md` plus four cluster pages, merged through https://github.com/sandbaseai/sandbase-blog/pull/13.
- Source verification: current official fal Model API documentation, Replicate official-model documentation, OpenRouter model/image API documentation, and the SandBase Docs repository.
- Validation: Blog tests passed (25 tests); production build passed with 1,124 pages; the release gate inspected 1,123 HTML files, 337 sitemap URLs, and 668 hreflang targets with unique indexable metadata and zero unresolved paths; rendered title, description, canonical, H1, JSON-LD, and backlinks were inspected.
- Deployment state: merged to `sandbase-blog` main at 2026-08-23 01:35:58 UTC and deployed successfully through https://github.com/sandbaseai/sandbase-blog/actions/runs/32610752608. The live URL returned HTTP 200 with the intended title/canonical and appears once in the 337-URL production sitemap.
- Baseline: no GSC data yet; official baseline remains blocked on `GOOGLE_SERVICE_ACCOUNT_JSON`.
- Review dates: 14 and 28 days after production deployment.
- Result: deployed; indexing and GSC measurement pending.
- Next action: prepare canonical DEV/Medium drafts when credentials are available, and review index/query performance after 14 and 28 days.

## Experiment 11: GitHub repository discovery metadata

- Objective: improve branded and non-brand discovery of SandBase's public developer assets in GitHub search and external search results.
- Evidence: nine active public repositories had no description, homepage, or topics even though their READMEs defined clear search-relevant use cases. This left GitHub result cards without a useful summary and prevented topic-based discovery.
- Action: reviewed each repository README, then added a specific English description, the most relevant live homepage, and five or six focused repository topics.
- Repositories updated:
  - `sandbase-daily-ops`: SandBase SEO, developer marketing, content marketing, and growth operations.
  - `dsh-kit`: 102 Cordis plugins for DeepSeek Harness, including search, data, multimodal AI, and MCP.
  - `dsh101`: bilingual DeepSeek Harness tutorial; homepage set to `https://dsh101.com`.
  - `sandbase-agents`: reusable SandBase Agent Services registry and delivery standard.
  - `global-ai-cold-start`: public 30-day developer-brand growth case study.
  - `awesome-agent-runtime`: curated 500-project production agent-runtime landscape.
  - `sandbase-lab-sitecheck`: SandBase-powered AI website personality and comprehension test; homepage set to `https://lab-sitecheck.sandbase.ai`.
  - `agent-sandbox-cookbook`: runnable sandbox compatibility examples and field notes.
  - `awesome-native-agent-platforms`: curated production agent infrastructure list.
- Validation: queried all nine repositories through the GitHub API after mutation and confirmed that every repository now returns the intended description, homepage, and topic set. All are active and public.
- Baseline: 0 of these 9 repositories had a description, homepage, or topic before this pass; 9 of 9 now have all three metadata surfaces populated.
- Review dates: GitHub referral/search impressions after 14 and 28 days; repository traffic and clone trends where GitHub Insights access permits.
- Result: deployed directly to GitHub repository metadata on 2026-08-23.
- Next action: audit the organization profile and README first-screen copy for consistent SandBase product positioning and contextual links to the unified LLM/image/video API surface.

## Experiment 12: GitHub organization unified API positioning

- Objective: make the SandBase GitHub organization homepage immediately relevant to developers searching for LLM, image, video, and unified AI APIs without discarding the established agent-runtime positioning.
- Evidence: the organization profile led with “safe runtime layer for enterprise AI agents” and had no first-screen mention of image API, video API, or the unified multimodal API. Its docs and blog navigation also used less direct URLs than the current live surfaces.
- Action: changed the first-screen value proposition to “One API for LLMs, image generation, video generation, tools, and production AI agents”; added a dedicated modality section covering the OpenAI-compatible LLM endpoint, Flux image jobs, Kling video jobs, and data/tool APIs; added direct CTAs for API keys, API reference, model/API catalog, and the unified AI API comparison hub.
- Implementation: merged https://github.com/sandbaseai/.github/pull/22 at 2026-08-23 01:44:03 UTC, merge commit `5c13b242200bb235c4056b7d250a412c5d04f240`.
- Link validation: website, live docs under `https://www.sandbase.ai/docs/`, console API-key page, Blog homepage, and unified API hub all returned HTTP 200 before merge.
- Additional repair: `docs.sandbase.ai` did not resolve during validation, so no new links were pointed there. The `sandbase-docs` repository homepage was changed from that non-resolving host to `https://www.sandbase.ai/docs/` and verified through the GitHub API.
- Baseline: zero first-screen mentions of LLM/image/video API modalities; after deployment all three modalities plus tools and agent runtime appear in the organization profile's opening section.
- Review dates: GitHub profile/referral traffic and branded query composition after 14 and 28 days.
- Result: deployed to the public GitHub organization profile.
- Next action: audit high-traffic repository README first screens for consistent product-category links, then repair or intentionally redirect the `docs.sandbase.ai` DNS surface.

## Experiment 13: official GSC baseline and 100× success criterion

- Objective: replace unmeasured growth claims with a reproducible Google Search Console baseline and an explicit 100× target.
- Action: after `GOOGLE_SERVICE_ACCOUNT_JSON` was configured for `sandbase-blog`, reran the corrected GSC workflow and archived both the generated report and a concise baseline definition in this repository.
- Workflow: https://github.com/sandbaseai/sandbase-blog/actions/runs/32611196712 completed successfully in 1m22s, including credential preflight, Search Console collection, and artifact upload.
- Baseline window: rolling 28 days ending with the standard two-day GSC delay, frozen on 2026-08-23.
- Primary metric: non-brand Google clicks = 119; 100× target = 11,900 in a comparable rolling 28-day window.
- Supporting metrics: Blog clicks = 168 (100× reference 16,800); whole-site clicks = 515 (100× reference 51,500); whole-site impressions = 44,665; Blog impressions = 5,578; non-brand impressions = 9,131 at 1.3% CTR.
- Index evidence: 7 of 10 tracked new articles were indexed; 232 current-sitemap Blog pages had GSC data.
- Artifacts: `outputs/seo-daily-reports/2026-08-23-gsc-100x-baseline.md` and `outputs/seo-daily-reports/2026-08-23-gsc-28d-baseline-raw.md`.
- Result: measurement blocker cleared and the 100× denominator frozen.
- Next action: optimize the position-5–20/low-CTR queue, starting with the three pages responsible for 1,006 impressions and only 3 clicks in the baseline window; rerun equivalent reports at 14 and 28 days.

## Experiment 14: high-authority GitHub README referral network

- Objective: connect SandBase's strongest GitHub discovery surfaces to the live unified LLM/image/video API conversion path.
- Action: added concise, project-contextual first-screen links to the live API quickstart, model/API catalog, and unified AI API comparison from Harness, Skills, and CLI READMEs.
- Deployments: https://github.com/sandbaseai/sandbase-harness/pull/71, https://github.com/sandbaseai/sandbase-skills/pull/57, and https://github.com/sandbaseai/cli/pull/26, all merged on 2026-08-23.
- Validation: Harness quality/test/build and PR-policy checks passed; CLI validation passed; all target URLs returned HTTP 200 before merge.
- Result: deployed across the 629-star Harness repository, 42-star Skills repository, and 32-star CLI repository.
- Next action: monitor GitHub referral traffic to the API documentation and unified API hub at 14 and 28 days.

## Experiment 15: Blog Skill compliance correction

- Trigger: operator review identified that the first unified AI API article release did not follow `sandbase-blog/skills/blog/SKILL.md` and omitted Chinese.
- Audit finding: confirmed. The initial release had only English, used `SandBase Team` instead of the API author persona, reused an unrelated LiteLLM/OpenRouter cover, omitted the content index, lacked the required review/evidence package, and had no embedded evidence screenshots.
- Corrective action: reread the complete Blog Skill and its article, format, writing, visual, quality, screenshot, and reviewer references; rewrote English; created a native Chinese counterpart under the same slug; changed the author to Sophie Lin; added three inspected evidence screenshots with captions and dated sources; added a dedicated cover; updated the content index; and created an approved review package.
- DataForSEO evidence: operator approved billable DataForSEO calls through the SandBase API. Google US evidence collected on 2026-08-23 found monthly search-volume estimates of 30 for `unified AI API`, 20 for `unified LLM API`, and 10 for `multimodal AI API`; the sampled SERP supported a commercial-comparison and technical-architecture angle. Metrics remain internal decision evidence, not a traffic promise.
- Visual QA: rejected one fal screenshot because a cookie overlay obscured it; rejected the first generated cover because it was 3:2 and too sparse. Neither rejected asset is referenced. The final cover is a visually inspected 1600×900 deterministic composition at `https://static.sandbase.ai/blog/covers-v2/unified-ai-api-llm-image-video-2026-00849aa8177f.webp`, shared by EN and ZH.
- Tool repair: fixed `skills/blog/scripts/generate_blog_cover_url.py` to request PNG from the current `openai/gpt-image-2` route, then use the documented deterministic composition and WebP upload flow.
- Validation: Node 24.19.0; 25 tests passed; Astro check reported 0 errors and 0 warnings; production build generated 1,129 pages; release gate verified 338 sitemap URLs, 672 hreflang targets, unique indexable metadata, and zero unresolved paths.
- Deployment: merged https://github.com/sandbaseai/sandbase-blog/pull/14 at 2026-08-23 02:10:07 UTC, merge commit `c27bb01799d8cb8753b69360ce8500f98e15bb09`; Cloudflare deployment https://github.com/sandbaseai/sandbase-blog/actions/runs/32612176132 succeeded in 1m22s.
- Production verification: English and Chinese routes returned HTTP 200 with distinct correct titles/H1/canonicals, reciprocal `en`/`zh-CN` hreflang, shared dedicated cover, and sitemap inclusion.
- Result: the identified publishing defect is corrected in production and preserved in the public audit trail.
- Process change: all future Blog content work must begin by reading `skills/blog/SKILL.md`; publication is blocked until a locale pair, content-index entry, durable dedicated cover, evidence visuals, review report, and full repository checks are present, unless the Skill explicitly permits an exception.

## Experiment 16: unified promotion context and alternatives correction

- Objective: consolidate website, Docs, Blog, GitHub, API, Skills, CLI/MCP, Harness, positioning, audiences, SEO clusters, conversion paths, claim boundaries, and inspection rules into one reusable promotion context.
- Action: created `promotion-plan/master-context.md`, `promotion-plan/daily-audit.md`, and the dated `promotion-plan/logs/2026-08-23.md`; updated the repository entry point so every future promotion task starts from the same context and records evidence back into the same folder.
- Portfolio verification: canonical website, Docs, Store, Blog, and GitHub organization returned HTTP 200. GitHub repository metadata and first-screen README positioning were reviewed for the core Docs, Skills, and Harness surfaces. The audit records `docs.sandbase.ai` as non-canonical/unresolved and routes promotion to `https://www.sandbase.ai/docs/`.
- Blog correction: operator review confirmed that `openai-api-alternatives-2026` and `openrouter-alternatives-2026` had the same compliance defects as the earlier unified API article. Both now have native Chinese counterparts, Sophie Lin authorship, independent covers, three evidence screenshots, content-index entries, DataForSEO evidence, and approved review reports.
- SEO evidence: Google US estimates collected through SandBase API on 2026-08-23 were 320 for `OpenAI API alternatives`, 390 for `OpenAI compatible API`, 720 for singular/plural `OpenRouter alternative(s)`, and 20 for `self hosted OpenRouter`. The evidence remains internal planning input.
- Validation: 25 Blog tests passed; Astro check reported 0 errors/0 warnings; build produced 1,133 pages, 340 sitemap URLs, 680 hreflang targets, and zero unresolved paths.
- Deployment: [sandbase-blog PR #15](https://github.com/sandbaseai/sandbase-blog/pull/15) merged as `e10134dca5b066bd0c757ef14995b9bd05bb1356`; [Cloudflare run 32612924193](https://github.com/sandbaseai/sandbase-blog/actions/runs/32612924193) succeeded.
- Production verification: all four English/Chinese alternatives routes returned HTTP 200 with Sophie Lin, reciprocal hreflang, and their correct dedicated cover.
- Result: deployed; shared promotion context and daily inspection system are ready for ongoing use.
- Review dates: 2026-09-06 and 2026-09-20 for page/query/indexing movement.
- Next action: repair stale Docs README links, then resume the three-page GSC low-CTR optimization queue.
