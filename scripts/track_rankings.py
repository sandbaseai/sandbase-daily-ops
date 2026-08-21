#!/usr/bin/env python3
"""Blog article ranking tracker using DataForSEO.

Checks where sandbase.ai ranks for each article's primary keyword.
Run weekly via cron to track ranking changes over time.

Usage:
  python3 track_rankings.py --env-file ~/.config/sandbase/.env --allow-billable-requests
  python3 track_rankings.py --env-file ~/.config/sandbase/.env --dry-run
"""

from __future__ import annotations

import argparse
import base64
import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

API_BASE = "https://api.dataforseo.com/v3"
TARGET_DOMAIN = "sandbase.ai"

# Keywords to track, mapped to the article slug they should drive traffic to
TRACKED_KEYWORDS = [
    # High-volume (verified by DataForSEO)
    {"keyword": "image to video AI", "locale": "en", "location": 2840, "slug": "best-image-to-video-models-agents-2026", "volume": 40500},
    {"keyword": "AI 视频生成", "locale": "zh", "location": 2156, "slug": "best-ai-video-generation-apis-2026", "volume": 1600},
    {"keyword": "anthropic prompt caching", "locale": "en", "location": 2840, "slug": "anthropic-cache-pricing-5m-1h-explained", "volume": 390},
    {"keyword": "AI agent 开发", "locale": "zh", "location": 2156, "slug": "best-models-autonomous-agents-2026", "volume": 260},
    {"keyword": "小红书 API", "locale": "zh", "location": 2156, "slug": "weibo-xiaohongshu-data-api-on-sandbase", "volume": 210},
    {"keyword": "大模型 API", "locale": "zh", "location": 2156, "slug": "llm-api-pricing-guide-2026", "volume": 140},
    {"keyword": "gpt 5.6 release", "locale": "en", "location": 2840, "slug": "gpt-5-6-luna-sol-terra-explained", "volume": 110},
    {"keyword": "LLM API cost comparison", "locale": "en", "location": 2840, "slug": "llm-api-pricing-guide-2026", "volume": 70},
    {"keyword": "text to video API", "locale": "en", "location": 2840, "slug": "text-to-video-vs-image-to-video-2026", "volume": 50},
    {"keyword": "抖音数据分析", "locale": "zh", "location": 2156, "slug": "douyin-data-api-on-sandbase", "volume": 30},
    {"keyword": "best AI image generation API", "locale": "en", "location": 2840, "slug": "best-ai-image-generation-apis-2026", "volume": 10},
    # Supplementary tracking (no verified volume, but strategic)
    {"keyword": "social media data API for AI agents", "locale": "en", "location": 2840, "slug": "social-media-data-apis-ai-agents-2026", "volume": 0},
    {"keyword": "per-call vs token pricing", "locale": "en", "location": 2840, "slug": "per-call-pricing-vs-token-pricing-api-agents", "volume": 0},
]


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip("\"'"))


def request_serp(keyword: str, location: int, language: str, login: str, password: str) -> dict:
    """Check Google SERP for a keyword, return sandbase.ai ranking."""
    credential = base64.b64encode(f"{login}:{password}".encode()).decode()
    payload = [{
        "keyword": keyword,
        "location_code": location,
        "language_code": language,
        "depth": 30,  # Check top 30
        "device": "desktop",
    }]
    req = Request(
        f"{API_BASE}/serp/google/organic/live/regular",
        data=json.dumps(payload).encode(),
        method="POST",
        headers={
            "Authorization": f"Basic {credential}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urlopen(req, timeout=60) as resp:
            return json.loads(resp.read())
    except Exception:
        return {"tasks": []}


def find_domain_rank(serp_result: dict, domain: str) -> tuple[int | None, str | None]:
    """Find where target domain ranks in SERP results."""
    tasks = serp_result.get("tasks", [])
    if not tasks:
        return None, None
    items = tasks[0].get("result", [{}])[0].get("items", [])
    for item in items:
        if item.get("type") == "organic" and domain in (item.get("domain") or ""):
            return item.get("rank_absolute"), item.get("url")
    return None, None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--env-file", required=True)
    parser.add_argument("--allow-billable-requests", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output", default="./ranking-history.csv")
    args = parser.parse_args()

    load_env(Path(args.env_file))
    login = os.environ.get("DATAFORSEO_LOGIN")
    password = os.environ.get("DATAFORSEO_PASSWORD")
    if not login or not password:
        print("ERROR: DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD required", file=sys.stderr)
        return 1

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    output_path = Path(args.output)

    if args.dry_run:
        print(f"Would check {len(TRACKED_KEYWORDS)} keywords for {TARGET_DOMAIN} ranking:")
        for kw in TRACKED_KEYWORDS:
            print(f"  [{kw['locale']}] \"{kw['keyword']}\" (vol={kw['volume']}) → {kw['slug']}")
        print(f"\nEstimated cost: ~{len(TRACKED_KEYWORDS)} SERP calls")
        return 0

    if not args.allow_billable_requests:
        print("ERROR: --allow-billable-requests required for live SERP checks", file=sys.stderr)
        return 1

    # Check rankings
    results = []
    for kw in TRACKED_KEYWORDS:
        lang = "en" if kw["locale"] == "en" else "en"  # DataForSEO needs valid lang code
        print(f"  Checking: \"{kw['keyword']}\" ({kw['locale']}, loc={kw['location']})...", end=" ")
        try:
            serp = request_serp(kw["keyword"], kw["location"], lang, login, password)
            rank, url = find_domain_rank(serp, TARGET_DOMAIN)
            status = f"#{rank}" if rank else "Not in top 30"
            print(status)
            results.append({
                "date": today,
                "keyword": kw["keyword"],
                "locale": kw["locale"],
                "volume": kw["volume"],
                "rank": rank or "",
                "url": url or "",
                "target_slug": kw["slug"],
            })
        except HTTPError as e:
            print(f"ERROR: {e}")
            results.append({
                "date": today,
                "keyword": kw["keyword"],
                "locale": kw["locale"],
                "volume": kw["volume"],
                "rank": "error",
                "url": "",
                "target_slug": kw["slug"],
            })

    # Append to CSV
    write_header = not output_path.exists()
    with open(output_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "keyword", "locale", "volume", "rank", "url", "target_slug"])
        if write_header:
            writer.writeheader()
        writer.writerows(results)

    # Print summary
    print(f"\n=== Ranking Summary ({today}) ===")
    ranked = [r for r in results if r["rank"] and r["rank"] != "error"]
    not_ranked = [r for r in results if not r["rank"]]
    print(f"  Ranked (top 30): {len(ranked)}/{len(results)}")
    for r in sorted(ranked, key=lambda x: int(x["rank"])):
        print(f"    #{r['rank']:>2} | {r['keyword']} (vol={r['volume']})")
    print(f"  Not ranked: {len(not_ranked)}")
    print(f"\n  Results appended to: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
