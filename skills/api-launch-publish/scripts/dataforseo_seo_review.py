#!/usr/bin/env python3
"""Create a bounded, DataForSEO-backed SEO evidence pack for a launch package.

The script intentionally requires --allow-billable-requests. It makes one Google Ads
search-volume request (up to ten keywords) and one Google Organic SERP request for the
declared primary query. Credentials are read only from an ignored environment file.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


API_BASE = "https://api.dataforseo.com/v3"
MAX_KEYWORDS = 10


def load_env(path: Path) -> None:
    """Load simple KEY=VALUE lines without echoing secret values."""
    if not path.exists():
        raise ValueError(f"environment file not found: {path}")
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        if key:
            os.environ.setdefault(key, value)


def request_json(endpoint: str, payload: list[dict[str, Any]], login: str, password: str) -> dict[str, Any]:
    credential = base64.b64encode(f"{login}:{password}".encode("utf-8")).decode("ascii")
    request = Request(
        f"{API_BASE}{endpoint}",
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Basic {credential}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "SandBaseApiLaunchPublish/1.0",
        },
    )
    try:
        with urlopen(request, timeout=90) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:1000]
        raise RuntimeError(f"DataForSEO HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"DataForSEO network error: {exc}") from exc


def ensure_success(response: dict[str, Any], label: str) -> list[dict[str, Any]]:
    tasks = response.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        status_code = response.get("status_code", "unknown")
        status_message = response.get("status_message", "no status message")
        raise RuntimeError(
            f"DataForSEO {label} returned no tasks: {status_code} {status_message}"
        )
    failed = [task for task in tasks if task.get("status_code") != 20000]
    if failed:
        status = failed[0].get("status_message", "unknown task failure")
        raise RuntimeError(f"DataForSEO {label} failed: {status}")
    return tasks


def unique_keywords(seo_review: dict[str, Any]) -> list[str]:
    candidates = [seo_review.get("primary_query", ""), *seo_review.get("seed_keywords", [])]
    keywords: list[str] = []
    for value in candidates:
        cleaned = " ".join(str(value).split())
        if cleaned and cleaned.lower() not in {item.lower() for item in keywords}:
            keywords.append(cleaned)
    if not keywords:
        raise ValueError("seo_review requires a primary_query")
    if len(keywords) > MAX_KEYWORDS:
        raise ValueError(f"DataForSEO review accepts at most {MAX_KEYWORDS} unique keywords")
    return keywords


def normalize_keyword_metrics(tasks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result = tasks[0].get("result", [])
    if not isinstance(result, list):
        return []
    metrics: list[dict[str, Any]] = []
    for item in result:
        if not isinstance(item, dict):
            continue
        metrics.append({
            "keyword": item.get("keyword"),
            "search_volume": item.get("search_volume"),
            "competition": item.get("competition"),
            "competition_index": item.get("competition_index"),
            "cpc": item.get("cpc"),
        })
    return metrics


def normalize_serp(tasks: list[dict[str, Any]]) -> dict[str, Any]:
    result = tasks[0].get("result", [])
    page = result[0] if isinstance(result, list) and result else {}
    items = page.get("items", []) if isinstance(page, dict) else []
    organic: list[dict[str, Any]] = []
    for item in items if isinstance(items, list) else []:
        if not isinstance(item, dict) or item.get("type") != "organic":
            continue
        organic.append({
            "rank": item.get("rank_group"),
            "domain": item.get("domain"),
            "title": item.get("title"),
            "url": item.get("url"),
            "description": item.get("description"),
        })
        if len(organic) == 10:
            break
    return {
        "se_results_count": page.get("se_results_count") if isinstance(page, dict) else None,
        "items_count": page.get("items_count") if isinstance(page, dict) else None,
        "organic_results": organic,
    }


def write_markdown(path: Path, evidence: dict[str, Any]) -> None:
    market = evidence["market"]
    lines = [
        "# DataForSEO SEO Evidence",
        "",
        f"- Fetched at: {evidence['fetched_at']}",
        f"- Primary query: {evidence['primary_query']}",
        f"- Reader: {evidence['reader']}",
        f"- Intended search intent: {evidence['search_intent']}",
        f"- Market: Google / location {market['location_code']} / language {market['language_code']}",
        "",
        "## Keyword Metrics",
        "",
        "| Keyword | Monthly search volume | Competition | CPC |",
        "| --- | ---: | --- | ---: |",
    ]
    for item in evidence["keyword_metrics"]:
        lines.append(
            f"| {item.get('keyword') or '-'} | {item.get('search_volume') or '-'} | "
            f"{item.get('competition') or '-'} | {item.get('cpc') or '-'} |"
        )
    lines += ["", "## SERP Sample", "", "| Rank | Domain | Title |", "| ---: | --- | --- |"]
    for item in evidence["serp"]["organic_results"]:
        lines.append(f"| {item.get('rank') or '-'} | {item.get('domain') or '-'} | {item.get('title') or '-'} |")
    lines += [
        "",
        "## Reviewer Use",
        "",
        "- Check whether the article's title and opening match the actual result-set intent.",
        "- Identify missing entities or decision criteria from the ranking pages.",
        "- Do not publish these metrics as a ranking, traffic, or demand guarantee.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Launch input JSON with seo_review.")
    parser.add_argument("--package", required=True, help="Output launch package directory.")
    parser.add_argument("--env-file", required=True, help="Ignored env file containing DataForSEO credentials.")
    parser.add_argument("--allow-billable-requests", action="store_true", help="Required before any paid API request is sent.")
    parser.add_argument("--dry-run", action="store_true", help="Validate input and print the bounded request plan without calling DataForSEO.")
    args = parser.parse_args()

    payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
    seo_review = payload.get("seo_review")
    if not isinstance(seo_review, dict):
        print("ERROR: input.json requires a seo_review object", file=sys.stderr)
        return 2
    required = ("primary_query", "reader", "search_intent", "location_code", "language_code")
    missing = [field for field in required if not seo_review.get(field)]
    if missing:
        print(f"ERROR: seo_review missing: {', '.join(missing)}", file=sys.stderr)
        return 2
    keywords = unique_keywords(seo_review)
    if args.dry_run:
        print("DataForSEO request plan (no network call):")
        print(f"- Search volume: {len(keywords)} keyword(s)")
        print("- SERP: 1 primary query")
        print(f"- Market: {seo_review['location_code']} / {seo_review['language_code']}")
        return 0
    if not args.allow_billable_requests:
        print("ERROR: pass --allow-billable-requests to send paid DataForSEO requests", file=sys.stderr)
        return 2

    load_env(Path(args.env_file))
    login = os.environ.get("DATAFORSEO_LOGIN")
    password = os.environ.get("DATAFORSEO_PASSWORD")
    if not login or not password:
        print("ERROR: DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD are required", file=sys.stderr)
        return 2

    market = {"location_code": seo_review["location_code"], "language_code": seo_review["language_code"]}
    try:
        volume_tasks = ensure_success(request_json(
            "/keywords_data/google_ads/search_volume/live",
            [{**market, "keywords": keywords}],
            login,
            password,
        ), "search volume")
        serp_tasks = ensure_success(request_json(
            "/serp/google/organic/live/advanced",
            [{**market, "keyword": seo_review["primary_query"], "depth": 10}],
            login,
            password,
        ), "SERP")
    except RuntimeError as exc:
        message = str(exc)
        if "40104" in message:
            message += " Complete account verification in https://app.dataforseo.com/ before retrying."
        print(f"ERROR: {message}", file=sys.stderr)
        return 1

    evidence = {
        "source": "DataForSEO",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "primary_query": seo_review["primary_query"],
        "reader": seo_review["reader"],
        "search_intent": seo_review["search_intent"],
        "target_domain": seo_review.get("target_domain"),
        "market": market,
        "keyword_metrics": normalize_keyword_metrics(volume_tasks),
        "serp": normalize_serp(serp_tasks),
        "reviewer_note": "Evidence informs intent and entity coverage. It does not guarantee ranking, traffic, demand, or conversion.",
    }
    package = Path(args.package)
    package.mkdir(parents=True, exist_ok=True)
    json_path = package / "dataforseo-seo-evidence.json"
    markdown_path = package / "dataforseo-seo-evidence.md"
    json_path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(markdown_path, evidence)
    print(f"Saved {json_path}")
    print(f"Saved {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
