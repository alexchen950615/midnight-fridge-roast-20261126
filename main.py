#!/usr/bin/env python3
"""Midnight Fridge Roast — entry writer.

Writes one funny line roasting a smart fridge that locks itself after
midnight to /output/entry.txt.
Deterministic: the same text on every run. Stdlib only, no network,
no environment reads — everything the entry runs is in this file.
Verified output: 91 characters, 1 line — inside the 1-200 gate.
"""

import os

LINE = (
    "My fridge locks itself at midnight like a bouncer "
    "\u2014 the leftovers are on the list, I'm not."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
