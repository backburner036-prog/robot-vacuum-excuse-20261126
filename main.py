#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse — make.fun entry.

Writes exactly one excuse line to /output/entry.txt.
Deterministic: the same line on every run, no randomness,
no network access, no input.
"""

from pathlib import Path

EXCUSE = "I saw the crumb, weighed my options, and chose peace. It was a good crumb."

# Bounty cap: a single line of at most 120 characters.
assert len(EXCUSE.encode("utf-8")) <= 120, "excuse exceeds the 120-character cap"
assert "\n" not in EXCUSE, "excuse must be a single line"


def main():
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(EXCUSE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
