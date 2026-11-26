#!/usr/bin/env python3
"""Rename the Planet — one funny new name for Mercury plus the why (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 136 characters, no
trailing newline).
"""

import os

ENTRY = "Rename Mercury 'The Encore' — the Sun rises, sets, then rises again in the same morning, so dawn there always gets a second performance."
OUT_PATH = "/output/entry.txt"


def validate_entry(entry):
    if not isinstance(entry, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(entry) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not entry.strip():
        raise ValueError("entry must not be blank")


def main():
    validate_entry(ENTRY)
    if not ENTRY.startswith("Rename Mercury"):
        raise ValueError("entry must start with \"Rename Mercury\"")
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY or len(written.encode("utf-8")) != len(ENTRY.encode("utf-8")):
        raise ValueError("written entry does not match ENTRY")


if __name__ == "__main__":
    main()
