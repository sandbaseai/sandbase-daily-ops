# SandBase Blog Format

Use this reference when the API launch package should include a real SandBase Blog draft.

Source of truth inspected from:

- `/Users/liyb/Documents/Codex/sandbase-monorepo/sandbase-blog/scripts/ai-content-generator/WRITING-METHOD.md`
- `/Users/liyb/Documents/Codex/sandbase-monorepo/sandbase-blog/src/content.config.ts`
- `/Users/liyb/Documents/Codex/sandbase-monorepo/sandbase-blog/src/utils/categories.ts`

## Content Locations

```text
sandbase-blog/src/content/en/<slug>.md
sandbase-blog/src/content/zh-CN/<slug>.md
```

English and Chinese posts use the same slug.

## Frontmatter Schema

```yaml
---
title: "<title>"
slug: <lowercase-hyphen-slug>
date: YYYY-MM-DD
updatedDate: YYYY-MM-DD
author: SandBase Team
tags:
  - sandbase
  - ai-agent
  - agent-service
  - developer-tools
category: product-updates
description: "<10-300 chars, include primary keyword>"
language: en
image: <optional cover URL>
imageAlt: "<optional image alt>"
draft: false
---
```

Required or expected fields:

- `title`: 1-200 chars.
- `slug`: lowercase letters, numbers, hyphens only.
- `date`: valid date.
- `updatedDate`: set when publishing or materially updating.
- `author`: use `SandBase Team`.
- `tags`: 4-6 focused SEO tags.
- `category`: one valid category slug.
- `description`: 10-300 chars.
- `language`: `en` or `zh-CN`.
- `image` and `imageAlt`: optional but preferred. For API launches, use the public URL from `cover-url.json`.
- `draft`: optional; default is false.

Valid categories:

```text
model-introduction
model-comparison
best-of
agent-best-picks
agent-use-cases
agent-daily-news
tutorials
product-updates
industry-insights
pricing-guides
developer-tools
```

For API launches, prefer `product-updates`. Use `developer-tools` for a technical guide and `agent-use-cases` for a workflow/story-led post.

## Writing Workflow

Use the direct-writing workflow. Do not call a text-generation API for long blog copy.

```text
topic -> dedupe -> research -> write EN -> rewrite ZH -> SEO check -> generate one reusable cover URL -> render check -> update index
```

Before writing into the real blog repo, check:

```text
sandbase-blog/scripts/ai-content-generator/content-index.md
```

Avoid repeating existing titles or slugs. If the topic overlaps, choose a sharper angle and add internal links to related posts.

## Required Blog Strategy Per Product

Every product or API launch should produce three SandBase Blog articles: one owned product landing article and two outward-facing SEO-oriented articles.

### Article 1: Owned Product Landing Article

Purpose:

- Give the SandBase ecosystem a durable product page for the new capability.
- Explain what the provider contributes, what SandBase contributes, and what a builder should do next.
- Convert readers who arrive through the comparison and Top N discovery articles.

Recommended title patterns:

```text
<Product> on SandBase: <Capability> for AI Agents
Connect <Product> to Agent Workflows with SandBase
<Product> Is Available Through the SandBase Ecosystem
```

Required structure:

```markdown
# <Product> on SandBase

## What is available

## What <Provider> provides

## What SandBase adds

## First workflows to build

## How to get started
```

This article is the owned conversion page. It may be product-led, but it must still use accurate ecosystem language: the provider supplies the raw capability; SandBase makes it discoverable, composable, and reusable by agents.

### Article 2: Same-Category Comparison

Purpose:

- Capture search demand from people comparing tools.
- Make the current product's advantages concrete.
- Keep credibility by naming where competitors are still better.

Recommended title patterns:

```text
<Product> vs <Competitor>: Which <Category> Tool Should Builders Use in 2026?
<Product> vs <Competitor A> vs <Competitor B>: <Category> Comparison for AI Agents
<Product> Alternatives: How It Compares with <Competitor A>, <Competitor B>, and <Competitor C>
```

Recommended slug patterns:

```text
<product>-vs-<competitor>-2026
<product>-vs-<competitor-a>-vs-<competitor-b>-2026
<product>-alternatives-<category>-2026
```

Suggested category:

```text
model-comparison
developer-tools
agent-use-cases
```

Use `model-comparison` only for model/provider comparisons. For API and tool capabilities, prefer `developer-tools` or `agent-use-cases`.

Required structure:

```markdown
# <Product> vs <Competitors>: <Category> Comparison for 2026

> **TL;DR** — <Direct verdict. Say where Product wins and when another tool is better.>

## Why this comparison matters

## Quick comparison table

| Tool | Best for | Strength | Trade-off |
|---|---|---|---|

## What <Product> does best

## Where competitors are still better

## How to choose

## FAQ

## Bottom line
```

