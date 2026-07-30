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
- `image` and `imageAlt`: optional but preferred.
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
topic -> dedupe -> research -> write EN -> rewrite ZH -> SEO check -> cover -> render check -> update index
```

Before writing into the real blog repo, check:

```text
sandbase-blog/scripts/ai-content-generator/content-index.md
```

Avoid repeating existing titles or slugs. If the topic overlaps, choose a sharper angle and add internal links to related posts.

## Blog Structure

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
- Clear product point of view: provider supplies raw capability; SandBase turns it into reusable Agent Services.

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
