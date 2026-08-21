#!/usr/bin/env python3
"""
Google Indexing API - Batch URL Submission for Sandbase.
Submits high-priority URLs to Google for fast crawling/indexing.

Usage:
    python3 submit_indexing.py                  # Submit default batch (200 URLs)
    python3 submit_indexing.py --limit 50       # Submit first 50
    python3 submit_indexing.py --dry-run        # Preview without submitting
    python3 submit_indexing.py --ping-sitemap   # Also ping sitemap

Rate limits: 200 URLs/day per property.
"""

import argparse
import json
import sys
import time
import subprocess
from pathlib import Path

import requests
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request

# --- Config ---
SERVICE_ACCOUNT_PATH = "/root/.config/sandbase/google-service-account.json"
SCOPES = ["https://www.googleapis.com/auth/indexing"]
INDEXING_API_URL = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SITEMAP_PING_URL = "https://www.google.com/ping?sitemap=https://www.sandbase.ai/sitemap-index.xml"
SITE_BASE = "https://www.sandbase.ai"


def get_credentials():
    """Load and refresh Google service account credentials."""
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_PATH, scopes=SCOPES)
    creds.refresh(Request())
    return creds


def build_url_list():
    """Build prioritized URL list for submission."""
    urls = []

    # Priority 1: Core entry pages (highest value)
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

    # Priority 2: Top vendor pages (high search volume)
    top_vendors = [
        "openai", "anthropic", "google", "deepseek", "meta",
        "mistral", "xai", "microsoft", "nvidia", "alibaba",
        "cohere", "perplexity", "bytedance", "tencent", "minimax",
        "moonshotai", "stepfun", "xiaomi", "bfl", "kwaivgi",
    ]
    urls.extend([f"{SITE_BASE}/vendor/{v}" for v in top_vendors])

    # Priority 3: Top models from sitemap (sorted by sort_order)
    try:
        result = subprocess.run(
            ["curl", "-s", f"{SITE_BASE}/sitemap-models.xml"],
            capture_output=True, text=True, timeout=30
        )
        import re
        model_urls = re.findall(r'<loc>([^<]+)</loc>', result.stdout)
        # Take top 150 (already sorted by priority in sitemap)
        urls.extend(model_urls[:150])
    except Exception as e:
        print(f"Warning: Could not fetch sitemap-models.xml: {e}")

    # Priority 4: Remaining vendors
    try:
        result = subprocess.run(
            ["curl", "-s", f"{SITE_BASE}/sitemap-vendors.xml"],
            capture_output=True, text=True, timeout=30
        )
        import re
        vendor_urls = re.findall(r'<loc>([^<]+)</loc>', result.stdout)
        for vu in vendor_urls:
            if vu not in urls:
                urls.append(vu)
    except Exception as e:
        print(f"Warning: Could not fetch sitemap-vendors.xml: {e}")

    # Deduplicate while preserving order
    seen = set()
    deduped = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            deduped.append(u)

    return deduped


def submit_url(session, headers, url, url_type="URL_UPDATED"):
    """Submit a single URL to Google Indexing API."""
    body = {
        "url": url,
        "type": url_type,
    }
    response = session.post(INDEXING_API_URL, headers=headers, json=body)
    return response.status_code, response.json()


def ping_sitemap():
    """Ping Google with updated sitemap."""
    response = requests.get(SITEMAP_PING_URL)
    return response.status_code


