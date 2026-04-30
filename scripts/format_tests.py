#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Normalisiert Test- und Loesungs-Markdown fuer stabiles Word Copy/Paste.

Anwendung:
    python3 scripts/format_tests.py
    python3 scripts/format_tests.py tests/pfad/datei.md
    python3 scripts/format_tests.py loesungen/pfad/datei.md

Verhalten:
1. Konvertiert Markdown-Tabellen in einheitliche HTML-Tabellen mit sichtbaren Rastern.
2. Lässt Fliesstext, Code-Bloecke und bestehendes HTML ansonsten unveraendert.
3. Ist idempotent: Mehrfaches Ausfuehren fuehrt nicht zu weiterem Layout-Drift.
"""

import html
import re
import sys
from pathlib import Path

TABLE_STYLE = (
    'style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; font-size: 11pt;"'
)
TH_STYLE = (
    'style="border: 1px solid #000000; padding: 6px 10px; background-color: #dde3ea; '
    'text-align: left; font-weight: bold;"'
)
TD_STYLE = (
    'style="border: 1px solid #000000; padding: 6px 10px; text-align: left; vertical-align: top;"'
)


def _parse_cells(line: str) -> list[str]:
    cells = [c.strip() for c in line.strip().split("|")]
    if cells and cells[0] == "":
        cells = cells[1:]
    if cells and cells[-1] == "":
        cells = cells[:-1]
    return cells


def _is_separator_row(cells: list[str]) -> bool:
    if not cells:
        return False
    return all(re.fullmatch(r"[:\- ]+", c) for c in cells)


def _to_html_table(markdown_table_lines: list[str]) -> list[str]:
    rows: list[list[str]] = []
    header: list[str] | None = None

    for line in markdown_table_lines:
        cells = _parse_cells(line)
        if not cells:
            continue
        if _is_separator_row(cells):
            if rows:
                header = rows.pop()
            continue
        rows.append(cells)

    if not rows and not header:
        return markdown_table_lines

    out = [f"<table {TABLE_STYLE}>"]
    if header:
        out.append("  <thead>")
        out.append("    <tr>")
        for cell in header:
            out.append(f"      <th {TH_STYLE}>{html.escape(cell)}</th>")
        out.append("    </tr>")
        out.append("  </thead>")

    out.append("  <tbody>")
    for row in rows:
        out.append("    <tr>")
        for cell in row:
            out.append(f"      <td {TD_STYLE}>{html.escape(cell)}</td>")
        out.append("    </tr>")
    out.append("  </tbody>")
    out.append("</table>")
    return out


def process_file(path: Path) -> None:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()

    result: list[str] = []
    table_buffer: list[str] = []
    in_code_block = False
    fence = ""

    for line in lines:
        fence_match = re.match(r"^(`{3,}|~{3,})", line)
        if fence_match:
            marker = fence_match.group(1)
            if table_buffer:
                result.extend(_to_html_table(table_buffer))
                table_buffer = []

            if not in_code_block:
                in_code_block = True
                fence = marker
            elif line.startswith(fence):
                in_code_block = False
                fence = ""

            result.append(line)
            continue

        if not in_code_block and line.strip().startswith("|"):
            table_buffer.append(line)
            continue

        if table_buffer:
            result.extend(_to_html_table(table_buffer))
            table_buffer = []

        result.append(line)

    if table_buffer:
        result.extend(_to_html_table(table_buffer))

    normalized = "\n".join(result).rstrip() + "\n"
    if normalized != original:
        path.write_text(normalized, encoding="utf-8")
        print(f"  ✓  {path}")
    else:
        print(f"  ·  {path} (keine Aenderung)")


def _default_targets(repo_root: Path) -> list[Path]:
    tests = sorted(repo_root.glob("tests/**/*.md"))
    solutions = sorted(repo_root.glob("loesungen/**/*.md"))
    return tests + solutions


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    targets = [Path(arg) for arg in sys.argv[1:]] if len(sys.argv) > 1 else _default_targets(repo_root)

    if not targets:
        print("Keine Markdown-Dateien gefunden.")
        return

    print(f"Verarbeite {len(targets)} Datei(en) ...")
    for target in targets:
        path = target if target.is_absolute() else repo_root / target
        try:
            process_file(path)
        except Exception as exc:
            print(f"  ✗  {path}: {exc}")

    print("\nFertig.")


if __name__ == "__main__":
    main()
