from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class ProjectPaths:
    vault_path: Path
    cache_path: Path
    log_path: Path


def repo_root() -> Path:
    return Path.cwd().resolve()


def resolve_repo_path(value: str | Path, label: str) -> Path:
    path = Path(value)

    if ".." in path.parts:
        raise ValueError(f"{label} must not contain parent-directory segments: {value}")

    if not path.is_absolute():
        path = repo_root() / path

    resolved = path.resolve()
    root = repo_root()

    if resolved != root and root not in resolved.parents:
        raise ValueError(f"{label} must stay inside the repository: {value}")

    return resolved


def ensure_project_paths(config: dict[str, Any]) -> ProjectPaths:
    vault_path = resolve_repo_path(config.get("vault_path", "./vault"), "vault_path")
    cache_path = resolve_repo_path(config.get("cache", {}).get("dir", ".cache"), "cache.dir")
    log_path = resolve_repo_path(config.get("logging", {}).get("log_dir", ".logs"), "logging.log_dir")

    required_dirs = [
        vault_path,
        vault_path / "kb",
        vault_path / "kb" / "_build",
        vault_path / "kb" / "mitre",
        vault_path / "kb" / "mitre" / "attack",
        vault_path / "kb" / "mitre" / "attack" / "tactics",
        vault_path / "kb" / "mitre" / "attack" / "techniques",
        vault_path / "kb" / "mitre" / "attack" / "mitigations",
        vault_path / "kb" / "mitre" / "attack" / "data-sources",
        vault_path / "kb" / "mitre" / "attack" / "software",
        vault_path / "kb" / "mitre" / "attack" / "indexes",
        vault_path / "kb" / "lolbas",
        vault_path / "kb" / "lolbas" / "tools",
        vault_path / "kb" / "gtfobins",
        vault_path / "kb" / "gtfobins" / "tools",
        vault_path / "kb" / "indexes",
        cache_path,
        cache_path / "mitre",
        log_path,
    ]

    for directory in required_dirs:
        directory.mkdir(parents=True, exist_ok=True)

    return ProjectPaths(vault_path=vault_path, cache_path=cache_path, log_path=log_path)
