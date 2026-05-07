from __future__ import annotations

import json
from typing import Any

import requests

from .paths import ProjectPaths, resolve_repo_path


def load_or_fetch_mitre(config: dict[str, Any], paths: ProjectPaths, logger) -> dict[str, Any]:
    mitre_config = config.get("sources", {}).get("mitre", {})
    cache_config = config.get("cache", {})

    local_path = mitre_config.get("local_path")
    if local_path:
        path = resolve_repo_path(local_path, "sources.mitre.local_path")
        logger.info(f"Loading MITRE data from local path: {path}")
        return json.loads(path.read_text(encoding="utf-8"))

    domain = mitre_config.get("domain", "enterprise-attack")
    cache_file = paths.cache_path / "mitre" / f"{domain}.json"

    refresh = bool(cache_config.get("refresh", False))
    if cache_file.exists() and not refresh:
        logger.info(f"Loading MITRE data from cache: {cache_file}")
        return json.loads(cache_file.read_text(encoding="utf-8"))

    url = mitre_config.get("url")
    if not url:
        raise ValueError("MITRE source requires either local_path or url")

    logger.info(f"Downloading MITRE data: {url}")
    response = requests.get(url, timeout=60)
    response.raise_for_status()

    cache_file.parent.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(response.text, encoding="utf-8")

    logger.info(f"Cached MITRE data: {cache_file}")
    return response.json()