Writing rule:

Do not write a fake neutral comparison that obviously sells SandBase or the current product. The product advantage should come from concrete criteria: latency, output quality, workflow fit, integration, state, artifacts, pricing, reliability, or developer experience.

### Article 3: 2026 Top N Roundup

Purpose:

- Capture broad category search demand.
- Place the product inside a market map.
- Build topical authority around the capability category.

Recommended title patterns:

```text
Top <N> <Category> Tools for AI Agents in 2026
Best <Category> APIs for Agent Workflows in 2026
Top <N> <Category> Platforms for Builders and FDEs in 2026
```

Recommended slug patterns:

```text
best-<category>-tools-ai-agents-2026
top-<n>-<category>-apis-agent-workflows-2026
best-<category>-platforms-builders-fdes-2026
```

Suggested category:

```text
best-of
agent-best-picks
developer-tools
```

Required structure:

```markdown
# Top <N> <Category> Tools for AI Agents in 2026

> **TL;DR** — <Who should pick what. Mention Product's best-fit scenario.>

## How we evaluated these tools

## Quick ranking table

| Rank | Tool | Best for | Why it stands out |
|---|---|---|---|

## 1. <Product>

## 2. <Competitor>

## 3. <Competitor>

## How to choose the right tool

## FAQ

## Bottom line
```

Writing rule:

The current product can rank #1 only when the positioning is defensible. Otherwise, rank it where credible and make its best-fit scenario explicit. Trust beats forced ranking.

## Launch Blog Structure

Use this only when the user asks for a short launch announcement. The default product SEO package should still include the two required articles above.

For public API launch posts, use a concise version of the site style:

```markdown
# <API> on SandBase.ai

> **TL;DR** — <2-4 direct bullets or one tight paragraph.>

<Hook: what changed, why builders should care.>

## Why this matters

## What <Provider> provides

## What SandBase adds

## First use cases

| Use case | What the agent does | Output |
|---|---|---|

## From API to Agent Service

## FAQ

## What comes next
```

For shorter launch posts, 600-1000 English words is acceptable. For SEO-led posts, target 1500+ English words or 2000+ Chinese characters.

## Cover URL

For launch packages, generate the cover once and reuse the same public image URL across:

- English blog post frontmatter
- Chinese blog post frontmatter
- LinkedIn
- X / Twitter
- Discord
- `launch-pack.md`

Use:

```bash
python skills/api-launch-publish/scripts/generate_blog_cover_url.py \
  --title "<API> on SandBase.ai" \
  --description "<short launch description>" \
  --category product-updates \
  --article-type launch \
  --out-json outputs/<api-slug>-launch/cover-url.json \
  --update-markdown outputs/<api-slug>-launch/blog/en/<slug>.md \
  --update-markdown outputs/<api-slug>-launch/blog/zh-CN/<slug>.md
```

The generated `cover-url.json` is the source of truth for all channel images unless the user asks for channel-specific mobile variants.

## Chinese Version

The Chinese post is a native rewrite, not a sentence-by-sentence translation.

Rules:

- Keep product and technical terms in English when natural: SandBase, API, SDK, Agent Service, runtime, artifact.
- Use Chinese punctuation.
- Put spaces between Chinese and English terms.
- Rewrite long English structures into short Chinese sentences.
- Avoid translation tone such as repeated passive voice, nested modifiers, and "进行了一个".

## SEO Checklist

Every blog-ready output should satisfy:

- Primary keyword in title, first paragraph, at least one H2, and description.
- 1 comparison or use-case table.
- 3-5 FAQ questions for SEO snippets.
- At least 1 internal link suggestion.
- At least 2 external authoritative source suggestions if the post makes factual third-party claims.
- Clear product point of view: provider supplies raw capability; SandBase helps agents discover, connect, and reuse it as part of a broader ecosystem.

## Index Row

When writing real files, also append rows to:

```text
sandbase-blog/scripts/ai-content-generator/content-index.md
```

Format:

```markdown
| YYYY-MM-DD | <title> | <slug> | <type> | <category> | tag1, tag2, tag3, tag4 | <description> | en | <words> | ❌ |
| YYYY-MM-DD | <title> | <slug> | <type> | <category> | tag1, tag2, tag3, tag4 | <description> | zh-CN | <words> | ❌ |
```

Use `✅` only after a cover exists and the frontmatter `image` is filled.

## Local Validation

From `sandbase-blog`:

```bash
npm run check
npm run build
```

For cover generation, use the existing blog image flow if operating inside the blog repo:

```bash
cd sandbase-blog/scripts/ai-content-generator
npx tsx batch-covers.ts --dry-run
npx tsx batch-covers.ts
```
