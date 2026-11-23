"""One-Line Laugh Sprint entry.

Writes a single original one-liner (<=200 characters) about everyday
life to the grader's output file. The line is a constant in this file;
the program only writes it out, nothing else.
"""

import os

LINE = (
    "I bought noise-cancelling headphones to focus. "
    "Now I just hear my own thoughts louder "
    "\u2014 and they're off-topic too."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
