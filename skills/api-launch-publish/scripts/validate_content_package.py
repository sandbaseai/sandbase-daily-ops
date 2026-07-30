#!/usr/bin/env python3
"""Validate the repeatable structure of a SandBase launch content package."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_INPUT_FIELDS = {
    "api_name",
    "provider",
    "provider_description",
    "sandbase_value",
    "channels",
    "locales",
    "author",
    "source_facts",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def has_markdown(directory: Path) -> bool:
    return directory.exists() and any(directory.glob("*.md"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Launch input JSON.")
    parser.add_argument("--package", required=True, help="Launch package directory.")
    parser.add_argument(
        "--require-approved-review",
        action="store_true",
        help="Fail unless review-report.md exists and ends in an APPROVED decision.",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    package = Path(args.package)
    errors: list[str] = []
    warnings: list[str] = []

    try:
        payload = json.loads(input_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read input JSON: {exc}")
        return 2

    if not isinstance(payload, dict):
        print("ERROR: launch input must be a JSON object")
        return 2

    for field in sorted(REQUIRED_INPUT_FIELDS - payload.keys()):
        fail(errors, f"input is missing required field: {field}")

    author = payload.get("author")
    if not isinstance(author, dict):
        fail(errors, "author must be an object")
    else:
        for field in ("name", "voice", "approved_first_person_facts"):
            if field not in author:
                fail(errors, f"author is missing required field: {field}")

    facts = payload.get("source_facts")
    if not isinstance(facts, list) or not facts:
        fail(errors, "source_facts must contain at least one sourced or approved claim")
    else:
        for index, item in enumerate(facts, start=1):
            if not isinstance(item, dict) or not item.get("claim") or not item.get("source_url"):
                fail(errors, f"source_facts[{index}] needs claim and source_url")

    channels = set(payload.get("channels", []))
    locales = set(payload.get("locales", []))
    if "blog" in channels:
        for locale in locales:
            if not has_markdown(package / "blog" / locale):
                fail(errors, f"blog channel selected but no Markdown found for locale: {locale}")

    if "medium" in channels and "en" in locales and not has_markdown(package / "medium" / "en"):
        fail(errors, "medium channel selected but no English Medium draft exists")
    if "devto" in channels and "en" in locales and not has_markdown(package / "devto" / "en"):
        fail(errors, "devto channel selected but no English DEV Community draft exists")
    if "zhihu" in channels and "zh-CN" in locales and not has_markdown(package / "zhihu" / "zh-CN"):
        fail(errors, "zhihu channel selected but no Chinese Zhihu draft exists")
    if "xiaohongshu" in channels and "zh-CN" in locales and not has_markdown(package / "xiaohongshu" / "zh-CN"):
        fail(errors, "xiaohongshu channel selected but no Chinese article-screenshot carousel exists")

    if not (package / "launch-pack.md").exists():
        fail(errors, "launch-pack.md is missing")
    manifest = package / "manifest.json"
    if not manifest.exists():
        fail(errors, "manifest.json is missing")
    else:
        try:
            manifest_data = json.loads(manifest.read_text(encoding="utf-8"))
            if not isinstance(manifest_data, dict) or "canonical" not in manifest_data:
                fail(errors, "manifest.json must contain a canonical object")
        except (OSError, json.JSONDecodeError) as exc:
            fail(errors, f"manifest.json is invalid: {exc}")

    if not (package / "cover-url.json").exists():
        warnings.append("cover-url.json is missing; this is allowed only before visual generation")

    review_report = package / "review-report.md"
    if args.require_approved_review:
        if not review_report.exists():
            fail(errors, "review-report.md is missing; publication requires an approved independent review")
        else:
            report = review_report.read_text(encoding="utf-8")
            if "Status: APPROVED" not in report:
                fail(errors, "review-report.md does not contain `Status: APPROVED`")

    for message in warnings:
        print(f"WARNING: {message}")
    for message in errors:
        print(f"ERROR: {message}")
    if errors:
        return 1

    print(f"OK: {package} has a valid launch content package structure")
    return 0


if __name__ == "__main__":
    sys.exit(main())
