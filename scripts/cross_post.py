#!/usr/bin/env python3
"""
Cross-post SandBase Blog articles to DEV.to and Medium.

Reads blog markdown files, strips frontmatter, adds canonical_url back to
blog.sandbase.ai, and publishes via platform APIs.

Usage:
    # Publish one article to DEV.to (draft mode)
    python3 cross_post.py --platform devto --slug lovable-ai-app-builder-guide-2026

    # Publish one article to DEV.to (live)
    python3 cross_post.py --platform devto --slug lovable-ai-app-builder-guide-2026 --publish

    # Publish to Medium (draft)
    python3 cross_post.py --platform medium --slug lovable-ai-app-builder-guide-2026

    # Batch: publish all EN articles to DEV.to as drafts
    python3 cross_post.py --platform devto --all --locale en

    # Dry run (preview what would be sent)
    python3 cross_post.py --platform devto --slug lovable-ai-app-builder-guide-2026 --dry-run

Environment variables (in ~/.config/sandbase/.env):
    DEVTO_API_KEY=xxx          # DEV.to API key from settings/extensions
    MEDIUM_TOKEN=xxx           # Medium integration token from me/settings
    MEDIUM_AUTHOR_ID=xxx       # Your Medium user ID (get via /v1/me)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

import requests
import yaml

# --- Config ---
BLOG_CONTENT_DIR = Path("/root/kiro/sandbase-blog/src/content")
BLOG_BASE_URL = "https://blog.sandbase.ai"
DEVTO_API_URL = "https://dev.to/api/articles"
MEDIUM_API_URL = "https://api.medium.com/v1"

# Max 4 tags on DEV.to, strip hyphens (DEV uses single-word or camelCase tags)
DEVTO_MAX_TAGS = 4


def load_env():
    """Load credentials from env file."""
    env_path = Path.home() / ".config/sandbase/.env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k and k not in os.environ:
                os.environ[k] = v


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and body from markdown."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not match:
        return {}, content
    fm = yaml.safe_load(match.group(1))
    body = match.group(2)
    return fm or {}, body


def load_article(slug: str, locale: str = "en") -> tuple[dict, str] | None:
    """Load a blog article by slug and locale."""
    path = BLOG_CONTENT_DIR / locale / f"{slug}.md"
    if not path.exists():
        print(f"  ❌ File not found: {path}")
        return None
    content = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(content)
    return fm, body


def get_canonical_url(slug: str, locale: str = "en") -> str:
    """Build canonical URL for the blog article."""
    if locale == "en":
        return f"{BLOG_BASE_URL}/{slug}/"
    return f"{BLOG_BASE_URL}/{locale}/{slug}/"


def format_devto_tags(tags: list[str]) -> list[str]:
    """Convert blog tags to DEV.to format (no hyphens, lowercase, max 4)."""
    formatted = []
    for tag in tags[:DEVTO_MAX_TAGS]:
        # DEV.to tags: lowercase, no spaces, hyphens allowed actually
        clean = tag.lower().strip()
        if len(clean) <= 30:
            formatted.append(clean)
    return formatted


def publish_to_devto(
    title: str,
    body: str,
    tags: list[str],
    canonical_url: str,
    description: str,
    cover_image: str | None,
    published: bool = False,
    dry_run: bool = False,
) -> dict | None:
    """Publish article to DEV.to."""
    api_key = os.environ.get("DEVTO_API_KEY")
    if not api_key:
        print("  ❌ DEVTO_API_KEY not set. Get one from https://dev.to/settings/extensions")
        return None

    payload = {
        "article": {
            "title": title,
            "body_markdown": body,
            "published": published,
            "tags": format_devto_tags(tags),
            "canonical_url": canonical_url,
            "description": description[:200] if description else "",
        }
    }
    if cover_image:
        payload["article"]["main_image"] = cover_image

    if dry_run:
        print(f"  [DRY RUN] Would POST to {DEVTO_API_URL}")
        print(f"    title: {title}")
        print(f"    tags: {payload['article']['tags']}")
        print(f"    canonical_url: {canonical_url}")
        print(f"    published: {published}")
        print(f"    body length: {len(body)} chars")
        return {"dry_run": True}

    resp = requests.post(
        DEVTO_API_URL,
        headers={
            "api-key": api_key,
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=30,
    )

    if resp.status_code in (200, 201):
        data = resp.json()
        print(f"  ✅ Published: {data.get('url', 'unknown')}")
        return data
    else:
        print(f"  ❌ HTTP {resp.status_code}: {resp.text[:200]}")
        return None


def publish_to_medium(
    title: str,
    body: str,
    tags: list[str],
    canonical_url: str,
    published: bool = False,
    dry_run: bool = False,
) -> dict | None:
    """Publish article to Medium."""
    token = os.environ.get("MEDIUM_TOKEN")
    author_id = os.environ.get("MEDIUM_AUTHOR_ID")

    if not token:
        print("  ❌ MEDIUM_TOKEN not set. Get one from https://medium.com/me/settings → Integration Tokens")
        return None

    # Get author ID if not set
    if not author_id:
        me_resp = requests.get(
            f"{MEDIUM_API_URL}/me",
            headers={"Authorization": f"Bearer {token}"},
            timeout=15,
        )
        if me_resp.status_code == 200:
            author_id = me_resp.json()["data"]["id"]
            print(f"  ℹ️  Medium author ID: {author_id} (add MEDIUM_AUTHOR_ID to .env to skip this)")
        else:
            print(f"  ❌ Failed to get Medium user: HTTP {me_resp.status_code}")
            return None

    payload = {
        "title": title,
        "contentFormat": "markdown",
        "content": f"# {title}\n\n{body}",
        "canonicalUrl": canonical_url,
        "tags": tags[:3],  # Medium max 3 tags
        "publishStatus": "public" if published else "draft",
    }

    if dry_run:
        print(f"  [DRY RUN] Would POST to {MEDIUM_API_URL}/users/{author_id}/posts")
        print(f"    title: {title}")
        print(f"    tags: {payload['tags']}")
        print(f"    canonical_url: {canonical_url}")
        print(f"    publishStatus: {payload['publishStatus']}")
        print(f"    body length: {len(body)} chars")
        return {"dry_run": True}

    resp = requests.post(
        f"{MEDIUM_API_URL}/users/{author_id}/posts",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=30,
    )

    if resp.status_code in (200, 201):
        data = resp.json().get("data", {})
        print(f"  ✅ Published: {data.get('url', 'unknown')}")
        return data
    else:
        print(f"  ❌ HTTP {resp.status_code}: {resp.text[:200]}")
        return None


def process_article(slug: str, locale: str, platform: str, published: bool, dry_run: bool) -> bool:
    """Process and publish a single article."""
    print(f"\n  [{slug}] → {platform}")

    result = load_article(slug, locale)
    if not result:
        return False

    fm, body = result
    title = fm.get("title", slug)
    tags = fm.get("tags", [])
    description = fm.get("description", "")
    cover_image = fm.get("image", "")
    canonical_url = get_canonical_url(slug, locale)

    if platform == "devto":
        return publish_to_devto(
            title=title,
            body=body,
            tags=tags,
            canonical_url=canonical_url,
            description=description,
            cover_image=cover_image,
            published=published,
            dry_run=dry_run,
        ) is not None
    elif platform == "medium":
        return publish_to_medium(
            title=title,
            body=body,
            tags=tags,
            canonical_url=canonical_url,
            published=published,
            dry_run=dry_run,
        ) is not None
    else:
        print(f"  ❌ Unknown platform: {platform}")
        return False


def get_all_slugs(locale: str = "en") -> list[str]:
    """Get all article slugs for a locale."""
    content_dir = BLOG_CONTENT_DIR / locale
    if not content_dir.exists():
        return []
    return sorted([f.stem for f in content_dir.glob("*.md")])


def main():
    parser = argparse.ArgumentParser(description="Cross-post SandBase Blog articles to DEV.to / Medium")
    parser.add_argument("--platform", required=True, choices=["devto", "medium"], help="Target platform")
    parser.add_argument("--slug", help="Single article slug to publish")
    parser.add_argument("--all", action="store_true", help="Publish all articles")
    parser.add_argument("--locale", default="en", help="Locale (default: en)")
    parser.add_argument("--publish", action="store_true", help="Publish live (default: draft)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without publishing")
    parser.add_argument("--limit", type=int, help="Max articles to process (with --all)")
    parser.add_argument("--delay", type=float, default=2.0, help="Delay between posts in seconds (default: 2)")
    args = parser.parse_args()

    load_env()

    print("=" * 60)
    print(f"Cross-Post → {args.platform.upper()}")
    print(f"Mode: {'LIVE' if args.publish else 'DRAFT'} {'(DRY RUN)' if args.dry_run else ''}")
    print("=" * 60)

    if args.slug:
        slugs = [args.slug]
    elif args.all:
        slugs = get_all_slugs(args.locale)
        if args.limit:
            slugs = slugs[:args.limit]
    else:
        print("Error: specify --slug or --all")
        sys.exit(1)

    print(f"\n📋 Articles to process: {len(slugs)}")

    success = 0
    failed = 0
    for i, slug in enumerate(slugs, 1):
        ok = process_article(slug, args.locale, args.platform, args.publish, args.dry_run)
        if ok:
            success += 1
        else:
            failed += 1

        # Rate limiting
        if i < len(slugs) and not args.dry_run:
            time.sleep(args.delay)

    print("\n" + "=" * 60)
    print(f"📊 Done: {success} success, {failed} failed, {len(slugs)} total")
    print("=" * 60)


if __name__ == "__main__":
    main()
