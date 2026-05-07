from __future__ import annotations


def wikilink(path_without_md: str, alias: str | None = None) -> str:
    if alias:
        return f"[[{path_without_md}|{alias}]]"
    return f"[[{path_without_md}]]"
