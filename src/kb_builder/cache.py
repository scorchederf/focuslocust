from __future__ import annotations

import json
from typing import Any

import requests

from .paths import ProjectPaths, resolve_repo_path


def network_allowed(config: dict[str, Any]) -> bool:
    runtime = config.get("runtime", {})
    if "allow_network" in runtime:
        return bool(runtime.get("allow_network"))
    return bool(config.get("cache", {}).get("allow_network", False))


def load_or_fetch_mitre(config: dict[str, Any], paths: ProjectPaths, logger) -> dict[str, Any]:
    """Load MITRE data from local/cache first; fetch only when explicitly allowed.

    This preserves the project rule that network access must be intentional and
    explainable. When network is disabled and the source is missing, the error
    includes the reason and URL so the operator can approve or manually cache it.
    """
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
        raise ValueError("MITRE source requires either local_path, cached file, or url")

    if not network_allowed(config):
        raise RuntimeError(
            "Network access required but disabled.\n\n"
            "Reason:\n"
            f"  MITRE {domain} source file is missing from cache or refresh was requested.\n\n"
            "Requested URL:\n"
            f"  {url}\n\n"
            "Action:\n"
            f"  Manually place the file at {cache_file}, set sources.mitre.local_path, "
            "or rerun after explicitly setting runtime.allow_network: true."
        )

    logger.info(f"Downloading MITRE data: {url}")
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(response.text, encoding="utf-8")
    logger.info(f"Cached MITRE data: {cache_file}")
    return response.json()
