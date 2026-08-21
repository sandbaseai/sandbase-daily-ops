#!/usr/bin/env python3
"""
每日 AI 热点监控脚本
通过 Exa Search + DataForSEO 搜索量，发现高潜力 SEO 选题。

用法：
  export $(grep -v '^#' ~/.config/sandbase/.env | xargs)
  python3 scripts/daily_hot_topics.py
"""

import json
import os
import sys
from datetime import datetime, timedelta
import urllib.request
from pathlib import Path

API_KEY = os.environ.get("SANDBASE_API_KEY")
if not API_KEY:
    print("ERROR: SANDBASE_API_KEY not set")
    sys.exit(1)

BASE_URL = "https://api.sandbase.ai/v1/run"

def call_sandbase(model: str, params: dict) -> dict:
    """调用 SandBase API"""
    body = {"model": model, **params}
    data = json.dumps(body).encode()
    req = urllib.request.Request(
        BASE_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read())


def search_hot_topics():
    """用 Exa Search 搜索最近 7 天的 AI 热门内容"""
    week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    queries = [
        "new AI model release coding agent 2026",
        "MCP protocol update server tools",
        "LLM benchmark comparison frontier model",
        "AI agent framework infrastructure production",
        "open source AI model weights release",
    ]

    all_results = []

    for q in queries:
        try:
            resp = call_sandbase("exa/search", {
                "query": q,
                "start_date": week_ago,
                "max_results": 5,
                "include_highlights": True
            })
            outputs = resp.get("outputs", [{}])
            if outputs and isinstance(outputs[0], dict):
                entities = outputs[0].get("entities", [])
                for e in entities:
                    all_results.append({
                        "title": e.get("title", ""),
                        "url": e.get("url", ""),
                        "date": e.get("published_date", "")[:10],
                        "highlight": (e.get("highlights", [""])[0] or "")[:200],
                        "query": q
                    })
        except Exception as ex:
            print(f"  ⚠️ Exa search failed for '{q}': {ex}")

    return all_results


def deduplicate_topics(results):
    """按 URL 去重，按日期排序"""
    seen = set()
    unique = []
    for r in results:
        url = r["url"]
        if url not in seen:
            seen.add(url)
            unique.append(r)
    return sorted(unique, key=lambda x: x["date"], reverse=True)


def extract_keywords(results):
    """从搜索结果中提取潜在关键词"""
    keywords = set()
    keyword_patterns = [
        "qwen 3.8", "qwen 3.9", "claude code", "mcp protocol", "mcp stateless",
        "deepseek v4", "kimi k3", "gemini", "gpt-5", "gpt-6",
        "ai agent", "coding agent", "ai sandbox", "open weights",
        "cursor ai", "windsurf", "bolt ai", "lovable",
        "langchain", "langgraph", "crewai", "autogen",
        "openai codex", "anthropic", "function calling",
        "rag", "embedding", "vector database",
    ]

    for r in results:
        text = (r["title"] + " " + r["highlight"]).lower()
        for kw in keyword_patterns:
            if kw in text:
                keywords.add(kw)

    return list(keywords)


def check_search_volume(keywords):
    """用 DataForSEO 检查关键词搜索量"""
    if not keywords:
        return []

    # 最多查 20 个
    keywords = keywords[:20]

    try:
        resp = call_sandbase("dataforseo/v3/keywords_data/google_ads/search_volume/live", {
            "keywords": keywords,
            "language_code": "en",
            "location_code": 2840
        })
        outputs = resp.get("outputs", [{}])
        if outputs:
            tasks = outputs[0].get("tasks", [{}])
            if tasks:
                results = tasks[0].get("result", [])
                volume_data = []
                for r in results:
                    sv = r.get("search_volume") or 0
                    if sv > 0:
                        volume_data.append({
                            "keyword": r["keyword"],
                            "volume": sv,
                            "cpc": r.get("cpc") or 0,
                            "competition": r.get("competition") or "N/A"
                        })
                return sorted(volume_data, key=lambda x: x["volume"], reverse=True)
    except Exception as ex:
        print(f"  ⚠️ DataForSEO failed: {ex}")

    return []


