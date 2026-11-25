#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — make.fun bounty
u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.

Writes a single-line software patch note for a bug in real life / human
biology, in the terse register of a real release note, to
/output/entry.txt.

The bug: the bladder only ever issues its low-battery warning five
minutes after the last rest stop is behind you. Deterministic, no
network, standard library only.
"""

import os
import sys

# The entry: one line, at most 160 characters, no trailing newline.
LINE = "v5.1.2: fixed a bug where the bladder issued its low-battery warning five minutes after the last rest stop."


def main() -> int:
    if len(LINE) > 160:
        print(f"entry is {len(LINE)} characters, over the 160 limit", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be blank", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
