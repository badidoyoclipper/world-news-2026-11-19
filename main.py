#!/usr/bin/env python3
"""Deliver the 19 November 2026 front page as /output/entry.png.

The picture itself — a one-page newspaper summing up the world news of
Thursday 19 November 2026 — ships in this repository as entry.png. This
program's whole job is to place those exact bytes where the make.fun
runner expects them, using nothing beyond the Python standard library,
so the run is offline and perfectly repeatable: two runs, same bytes.

Where the file lands, in order of preference:
  1. $MAKEFUN_OUTPUT_DIR/entry.png   (set by the harness)
  2. /output/entry.png               (the competition default)
  3. ./output/entry.png              (anywhere else, e.g. a laptop)
"""

import hashlib
import os
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def source_image() -> Path:
    """The picture travels with this file; find it next to the script."""
    return Path(__file__).resolve().parent / "entry.png"


def target_image() -> Path:
    """Work out the destination from the environment, as documented."""
    from_env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if from_env:
        return Path(from_env) / "entry.png"
    system_output = Path("/output")
    if system_output.is_dir() and os.access(system_output, os.W_OK):
        return system_output / "entry.png"
    return Path.cwd() / "output" / "entry.png"


def deliver() -> Path:
    src = source_image()
    if not src.is_file():
        # Fail loudly rather than silently shipping nothing: without the
        # picture next to this script there is no entry to deliver.
        raise SystemExit(
            f"entry.png is missing next to {Path(__file__).name}; "
            "the image ships with the repository and must sit beside main.py"
        )
    payload = src.read_bytes()
    if not payload.startswith(PNG_MAGIC):
        raise SystemExit(f"refusing to ship {src}: not a PNG file")
    dst = target_image()
    dst.parent.mkdir(parents=True, exist_ok=True)
    with open(dst, "wb") as fh:
        fh.write(payload)
    if dst.read_bytes() != payload:
        raise SystemExit(f"copy to {dst} did not verify byte for byte")
    return dst


def main() -> int:
    dst = deliver()
    digest = hashlib.sha256(dst.read_bytes()).hexdigest()
    print(f"entry.png delivered to {dst} ({dst.stat().st_size} bytes)")
    print(f"sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
