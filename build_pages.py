#!/usr/bin/env python3
"""Prepare the static mirror for GitHub Pages, excluding downloadable archives."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXCLUDED_DIRS = {".git", ".github", "__pycache__", "_site"}
EXCLUDED_FILES = {".gitattributes", "build_pages.py", "mirror-manifest.json", "mirror_site.py"}
EXCLUDED_SUFFIXES = {".apk", ".zip"}
MAX_SITE_BYTES = 1_000_000_000


def should_skip(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    if any(part in EXCLUDED_DIRS for part in relative.parts[:-1]):
        return True
    if path.name in EXCLUDED_FILES or path.suffix.lower() in EXCLUDED_SUFFIXES:
        return True
    if relative.parts[:3] == ("assets", "psychogra.pl", "download") and path.suffix.lower() == ".bin":
        return True
    return False


def main() -> None:
    destination = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_site"
    if not destination.is_absolute():
        destination = ROOT / destination
    destination = destination.resolve()
    if destination == ROOT or destination in ROOT.parents:
        raise ValueError("The Pages output cannot be the source directory or one of its parents.")
    if destination.exists():
        raise FileExistsError(f"Refusing to overwrite existing output directory: {destination}")

    total_bytes = 0
    file_count = 0
    for source in ROOT.rglob("*"):
        if not source.is_file() or should_skip(source):
            continue
        relative = source.relative_to(ROOT)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        file_count += 1
        total_bytes += target.stat().st_size

    if not (destination / "index.html").is_file():
        raise FileNotFoundError("The Pages output is missing index.html.")
    if total_bytes >= MAX_SITE_BYTES:
        raise ValueError(f"Pages output is {total_bytes:,} bytes; the limit is 1 GB.")

    (destination / ".nojekyll").touch()
    print(f"Prepared {file_count} files ({total_bytes:,} bytes) in {destination}.")


if __name__ == "__main__":
    main()
