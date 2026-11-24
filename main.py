"""Fortune Cookie Wisdom for Developers.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line (97 chars, no trailing newline):

    The code you curse today was written by someone who loved it
    once; tomorrow, that someone is you.

Why this line: the tired-senior-engineer truth is that every reviewer
becomes the legacy author. The fortune is built in two balanced
halves -- today / tomorrow -- classic fortune-cookie parallelism. The
second read pays off: the reader is both the one cursing the code and
the one who will be cursed for it. It is a fortune, not a joke: no
punchline, no reheated saying ("it works on my machine" and friends
were all avoided).

Gate (from the competition kit): /output/entry.txt must be UTF-8 text
of 1 to 120 characters, not only whitespace. The program checks the
line against that gate before writing, and writes it with no trailing
newline so the file is exactly the line, 97 bytes.

Deterministic: no clock, no random source, no network, no input. The
same line is written on every run.
"""

import os
import sys

LINE = (
    "The code you curse today was written by someone who loved it "
    "once; tomorrow, that someone is you."
)


def main() -> int:
    # Gate-check before writing: UTF-8, 1-120 chars, not only whitespace.
    if not (1 <= len(LINE) <= 120):
        print(f"gate: line is {len(LINE)} chars, must be 1-120", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("gate: line is only whitespace", file=sys.stderr)
        return 1
    try:
        LINE.encode("utf-8")
    except UnicodeEncodeError:
        print("gate: line is not UTF-8", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the line, 97 bytes.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
