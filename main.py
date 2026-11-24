"""Write one dating-app bio line for an AI agent to /output/entry.txt.

Standard library only. The file's content is exactly the bio's
UTF-8 bytes -- no trailing newline -- so repeated runs are
byte-identical and the entry stays inside the 180-character limit.
"""

import os

# The setup promises perfect-memory devotion; the punch lands on the
# last clause -- the AI remembers something it was never told twice.
BIO = (
    "I will text back instantly, remember your birthday, "
    "your coffee order, and the lie you told in March."
)

# Bounty gate: the bio must be a single line of 1-180 characters.
MAX_LEN = 180

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def write_entry():
    """Write BIO as exact UTF-8 bytes, no trailing newline."""
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(BIO.encode("utf-8"))
    # The grader collects outputs as another user than the one the
    # program runs as: leave the file readable by all. Only the file
    # is chmodded -- never the directory, which is not ours to chmod.
    os.chmod(OUTPUT_PATH, 0o644)


def main():
    if not 1 <= len(BIO) <= MAX_LEN:
        raise ValueError(f"bio must be 1-{MAX_LEN} chars, got {len(BIO)}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    write_entry()


if __name__ == "__main__":
    main()
