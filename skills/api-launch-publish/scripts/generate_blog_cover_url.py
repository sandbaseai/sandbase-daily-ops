#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_API_BASE = "https://api.sandbase.ai"
DEFAULT_MODEL = "google/nano-banana-pro"
DEFAULT_ENV_FILES = [
    "/Users/liyb/Documents/Codex/sandbase-monorepo/sandbase-registry/.env",
]


def load_env_file(path: str) -> None:
    env_path = Path(path).expanduser()
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def request_json(method: str, url: str, api_key: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    req = Request(
        url,
        data=body,
        method=method,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "SandBaseBlogCoverUrl/1.0",
        },
    )
    try:
        with urlopen(req, timeout=90) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        message = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {message}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error: {exc}") from exc


def build_prompt(title: str, description: str, category: str, article_type: str) -> str:
    return (
        f'Blog and social cover image for "{title}". '
        f"Context: {description}. "
        f"Category: {category}. Article type: {article_type}. "
        "Use SandBase website style: white or near-white background, subtle square grid, oversized black geometric sans-serif headline, "
        "small uppercase letter-spaced eyebrow label, restrained SandBase green accents, thin-line agent workflow diagram, lots of negative space. "
        "The image should work for Blog, LinkedIn, X/Twitter, and Discord. "
        "Visible text should be minimal and readable: main title only, plus a tiny SandBase-style capability label if needed. "
        "Do not use fake logos, fake metrics, fake users, fake dashboards, screenshots, people, dense code, dark cyberpunk, chaotic dots, or tiny text."
    )


def extract_output_url(result: dict[str, Any]) -> str | None:
    outputs = result.get("outputs")
    if isinstance(outputs, list):
        for item in outputs:
            if isinstance(item, dict) and isinstance(item.get("url"), str):
                return item["url"]
            if isinstance(item, str) and item.startswith(("http://", "https://")):
                return item
    return None


def generate_cover_url(
    title: str,
    description: str,
    category: str,
    article_type: str,
    api_base: str,
    api_key: str,
    model: str,
    aspect_ratio: str,
    poll_timeout: int,
) -> tuple[str, dict[str, Any]]:
    prompt = build_prompt(title, description, category, article_type)
    submit = request_json(
        "POST",
        f"{api_base.rstrip('/')}/v1/run",
        api_key,
        {
            "model": model,
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "output_format": "png",
        },
    )

    if submit.get("status") == "completed":
        url = extract_output_url(submit)
        if url:
            return url, {"submit": submit, "prompt": prompt}

    run_id = submit.get("id")
    if not isinstance(run_id, str) or not run_id:
        raise RuntimeError(f"No run id returned: {json.dumps(submit, ensure_ascii=False)[:1000]}")

    deadline = time.time() + poll_timeout
    result: dict[str, Any] = submit
    while time.time() < deadline:
        time.sleep(3)
        result = request_json("GET", f"{api_base.rstrip('/')}/v1/run/{run_id}", api_key)
        status = result.get("status")
        print(f"cover: {status}", flush=True)
        if status == "completed":
            url = extract_output_url(result)
            if url:
                return url, {"submit": submit, "result": result, "prompt": prompt}
            raise RuntimeError(f"Completed run did not include an output URL: {json.dumps(result, ensure_ascii=False)[:1000]}")
        if status in {"failed", "timeout"}:
            raise RuntimeError(f"Cover generation {status}: {json.dumps(result, ensure_ascii=False)[:1000]}")

    raise RuntimeError(f"Cover generation timed out after {poll_timeout}s")


def quote_yaml(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def upsert_frontmatter(markdown_path: Path, image_url: str, image_alt: str) -> None:
    text = markdown_path.read_text(encoding="utf-8")
    match = re.match(r"^(---\r?\n)(.*?)(\r?\n---\r?\n)", text, flags=re.S)
    if not match:
        raise RuntimeError(f"No YAML frontmatter found: {markdown_path}")

    start, body, end = match.group(1), match.group(2), match.group(3)
    lines = [
        line
        for line in body.splitlines()
        if not re.match(r"^\s*image\s*:", line) and not re.match(r"^\s*imageAlt\s*:", line)
    ]
    lines.append(f"image: {image_url}")
    lines.append(f"imageAlt: {quote_yaml(image_alt)}")
    updated = start + "\n".join(lines).rstrip() + end + text[match.end():]
    markdown_path.write_text(updated, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate one reusable SandBase blog/social cover URL.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--category", default="product-updates")
    parser.add_argument("--article-type", default="launch")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--aspect-ratio", default="16:9")
    parser.add_argument("--api-base", default=os.environ.get("SANDBASE_API_BASE", DEFAULT_API_BASE))
    parser.add_argument("--env-file", action="append", default=[])
    parser.add_argument("--out-json", help="Write generated URL and prompt metadata to this JSON file.")
    parser.add_argument("--update-markdown", action="append", default=[], help="Markdown file whose frontmatter should receive image/imageAlt.")
    parser.add_argument("--image-alt", help="Image alt text. Defaults to title.")
    parser.add_argument("--poll-timeout", type=int, default=120)
    args = parser.parse_args()

    for env_file in DEFAULT_ENV_FILES + args.env_file:
        load_env_file(env_file)

    api_key = os.environ.get("SANDBASE_API_KEY")
    if not api_key:
        raise RuntimeError("SANDBASE_API_KEY is missing. Set it in the environment or pass --env-file.")

    url, metadata = generate_cover_url(
        args.title,
        args.description,
        args.category,
        args.article_type,
        args.api_base,
        api_key,
        args.model,
        args.aspect_ratio,
        args.poll_timeout,
    )

    image_alt = args.image_alt or args.title
    for markdown in args.update_markdown:
        upsert_frontmatter(Path(markdown), url, image_alt)

    output = {
        "url": url,
        "title": args.title,
        "description": args.description,
        "category": args.category,
        "article_type": args.article_type,
        "model": args.model,
        "aspect_ratio": args.aspect_ratio,
        "prompt": metadata["prompt"],
    }
    if args.out_json:
        out_path = Path(args.out_json)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(url)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
