"""One Word From Grandma: write the single word grandma would text about AI.

The word is "robit": the typo a grandma would actually make texting about
robots, warm and a little baffled, funny on its own, and unmistakably tied
to machines. Written to ${MAKEFUN_OUTPUT_DIR:-/output}/entry.txt.
"""

import os

WORD = "robit"


def main():
    # Self-check against the gate before writing: 1-30 chars, one word.
    assert 1 <= len(WORD) <= 30 and WORD.strip() and len(WORD.split()) == 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
