#!/usr/bin/env python3
"""Extract time signatures from kern files across all sources and output a CSV."""

import csv
import re
import sys
from pathlib import Path


def get_field(lines: list[str], tag: str) -> str:
    for line in lines:
        if line.startswith(tag):
            return line[len(tag):].strip()
    return ""


def get_time_signatures(lines: list[str]) -> list[str]:
    seen = []
    for line in lines:
        # Match *M followed by time sig, tab-separated spines — grab first token
        token = line.split("\t")[0]
        m = re.match(r"^\*M(\d+/\d+)$", token)
        if m:
            sig = m.group(1)
            if sig not in seen:
                seen.append(sig)
    return seen


def main():
    repo_root = Path(__file__).parent.parent
    rows = []

    for kern_dir in sorted(repo_root.glob("*/kern")):
        source = kern_dir.parent.name
        krn_files = sorted(kern_dir.glob("*.krn"))
        if not krn_files:
            continue

        for krn_file in krn_files:
            lines = krn_file.read_text(encoding="utf-8").splitlines()

            song_id = (
                get_field(lines, "!!!id: ")
                or get_field(lines, "!!!id:")
                or krn_file.stem
            )
            title = (
                get_field(lines, "!!!OTL@@FR:")
                or get_field(lines, "!!!OTL:")
                or ""
            )
            time_sigs = get_time_signatures(lines)

            rows.append({
                "source": source,
                "id": song_id,
                "title": title,
                "time_signatures": "; ".join(time_sigs) if time_sigs else "",
            })

    writer = csv.DictWriter(
        sys.stdout,
        fieldnames=["source", "id", "title", "time_signatures"],
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(rows)


if __name__ == "__main__":
    main()