def check_existing_coverage(keywords):
    """检查我们博客已有的文章是否覆盖这些关键词"""
    import glob
    local_blog = Path(os.environ.get("SANDBASE_BLOG_REPO", Path(__file__).resolve().parents[2] / "sandbase-blog"))
    existing_slugs = [Path(f).stem for f in glob.glob(str(local_blog / "src/content/en/*.md"))]

    if not existing_slugs:
        try:
            with urllib.request.urlopen("https://blog.sandbase.ai/sitemap-0.xml", timeout=30) as response:
                sitemap = response.read().decode("utf-8")
            import re
            existing_slugs = [
                url.removeprefix("https://blog.sandbase.ai/").strip("/")
                for url in re.findall(r"<loc>([^<]+)</loc>", sitemap)
                if url.startswith("https://blog.sandbase.ai/") and "/zh-CN/" not in url
            ]
        except Exception as ex:
            print(f"  ⚠️ Blog coverage lookup failed: {ex}")

    covered = {}
    for kw in keywords:
        kw_parts = kw.replace("-", " ").split()
        for slug in existing_slugs:
            slug_parts = slug.replace("-", " ")
            if all(p in slug_parts for p in kw_parts):
                covered[kw] = slug
                break

    return covered


def main():
    print("=" * 70)
    print(f"  📡 AI 热点监控 — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)

    # Step 1: Exa Search 搜索热门内容
    print("\n🔍 Step 1: 搜索最近 7 天 AI 热门内容...")
    results = search_hot_topics()
    results = deduplicate_topics(results)

    print(f"  找到 {len(results)} 条去重结果")
    print(f"\n{'='*70}")
    print("  📰 最近热门内容 Top 10:")
    print(f"{'='*70}")

    for i, r in enumerate(results[:10], 1):
        print(f"\n  {i:>2}. [{r['date']}] {r['title'][:70]}")
        print(f"      {r['url'][:80]}")
        if r['highlight']:
            print(f"      → {r['highlight'][:120]}...")

    # Step 2: 提取关键词
    print(f"\n{'='*70}")
    print("  🏷️ Step 2: 提取热门关键词...")
    keywords = extract_keywords(results)
    print(f"  发现 {len(keywords)} 个热门关键词: {', '.join(keywords[:15])}")

    # Step 3: 查询搜索量
    print(f"\n{'='*70}")
    print("  📊 Step 3: 关键词搜索量查询...")
    volume_data = check_search_volume(keywords)

    if volume_data:
        print(f"\n  {'Keyword':<25} {'Volume':>8} {'CPC':>7} {'Comp':>6}")
        print(f"  {'-'*50}")
        for v in volume_data[:15]:
            print(f"  {v['keyword']:<25} {v['volume']:>8} {'$'+str(v['cpc']):>7} {v['competition']:>6}")

    # Step 4: 检查已有覆盖
    print(f"\n{'='*70}")
    print("  ✅ Step 4: 检查博客已有覆盖...")
    covered = check_existing_coverage([v["keyword"] for v in volume_data])

    # Step 5: 选题建议
    print(f"\n{'='*70}")
    print("  💡 Step 5: 选题建议（高搜索量 + 未覆盖）")
    print(f"{'='*70}")

    suggestions = []
    for v in volume_data:
        kw = v["keyword"]
        if kw not in covered:
            suggestions.append(v)
        else:
            print(f"  ⏭️  {kw} — 已有文章: {covered[kw]}")

    if suggestions:
        print(f"\n  🔥 推荐写的选题（按搜索量排序）：")
        for i, s in enumerate(suggestions[:5], 1):
            print(f"  {i}. {s['keyword']} — {s['volume']:,}/月 (CPC ${s['cpc']})")
    else:
        print("  所有热门关键词都已覆盖 ✅")

    # 保存报告
    report = {
        "date": datetime.now().isoformat(),
        "hot_content": results[:10],
        "keywords_with_volume": volume_data,
        "already_covered": covered,
        "suggestions": suggestions[:5]
    }

    report_dir = Path(__file__).resolve().parents[1] / "outputs/seo-daily-reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_file = report_dir / f"hot-topics-{datetime.now().strftime('%Y%m%d')}.json"
    with report_file.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\n  📁 报告已保存: {report_file}")
    print("=" * 70)


if __name__ == "__main__":
    main()
