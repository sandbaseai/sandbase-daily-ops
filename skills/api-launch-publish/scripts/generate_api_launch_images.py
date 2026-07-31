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


from sandbase_env import load_credentials, require


DEFAULT_API_BASE = "https://api.sandbase.ai/v1"

FORMATS = {
    "16x9": {
        "aspect_ratio": "16:9",
        "suffix": "16x9",
        "prompt_suffix": (
            "Create a 16:9 abstract background for a SandBase ecosystem launch asset. "
            "The upper-left 55 percent must remain intentionally empty for post-rendered typography."
        ),
    },
    "4x5": {
        "aspect_ratio": "4:5",
        "suffix": "4x5",
        "prompt_suffix": (
            "Create a 4:5 abstract background for a SandBase ecosystem launch asset. "
            "The upper half must remain intentionally empty for post-rendered typography."
        ),
    },
}


COVER_KIND_PROMPTS = {
    "launch": (
        "Place one external capability node entering a compact agent workflow and producing one real-world outcome. "
        "Keep the diagram restrained and place it in the lower-right third."
    ),
    "comparison": (
        "Create a neutral comparison and decision diagram: two to four equal, unlabeled capability paths enter one agent decision gate. "
        "Use parallel lanes and distinct line patterns, never a literal versus split, podium, or winner badge. "
        "Keep the visual in the lower-right third so the comparison title can be rendered cleanly at upper-left."
    ),
    "top-n": (
        "Create a curated market-map or shortlist diagram: five to six equal, unlabeled capability nodes form a calm orbit around one neutral agent-workflow hub. "
        "Use one restrained green selection marker only. Do not rank nodes, draw a podium, or use trophy imagery. "
        "Keep the visual in the lower-right third so the Top N title can be rendered cleanly at upper-left."
    ),
}


def request_json(method: str, url: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    req = Request(
        url,
        data=body,
        method=method,
        headers={
            "Authorization": f"Bearer {os.environ['SANDBASE_API_KEY']}",
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
    cover_kind = config.get("cover_kind", "launch")
    if cover_kind not in COVER_KIND_PROMPTS:
        allowed = ", ".join(sorted(COVER_KIND_PROMPTS))
        raise ValueError(f"Unknown cover_kind {cover_kind!r}. Use one of: {allowed}.")
    return (
        f"{fmt['prompt_suffix']} "
        f"Visual concept: {config['visual_concept']}. "
        f"Composition: {COVER_KIND_PROMPTS[cover_kind]} "
        "Draw no text, letters, numbers, logos, brand marks, dashboards, browser screenshots, code, people, or devices. "
        "Use a near-white canvas, subtle square grid, restrained deep green linework, and one elegant abstract diagram of an external capability entering an agent workflow and producing a real-world outcome. "
        "A deterministic renderer will add the exact eyebrow, headline, subtitle, and capability label after generation; preserve all typography safe areas completely empty. "
        "The composition must feel precise, calm, technical, and premium. "
        "Avoid dark themes, gradients, cyberpunk, floating dots, 3D blobs, warm beige editorial styling, excessive glow, dense detail, fake metrics, and fake UI."
    )


def generate(out_dir: Path, output_name: str, aspect_ratio: str, prompt: str) -> Path:
    base = os.environ.get("SANDBASE_API_BASE", DEFAULT_API_BASE)
    submitted = request_json("POST", f"{base}/run", {
        "model": "openai/gpt-image-2",
        "aspect_ratio": aspect_ratio,
        "output_format": "png",
        "quality": "high",
        "prompt": prompt,
    })
    run_id = submitted["id"]
    print(f"{output_name}: submitted {run_id}", flush=True)
    while True:
        result = request_json("GET", f"{base}/run/{run_id}")
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
    parser.add_argument("--background-only", action="store_true", help="Keep API backgrounds without deterministic title composition.")
    parser.add_argument(
        "--env-file",
        action="append",
        default=[],
        help="Credential file containing SANDBASE_API_KEY. Repeatable.",
    )
    args = parser.parse_args()

    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    out_dir = Path(args.out_dir)
    slug = config["slug"]

    # --print-prompts is offline, so only require a credential for real API calls.
    if not args.print_prompts:
        load_credentials(args.env_file)
        require("SANDBASE_API_KEY")

    saved: list[Path] = []
    for format_name in args.formats:
        fmt = FORMATS[format_name]
        prompt = build_prompt(config, format_name)
        output_name = f"{slug}-{fmt['suffix']}"
        if args.print_prompts:
            print(f"\n## {output_name}\n{prompt}")
            continue
        background_name = f"{output_name}-background"
        background = generate(out_dir, background_name, fmt["aspect_ratio"], prompt)
        if args.background_only:
            saved.append(background)
            continue
        final_path = out_dir / f"{output_name}.png"
        from render_launch_cover import render
        render(background, final_path, config, format_name)
        saved.append(final_path)

    if saved:
        print("Saved:")
        for path in saved:
            print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
