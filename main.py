#!/usr/bin/env python3
"""Rename the Planet — one funny new name for Mercury plus the why (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 136 characters, no
trailing newline).
"""

import os

ENTRY = "Rename Mercury 'The Encore' — the Sun rises, sets, then rises again in the same morning, so dawn there always gets a second performance."
OUT_PATH = "/output/entry.txt"


def main():
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
