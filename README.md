# SandBase Daily Ops

Daily operating system for SandBase social distribution and community updates. Blog authoring, topic discovery, GSC, ranking, indexing, Medium/DEV/Zhihu long-form adaptations, and publication now live with the site code in [sandbase-blog](https://github.com/sandbaseai/sandbase-blog).

This repository is the **canonical operations ledger** for SandBase growth work. Implementation stays in the owning product repository, while every SEO, content, GitHub, distribution, or outreach action is recorded here with its evidence, deployment state, and review date. See [`playbooks/operations-ledger.md`](playbooks/operations-ledger.md).

## Structure

```text
playbooks/
  operations-ledger.md       # canonical recording rules and experiment template
  seo-geo-daily.md           # www.sandbase.ai main-site checklist
scripts/
skills/
  social-publish/            # LinkedIn, X, Discord, Xiaohongshu skill
outputs/
  seo-daily-reports/         # dated SEO reports and cross-repository execution ledger
```

## Blog operations moved

The canonical copies now live in `sandbase-blog`:

- [`skills/blog/`](https://github.com/sandbaseai/sandbase-blog/tree/main/skills/blog) — the single home for the skill, guides, prompts, references, and helper scripts
- [`scripts/operations/`](https://github.com/sandbaseai/sandbase-blog/tree/main/scripts/operations) — topic, GSC, ranking, indexing, and Medium/DEV helpers
- [`docs/content-operations.md`](https://github.com/sandbaseai/sandbase-blog/blob/main/docs/content-operations.md) — complete operating flow

Make future Blog workflow changes there so implementation and documentation stay in sync.

X/Twitter, LinkedIn, Discord, and Xiaohongshu distribution stays here under `skills/social-publish/`; Blog, Medium, DEV Community, and Zhihu long-form content stay in `sandbase-blog`. There is no cross-repository notification dependency: social work starts from an approved or live canonical Blog URL.
