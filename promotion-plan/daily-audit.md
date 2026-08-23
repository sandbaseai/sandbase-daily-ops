# SandBase Daily Promotion Audit

Use this checklist after reading [`master-context.md`](master-context.md). Record results in `logs/YYYY-MM-DD.md`; link to exact workflows, commits, PRs, URLs, and metric artifacts.

## Daily: health and opportunity

### 1. Cross-surface availability

- [ ] Website, Docs, Store, Blog, GitHub organization, Skills, CLI, and Harness canonical URLs return the expected status.
- [ ] Latest production workflows succeeded; failures have an owner and next action.
- [ ] No newly promoted URL resolves through an unintended redirect, stale host, 404, or 5xx.

### 2. Google Search Console

- [ ] Record comparable non-brand clicks, impressions, CTR, and average position.
- [ ] Identify pages with meaningful impressions, CTR below expectation, and average position 5–20.
- [ ] Check query-to-page fit before editing title or description.
- [ ] Check new high-value URLs for sitemap inclusion and indexing evidence.
- [ ] Do not interpret normal daily GSC delay as a deployment failure.

### 3. Website and Docs

- [ ] Treat `sandbase-monorepo` as PR-only: do not push directly to main and do not trigger production deployment; record the PR for operator review.
- [ ] Homepage and main capability pages preserve the master positioning and one clear CTA.
- [ ] Quickstart, authentication, current API base URL, model/API selection, streaming, async jobs, and errors are reachable.
- [ ] Claims such as model count, API count, supported clients, and pricing are verified before reuse.
- [ ] New product routes have canonical, description, structured data, sitemap inclusion, and useful internal links.

### 4. Blog

- [ ] New or changed articles satisfy `sandbase-blog/skills/blog/SKILL.md`.
- [ ] EN and native ZH pair, author, durable cover, screenshots, sources, index, and review report are complete.
- [ ] Tests/check/build and deployment succeeded; live routes return 200 with reciprocal hreflang.
- [ ] Existing high-impression pages are improved before publishing overlapping articles.

### 5. GitHub and tools

- [ ] Core repositories have accurate description, homepage, topics, first-screen positioning, install command, license, and release link.
- [ ] Skills count, supported-client count, release version, and API claims match current sources.
- [ ] Cross-links are contextual and do not crowd out each repository's own job.
- [ ] Issues/discussions/releases reveal recurring questions worth a Docs or Blog response.

### 6. Distribution

- [ ] Only approved live canonical content enters DEV, Medium, Zhihu, social, or community queues.
- [ ] Adaptation adds channel-specific value and preserves canonical attribution.
- [ ] No unsolicited mass posting, fabricated community participation, or unreviewed third-party claims.

### 7. Record and prioritize

- [ ] Append evidence, action, owner, deployment state, metric baseline, and 14/28-day review dates to today's log.
- [ ] Update `master-context.md` if a canonical fact changed.
- [ ] Choose the next action by expected non-brand impact, evidence strength, effort, and reversibility.

## Weekly: system integrity

- [ ] Crawl canonical surfaces and validate internal/external links, canonical, hreflang, sitemap, robots, and structured data.
- [ ] Compare keyword clusters for cannibalization, orphan pages, and missing decision-stage content.
- [ ] Review GitHub traffic/stars/clones, Blog referrals, first-call funnel data, and install/release health where available.
- [ ] Audit private/public ownership boundaries and make sure no secret or private context entered the public ledger.
- [ ] Confirm no automation, script, or operator run bypassed the `sandbase-monorepo` PR-only/no-deploy boundary.
- [ ] Reconcile website, Docs, Blog, organization profile, and core README wording against the master context.

## Monthly: outcome review

- [ ] Compare the rolling 28-day non-brand click window with the frozen 119-click baseline and previous comparable window.
- [ ] Attribute movement by page, query, cluster, channel, and release window where evidence permits.
- [ ] Keep, revise, or stop experiments based on evidence; archive stale assumptions.
- [ ] Refresh the 100× gap and next-month portfolio without lowering the original target.

## Log template

```markdown
# Promotion Audit — YYYY-MM-DD

## Snapshot
- GSC window and metrics:
- Availability/deployment:
- GitHub/tool health:

## Findings
1. Finding, evidence, impact.

## Actions shipped
1. Action, owning repo, PR/commit, deployment, verification.

## Decisions and context changes
- None, or exact master-context change and evidence.

## Next queue
1. Action, owner, success signal, review date.
```
