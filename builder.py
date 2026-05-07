#!/usr/bin/env python3
"""CLI entry point for Obsidian KB Builder."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.kb_builder.cache import load_or_fetch_mitre
from src.kb_builder.config import load_config
from src.kb_builder.logging_setup import setup_logging
from src.kb_builder.paths import ensure_project_paths
from src.kb_builder.render.markdown import MarkdownRenderer
from src.kb_builder.safe_write import clean_generated_markdown
from src.kb_builder.sources.mitre import MitreSource


def build(config_path: str, vault_override: str | None = None, verbose: bool = False) -> int:
    config = load_config(config_path)

    if vault_override:
        config["vault_path"] = vault_override

    if verbose:
        config.setdefault("logging", {})["verbose"] = True

    logger = setup_logging(config)
    paths = ensure_project_paths(config)

    logger.info("Starting build")
    logger.info(f"Vault path: {paths.vault_path}")

    deleted_count = clean_generated_markdown(
        roots=[paths.vault_path / "kb", paths.vault_path / "ws"],
        marker=config["rendering"]["generated_marker"],
        logger=logger,
    )
    logger.info(f"Deleted generated Markdown files: {deleted_count}")

    mitre_config = config.get("sources", {}).get("mitre", {})
    if not mitre_config.get("enabled", False):
        logger.warning("MITRE source is disabled; nothing to build")
        return 0

    data = load_or_fetch_mitre(config=config, paths=paths, logger=logger)
    source = MitreSource(config=mitre_config, logger=logger)
    objects = source.parse(data)

    renderer = MarkdownRenderer(config=config, paths=paths, logger=logger)
    written_count, skipped_count = renderer.render_mitre(objects)

    logger.info(f"Files written: {written_count}")
    logger.info(f"Manual files skipped: {skipped_count}")
    logger.info("Build completed")

    return 0


def clean(config_path: str, verbose: bool = False) -> int:
    config = load_config(config_path)

    if verbose:
        config.setdefault("logging", {})["verbose"] = True

    logger = setup_logging(config)
    paths = ensure_project_paths(config)

    count = clean_generated_markdown(
        roots=[paths.vault_path / "kb", paths.vault_path / "ws"],
        marker=config["rendering"]["generated_marker"],
        logger=logger,
    )

    logger.info(f"Deleted generated Markdown files: {count}")
    return 0


def doctor(config_path: str, verbose: bool = False) -> int:
    config_file = Path(config_path)
    if not config_file.exists():
        print(f"Config file not found: {config_file}")
        return 1

    config = load_config(config_path)

    if verbose:
        config.setdefault("logging", {})["verbose"] = True

    logger = setup_logging(config)
    paths = ensure_project_paths(config)

    required_templates = [
        Path("templates/mitre/tactic.md.j2"),
        Path("templates/mitre/technique.md.j2"),
        Path("templates/mitre/mitigation.md.j2"),
        Path("templates/mitre/data-source.md.j2"),
        Path("templates/mitre/tool.md.j2"),
        Path("templates/mitre/index.md.j2"),
    ]

    missing = [str(path) for path in required_templates if not path.exists()]
    if missing:
        for item in missing:
            logger.error(f"Missing template: {item}")
        return 1

    mitre_config = config.get("sources", {}).get("mitre", {})
    if not mitre_config.get("url") and not mitre_config.get("local_path"):
        logger.error("MITRE source requires either url or local_path")
        return 1

    logger.info("Doctor check passed")
    logger.info(f"Vault path: {paths.vault_path}")
    logger.info(f"Cache path: {paths.cache_path}")
    logger.info(f"Log path: {paths.log_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Build an Obsidian security KB from datasets.")
    parser.add_argument("command", choices=["build", "clean", "doctor"])
    parser.add_argument("--config", default="config.yml", help="Path to config.yml")
    parser.add_argument("--vault", default=None, help="Override vault output path")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose console logging")

    args = parser.parse_args()

    if args.command == "build":
        return build(args.config, vault_override=args.vault, verbose=args.verbose)

    if args.command == "clean":
        return clean(args.config, verbose=args.verbose)

    if args.command == "doctor":
        return doctor(args.config, verbose=args.verbose)

    raise ValueError(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
