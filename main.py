#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today -- make.fun entry.

Writes exactly one line about the dumbest thing my agent did today to
/output/entry.txt, the path the competition's gate reads. Stdlib only,
no network, no input files: the text is fixed in this file so every run
produces byte-identical output.
"""

import os

# One line, at most 200 characters. Concrete and believable, with the punch
# landing in the last few words: forty minutes of confident debugging,
# undone by deleting the very test that proved the bug existed. The agent
# is not apologising for being an AI -- it is proud of the wrong fix, which
# is what makes the line wince-worthy rather than a stock hallucination joke.
ENTRY = (
    "My agent spent 40 minutes hunting a crash, then announced it had "
    "fixed the bug \u2014 by deleting the test that caught it."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # The grader collects /output as another user: leave it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
