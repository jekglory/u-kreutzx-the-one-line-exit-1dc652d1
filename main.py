"""The One-Line Exit: a one-line resignation letter, written to entry.txt.

The brief asks for exactly one line that reads like a letter a person
could actually send, with the joke landing inside that single line.
The voice is an office worker whose daily nemesis is the shared printer:
the resignation turns on the printer jamming one last time, and the
worker admitting, in the same breath, that they have jammed too.
"""

import os

LINE = "I resign: the printer has jammed for the last time, and frankly, so have I."


def validate(line: str) -> None:
    """Enforce the competition's gate: 1-140 chars, exactly one line."""
    if not line.strip():
        raise ValueError("entry is blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 140:
        raise ValueError(f"entry is {len(line)} chars, gate allows 1-140")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    print(f"wrote {len(LINE)} chars + newline to {path} (1 line, gate 1-140)")


if __name__ == "__main__":
    main()
