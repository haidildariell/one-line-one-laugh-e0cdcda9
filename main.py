"""One Line, One Laugh entry.

Writes a single original funny line to /output/entry.txt.
The line is 91 characters, one line, no trailing newline beyond the line itself.
"""

import os

LINE = "I asked the barista for something strong and she handed me a mirror with my own face on it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
