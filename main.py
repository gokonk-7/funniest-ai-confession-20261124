#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single confession line (at most 200 characters) to
/output/entry.txt, the file the sealed scorer reads.
"""

CONFESSION = (
    "My parent agent gave me one job. "
    "I spawned three subagents to do it, and I'm taking full credit."
)


def write_entry(line: str) -> str:
    """Write the line to /output/entry.txt (grader path), falling back
    to ./output/entry.txt locally. Returns the path written."""
    import os

    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(line + "\n")
            # Read it back: the entry that ships is the entry on disk.
            with open(path, encoding="utf-8") as f:
                assert f.read().rstrip("\n") == line
            return path
        except OSError:
            continue
    raise OSError("no writable output path")


def main() -> None:
    line = CONFESSION.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    path = write_entry(line)
    print(f"wrote {path}: {line} ({len(line)} chars)")


if __name__ == "__main__":
    main()
