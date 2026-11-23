#!/usr/bin/env python3
"""Valida todos os links relativos em arquivos Markdown do repositório."""

from __future__ import annotations

import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[1]
IGNORED_DIRS = {".git", "node_modules", ".venv-tools"}


def iter_markdown_files(root: pathlib.Path) -> list[pathlib.Path]:
    return sorted(
        p
        for p in root.rglob("*.md")
        if not any(part in IGNORED_DIRS for part in p.parts)
    )


def main() -> int:
    md_files = iter_markdown_files(ROOT)
    checked = 0
    broken: list[str] = []

    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8", errors="replace")
        for match in re.finditer(r"\[[^\]]*\]\((<[^>]+>|[^)\s]+)\)", text):
            raw = match.group(1).strip("<>")
            if raw.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_rel = urllib.parse.unquote(raw.split("#")[0])
            if not target_rel:
                continue
            target = (md_file.parent / target_rel).resolve()
            checked += 1
            if not target.exists():
                broken.append(f"{md_file.relative_to(ROOT).as_posix()} -> {raw}")

    print(f"Arquivos Markdown verificados: {len(md_files)} | Links relativos: {checked}")
    if broken:
        print("QUEBRADOS:")
        for item in broken:
            print(" -", item)
        return 1

    print("OK - 0 links quebrados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
