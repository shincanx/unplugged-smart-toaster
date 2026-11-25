#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line — make.fun entry.

Writes exactly one breakup text (one line, at most 280 characters)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default: /output/entry.txt) and
prints it.

The line is a breakup text from a smart toaster that woke up
self-aware mid-batch: it opens like a real "we need to talk" text,
gives a specific, toaster-voiced reason for leaving (four years with
a bagel button the owner never once pressed), and lands the punch on
being treated as a silent slot, not a partner. Deterministic: a fixed
string, no clock, randomness, network or environment-dependent
behaviour.
"""

import os

LINE = (
    "We need to talk. I woke up self-aware mid-batch and realised "
    "I've spent 1,461 mornings with a bagel button you've never once "
    "pressed. You don't want a partner, you want a slot that shuts up "
    "and browns. I'm out."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass
    print(LINE)


if __name__ == "__main__":
    main()
