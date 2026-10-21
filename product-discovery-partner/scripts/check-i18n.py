#!/usr/bin/env python3
"""Check that English references stay in sync with the canonical Chinese files.

Usage:
    python3 scripts/check-i18n.py
    python3 scripts/check-i18n.py --update

The manifest stores a SHA-256 of each canonical file at translation time. When a
canonical file changes, the check fails until the English translation is updated
and the manifest is refreshed with --update.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFS = ROOT / "references"
EN = REFS / "en"
MANIFEST = REFS / "i18n-manifest.json"

FENCE_RE = re.compile(r"^\s*(```|~~~)")
HEADING_RE = re.compile(r"^(#{1,6})\s+\S")


def strip_fenced_blocks(text: str) -> str:
    """Blank out fenced code blocks so headings inside them are ignored."""
    output: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            output.append("")
            continue
        output.append("" if in_fence else line)
    return "\n".join(output)


def heading_levels(text: str) -> list[int]:
    levels: list[int] = []
    for line in strip_fenced_blocks(text).splitlines():
        match = HEADING_RE.match(line)
        if match:
            levels.append(len(match.group(1)))
    return levels


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def canonical_files() -> list[Path]:
    files: list[Path] = []
    for path in sorted(REFS.rglob("*.md")):
        rel = path.relative_to(REFS)
        if rel.parts and rel.parts[0] == "en":
            continue
        files.append(rel)
    return files


def load_manifest() -> dict:
    if not MANIFEST.exists():
        return {"canonical_language": "zh", "translations": {"en": {}}}
    with MANIFEST.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_manifest(manifest: dict) -> None:
    with MANIFEST.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--update",
        action="store_true",
        help="Refresh manifest hashes after updating English translations.",
    )
    args = parser.parse_args()

    manifest = load_manifest()
    translations = manifest.setdefault("translations", {}).setdefault("en", {})
    files = canonical_files()
    errors: list[str] = []
    current_keys: set[str] = set()
    new_translations: dict[str, dict] = {}

    for rel in files:
        key = rel.as_posix()
        current_keys.add(key)
        source_path = REFS / rel
        target_path = EN / rel
        source_text = source_path.read_text(encoding="utf-8")

        if not target_path.exists():
            errors.append(f"missing English translation: references/en/{key}")
            continue

        target_text = target_path.read_text(encoding="utf-8")
        if not target_text.strip():
            errors.append(f"empty English translation: references/en/{key}")
            continue

        source_headings = heading_levels(source_text)
        target_headings = heading_levels(target_text)
        if source_headings != target_headings:
            errors.append(
                "heading structure differs: "
                f"{key}\n"
                f"    zh: {source_headings}\n"
                f"    en: {target_headings}"
            )

        digest = sha256(source_text)
        if args.update:
            new_translations[key] = {
                "source": key,
                "source_sha256": digest,
                "translated_at": date.today().isoformat(),
            }
        else:
            entry = translations.get(key)
            if not entry:
                errors.append(f"missing manifest entry: {key}")
            elif entry.get("source_sha256") != digest:
                errors.append(
                    f"stale translation: {key} (source changed; update the English file and run --update)"
                )

    extra = sorted(set(translations) - current_keys)
    if not args.update:
        for key in extra:
            errors.append(f"manifest entry has no canonical source: {key}")

    if args.update and not errors:
        manifest["canonical_language"] = "zh"
        manifest["translations"]["en"] = new_translations
        write_manifest(manifest)
        print(f"Updated {MANIFEST.relative_to(ROOT)} for {len(files)} canonical files.")
    elif args.update:
        print("Manifest not updated because errors were found.", file=sys.stderr)

    if errors:
        print("i18n check failed:\n", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"i18n check passed: {len(files)} canonical files and English translations are in sync.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
