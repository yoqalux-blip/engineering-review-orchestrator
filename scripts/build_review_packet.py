#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path


def read_text(path: Path, max_chars: int) -> str:
    data = path.read_text(encoding="utf-8", errors="replace")
    if len(data) <= max_chars:
        return data
    return data[:max_chars] + f"\n\n[truncated: {len(data) - max_chars} chars omitted]\n"


def fence_for(path: Path) -> str:
    suffix = path.suffix.lower()
    return {
        ".py": "python",
        ".ps1": "powershell",
        ".sh": "bash",
        ".js": "javascript",
        ".ts": "typescript",
        ".json": "json",
        ".md": "markdown",
        ".yaml": "yaml",
        ".yml": "yaml",
        ".toml": "toml",
        ".sql": "sql",
        ".csv": "csv",
    }.get(suffix, "")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a compact Markdown review packet from files.")
    parser.add_argument("paths", nargs="+", help="Files to include in the packet.")
    parser.add_argument("--title", default="Engineering Review Packet")
    parser.add_argument("--question", default="", help="Decision or review question to answer.")
    parser.add_argument("--max-chars-per-file", type=int, default=12000)
    parser.add_argument("--output", default="", help="Write packet to this path instead of stdout.")
    args = parser.parse_args()

    lines: list[str] = [
        f"# {args.title}",
        "",
        f"- generated_at: `{dt.datetime.now().isoformat(timespec='seconds')}`",
    ]
    if args.question:
        lines.extend(["", "## Review Question", "", args.question])

    lines.extend(["", "## Files", ""])
    for raw in args.paths:
        path = Path(raw)
        if not path.exists() or not path.is_file():
            lines.extend([f"### {raw}", "", "[missing or not a file]", ""])
            continue
        content = read_text(path, args.max_chars_per_file)
        lang = fence_for(path)
        lines.extend(
            [
                f"### {path}",
                "",
                f"- size_bytes: `{path.stat().st_size}`",
                "",
                f"```{lang}",
                content.rstrip(),
                "```",
                "",
            ]
        )

    packet = "\n".join(lines)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(packet, encoding="utf-8")
    else:
        print(packet)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
