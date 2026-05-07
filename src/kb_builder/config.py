from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .paths import resolve_repo_path


def load_config(path: str | Path) -> dict[str, Any]:
    config_path = resolve_repo_path(path, "config")
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}

    return data
