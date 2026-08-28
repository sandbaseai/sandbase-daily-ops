# SandBase Daily Ops

Daily operating system for SandBase social distribution and community updates. Blog authoring, topic discovery, GSC, ranking, indexing, Medium/DEV/Zhihu long-form adaptations, and publication now live with the site code in [sandbase-blog](https://github.com/sandbaseai/sandbase-blog).

This repository is the **canonical operations ledger** for SandBase growth work. Implementation stays in the owning product repository, while every SEO, content, GitHub, distribution, or outreach action is recorded here with its evidence, deployment state, and review date. See [`playbooks/operations-ledger.md`](playbooks/operations-ledger.md).

## Active public experiment

The current open-source distribution milestone is helping [`sandbaseai/cli`](https://github.com/sandbaseai/cli) reach 100 legitimate GitHub Stars through useful documentation, working installation paths, and relevant ecosystem discovery. Follow the dated [2026-08-28 evidence log](promotion-plan/logs/2026-08-28.md) for the authoritative snapshot, completed actions, guardrails, and next queue. Star the project only if the CLI or its six MCP tools are useful to you.

## Structure

```text
promotion-plan/
  master-context.md          # canonical product, positioning, channel, and SEO context
  daily-audit.md             # repeatable daily/weekly inspection checklist
  logs/                      # dated audit and promotion execution records
playbooks/
  operations-ledger.md       # canonical recording rules and experiment template
  seo-geo-daily.md           # www.sandbase.ai main-site checklist
scripts/
skills/
  social-publish/            # LinkedIn, X, Discord, Xiaohongshu skill
outputs/
  seo-daily-reports/         # dated SEO reports and cross-repository execution ledger
```

## Promotion system

Start every promotion or SEO task with [`promotion-plan/master-context.md`](promotion-plan/master-context.md). It is the canonical cross-channel brief for the website, Docs, Blog, GitHub, API, CLI/MCP, Skills, Harness, audiences, positioning, keyword clusters, and conversion paths. Run [`promotion-plan/daily-audit.md`](promotion-plan/daily-audit.md) and append evidence to `promotion-plan/logs/`; do not silently change product claims or channel roles in an isolated repository.

## Blog operations moved

The canonical copies now live in `sandbase-blog`:

- [`skills/blog/`](https://github.com/sandbaseai/sandbase-blog/tree/main/skills/blog) — the single home for the skill, guides, prompts, references, and helper scripts
- [`scripts/operations/`](https://github.com/sandbaseai/sandbase-blog/tree/main/scripts/operations) — topic, GSC, ranking, indexing, and Medium/DEV helpers
- [`docs/content-operations.md`](https://github.com/sandbaseai/sandbase-blog/blob/main/docs/content-operations.md) — complete operating flow

Make future Blog workflow changes there so implementation and documentation stay in sync.

X/Twitter, LinkedIn, Discord, and Xiaohongshu distribution stays here under `skills/social-publish/`; Blog, Medium, DEV Community, and Zhihu long-form content stay in `sandbase-blog`. There is no cross-repository notification dependency: social work starts from an approved or live canonical Blog URL.
