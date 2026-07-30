# Image Formats

Default image set for API launch:

| Channel | Aspect Ratio | Recommended Use |
| --- | --- | --- |
| Blog | 16:9 | Header image |
| LinkedIn | 16:9 | Feed post image |
| X / Twitter | 16:9 | Feed post image |
| Discord | 16:9 | Announcement image |
| Optional mobile/social | 4:5 | Reuse later for Xiaohongshu/Moments |

Generate first as one reusable public URL:

```text
16x9
```

Use the URL from `cover-url.json` for Blog, LinkedIn, X / Twitter, and Discord. Generate second only if the user wants broader mobile reuse:

```text
4x5
```

Safe-area:

- Keep critical text at least 8% from the edges.
- Keep title to one or two lines.
- Use one title, one subtitle, one capability row.
- Avoid dense diagrams for Discord and X.

SandBase website style:

- White background.
- Subtle square grid.
- Very large black sans-serif title.
- Green accent line/pill.
- Minimal workflow diagram.
