#!/usr/bin/env python3
"""
IndexNow - Batch URL Submission for Sandbase.
Notifies Bing, Yandex, and other supporting search engines about new/updated URLs.

No approval process needed - just submit and they crawl.

Usage:
    python3 submit_indexnow.py                  # Submit default batch (200 URLs)
    python3 submit_indexnow.py --limit 50       # Submit first 50
    python3 submit_indexnow.py --dry-run        # Preview without submitting
"""

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

import requests

# --- Config ---
SITE_HOST = "www.sandbase.ai"
SITE_BASE = f"https://{SITE_HOST}"
# IndexNow key - this file must also be accessible at https://www.sandbase.ai/{KEY}.txt
INDEXNOW_KEY = "fe52fdd42c4d42cbbcce6c1a94f7fb5d"
INDEXNOW_ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://yandex.com/indexnow",
]


def build_url_list():
    """Build prioritized URL list for submission."""
    urls = []

    # Priority 1: Core entry pages
    core_pages = [
        "/models",
        "/apis",
        "/vendor",
        "/pricing",
        "/agents",
        "/skills",
        "/",
    ]
    urls.extend([f"{SITE_BASE}{p}" for p in core_pages])

    # Priority 2: Top vendor pages
    top_vendors = [
        "openai", "anthropic", "google", "deepseek", "meta",
        "mistral", "xai", "microsoft", "nvidia", "alibaba",
        "cohere", "perplexity", "bytedance", "tencent", "minimax",
        "moonshotai", "stepfun", "xiaomi", "bfl", "kwaivgi",
    ]
    urls.extend([f"{SITE_BASE}/vendor/{v}" for v in top_vendors])

    # Priority 3: Top models from sitemap
    try:
        result = subprocess.run(
            ["curl", "-s", f"{SITE_BASE}/sitemap-models.xml"],
            capture_output=True, text=True, timeout=30
        )
        model_urls = re.findall(r'<loc>([^<]+)</loc>', result.stdout)
        urls.extend(model_urls[:150])
    except Exception as e:
        print(f"Warning: Could not fetch sitemap-models.xml: {e}")

    # Priority 4: Remaining vendors
    try:
        result = subprocess.run(
            ["curl", "-s", f"{SITE_BASE}/sitemap-vendors.xml"],
            capture_output=True, text=True, timeout=30
        )
        vendor_urls = re.findall(r'<loc>([^<]+)</loc>', result.stdout)
        for vu in vendor_urls:
            if vu not in urls:
                urls.append(vu)
    except Exception as e:
        print(f"Warning: Could not fetch sitemap-vendors.xml: {e}")

    # Deduplicate
    seen = set()
    deduped = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            deduped.append(u)

    return deduped


def submit_batch(endpoint, urls):
    """Submit a batch of URLs to an IndexNow endpoint. Max 10,000 per request."""
    body = {
        "host": SITE_HOST,
        "key": INDEXNOW_KEY,
        "urlList": urls,
    }
    try:
        response = requests.post(
            endpoint,
            headers={"Content-Type": "application/json"},
            json=body,
            timeout=30,
        )
        return response.status_code, response.text[:200]
    except Exception as e:
        return 0, str(e)


def main():
    parser = argparse.ArgumentParser(description="Submit URLs via IndexNow protocol")
    parser.add_argument("--limit", type=int, default=200, help="Max URLs to submit (default: 200)")
    parser.add_argument("--dry-run", action="store_true", help="Preview URLs without submitting")
    args = parser.parse_args()

    print("=" * 60)
    print("IndexNow - Sandbase URL Submission")
    print("(Bing, Yandex, and supporting search engines)")
    print("=" * 60)

    # Build URL list
    urls = build_url_list()
    urls = urls[:args.limit]
    print(f"\n📋 Total URLs to submit: {len(urls)}")

    if args.dry_run:
        print("\n🔍 DRY RUN - URLs that would be submitted:")
        for i, url in enumerate(urls[:30], 1):
            print(f"  {i:3d}. {url}")
        if len(urls) > 30:
            print(f"  ... and {len(urls) - 30} more")
        return

    # Submit to each IndexNow endpoint
    print(f"\n🚀 Submitting {len(urls)} URLs to IndexNow endpoints...\n")

    for endpoint in INDEXNOW_ENDPOINTS:
        engine_name = endpoint.split("//")[1].split("/")[0].replace("api.indexnow.org", "IndexNow (all)")
        status, body = submit_batch(endpoint, urls)

        if status in (200, 202):
            print(f"  ✅ {engine_name}: HTTP {status} — Accepted")
        elif status == 207:
            print(f"  ⚠️  {engine_name}: HTTP {status} — Partial (some URLs may be invalid)")
        else:
            print(f"  ❌ {engine_name}: HTTP {status} — {body[:100]}")

    # Summary
    print("\n" + "=" * 60)
    print(f"📊 Submitted {len(urls)} URLs to {len(INDEXNOW_ENDPOINTS)} search engines")
    print(f"   Engines: Bing, Yandex, and IndexNow partners")
    print(f"   Expected crawl: within 24-48 hours")

    # Save report
    report_dir = Path("/root/kiro/sandbase-daily-ops/outputs/seo-daily-reports")
    report_dir.mkdir(parents=True, exist_ok=True)
    report_file = report_dir / f"indexnow-{time.strftime('%Y%m%d-%H%M%S')}.json"
    report = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_submitted": len(urls),
        "urls_sample": urls[:20],
    }
    report_file.write_text(json.dumps(report, indent=2))
    print(f"\n📁 Report saved: {report_file}")
    print("=" * 60)


if __name__ == "__main__":
    main()
