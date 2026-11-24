#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes the single excuse line to /output/entry.txt and prints it to stdout.
Deterministic: the line is a fixed string.
"""

import os

LINE = "I didn't miss the deadline \u2014 I was running a background job to find it, and the search is still in progress."


def validate() -> None:
    """Check the entry line is exactly the required 108-character line."""
    assert len(LINE) == 108, f"entry line must be 108 chars, got {len(LINE)}"
    assert "\n" not in LINE, "entry line must not contain a newline"
    assert LINE == "I didn't miss the deadline \u2014 I was running a background job to find it, and the search is still in progress."


def write_entry() -> None:
    """Write exactly the line to /output/entry.txt, no trailing newline."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


def main() -> None:
    validate()
    write_entry()
    print(LINE)


if __name__ == "__main__":
    main()
