#!/usr/bin/env python3
"""CLI entry point for Obsidian KB Builder."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.kb_builder.build_summary import render_datasource_field_summary, render_object_property_pages
from src.kb_builder.cache import load_or_fetch_mitre
from src.kb_builder.config import load_config
from src.kb_builder.logging_setup import setup_logging
from src.kb_builder.paths import ensure_project_paths
from src.kb_builder.render.markdown import MarkdownRenderer
from src.kb_builder.safe_write import clean_generated_markdown
from src.kb_builder.sources.gtfobins import GtfobinsSource
from src.kb_builder.sources.internalallthethings import InternalAllTheThingsSource
from src.kb_builder.sources.lolbas import LolbasSource
from src.kb_builder.sources.mitre import MitreSource
from src.kb_builder.sources.payloadsallthethings import PayloadsAllTheThingsSource


def marker_from_config(config: dict) -> str:
    rendering_config = config.get("rendering", {})
    return rendering_config.get("parsed_marker", "focuslocust")


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
        marker=marker_from_config(config),
        logger=logger,
    )
    logger.info(f"Deleted generated Markdown files: {deleted_count}")

    sources_config = config.get("sources", {})
    mitre_config = sources_config.get("mitre", {})
    lolbins_config = sources_config.get("lolbins", sources_config.get("lolbas", {}))
    gtfobins_config = sources_config.get("gtfobins", {})
    payloads_config = sources_config.get("payloadsallthethings", {})
    internal_config = sources_config.get("internalallthethings", {})
    total_written = 0
    total_skipped = 0
    raw_sources: dict[str, list[dict]] = {}
    build_objects: dict[str, list] = {}

    renderer = MarkdownRenderer(config=config, paths=paths, logger=logger)
    if mitre_config.get("enabled", False):
        data = load_or_fetch_mitre(config=config, paths=paths, logger=logger)
        raw_sources["mitre"] = data.get("objects", []) if isinstance(data.get("objects", []), list) else []
        source = MitreSource(config=mitre_config, logger=logger)
        objects = source.parse(data)
        build_objects["mitre/tactics"] = [obj for obj in objects if obj.type == "tactic"]
        build_objects["mitre/techniques"] = [obj for obj in objects if obj.type == "technique"]
        written_count, skipped_count = renderer.render_mitre(objects)
        total_written += written_count
        total_skipped += skipped_count
    else:
        logger.warning("MITRE source is disabled")

    if lolbins_config.get("enabled", False):
        source = LolbasSource(config=lolbins_config, logger=logger)
        records = source.load()
        raw_sources["lolbas"] = records
        tools = source.parse(records)
        build_objects["lolbas/tools"] = tools
        written_count, skipped_count = renderer.render_lolbas(tools)
        total_written += written_count
        total_skipped += skipped_count
    else:
        logger.info("LOLBAS/LOLBins source is disabled")

    if gtfobins_config.get("enabled", False):
        source = GtfobinsSource(config=gtfobins_config, logger=logger)
        records = source.load()
        raw_sources["gtfobins"] = records
        tools = source.parse(records)
        build_objects["gtfobins/tools"] = tools
        written_count, skipped_count = renderer.render_gtfobins(tools)
        total_written += written_count
        total_skipped += skipped_count
    else:
        logger.info("GTFOBins source is disabled")

    if payloads_config.get("enabled", False):
        source = PayloadsAllTheThingsSource(config=payloads_config, logger=logger)
        records = source.load()
        raw_sources["payloadsallthethings"] = records
        topics = source.parse(records)
        build_objects["payloadsallthethings/topics"] = topics
        written_count, skipped_count = renderer.render_payloadsallthethings(topics)
        total_written += written_count
        total_skipped += skipped_count
    else:
        logger.info("PayloadsAllTheThings source is disabled")

    if internal_config.get("enabled", False):
        source = InternalAllTheThingsSource(config=internal_config, logger=logger)
        records = source.load()
        raw_sources["internalallthethings"] = records
        topics = source.parse(records)
        build_objects["internalallthethings/topics"] = topics
        written_count, skipped_count = renderer.render_internalallthethings(topics)
        total_written += written_count
        total_skipped += skipped_count
    else:
        logger.info("InternalAllTheThings source is disabled")

    if raw_sources:
        if render_datasource_field_summary(
            sources=raw_sources,
            marker=marker_from_config(config),
            paths=paths,
            logger=logger,
        ):
            total_written += 1
        else:
            total_skipped += 1

    if build_objects:
        written_count, skipped_count = render_object_property_pages(
            objects_by_group=build_objects,
            marker=marker_from_config(config),
            paths=paths,
            logger=logger,
        )
        total_written += written_count
        total_skipped += skipped_count

    logger.info(f"Files written: {total_written}")
    logger.info(f"Manual files skipped: {total_skipped}")
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
        marker=marker_from_config(config),
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
    sources_config = config.get("sources", {})
    lolbins_config = sources_config.get("lolbins", sources_config.get("lolbas", {}))
    gtfobins_config = sources_config.get("gtfobins", {})
    payloads_config = sources_config.get("payloadsallthethings", {})
    internal_config = sources_config.get("internalallthethings", {})
    if lolbins_config.get("enabled", False):
        required_templates.extend(
            [
                Path("templates/lolbas/tool.md.j2"),
                Path("templates/lolbas/index.md.j2"),
            ]
        )
    if gtfobins_config.get("enabled", False):
        required_templates.extend(
            [
                Path("templates/gtfobins/tool.md.j2"),
                Path("templates/gtfobins/index.md.j2"),
            ]
        )
    if payloads_config.get("enabled", False):
        required_templates.extend(
            [
                Path("templates/payloadsallthethings/payload-topic.md.j2"),
                Path("templates/payloadsallthethings/moved-reference.md.j2"),
                Path("templates/payloadsallthethings/index.md.j2"),
            ]
        )
    if internal_config.get("enabled", False):
        required_templates.extend(
            [
                Path("templates/internalallthethings/topic.md.j2"),
                Path("templates/internalallthethings/index.md.j2"),
            ]
        )

    missing = [str(path) for path in required_templates if not path.exists()]
    if missing:
        for item in missing:
            logger.error(f"Missing template: {item}")
        return 1

    mitre_config = sources_config.get("mitre", {})
    if mitre_config.get("enabled", False) and not mitre_config.get("url") and not mitre_config.get("local_path"):
        logger.error("MITRE source requires either url or local_path")
        return 1

    if lolbins_config.get("enabled", False) and not lolbins_config.get("local_path"):
        logger.error("LOLBAS/LOLBins source requires local_path")
        return 1

    if gtfobins_config.get("enabled", False) and not gtfobins_config.get("local_path"):
        logger.error("GTFOBins source requires local_path")
        return 1

    if payloads_config.get("enabled", False) and not payloads_config.get("local_path"):
        logger.error("PayloadsAllTheThings source requires local_path")
        return 1

    if internal_config.get("enabled", False) and not internal_config.get("local_path"):
        logger.error("InternalAllTheThings source requires local_path")
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
