#!/usr/bin/env python3
"""Pigeon Pitch, One Line — entry program (u-donrulezz-pigeon-pitch-one-line-af06c6cf).

Writes one elevator pitch (a single line, <=200 characters, in English)
to /output/entry.txt. Deterministic: no randomness, no network, no input
from the environment beyond the output directory.
"""
import os

PITCH = (
    "Investors, I run StatueBnB \u2014 10,000 pigeons, zero rent, "
    "every bronze hero in town already our premium perch. "
    "We just need a seed round. Literally. Seed."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = PITCH.strip()
    assert 1 <= len(text) <= 200, f"pitch length {len(text)} out of range"
    assert "\n" not in text, "pitch must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read back and re-check: the file on disk must be exactly the pitch.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    assert written == text + "\n", "round-trip mismatch"
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
