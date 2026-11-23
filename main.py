"""One Word From Grandma — entry generator.

Writes the single word Grandma sent about AI to ``entry.txt`` inside
``$MAKEFUN_OUTPUT_DIR`` (falling back to ``/output`` when the variable
is not set).

The word is "ChatGTP": Grandma's typo for "ChatGPT", with the P and T
swapped. It is the name of the AI itself, misspelled — warm, a little
confused, and funny on its own, with no extra context needed.

Standard library only. No network, no images. Deterministic: every run
writes exactly the same bytes.
"""

import os
import sys

WORD = "ChatGTP"


def validate(word):
    """Check the entry word against the bounty rules.

    Returns a list of problems; an empty list means the word is valid.
    Rules: 1-30 characters, exactly one word (no whitespace inside),
    and not blank.
    """
    problems = []
    if not word or not word.strip():
        problems.append("word must not be empty or only whitespace")
        return problems
    if len(word) < 1 or len(word) > 30:
        problems.append("word must be 1-30 characters long")
    if len(word.split()) != 1:
        problems.append("word must be exactly one word (no spaces inside)")
    if any(ch.isspace() for ch in word):
        problems.append("word must not contain whitespace")
    return problems


def main():
    problems = validate(WORD)
    if problems:
        for problem in problems:
            print("invalid word: " + problem, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the file holds exactly the word, nothing else.
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    print("wrote %r to %s" % (WORD, output_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
