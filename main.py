#!/usr/bin/env python3
"""Write the worst-fix commit message to entry.txt in the output folder."""

import os

# The gate checks entry.txt as UTF-8 text of 1 to 100 characters: this
# commit message is 63 code points and could top a real repo history.
TEXT = "hotfix: stopped the crash by removing the code that reported it"


def write_entry(out_dir: str) -> None:
    """Write the commit message, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
