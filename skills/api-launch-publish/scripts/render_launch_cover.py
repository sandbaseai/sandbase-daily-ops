#!/usr/bin/env python3
"""Render exact SandBase launch typography over an API-generated background."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


TOKENS = {
    "canvas": "#F8F8F6",
    "ink": "#101311",
    "muted": "#737A78",
    "green": "#20B987",
    "grid": "#E6E9E7",
    "border": "#D9DEDB",
}
FORMATS = {
    "16x9": (1600, 900),
    "4x5": (1600, 2000),
    "1x1": (1600, 1600),
}
LATIN_FONT = "/System/Library/Fonts/SFNS.ttf"
CJK_FONT = "/System/Library/Fonts/Hiragino Sans GB.ttc"


def contains_cjk(value: str) -> bool:
    return any(ord(char) > 127 for char in value)


def font_for(value: str, size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = CJK_FONT if contains_cjk(value) else LATIN_FONT
    return ImageFont.truetype(path, size=size, index=0)


def text_width(draw: ImageDraw.ImageDraw, value: str, font: ImageFont.FreeTypeFont) -> int:
    return int(draw.textbbox((0, 0), value, font=font)[2])


def wrap_text(draw: ImageDraw.ImageDraw, value: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = value.split(" ") if " " in value else list(value)
    lines: list[str] = []
    current = ""
    joiner = " " if " " in value else ""
    for word in words:
        candidate = word if not current else f"{current}{joiner}{word}"
        if current and text_width(draw, candidate, font) > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def fit_headline(draw: ImageDraw.ImageDraw, headline: str, max_width: int, max_lines: int, start_size: int) -> tuple[ImageFont.FreeTypeFont, list[str]]:
    for size in range(start_size, 44, -4):
        font = font_for(headline, size)
        lines = wrap_text(draw, headline, font, max_width)
        if len(lines) <= max_lines:
            return font, lines
    font = font_for(headline, 44)
    return font, wrap_text(draw, headline, font, max_width)


def draw_grid(draw: ImageDraw.ImageDraw, width: int, height: int) -> None:
    step = max(56, round(width / 24))
    for x in range(0, width + 1, step):
        draw.line((x, 0, x, height), fill=TOKENS["grid"], width=1)
    for y in range(0, height + 1, step):
        draw.line((0, y, width, y), fill=TOKENS["grid"], width=1)


def render(background: Path, output: Path, config: dict, format_name: str) -> None:
    width, height = FORMATS[format_name]
    raw = Image.open(background).convert("RGBA")
    raw = ImageOps.fit(raw, (width, height), method=Image.Resampling.LANCZOS)
    base = Image.new("RGBA", (width, height), TOKENS["canvas"])
    raw.putalpha(46)
    base.alpha_composite(raw)
    draw = ImageDraw.Draw(base)
    draw_grid(draw, width, height)

    margin_x = int(width * 0.09)
    margin_y = int(height * 0.09)
    text_width_limit = int(width * (0.54 if format_name == "16x9" else 0.82))
    headline = config["headline"]
    subtitle = config.get("mobile_subtitle") if format_name == "4x5" else config.get("subtitle")
    capability = config.get("mobile_capability_line") if format_name == "4x5" else config.get("capability_line")
    eyebrow = config.get("eyebrow", "AGENT ECOSYSTEM")
    if not subtitle:
        subtitle = config.get("sandbase_value", "")
    if not capability:
        capability = "Connected capability"

    eyebrow_font = font_for(eyebrow, max(22, round(width * 0.016)))
    draw.line((margin_x, margin_y + 14, margin_x + 70, margin_y + 14), fill=TOKENS["green"], width=3)
    draw.text((margin_x + 92, margin_y), eyebrow.upper(), fill=TOKENS["muted"], font=eyebrow_font)

    max_lines = 2 if format_name == "16x9" else 3
    start_size = round(width * (0.062 if format_name == "16x9" else 0.073))
    headline_font, headline_lines = fit_headline(draw, headline, text_width_limit, max_lines, start_size)
    line_height = int(headline_font.size * 1.06)
    headline_y = margin_y + int(height * 0.105)
    for index, line in enumerate(headline_lines):
        draw.text((margin_x, headline_y + index * line_height), line, fill=TOKENS["ink"], font=headline_font)

    subtitle_y = headline_y + len(headline_lines) * line_height + int(height * 0.035)
    subtitle_font = font_for(subtitle, max(26, round(width * 0.021)))
    for index, line in enumerate(wrap_text(draw, subtitle, subtitle_font, text_width_limit)):
        draw.text((margin_x, subtitle_y + index * int(subtitle_font.size * 1.3)), line, fill=TOKENS["muted"], font=subtitle_font)

    pill_font = font_for(capability, max(22, round(width * 0.017)))
    pill_y = height - margin_y - int(pill_font.size * 2.2)
    pill_width = min(text_width_limit, text_width(draw, capability, pill_font) + 52)
    draw.rounded_rectangle((margin_x, pill_y, margin_x + pill_width, pill_y + pill_font.size * 2), radius=12, fill="#FFFFFF", outline=TOKENS["border"], width=2)
    draw.ellipse((margin_x + 18, pill_y + pill_font.size - 7, margin_x + 32, pill_y + pill_font.size + 7), fill=TOKENS["green"])
    draw.text((margin_x + 44, pill_y + int(pill_font.size * 0.37)), capability, fill=TOKENS["ink"], font=pill_font)

    output.parent.mkdir(parents=True, exist_ok=True)
    base.convert("RGB").save(output, quality=95)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--background", required=True)
    parser.add_argument("--config", required=True)
    parser.add_argument("--format", required=True, choices=sorted(FORMATS))
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    render(Path(args.background), Path(args.out), json.loads(Path(args.config).read_text(encoding="utf-8")), args.format)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
