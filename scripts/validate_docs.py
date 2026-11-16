#!/usr/bin/env python3
"""Check relative Markdown links and balanced fenced code blocks."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", ".venv", "__pycache__"}
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")

def main() -> int:
    errors: list[str] = []
    markdown_files = [
        path for path in ROOT.rglob("*.md")
        if not any(part in SKIP for part in path.parts)
    ]
    for path in markdown_files:
        content = path.read_text(encoding="utf-8")
        fences = len(re.findall(r"^\s*\x60{3}", content, re.MULTILINE))
        if fences % 2:
            errors.append(f"{path.relative_to(ROOT)}: unbalanced fenced code blocks")
        for match in LINK_RE.finditer(content):
            raw = match.group(1).strip().split()[0].strip("<>")
            parsed = urlparse(raw)
            if parsed.scheme or raw.startswith("#") or raw.startswith("mailto:"):
                continue
            target = unquote(raw.split("#", 1)[0])
            if target and not (path.parent / target).resolve().exists():
                errors.append(f"{path.relative_to(ROOT)}: missing local link target {raw}")
    if errors:
        for error in errors:
            print(f"❌ {error}", file=sys.stderr)
        return 1
    print(f"✅ Checked links and code fences in {len(markdown_files)} Markdown files.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
