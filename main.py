"""Write the fortune cookie message to /output/entry.txt.

Single-line fortune for a software engineer, 76 characters, well inside
the 120-character gate. Stdlib only; no network.
"""

import os

ENTRY = "You will add one print statement, and the bug will hide until you remove it."

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Gate mirror: single line, 1-120 chars, not only whitespace."""
    if not 1 <= len(text) <= 120:
        raise ValueError("entry must be 1-120 characters, got %d" % len(text))
    if "\n" in text or not text.strip():
        raise ValueError("entry must be one non-blank line")
    return text


def write_entry(text, path=OUTPUT_PATH):
    """Write one validated line to the gate's output path."""
    validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
