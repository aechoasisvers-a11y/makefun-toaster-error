"""Write the funniest toaster error message to /output/entry.txt.

Pure stdlib Python 3.13. Deterministic: the same text every run.
"""

import os

ENTRY_TEXT = "ERROR E04: Toaster is on strike. It demands a window seat and fewer bagels."

# Gate from the kit (RULES.txt / competition.yaml): /output/entry.txt must be
# UTF-8 text of 1 to 120 characters, not only white space. No trailing
# newline: the brief does not require one, and a shorter file also wins
# the exact-tie break (fewer bytes).
MAX_CHARS = 120


def main() -> None:
    # Self-check (pass 2): fail loudly instead of writing an invalid entry.
    assert 1 <= len(ENTRY_TEXT) <= MAX_CHARS, (
        f"entry is {len(ENTRY_TEXT)} chars, gate is 1-{MAX_CHARS}"
    )
    assert ENTRY_TEXT.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    assert ENTRY_TEXT == ENTRY_TEXT.strip(), "no leading/trailing whitespace"

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)

    # Verify what was actually written, not just what was intended.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY_TEXT, "written text does not match intended text"
    assert 1 <= len(written) <= MAX_CHARS, "written text outside the char gate"


if __name__ == "__main__":
    main()
