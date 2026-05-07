from __future__ import annotations

from pathlib import Path
from typing import Iterable


def generated_marker_text(marker: str) -> str:
    return f"generated_by: {marker}"


def is_generated_file(path: Path, marker: str) -> bool:
    if not path.exists() or not path.is_file():
        return False

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False

    return generated_marker_text(marker) in text


def safe_write_text(path: Path, content: str, marker: str, logger=None) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists() and not is_generated_file(path, marker):
        if logger:
            logger.warning(f"Skipped {path} because it does not contain generated_by marker")
        return False

    path.write_text(content, encoding="utf-8")
    return True


def clean_generated_markdown(roots: Iterable[Path], marker: str, logger=None) -> int:
    deleted = 0

    for root in roots:
        if not root.exists():
            continue

        for path in root.rglob("*.md"):
            if is_generated_file(path, marker):
                path.unlink()
                deleted += 1
                if logger:
                    logger.debug(f"Deleted generated file: {path}")

    return deleted
