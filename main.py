"""One Word From Grandma — entrypoint.

Writes the single word Grandma would text about AI to /output/entry.txt.

The grader runs this program with no arguments in a sandbox with no
network. It must be deterministic: the same word, byte for byte, on
every run. It reads nothing from the environment, the network or any
file outside this repository — the word lives in word.py, next to it.
"""

import os
import sys

from word import WORD

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 30


def validate(word: str) -> str:
    """Check the word against the competition gate before writing it."""
    if not isinstance(word, str):
        raise ValueError("word must be a string")
    if not word or word.strip() == "":
        raise ValueError("word must not be empty or only whitespace")
    if len(word) > MAX_CHARS:
        raise ValueError(f"word is {len(word)} characters, gate allows at most {MAX_CHARS}")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word, no whitespace")
    word.encode("utf-8")  # gate requires UTF-8 text
    return word


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    # Optional first argument overrides the output path for local runs
    # (e.g. `python3 main.py /tmp/out/entry.txt`); the grader runs with
    # no arguments and the word lands at /output/entry.txt.
    out_path = argv[0] if argv else OUTPUT_PATH
    word = validate(WORD)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    # Read it back: the file the judge sees must be exactly the word,
    # byte for byte, with no trailing newline or stray whitespace.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != word:
        raise RuntimeError(f"wrote {written!r}, expected {word!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
