#!/usr/bin/env python3
"""Verifica higiene do índice Git: ausência de caches locais do Graphify e de paths absolutos da máquina."""

from __future__ import annotations

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

FORBIDDEN_EXACT = {
    "graphify-out/.graphify_python",
    "graphify-out/.graphify_root",
    "graphify-out/cost.json",
}
FORBIDDEN_PREFIXES = ("graphify-out/cache/",)

CODE_EXTENSIONS = {".py", ".js", ".ts", ".json", ".yml", ".yaml", ".css"}
LOCAL_PATH_RX = re.compile(
    r"(?:"
    + r"[A-Za-z]:" + r"\\" + r"Users" + r"\\"
    + r"|"
    + r"[A-Za-z]:/" + r"Users/"
    + r"|"
    + r"(?<![A-Za-z0-9._-])/" + r"Users/"
    + r")",
    re.IGNORECASE,
)


def git_tracked_files() -> list[str]:
    res = subprocess.run(
        ["git", "-c", "core.quotepath=false", "ls-files"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    return [line for line in res.stdout.splitlines() if line.strip()]


def main() -> int:
    tracked = git_tracked_files()
    violations: list[str] = []

    for rel in tracked:
        if rel in FORBIDDEN_EXACT or rel.startswith(FORBIDDEN_PREFIXES):
            violations.append(f"Arquivo de cache/ambiente local rastreado no Git: {rel}")
            continue

        file_path = ROOT / rel
        if not file_path.is_file() or file_path.suffix.lower() not in CODE_EXTENSIONS:
            continue

        lines = file_path.read_text(encoding="utf-8", errors="replace").splitlines()
        for line_no, line in enumerate(lines, 1):
            if LOCAL_PATH_RX.search(line):
                violations.append(f"Path local absoluto em {rel}:{line_no} -> {line.strip()[:120]}")

    print(f"Arquivos rastreados analisados: {len(tracked)}")
    if violations:
        print("VIOLACOES DE HIGIENE:")
        for v in violations:
            print(" -", v)
        return 1

    print("OK - 0 arquivos de cache/ambiente local ou paths absolutos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
