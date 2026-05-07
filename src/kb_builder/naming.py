from __future__ import annotations

import re


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = value.replace("&", "and")
    value = re.sub(r"[^a-z0-9.]+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-")


def make_id_slug_filename(canonical_id: str, name: str) -> str:
    return f"{canonical_id}-{slugify(name)}.md"


def strip_md(path: str) -> str:
    if path.endswith(".md"):
        return path[:-3]
    return path