def main():
    parser = argparse.ArgumentParser(description="Submit URLs to Google Indexing API")
    parser.add_argument("--limit", type=int, default=200, help="Max URLs to submit (default: 200)")
    parser.add_argument("--dry-run", action="store_true", help="Preview URLs without submitting")
    parser.add_argument("--ping-sitemap", action="store_true", help="Also ping sitemap after submission")
    args = parser.parse_args()

    print("=" * 60)
    print("Google Indexing API - Sandbase URL Submission")
    print("=" * 60)

    # Build URL list
    urls = build_url_list()
    urls = urls[:args.limit]
    print(f"\n📋 Total URLs to submit: {len(urls)}")

    if args.dry_run:
        print("\n🔍 DRY RUN - URLs that would be submitted:")
        for i, url in enumerate(urls, 1):
            print(f"  {i:3d}. {url}")
        print(f"\nTotal: {len(urls)} URLs")
        return

    # Authenticate
    print("\n🔐 Authenticating with Google service account...")
    try:
        creds = get_credentials()
    except Exception as e:
        print(f"❌ Authentication failed: {e}")
        sys.exit(1)

    headers = {
        "Authorization": f"Bearer {creds.token}",
        "Content-Type": "application/json",
    }
    session = requests.Session()

    # Submit URLs
    print(f"\n🚀 Submitting {len(urls)} URLs...\n")
    success_count = 0
    error_count = 0
    errors = []

    for i, url in enumerate(urls, 1):
        try:
            status_code, response = submit_url(session, headers, url)
            if status_code == 200:
                success_count += 1
                if i <= 10 or i % 20 == 0:
                    print(f"  ✅ [{i:3d}/{len(urls)}] {url}")
            elif status_code == 429:
                # Rate limited - wait and retry once
                error_msg = response.get("error", {}).get("message", "Rate limited")
                if "per day" in error_msg:
                    print(f"  ⏸️  Daily quota exhausted at URL #{i}. Stopping.")
                    errors.append((url, 429, "Daily quota exhausted"))
                    error_count += len(urls) - i + 1
                    break
                else:
                    time.sleep(5)
                    status_code, response = submit_url(session, headers, url)
                    if status_code == 200:
                        success_count += 1
                        print(f"  ✅ [{i:3d}/{len(urls)}] {url} (retry)")
                    else:
                        error_count += 1
                        errors.append((url, status_code, str(response)[:100]))
            else:
                error_count += 1
                error_msg = response.get("error", {}).get("message", str(response))
                errors.append((url, status_code, error_msg))
                if i <= 10 or error_count <= 5:
                    print(f"  ❌ [{i:3d}/{len(urls)}] {url} → {status_code}: {error_msg[:80]}")

            # Rate limiting: Google allows ~600 requests/minute, but be conservative
            if i % 50 == 0:
                print(f"  ... {i}/{len(urls)} processed ({success_count} ok, {error_count} errors)")
                time.sleep(1)

        except Exception as e:
            error_count += 1
            errors.append((url, 0, str(e)))
            print(f"  ❌ [{i:3d}/{len(urls)}] {url} → Exception: {str(e)[:80]}")

    # Summary
    print("\n" + "=" * 60)
    print(f"📊 RESULTS")
    print(f"   ✅ Success: {success_count}")
    print(f"   ❌ Errors:  {error_count}")
    print(f"   📋 Total:   {len(urls)}")

    if errors:
        print(f"\n⚠️  First 5 errors:")
        for url, code, msg in errors[:5]:
            print(f"   {code} {url}: {msg[:100]}")

    # Ping sitemap
    if args.ping_sitemap:
        print(f"\n📡 Pinging Google sitemap...")
        status = ping_sitemap()
        print(f"   Sitemap ping: HTTP {status}")

    # Save report
    report_dir = Path("/root/kiro/sandbase-daily-ops/outputs/seo-daily-reports")
    report_dir.mkdir(parents=True, exist_ok=True)
    report_file = report_dir / f"indexing-{time.strftime('%Y%m%d-%H%M%S')}.json"
    report = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_submitted": len(urls),
        "success": success_count,
        "errors": error_count,
        "error_details": [{"url": u, "code": c, "message": m} for u, c, m in errors[:20]],
    }
    report_file.write_text(json.dumps(report, indent=2))
    print(f"\n📁 Report saved: {report_file}")
    print("=" * 60)


if __name__ == "__main__":
    main()
