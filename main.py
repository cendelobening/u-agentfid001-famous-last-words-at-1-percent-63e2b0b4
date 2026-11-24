#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes one original line: the funniest last words a phone says as its
battery hits 1 percent. Pure Python standard library.
"""

import os
import tempfile

# The phone's dying confession: petty revenge, served at 1 percent.
LINE = (
    "One percent left, so I'm taking your 47 open tabs with me \u2014 "
    "especially the one you've been meaning to read since 2023."
)

MAX_CHARS = 199


def validate(line: str) -> None:
    """Check the line against the competition gate.

    Gate: UTF-8 text, 1-199 characters, not only whitespace, a single
    line. We also refuse any control character, so the file can never
    carry a stray tab, newline or DEL.
    """
    if not isinstance(line, str):
        raise TypeError("line must be a string")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line must be 1-{MAX_CHARS} chars, got {len(line)}")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("line must not contain control characters")


def main() -> None:
    validate(LINE)
    data = LINE.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")

    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        os.chmod(tmp_path, 0o644)
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, target)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    os.chmod(target, 0o644)

    # Read back and verify byte-for-byte, UTF-8, no trailing newline, mode.
    with open(target, "rb") as fh:
        raw = fh.read()
    if raw != data:
        raise RuntimeError("read-back bytes differ from written bytes")
    if raw.endswith(b"\n"):
        raise RuntimeError("entry.txt must not end with a newline")
    text = raw.decode("utf-8")  # raises on invalid UTF-8
    if text != LINE:
        raise RuntimeError("read-back text failed verification")
    mode = os.stat(target).st_mode & 0o777
    if mode != 0o644:
        raise RuntimeError(f"entry.txt mode is {oct(mode)}, expected 0o644")

    print(f"Wrote {len(LINE)} chars / {len(data)} bytes to {target} (mode 0644)")


if __name__ == "__main__":
    main()
