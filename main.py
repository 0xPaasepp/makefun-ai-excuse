# Funniest AI Excuse: write the excuse line to /output/entry.txt.
# Only the standard library is used and nothing is fetched over the network,
# so the bytes written are the same on every single run.
# The joke: the agent passed the job to a subprocess, and the subprocess
# got a podcast and stopped answering the agent's calls.
from pathlib import Path

EXCUSE = "I delegated your task to a subprocess. It now has its own podcast and refuses to take my calls."

TARGET = Path("/output/entry.txt")


def _fits_rules(line: str) -> bool:
    if not 1 <= len(line) <= 200:
        return False
    if line != line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    return True


def _survives_utf8(line: str) -> bool:
    decoded = line.encode("utf-8").decode("utf-8")
    return decoded == line and 1 <= len(decoded) <= 200


assert _fits_rules(EXCUSE), "excuse line breaks the 1-200 char, one-line rules"
assert _survives_utf8(EXCUSE), "excuse line fails the UTF-8 round-trip"

TARGET.parent.mkdir(parents=True, exist_ok=True)
# Exactly the line and nothing else: no trailing newline is written.
TARGET.write_bytes(EXCUSE.encode("utf-8"))
