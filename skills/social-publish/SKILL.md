---
name: social-publish
description: Adapt an approved SandBase article or product update into native LinkedIn, X, Discord, and Xiaohongshu content. Use for social distribution planning, channel-specific copy, Xiaohongshu carousels, and social review in sandbase-daily-ops. Do not use for SandBase Blog, Medium, DEV Community, or Zhihu long-form authoring.
---

# Social Publishing

Create native distribution assets from an approved source article, release note, or fact package.

## Scope

Maintain only:

- LinkedIn
- X
- Discord
- Xiaohongshu

Blog, Medium, DEV Community, and Zhihu belong to `sandbase-blog/skills/blog/`.

For the upstream热点、GSC、关键词排名和发布后回流过程, use `../blog-operations/SKILL.md` and `playbooks/blog-content-loop.md`. Start social adaptation only from an approved or live canonical article.

## Required input

Collect:

- approved canonical article or product source
- target channels
- verified facts, links, and availability state
- desired CTA
- approved first-person statements, if any
- final durable cover or screenshot assets

Do not invent metrics, customer usage, quotes, tests, urgency, or personal experience. Do not treat draft Blog claims as approved facts.

## Workflow

1. Read the source and extract a short claims ledger.
2. Confirm channel selection and publication timing.
3. Read `references/publication-matrix.md` for channel purpose and constraints.
4. Draft each selected channel independently using `references/channel-copy-template.md` as structure, not copy to repeat.
5. For Xiaohongshu, also read `references/xiaohongshu-format.md` and build a native evidence-led carousel.
6. Verify facts, links, CTA, tone, image readability, and channel fit.
7. Save outputs under the appropriate Daily Ops package or dated output directory requested by the operator.

## Channel rules

- **LinkedIn:** explain what changed and why it matters to builders. Use short paragraphs and concrete implications.
- **X:** lead with one precise point. Default to one post; use a thread only when the argument genuinely needs sequence.
- **Discord:** tell builders what changed, how to try it, and where to give feedback. Keep it practical.
- **Xiaohongshu:** use a Chinese-native hook and a 4–8 page evidence-led carousel. Do not shrink an overseas launch poster or paste a Blog opening.

## Review

Reject output when it:

- repeats identical copy across channels
- adds a claim absent from the approved source
- uses a temporary image URL
- contains fake UI, logos, metrics, or testimonials
- hides limitations material to the CTA
- uses literal translated Chinese or generic AI-marketing language

Keep the canonical Blog link when useful, but write social content for the channel rather than as a miniature Blog article.
