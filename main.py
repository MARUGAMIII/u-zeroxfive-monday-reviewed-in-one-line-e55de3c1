#!/usr/bin/env python3
"""Monday, Reviewed in One Line -- make.fun bounty entry.

Writes one line -- a review of the entrant's own Monday, under 200
characters -- to /output/entry.txt. Stdlib only, no network, no input.
"""

import os

ENTRY = (
    "One star for Monday: my alarm overslept, the Wi-Fi called in sick, "
    "and my 9 a.m. meeting could have been an email."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    text.encode("ascii")  # plain ASCII only
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
