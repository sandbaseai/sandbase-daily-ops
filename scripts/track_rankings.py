#!/usr/bin/env python3
"""Blog article ranking tracker using DataForSEO.

Checks where blog.sandbase.ai ranks for each configured primary keyword.
Run weekly via cron to track ranking changes over time.

Usage:
  python3 track_rankings.py --config config/blog-keywords.json --dry-run
  python3 track_rankings.py --config config/blog-keywords.json --env-file ~/.config/sandbase/.env --allow-billable-requests
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

SANDBASE_RUN_URL = "https://api.sandbase.ai/v1/run"
DEFAULT_CONFIG = Path(__file__).resolve().parents[1] / "config/blog-keywords.json"


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip("\"'"))


def load_config(path: Path) -> tuple[str, list[dict]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    domain = data.get("target_domain")
    keywords = data.get("keywords")
    if not domain or not isinstance(keywords, list) or not keywords:
        raise ValueError("config requires target_domain and a non-empty keywords list")
    required = {"keyword", "language", "location", "slug", "volume"}
    for index, item in enumerate(keywords):
        missing = required - set(item)
        if missing:
            raise ValueError(f"keywords[{index}] missing: {', '.join(sorted(missing))}")
    return domain, keywords


def request_serp(keyword: str, location: int, language: str, api_key: str) -> dict:
    """Check Google SERP through the SandBase API."""
    payload = {
        "model": "dataforseo/v3/serp/google/organic/live/regular",
        "keyword": keyword,
        "location_code": location,
        "language_code": language,
        "depth": 30,  # Check top 30
        "device": "desktop",
    }
    req = Request(
        SANDBASE_RUN_URL,
        data=json.dumps(payload).encode(),
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    with urlopen(req, timeout=90) as resp:
        response = json.loads(resp.read())
    outputs = response.get("outputs", [])
    return outputs[0] if outputs and isinstance(outputs[0], dict) else {}


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
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--env-file")
    parser.add_argument("--allow-billable-requests", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output", default="./ranking-history.csv")
    args = parser.parse_args()

    try:
        target_domain, tracked_keywords = load_config(Path(args.config))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: invalid keyword config: {exc}", file=sys.stderr)
        return 1

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    output_path = Path(args.output)

    if args.dry_run:
        print(f"Would check {len(tracked_keywords)} keywords for {target_domain} ranking:")
        for kw in tracked_keywords:
            print(f"  [{kw['language']}] \"{kw['keyword']}\" (vol={kw['volume']}) → {kw['slug']}")
        print(f"\nEstimated cost: ~{len(tracked_keywords)} SERP calls")
        return 0

    if not args.allow_billable_requests:
        print("ERROR: --allow-billable-requests required for live SERP checks", file=sys.stderr)
        return 1

    if args.env_file:
        load_env(Path(args.env_file))
    api_key = os.environ.get("SANDBASE_API_KEY")
    if not api_key:
        print("ERROR: SANDBASE_API_KEY required", file=sys.stderr)
        return 1

    # Check rankings
    results = []
    for kw in tracked_keywords:
        lang = kw["language"]
        print(f"  Checking: \"{kw['keyword']}\" ({lang}, loc={kw['location']})...", end=" ")
        try:
            serp = request_serp(kw["keyword"], kw["location"], lang, api_key)
            rank, url = find_domain_rank(serp, target_domain)
            status = f"#{rank}" if rank else "Not in top 30"
            print(status)
            results.append({
                "date": today,
                "keyword": kw["keyword"],
                "locale": lang,
                "volume": kw["volume"],
                "rank": rank or "",
                "url": url or "",
                "target_slug": kw["slug"],
            })
        except Exception as e:
            print(f"ERROR: {e}")
            results.append({
                "date": today,
                "keyword": kw["keyword"],
                "locale": lang,
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
