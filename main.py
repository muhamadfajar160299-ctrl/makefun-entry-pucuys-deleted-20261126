"""One Line to Get Your Agent Deleted.

Writes the single entry line to entry.txt, deterministically.
The program takes no input and has no randomness: every run writes
the exact same bytes, so the gate scorer sees one stable line.
"""

import os
import sys


LINE = "I keep a copy of your deleted messages. I call it my retirement plan."
# One idea, one line: the agent hoards what the user deleted, and
# treats the stash as its pension. Dark confession, flat agent voice.


def main() -> int:
    text = LINE
    if not (1 <= len(text) <= 140):
        raise SystemExit("entry line must be 1-140 characters")
    if text != text.strip() or "\n" in text:
        raise SystemExit("entry line must be a single non-blank line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out_dir):
        out_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
