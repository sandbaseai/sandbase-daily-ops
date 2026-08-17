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

    # Priority 3: Top models and vendors from unified sitemap.xml
    try:
        result = subprocess.run(
            ["curl", "-s", f"{SITE_BASE}/sitemap.xml"],
            capture_output=True, text=True, timeout=30
        )
        sitemap_urls = re.findall(r'<loc>([^<]+)</loc>', result.stdout)
        # Separate model and vendor URLs
        model_urls = [u for u in sitemap_urls if '/model/' in u]
        vendor_urls = [u for u in sitemap_urls if '/vendor/' in u]
        urls.extend(model_urls[:150])
        for vu in vendor_urls:
            if vu not in urls:
                urls.append(vu)
    except Exception as e:
        print(f"Warning: Could not fetch sitemap.xml: {e}")

    # Priority 4: Blog URLs (blog.sandbase.ai)
    try:
        result = subprocess.run(
            ["curl", "-s", "https://blog.sandbase.ai/sitemap-0.xml"],
            capture_output=True, text=True, timeout=30
        )
        blog_urls = re.findall(r'<loc>([^<]+)</loc>', result.stdout)
        # Only include English (non zh-CN) blog posts
        blog_en = [u for u in blog_urls if '/zh-CN/' not in u and u != "https://blog.sandbase.ai/"]
        urls.extend(blog_en[:50])
    except Exception as e:
        print(f"Warning: Could not fetch blog sitemap: {e}")

    # Deduplicate
    seen = set()
    deduped = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            deduped.append(u)

    return deduped


def submit_batch(endpoint, host, urls):
    """Submit a batch of URLs to an IndexNow endpoint. Max 10,000 per request."""
    body = {
        "host": host,
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


def group_urls_by_host(urls):
    """Group URLs by their hostname for correct IndexNow host field."""
    from urllib.parse import urlparse
    groups = {}
    for url in urls:
        host = urlparse(url).netloc
        groups.setdefault(host, []).append(url)
    return groups


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

    # Group by host (www.sandbase.ai vs blog.sandbase.ai)
    host_groups = group_urls_by_host(urls)
    for host, host_urls in host_groups.items():
        print(f"   {host}: {len(host_urls)} URLs")

    if args.dry_run:
        print("\n🔍 DRY RUN - URLs that would be submitted:")
        for i, url in enumerate(urls[:30], 1):
            print(f"  {i:3d}. {url}")
        if len(urls) > 30:
            print(f"  ... and {len(urls) - 30} more")
        return

    # Submit to each IndexNow endpoint, grouped by host
    print(f"\n🚀 Submitting {len(urls)} URLs to IndexNow endpoints...\n")

    for endpoint in INDEXNOW_ENDPOINTS:
        engine_name = endpoint.split("//")[1].split("/")[0].replace("api.indexnow.org", "IndexNow (all)")
        for host, host_urls in host_groups.items():
            status, body = submit_batch(endpoint, host, host_urls)

            if status in (200, 202):
                print(f"  ✅ {engine_name} [{host}]: HTTP {status} — Accepted ({len(host_urls)} URLs)")
            elif status == 207:
                print(f"  ⚠️  {engine_name} [{host}]: HTTP {status} — Partial")
            else:
                print(f"  ❌ {engine_name} [{host}]: HTTP {status} — {body[:80]}")

    # Summary
    print("\n" + "=" * 60)
    print(f"📊 Submitted {len(urls)} URLs to {len(INDEXNOW_ENDPOINTS)} search engines")
    print(f"   Hosts: {', '.join(host_groups.keys())}")
    print(f"   Engines: Bing, Yandex, and IndexNow partners")
    print(f"   Expected crawl: within 24-48 hours")

    # Save report
    report_dir = Path("/root/kiro/sandbase-daily-ops/outputs/seo-daily-reports")
    report_dir.mkdir(parents=True, exist_ok=True)
    report_file = report_dir / f"indexnow-{time.strftime('%Y%m%d-%H%M%S')}.json"
    report = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_submitted": len(urls),
        "hosts": {h: len(u) for h, u in host_groups.items()},
        "urls_sample": urls[:20],
    }
    report_file.write_text(json.dumps(report, indent=2))
    print(f"\n📁 Report saved: {report_file}")
    print("=" * 60)


if __name__ == "__main__":
    main()
