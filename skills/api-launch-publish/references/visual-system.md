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

## Visual Variants

- `capability-flow`: one external node flowing into a simple agent-workflow diagram.
- `ecosystem-map`: several restrained capability nodes connected to one agent hub; use only when the post is about ecosystem breadth.
- `artifact-outcome`: one capability node becomes a report, task, or artifact; use for FDE and delivery stories.

Choose one variant. Do not combine all three in one image.
