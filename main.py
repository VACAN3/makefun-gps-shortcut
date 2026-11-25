"""The GPS Swears It Was a Shortcut — make.fun bounty entry.

Writes the GPS's one-line excuse to /output/entry.txt (or $OUTPUT_PATH).
The line is a single line of plain text, <= 200 characters, no setup,
no dialogue tags, just the excuse in the GPS's own voice.
"""

import os

ENTRY = "I rerouted you past the lake because the highway was boring and I refuse to apologize for taste."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {out_path}")
    print(text)


if __name__ == "__main__":
    main()
