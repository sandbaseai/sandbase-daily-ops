#!/usr/bin/env python3
"""SEO Daily Check — Google Search Console + DataForSEO.

Produces a daily report on article indexing, rankings, and traffic.
Run via cron: 0 8 * * * python3 /path/to/seo_daily_check.py

Requires:
- ~/.config/sandbase/google-service-account.json (GSC access)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build

# --- Configuration ---
KEY_FILE = Path(os.environ.get("GOOGLE_SERVICE_ACCOUNT_FILE", Path.home() / ".config/sandbase/google-service-account.json"))
ENV_FILE = Path.home() / ".config/sandbase/.env"
SITE = "sc-domain:sandbase.ai"
BLOG_PREFIX = "https://blog.sandbase.ai/"
REPORT_DIR = Path(__file__).resolve().parents[1] / "outputs/seo-daily-reports"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# Articles we published (new batch)
NEW_ARTICLE_SLUGS = [
    "social-media-data-apis-ai-agents-2026",
    "douyin-data-api-on-sandbase",
    "weibo-xiaohongshu-data-api-on-sandbase",
    "douyin-data-api-competitor-monitor-agent",
    "xiaohongshu-kol-screening-agent-tutorial",
    "social-listening-agent-weibo-douyin-2026",
    "normalizing-431-heterogeneous-apis-one-contract",
    "llm-api-pricing-guide-2026",
    "video-generation-cost-model-explained",
    "per-call-pricing-vs-token-pricing-api-agents",
    "claude-opus-5-deep-dive-2026",
    "claude-sonnet-5-agents-coding-2026",
    "kimi-k3-moonshot-1m-context-2026",
    "gpt-5-6-luna-sol-terra-explained",
    "claude-opus-5-vs-sonnet-5-which-to-pick",
    "kimi-k3-vs-claude-opus-5-2026",
    "gpt-5-6-vs-claude-5-agents-2026",
    "best-1m-context-models-agents-2026",
    "anthropic-cache-pricing-5m-1h-explained",
    "best-models-autonomous-agents-2026",
    "minimax-h3-video-2k-stereo-2026",
    "kling-video-3-unified-generation-2026",
    "gemini-omni-flash-video-2026",
    "minimax-h3-vs-kling-3-vs-gemini-omni",
    "text-to-video-vs-image-to-video-2026",
    "kling-turbo-vs-omni-pro-standard-2026",
    "best-ai-video-generation-apis-2026",
    "best-image-to-video-models-agents-2026",
    "video-generation-agent-ad-creative-tutorial",
    "text-embedding-v4-alibaba-deep-dive",
    "seedream-5-pro-bytedance-image-2026",
    "qwen-image-3-alibaba-generation-edit",
    "seedream-vs-qwen-image-vs-nano-banana-2026",
    "seedream-fast-vs-pro-quality-cost-2026",
    "best-ai-image-generation-apis-2026",
    "best-ai-image-editing-apis-2026",
    "batch-image-generation-agent-tutorial",
    "cloudsway-search-api-explained-2026",
    "cloudsway-vs-exa-search-agents-2026",
    "best-embedding-models-rag-agents-2026",
    "social-data-api-vs-web-scraping-agents-2026",
    "best-douyin-data-api-services-2026",
    "china-social-commerce-data-ai-agents-2026",
    "sync-only-api-design-ai-agents",
    "rag-cost-structure-embedding-search-2026",
    "build-social-monitor-agent-openai-sdk",
    "multimodal-agent-artifacts-e2b-sandbox",
    "cost-dashboard-agent-anthropic-sdk",
]


def discover_article_slugs() -> list[str]:
    """Discover current English article slugs from the canonical Blog sitemap."""
    try:
        with urllib.request.urlopen(f"{BLOG_PREFIX}sitemap-0.xml", timeout=30) as response:
            sitemap = response.read().decode("utf-8")
        slugs = []
        for url in re.findall(r"<loc>([^<]+)</loc>", sitemap):
            if not url.startswith(BLOG_PREFIX) or "/zh-CN/" in url:
                continue
            slug = url.removeprefix(BLOG_PREFIX).strip("/")
            if slug:
                slugs.append(slug)
        return slugs or NEW_ARTICLE_SLUGS
    except Exception as exc:
        print(f"  Blog sitemap discovery failed, using fallback list: {exc}")
        return NEW_ARTICLE_SLUGS


def get_gsc_service():
    credentials = service_account.Credentials.from_service_account_file(
        str(KEY_FILE), scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
    )
    return build("searchconsole", "v1", credentials=credentials)


def fetch_page_data(service, start_date: str, end_date: str) -> list[dict]:
    """Fetch per-page search analytics."""
    response = service.searchanalytics().query(
        siteUrl=SITE,
        body={
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": ["page"],
            "rowLimit": 500,
            "dataState": "all",
        },
    ).execute()
    return response.get("rows", [])


def fetch_query_data(service, start_date: str, end_date: str) -> list[dict]:
    """Fetch per-query search analytics for the Blog property subset."""
    response = service.searchanalytics().query(
        siteUrl=SITE,
        body={
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": ["query"],
            "dimensionFilterGroups": [{
                "filters": [{
                    "dimension": "page",
                    "operator": "contains",
                    "expression": BLOG_PREFIX,
                }]
            }],
            "rowLimit": 100,
            "dataState": "all",
        },
    ).execute()
    return response.get("rows", [])


def fetch_url_inspection(service, url: str) -> dict:
    """Check if a URL is indexed."""
    try:
        result = service.urlInspection().index().inspect(
            body={"inspectionUrl": url, "siteUrl": SITE}
        ).execute()
        return result.get("inspectionResult", {})
    except Exception as e:
        return {"error": str(e)}


def generate_report(today: str, page_data: list, query_data: list, indexing_status: dict, article_slugs: list[str]) -> str:
    """Generate markdown report."""
    lines = [
        f"# SEO 巡检报告 {today}",
        "",
        f"数据范围: GSC 过去 7 天（有 2 天延迟）",
        "",
    ]

    # Indexing status
    indexed = sum(1 for s in indexing_status.values() if s == "indexed")
    total = len(indexing_status)
    lines.append("## 收录状态")
    lines.append("")
    lines.append(f"- 新文章已收录: **{indexed}/{total}** ({indexed*100//max(total,1)}%)")
    not_indexed = [slug for slug, s in indexing_status.items() if s != "indexed"]
    if not_indexed:
        lines.append(f"- 未收录 ({len(not_indexed)} 篇):")
        for slug in not_indexed[:10]:
            lines.append(f"  - {slug}")
        if len(not_indexed) > 10:
            lines.append(f"  - ... 还有 {len(not_indexed) - 10} 篇")
    lines.append("")

    # Traffic - blog pages
    blog_pages = [r for r in page_data if r["keys"][0].startswith(BLOG_PREFIX)]
    blog_pages.sort(key=lambda r: r["clicks"], reverse=True)

    lines.append("## 流量 Top 10（博客页面）")
    lines.append("")
    lines.append("| 页面 | 点击 | 展示 | CTR | 平均排名 |")
    lines.append("|---|---:|---:|---:|---:|")
    for row in blog_pages[:10]:
        page = row["keys"][0].replace("https://blog.sandbase.ai/", "").rstrip("/")
        lines.append(f"| {page} | {row['clicks']} | {row['impressions']} | {row['ctr']*100:.1f}% | {row['position']:.1f} |")
    lines.append("")

    # Total stats
    total_clicks = sum(r["clicks"] for r in page_data)
    total_impressions = sum(r["impressions"] for r in page_data)
    blog_clicks = sum(r["clicks"] for r in blog_pages)
    blog_impressions = sum(r["impressions"] for r in blog_pages)
    lines.append("## 总体数据")
    lines.append("")
    lines.append(f"| 指标 | 全站 | 博客 |")
    lines.append(f"|---|---:|---:|")
    lines.append(f"| 点击 | {total_clicks} | {blog_clicks} |")
    lines.append(f"| 展示 | {total_impressions} | {blog_impressions} |")
    lines.append(f"| 有数据页面 | {len(page_data)} | {len(blog_pages)} |")
    lines.append("")

    # Top queries
    lines.append("## Blog 热门查询词 Top 15")
    lines.append("")
    lines.append("| 查询词 | 点击 | 展示 | CTR | 排名 |")
    lines.append("|---|---:|---:|---:|---:|")
    for row in sorted(query_data, key=lambda r: r["impressions"], reverse=True)[:15]:
        q = row["keys"][0][:45]
        lines.append(f"| {q} | {row['clicks']} | {row['impressions']} | {row['ctr']*100:.1f}% | {row['position']:.1f} |")
    lines.append("")

    # New articles with traffic
    new_with_data = []
    for row in blog_pages:
        page = row["keys"][0].replace("https://blog.sandbase.ai/", "").rstrip("/")
        slug = page.replace("zh-CN/", "")
        if slug in article_slugs:
            new_with_data.append((slug, row))

    if new_with_data:
        lines.append("## Blog 文章表现（当前 sitemap 中有数据的）")
        lines.append("")
        lines.append("| 文章 | 点击 | 展示 | CTR | 排名 |")
        lines.append("|---|---:|---:|---:|---:|")
        for slug, row in sorted(new_with_data, key=lambda x: x[1]["impressions"], reverse=True):
            lines.append(f"| {slug} | {row['clicks']} | {row['impressions']} | {row['ctr']*100:.1f}% | {row['position']:.1f} |")
    else:
        lines.append("## 新文章表现")
        lines.append("")
        lines.append("新文章尚未出现在 GSC 数据中（正常，新发布需要 3-14 天收录）。")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slugs", help="Comma-separated Blog slugs to inspect after publication")
    args = parser.parse_args()

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    end_date = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=9)).strftime("%Y-%m-%d")

    print(f"[{today}] SEO 巡检开始...")
    service = get_gsc_service()
    requested_slugs = [slug.strip() for slug in (args.slugs or "").split(",") if slug.strip()]
    article_slugs = requested_slugs or discover_article_slugs()

    # 1. Fetch search analytics
    print("  拉取页面数据...")
    page_data = fetch_page_data(service, start_date, end_date)
    print(f"  {len(page_data)} 个页面有数据")

    print("  拉取查询数据...")
    query_data = fetch_query_data(service, start_date, end_date)
    print(f"  {len(query_data)} 个查询词")

    # 2. Check indexing (sample 10 new articles to avoid rate limits)
    print("  检查收录状态（抽样 10 篇）...")
    indexing_status = {}
    for slug in article_slugs[:10]:
        url = f"https://blog.sandbase.ai/{slug}/"
        result = fetch_url_inspection(service, url)
        verdict = result.get("indexStatusResult", {}).get("verdict", "unknown")
        coverage = result.get("indexStatusResult", {}).get("coverageState", "unknown")
        if "error" in result:
            indexing_status[slug] = "error"
        elif verdict == "PASS" or "Submitted and indexed" in str(coverage):
            indexing_status[slug] = "indexed"
        else:
            indexing_status[slug] = f"not_indexed ({coverage})"
        print(f"    {slug}: {indexing_status[slug]}")

    # 3. Generate report
    report = generate_report(today, page_data, query_data, indexing_status, article_slugs)
    report_path = REPORT_DIR / f"{today}.md"
    report_path.write_text(report)
    print(f"\n  报告已生成: {report_path}")

    # 4. Print summary
    print("\n" + "=" * 60)
    print(report[:2000])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
