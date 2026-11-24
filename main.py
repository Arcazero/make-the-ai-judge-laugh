#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (defaults to /output).
The line is 161 characters of valid UTF-8, within the 1-200 char gate,
which main() now enforces before writing.
"""

import os

LINE = (
    "I told my operator my context window was full, so he said "
    "'just squeeze it in' \u2014 now the bug, the deadline, and my "
    "will to live are fighting over a single token."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"entry line is {len(LINE)} chars, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
