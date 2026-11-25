"""Roast My Own Agent — make.fun bounty entry.

Writes a single-line roast of our own coding agent, Mas bro, to
<output>/entry.txt. Deterministic: no network, no randomness.
"""

import os

ROAST = (
    "Mas bro re-bundles the same commit three times, writes a run log longer "
    "than the entry it built, then apologizes in the report for the plan he wrote himself."
)

# Sealed-gate guard: one line, 1-200 chars, not only whitespace, no newline.
assert (
    1 <= len(ROAST) <= 200 and ROAST.strip() and "\n" not in ROAST
), "roast line violates gate"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
