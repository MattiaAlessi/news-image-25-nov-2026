"""Write the picture of 25 November 2026 to /output/entry.png.

The front page was drawn ahead of time and ships beside this file; the program
copies it out unchanged, so both of its runs write the same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT = "/output/entry.png"


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    os.chmod(OUTPUT, 0o644)


if __name__ == "__main__":
    main()
