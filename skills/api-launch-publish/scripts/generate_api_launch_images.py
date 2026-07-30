#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


BASE = os.environ.get("SANDBASE_API_BASE", "https://api.sandbase.ai/v1")
API_KEY = os.environ.get("SANDBASE_API_KEY")

FORMATS = {
    "16x9": {
        "aspect_ratio": "16:9",
        "suffix": "16x9",
        "prompt_suffix": (
            "Create a premium 16:9 API launch card for Blog, LinkedIn, X/Twitter, and Discord. "
            "Use the SandBase website style: very large black geometric sans-serif title, huge whitespace, subtle square grid background, small uppercase eyebrow, minimal green accents, and a restrained thin-line workflow diagram."
        ),
    },
    "4x5": {
        "aspect_ratio": "4:5",
        "suffix": "4x5",
        "prompt_suffix": (
            "Create a premium 4:5 mobile social launch card. "
            "Use the SandBase website style: very large black geometric sans-serif title, huge whitespace, subtle square grid background, small uppercase eyebrow, minimal green accents, and a clean thin-line workflow diagram."
        ),
    },
}


def request_json(method: str, url: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    req = Request(
        url,
        data=body,
        method=method,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "SandBaseApiLaunchPublish/1.0",
        },
    )
    try:
        with urlopen(req, timeout=90) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        msg = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {msg}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error: {exc}") from exc


def find_images(value: Any) -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, item in value.items():
            if key.lower() in {"url", "image", "image_url", "b64_json", "base64"} and isinstance(item, str):
                found.append(item)
            else:
                found.extend(find_images(item))
    elif isinstance(value, list):
        for item in value:
            found.extend(find_images(item))
    return found


def save_image(out_dir: Path, name: str, image: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    if image.startswith("http://") or image.startswith("https://"):
        req = Request(image, headers={"User-Agent": "SandBase image downloader"})
        with urlopen(req, timeout=120) as resp:
            data = resp.read()
            content_type = resp.headers.get("content-type", "")
        ext = ".png"
        if "jpeg" in content_type or "jpg" in content_type:
            ext = ".jpg"
        elif "webp" in content_type:
            ext = ".webp"
        path = out_dir / f"{name}{ext}"
        path.write_bytes(data)
        return path

    raw = re.sub(r"^data:image/[^;]+;base64,", "", image)
    path = out_dir / f"{name}.png"
    path.write_bytes(base64.b64decode(raw))
    return path


def build_prompt(config: dict[str, Any], format_name: str) -> str:
    fmt = FORMATS[format_name]
    subtitle = config.get("mobile_subtitle") if format_name == "4x5" else config.get("subtitle")
    capability_line = config.get("mobile_capability_line") if format_name == "4x5" else config.get("capability_line")
    return (
        f"{fmt['prompt_suffix']} "
        "Exact visible text only: "
        f"Title: '{config['headline']}'. "
        f"Subtitle: '{subtitle}'. "
        f"Capability line: '{capability_line}'. "
        f"Small label: '{config['small_label']}'. "
        f"Visual concept: {config['visual_concept']}. "
        "Make SandBase the runtime/workflow layer and the provider the capability layer. "
        "Style: SandBase website-aligned product image: white or near-white background, subtle square grid, oversized black geometric sans-serif typography, small uppercase letter-spaced eyebrow label, restrained deep green accents, minimal black/green pills, thin-line UI diagram elements. "
        "Keep text large and readable. Use only the exact text requested. "
        "Avoid: serif typography, warm beige editorial magazine styling, real logos, fake logos, fake metrics, fake dashboards, screenshots, stock-photo people, dark cyberpunk, chaotic dots, excessive glow, tiny text, misspellings, random code blocks, decorative 3D illustrations."
    )


def generate(out_dir: Path, output_name: str, aspect_ratio: str, prompt: str) -> Path:
    if not API_KEY:
        raise RuntimeError("SANDBASE_API_KEY is missing.")
    submitted = request_json("POST", f"{BASE}/run", {
        "model": "openai/gpt-image-2",
        "aspect_ratio": aspect_ratio,
        "output_format": "png",
        "quality": "high",
        "prompt": prompt,
    })
    run_id = submitted["id"]
    print(f"{output_name}: submitted {run_id}", flush=True)
    while True:
        result = request_json("GET", f"{BASE}/run/{run_id}")
        status = result.get("status")
        print(f"{output_name}: {status}", flush=True)
        if status in {"completed", "failed", "timeout"}:
            break
        time.sleep(2)
    if status != "completed":
        raise RuntimeError(f"{output_name} failed: {json.dumps(result, ensure_ascii=False)[:1000]}")
    images = find_images(result)
    if not images:
        response_path = out_dir / f"{output_name}.json"
        response_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        raise RuntimeError(f"{output_name}: no image found; saved response to {response_path}")
    return save_image(out_dir, output_name, images[0])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Path to API launch config JSON.")
    parser.add_argument("--out-dir", default="outputs/api-launch", help="Directory for generated images.")
    parser.add_argument("--formats", nargs="+", default=["16x9"], choices=sorted(FORMATS))
    parser.add_argument("--print-prompts", action="store_true", help="Print prompts without calling the API.")
    args = parser.parse_args()

    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    out_dir = Path(args.out_dir)
    slug = config["slug"]

    saved: list[Path] = []
    for format_name in args.formats:
        fmt = FORMATS[format_name]
        prompt = build_prompt(config, format_name)
        output_name = f"{slug}-{fmt['suffix']}"
        if args.print_prompts:
            print(f"\n## {output_name}\n{prompt}")
            continue
        saved.append(generate(out_dir, output_name, fmt["aspect_ratio"], prompt))

    if saved:
        print("Saved:")
        for path in saved:
            print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
