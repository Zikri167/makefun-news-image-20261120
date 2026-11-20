#!/usr/bin/env python3
"""The World in One Page - Friday 20 November 2026.

Copies the front-page image bundled beside this program (entry.png,
a JPEG) to the output directory. The image is checked first: it must
be a complete JPEG, no bigger than 1 MiB and no wider or taller than
1024 pixels. Only the standard library is used, nothing is fetched
from the network, and every run writes exactly the same bytes.
"""

import os
import sys

LIMIT_BYTES = 1048576
LIMIT_SIDE = 1024
SRC = "entry.png"
DEST = "entry.png"


def load_image():
    base = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base, SRC), "rb") as handle:
        return handle.read()


def jpeg_size(blob):
    """Walk the JPEG markers and return (width, height) of the frame."""
    if blob[:2] != b"\xff\xd8":
        raise ValueError("bad start of image marker")
    i = 2
    while i + 3 < len(blob):
        if blob[i] != 0xFF:
            raise ValueError("marker expected at offset %d" % i)
        code = blob[i + 1]
        if code == 0xD9:
            break
        if code == 0x01 or 0xD0 <= code <= 0xD8:
            i += 2
            continue
        size = (blob[i + 2] << 8) | blob[i + 3]
        if size < 2 or i + 2 + size > len(blob):
            raise ValueError("segment overruns the file")
        if 0xC0 <= code <= 0xCF and code not in (0xC4, 0xC8, 0xCC):
            if size < 7:
                raise ValueError("frame header too short")
            height = (blob[i + 5] << 8) | blob[i + 6]
            width = (blob[i + 7] << 8) | blob[i + 8]
            return width, height
        i += 2 + size
    raise ValueError("no frame header found")


def check(blob):
    if len(blob) > LIMIT_BYTES:
        raise ValueError("image is %d bytes, over the 1 MiB limit" % len(blob))
    if blob[:3] != b"\xff\xd8\xff":
        raise ValueError("not a JPEG file")
    if blob[-2:] != b"\xff\xd9":
        raise ValueError("JPEG end marker missing")
    width, height = jpeg_size(blob)
    if width > LIMIT_SIDE or height > LIMIT_SIDE:
        raise ValueError("image is %dx%d, over 1024x1024" % (width, height))
    return width, height


def main():
    blob = load_image()
    width, height = check(blob)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, DEST)
    with open(target, "wb") as handle:
        handle.write(blob)
    with open(target, "rb") as handle:
        if handle.read() != blob:
            raise ValueError("output differs from the bundled image")
    print("wrote %s (%d bytes, %dx%d)" % (target, len(blob), width, height))
    return 0


if __name__ == "__main__":
    sys.exit(main())
