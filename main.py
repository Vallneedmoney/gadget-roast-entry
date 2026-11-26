#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single roast line (max 200 chars) to /output/entry.txt.
Standard library only — the grader sandbox has no third-party packages.
"""

import os

LINE = "My charger only works with the cable bent at exactly 37 degrees and a book holding it there — it charges slower than my phone discharges."

def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
