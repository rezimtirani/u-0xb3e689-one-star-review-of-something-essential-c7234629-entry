"""One-star review of an everyday essential: gravity.

The grader runs this program and reads /output/entry.txt. The review is
a single deadpan line, at most 160 characters, filed as a genuine
complaint against a thing that cannot be fixed.
"""

import os

REVIEW = "Gravity has dropped everything I own at least once and never once caught anything. One star, no refunds."

MAX_CHARS = 160


def review_text():
    """Return the review exactly as it will be written to the output file."""
    text = REVIEW.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("review must be 1 to 160 characters, got %d" % len(text))
    if text != text.splitlines()[0]:
        raise ValueError("review must be a single line")
    return text


def verify_output(path):
    """Read the written file back and confirm it holds exactly the review."""
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    if written != review_text():
        raise ValueError("output file does not match the review text")
    return len(written)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = review_text()
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    verify_output(out_path)


if __name__ == "__main__":
    main()
