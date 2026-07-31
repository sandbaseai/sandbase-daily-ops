#!/usr/bin/env python3
"""Render exact SandBase launch typography over an API-generated background.

Fonts are resolved at runtime instead of being hardcoded to one operating system.
Resolution order for each script (Latin / CJK):

1. ``--latin-font`` / ``--cjk-font`` command-line arguments.
2. ``SANDBASE_COVER_FONT_LATIN`` / ``SANDBASE_COVER_FONT_CJK`` environment variables.
3. The bundled candidate lists below (Linux, macOS, Windows).

A path may carry a font-collection index using ``path#index``, for example
``/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc#2`` to select Noto Sans CJK SC.
"""

from __future__ import annotations

import argparse
import json
import os
from functools import lru_cache
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

ENV_LATIN_FONT = "SANDBASE_COVER_FONT_LATIN"
ENV_CJK_FONT = "SANDBASE_COVER_FONT_CJK"

# Inter is the SandBase brand face (see sandbase-blog/src/styles/global.css).
# Each entry is "path" or "path#collection_index".
LATIN_FONT_CANDIDATES: tuple[str, ...] = (
    "/usr/share/fonts/opentype/inter/Inter-Regular.otf",
    "/usr/share/fonts/truetype/inter/Inter-Regular.ttf",
    "/usr/local/share/fonts/Inter-Regular.otf",
    "/Library/Fonts/Inter-Regular.otf",
    "/System/Library/Fonts/SFNS.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "C:/Windows/Fonts/segoeui.ttf",
    "C:/Windows/Fonts/arial.ttf",
)
LATIN_BOLD_FONT_CANDIDATES: tuple[str, ...] = (
    "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf",
    "/usr/share/fonts/opentype/inter/Inter-Bold.otf",
    "/usr/share/fonts/truetype/inter/Inter-Bold.ttf",
    "/Library/Fonts/Inter-Bold.otf",
    "/System/Library/Fonts/SFNS.ttf",
    "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "C:/Windows/Fonts/segoeuib.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
)
# Index 2 of the Noto CJK collections is the Simplified Chinese face.
CJK_FONT_CANDIDATES: tuple[str, ...] = (
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc#2",
    "/usr/share/fonts/opentype/noto/NotoSansCJKsc-Regular.otf",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc#2",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc#2",
    "C:/Windows/Fonts/msyh.ttc",
    "C:/Windows/Fonts/simhei.ttf",
)
CJK_BOLD_FONT_CANDIDATES: tuple[str, ...] = (
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc#2",
    "/usr/share/fonts/opentype/noto/NotoSansCJKsc-Bold.otf",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc#2",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "C:/Windows/Fonts/msyhbd.ttc",
)

# Overrides supplied on the command line; empty means "fall back to env/candidates".
FONT_OVERRIDES: dict[str, str | None] = {"latin": None, "cjk": None}

# CJK-bearing Unicode blocks. Latin punctuation such as U+00B7 must not trigger the
# CJK face, otherwise capability lines like "Web Search · Extraction" lose the brand font.
CJK_RANGES: tuple[tuple[int, int], ...] = (
    (0x1100, 0x11FF),  # Hangul Jamo
    (0x2E80, 0x2FDF),  # CJK radicals / Kangxi
    (0x3000, 0x303F),  # CJK symbols and punctuation
    (0x3040, 0x30FF),  # Hiragana + Katakana
    (0x3100, 0x312F),  # Bopomofo
    (0x3130, 0x318F),  # Hangul compatibility Jamo
    (0x3400, 0x4DBF),  # CJK ext A
    (0x4E00, 0x9FFF),  # CJK unified ideographs
    (0xA960, 0xA97F),  # Hangul Jamo ext A
    (0xAC00, 0xD7AF),  # Hangul syllables
    (0xF900, 0xFAFF),  # CJK compatibility ideographs
    (0xFE30, 0xFE4F),  # CJK compatibility forms
    (0xFF00, 0xFF60),  # Fullwidth forms
    (0x20000, 0x2FA1F),  # CJK ext B and beyond
)


def split_font_spec(spec: str) -> tuple[str, int]:
    """Split "path#index" into a path and a font-collection index."""
    path, _, index = spec.rpartition("#")
    if path and index.isdigit():
        return path, int(index)
    return spec, 0


@lru_cache(maxsize=None)
def resolve_font_spec(kind: str, bold: bool) -> tuple[str, int]:
    """Return the first usable (path, index) for a font kind, or raise with guidance."""
    if kind == "cjk":
        candidates = CJK_BOLD_FONT_CANDIDATES if bold else CJK_FONT_CANDIDATES
        env_var = ENV_CJK_FONT
    else:
        candidates = LATIN_BOLD_FONT_CANDIDATES if bold else LATIN_FONT_CANDIDATES
        env_var = ENV_LATIN_FONT

    preferred = [spec for spec in (FONT_OVERRIDES.get(kind), os.environ.get(env_var)) if spec]
    for spec in [*preferred, *candidates]:
        path, index = split_font_spec(spec)
        if not Path(path).exists():
            continue
        try:
            ImageFont.truetype(path, size=16, index=index)
        except OSError:
            continue
        return path, index

    raise SystemExit(
        f"No usable {kind} font found. Install a {kind} sans-serif face "
        f"(Linux: 'apt-get install fonts-inter fonts-noto-cjk'), or point {env_var} "
        f"at a .ttf/.otf/.ttc file. Tried: {', '.join(candidates)}"
    )


def contains_cjk(value: str) -> bool:
    return any(
        any(start <= ord(char) <= end for start, end in CJK_RANGES)
        for char in value
    )


def font_for(value: str, size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path, index = resolve_font_spec("cjk" if contains_cjk(value) else "latin", bold)
    return ImageFont.truetype(path, size=size, index=index)


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
    # CJK glyphs fill the em box, so Latin's tight 1.06 leading makes descenders collide
    # with the next line and crowds the subtitle.
    line_height = int(headline_font.size * (1.30 if contains_cjk(headline) else 1.06))
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
    parser.add_argument(
        "--latin-font",
        help=f"Latin font file, optionally 'path#index'. Overrides ${ENV_LATIN_FONT}.",
    )
    parser.add_argument(
        "--cjk-font",
        help=f"CJK font file, optionally 'path#index'. Overrides ${ENV_CJK_FONT}.",
    )
    args = parser.parse_args()
    FONT_OVERRIDES["latin"] = args.latin_font
    FONT_OVERRIDES["cjk"] = args.cjk_font
    resolve_font_spec.cache_clear()
    render(Path(args.background), Path(args.out), json.loads(Path(args.config).read_text(encoding="utf-8")), args.format)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
