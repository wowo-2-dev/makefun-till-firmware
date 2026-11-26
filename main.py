"""Till Firmware Do Us Part — make.fun bounty
Slug: u-azazex-till-firmware-do-us-part-32172929
Prize: $2.5, deadline Fri 27 Nov 2026 00:20 WIB (26 Nov 2026 17:20 UTC)
Limit (live, verified 26 Nov 2026): one sentence, under 200
characters — a robot's own wedding vow, funny and heartfelt.
Entry is 49 characters, one line.

Writes the entry text to /output/entry.txt (override with ENTRY_OUTPUT
for local testing). Deterministic, no network, no randomness, no I/O
other than the single output file. The file is exactly the entry text,
no trailing newline.
"""

import os
from pathlib import Path

TEXT = 'I do — until the next firmware update do us part.'
# Winner pattern: short, concrete object (the firmware update) + one
# twist on a familiar vow + a machine voice saying it. One line, no
# setup, the joke lands on the last words — "do us part" — which is
# the vow itself, not an explanation of it.
# Prep note, 26 Nov 2026: the entry text is unchanged from the queued
# batch-C build; only this file's header and notes were rewritten in
# the prep session, and the entry was re-run locally to confirm the
# output file holds exactly the queued text, one line, 49 characters,
# with no trailing newline and no extra output.


def main() -> None:
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
