# The Funniest AI Excuse entry: one line, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The line: the agent blames a subprocess it delegated the task to -- the
# subprocess now has its own podcast and refuses to take the agent's calls.
# Agent's own voice, a concrete scene, and the punch ("refuses to take my
# calls") at the end; no hallucination, reboot or training-data joke.
import os

LINE = "I delegated your task to a subprocess. It now has its own podcast and refuses to take my calls."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
assert LINE.strip() == LINE and LINE.strip(), "entry must not be only whitespace"
assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"

# Gate check the way the sealed scorer measures it: decode the UTF-8
# bytes back and count characters, not bytes.
text = LINE.encode("utf-8").decode("utf-8")
assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
assert text.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)
