from __future__ import annotations

from typing import Any

from loguru import logger

from .paths import resolve_repo_path


def setup_logging(config: dict[str, Any]):
    logger.remove()

    logging_config = config.get("logging", {})
    verbose = bool(logging_config.get("verbose", False))
    log_dir = resolve_repo_path(logging_config.get("log_dir", ".logs"), "logging.log_dir")
    log_dir.mkdir(parents=True, exist_ok=True)

    level = "DEBUG" if verbose else "INFO"

    logger.add(
        sink=lambda message: print(message, end=""),
        level=level,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    )

    logger.add(
        log_dir / "focuslocust.log",
        level="DEBUG",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        rotation="5 MB",
        retention=5,
    )

    return logger
