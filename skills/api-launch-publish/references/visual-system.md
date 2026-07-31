# SandBase Launch Visual System

## Rule

The image model draws atmosphere and abstract capability shapes. It never draws product text, logos, metrics, code, screenshots, or UI. A deterministic renderer owns every visible word.

## Brand Tokens

| Token | Value | Use |
|---|---|---|
| Canvas | `#F8F8F6` | near-white background |
| Ink | `#101311` | headline and labels |
| Muted | `#737A78` | subtitle and eyebrow |
| SandBase green | `#20B987` | accent line, dot, pill detail |
| Grid | `#E6E9E7` | subtle background grid |
| Border | `#D9DEDB` | thin diagram and pill borders |

## Layout

Use a 12-column implicit grid. Keep text in the left seven columns and reserve the right or lower third for an abstract capability visual.

- Safe area: 9% left/right, 8% top/bottom.
- Eyebrow: top 12%, uppercase, small, letter-spaced.
- Headline: top 20-44%, maximum two lines, left aligned.
- Subtitle: below headline, one or two lines.
- Capability pill: lower-left, one concise phrase only.
- Abstract visual: lower-right or bottom third, never behind the headline.

## Formats

| Format | Pixel target | Use | Headline limit |
|---|---:|---|---|
| `16x9` | 1600×900 | Blog, LinkedIn, X, Discord | 46 characters / two lines |
| `4x5` | 1600×2000 | Xiaohongshu, Moments, mobile | 26 characters / three lines |
| `1x1` | 1600×1600 | Store cards, social tiles | 28 characters / three lines |

## Fixed Background Prompt

```text
Create a clean abstract background for a SandBase product launch image. No text, letters, numbers, logos, brand marks, dashboards, browser screenshots, code, people, or devices. Use a near-white canvas, a very subtle technical grid, restrained deep green linework, and one elegant abstract diagram showing a capability entering an agent workflow and becoming a real-world outcome. Keep the upper-left 55% intentionally empty for deterministic typography. The composition must feel precise, calm, technical, and premium. Avoid dark themes, gradients, cyberpunk, floating dots, 3D blobs, warm beige editorial styling, excessive glow, and dense visual detail.
```

## Cover Kinds

Every final cover has exact text rendered by `render_launch_cover.py`: an eyebrow, headline, subtitle, and capability pill. Do not ask the image model to render these words. The model only supplies the clean diagram background.

| `cover_kind` | When to use it | Background composition | Required final typography |
|---|---|---|---|
| `launch` | A new API, model, skill, or ecosystem capability | One capability flows into a compact agent workflow and creates one outcome. | `AGENT ECOSYSTEM` or `PRODUCT UPDATE`; product name; one outcome statement. |
| `comparison` | A versus / alternatives article | 2-4 equal, unlabeled routes meet at one neutral decision gate. No VS split or winner visual. | `2026 COMPARISON`; `A vs B vs C`; decision criterion subtitle. |
| `top-n` | A curated list, shortlist, or market map | 5-6 equal, unlabeled nodes around a neutral hub. One quiet green selection mark, never a podium or ranking numbers. | `2026 TOP PICKS`; `Best <capability> 2026`; one audience/use-case subtitle. |

### Comparison Example

```json
{
  "cover_kind": "comparison",
  "eyebrow": "2026 COMPARISON",
  "headline": "Exa vs Tavily vs Firecrawl",
  "subtitle": "Which search API fits your agent workflow?",
  "capability_line": "Semantic search · Research · Crawling"
}
```

### Top N Example

```json
{
  "cover_kind": "top-n",
  "eyebrow": "2026 TOP PICKS",
  "headline": "Best AI Search APIs 2026",
  "subtitle": "A practical shortlist for agent workflows",
  "capability_line": "Research · Monitoring · Lead discovery"
}
```

## Visual Variants

- `capability-flow`: use with `launch`; one external node flows into a simple agent-workflow diagram.
- `comparison-gate`: use with `comparison`; equal paths meet at a neutral decision point.
- `shortlist-map`: use with `top-n`; a few equal candidate nodes form a calm, curated market map.
- `artifact-outcome`: use with `launch`; one capability node becomes a report, task, or artifact for FDE and delivery stories.

Choose one variant. Do not combine all three in one image.
