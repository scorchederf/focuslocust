#!/usr/bin/env python3
"""CLI entry point for Focus Locust."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from src.kb_builder.build_summary import (
    render_datasource_field_summary,
    render_object_property_pages,
)
from src.kb_builder.cache import load_or_fetch_mitre
from src.kb_builder.config import load_config
from src.kb_builder.logging_setup import setup_logging
from src.kb_builder.paths import ensure_project_paths, resolve_repo_path
from src.kb_builder.render.ghvault import GhVaultRenderer
from src.kb_builder.render.markdown import MarkdownRenderer
from src.kb_builder.safe_write import clean_generated_markdown
from src.kb_builder.sources.gtfobins import GtfobinsSource
from src.kb_builder.sources.hacktricks import HackTricksSource
from src.kb_builder.sources.internalallthethings import InternalAllTheThingsSource
from src.kb_builder.sources.lolbas import LolbasSource
from src.kb_builder.sources.mitre import MitreSource
from src.kb_builder.sources.payloadsallthethings import PayloadsAllTheThingsSource
from src.kb_builder.sources.redteamingtactics import RedTeamingTacticsSource

BuildTarget = str


def marker_from_config(config: dict[str, Any]) -> str:
    rendering_config = config.get("rendering", {})
    return rendering_config.get("parsed_marker", "focuslocust")


def target_includes_source(target: BuildTarget) -> bool:
    return target in {"source", "both"}


def target_includes_ghvault(target: BuildTarget) -> bool:
    return target in {"ghvault", "both"}


def load_sources(config: dict[str, Any], paths, logger) -> tuple[dict[str, list[dict[str, Any]]], dict[str, list[Any]]]:
    """Load and parse configured sources once for one or more render targets.

    The source-first Obsidian vault and the GitHub retrieval vault must use the
    same parsed objects so both outputs are repeatable and comparable.
    """
    sources_config = config.get("sources", {})
    mitre_config = sources_config.get("mitre", {})
    lolbins_config = sources_config.get("lolbins", sources_config.get("lolbas", {}))
    gtfobins_config = sources_config.get("gtfobins", {})
    payloads_config = sources_config.get("payloadsallthethings", {})
    internal_config = sources_config.get("internalallthethings", {})
    hacktricks_config = sources_config.get("hacktricks", {})
    redteaming_config = sources_config.get("redteamingtactics", {})

    raw_sources: dict[str, list[dict[str, Any]]] = {}
    build_objects: dict[str, list[Any]] = {}

    if mitre_config.get("enabled", False):
        data = load_or_fetch_mitre(config=config, paths=paths, logger=logger)
        raw_sources["mitre"] = data.get("objects", []) if isinstance(data.get("objects", []), list) else []
        source = MitreSource(config=mitre_config, logger=logger)
        objects = source.parse(data)
        build_objects["mitre/tactics"] = [obj for obj in objects if obj.type == "tactic"]
        build_objects["mitre/techniques"] = [obj for obj in objects if obj.type == "technique"]
        build_objects["mitre/mitigations"] = [obj for obj in objects if obj.type == "mitigation"]
        build_objects["mitre/data-sources"] = [obj for obj in objects if obj.type == "data-source"]
        build_objects["mitre/tools"] = [obj for obj in objects if obj.type == "tool"]
    else:
        logger.warning("MITRE source is disabled")

    if lolbins_config.get("enabled", False):
        source = LolbasSource(config=lolbins_config, logger=logger)
        records = source.load()
        raw_sources["lolbas"] = records
        build_objects["lolbas/tools"] = source.parse(records)
    else:
        logger.info("LOLBAS/LOLBins source is disabled")

    if gtfobins_config.get("enabled", False):
        source = GtfobinsSource(config=gtfobins_config, logger=logger)
        records = source.load()
        raw_sources["gtfobins"] = records
        build_objects["gtfobins/tools"] = source.parse(records)
    else:
        logger.info("GTFOBins source is disabled")

    if payloads_config.get("enabled", False):
        source = PayloadsAllTheThingsSource(config=payloads_config, logger=logger)
        records = source.load()
        raw_sources["payloadsallthethings"] = records
        build_objects["payloadsallthethings/topics"] = source.parse(records)
    else:
        logger.info("PayloadsAllTheThings source is disabled")

    if internal_config.get("enabled", False):
        source = InternalAllTheThingsSource(config=internal_config, logger=logger)
        records = source.load()
        raw_sources["internalallthethings"] = records
        build_objects["internalallthethings/topics"] = source.parse(records)
    else:
        logger.info("InternalAllTheThings source is disabled")

    if hacktricks_config.get("enabled", False):
        source = HackTricksSource(config=hacktricks_config, logger=logger)
        records = source.load()
        raw_sources["hacktricks"] = records
        build_objects["hacktricks/topics"] = source.parse(records)
    else:
        logger.info("HackTricks source is disabled")

    if redteaming_config.get("enabled", False):
        source = RedTeamingTacticsSource(config=redteaming_config, logger=logger)
        records = source.load()
        raw_sources["redteamingtactics"] = records
        build_objects["redteamingtactics/topics"] = source.parse(records)
    else:
        logger.info("RedTeaming Tactics source is disabled")

    return raw_sources, build_objects


def render_source_vault(config: dict[str, Any], paths, logger, raw_sources: dict[str, list[dict[str, Any]]], build_objects: dict[str, list[Any]]) -> tuple[int, int]:
    """Render the existing source-first Obsidian vault."""
    marker = marker_from_config(config)
    deleted_count = clean_generated_markdown(
        roots=[paths.vault_path / "kb", paths.vault_path / "ws"],
        marker=marker,
        logger=logger,
    )
    logger.info(f"Deleted generated source-vault Markdown files: {deleted_count}")

    renderer = MarkdownRenderer(config=config, paths=paths, logger=logger)
    total_written = 0
    total_skipped = 0

    if "mitre/tactics" in build_objects or "mitre/techniques" in build_objects:
        mitre_objects = []
        for group in (
            "mitre/tactics",
            "mitre/techniques",
            "mitre/mitigations",
            "mitre/data-sources",
            "mitre/tools",
        ):
            mitre_objects.extend(build_objects.get(group, []))
        written_count, skipped_count = renderer.render_mitre(mitre_objects)
        total_written += written_count
        total_skipped += skipped_count

    source_renderers = [
        ("lolbas/tools", renderer.render_lolbas),
        ("gtfobins/tools", renderer.render_gtfobins),
        ("payloadsallthethings/topics", renderer.render_payloadsallthethings),
        ("internalallthethings/topics", renderer.render_internalallthethings),
        ("hacktricks/topics", renderer.render_hacktricks),
        ("redteamingtactics/topics", renderer.render_redteamingtactics),
    ]
    for group_name, render_func in source_renderers:
        objects = build_objects.get(group_name, [])
        if not objects:
            continue
        written_count, skipped_count = render_func(objects)
        total_written += written_count
        total_skipped += skipped_count

    if raw_sources:
        if render_datasource_field_summary(
            sources=raw_sources,
            marker=marker,
            paths=paths,
            logger=logger,
        ):
            total_written += 1
        else:
            total_skipped += 1

    if build_objects:
        written_count, skipped_count = render_object_property_pages(
            objects_by_group=build_objects,
            marker=marker,
            paths=paths,
            logger=logger,
        )
        total_written += written_count
        total_skipped += skipped_count

    return total_written, total_skipped


def build(
    config_path: str,
    vault_override: str | None = None,
    verbose: bool = False,
    target: BuildTarget = "both",
    strict: bool = False,
) -> int:
    config = load_config(config_path)
    if vault_override:
        if target == "ghvault":
            config.setdefault("ghvault", {})["path"] = vault_override
        else:
            config["vault_path"] = vault_override
    if verbose:
        config.setdefault("logging", {})["verbose"] = True

    logger = setup_logging(config)
    paths = ensure_project_paths(config)
    logger.info("Starting build")
    logger.info(f"Build target: {target}")
    logger.info(f"Source vault path: {paths.vault_path}")

    raw_sources, build_objects = load_sources(config=config, paths=paths, logger=logger)

    total_written = 0
    total_skipped = 0

    if target_includes_source(target):
        written_count, skipped_count = render_source_vault(
            config=config,
            paths=paths,
            logger=logger,
            raw_sources=raw_sources,
            build_objects=build_objects,
        )
        total_written += written_count
        total_skipped += skipped_count

    if target_includes_ghvault(target):
        ghvault_config = config.get("ghvault", {})
        ghvault_path = resolve_repo_path(ghvault_config.get("path", "./ghvault"), "ghvault.path")
        logger.info(f"GitHub retrieval vault path: {ghvault_path}")
        renderer = GhVaultRenderer(
            config=config,
            root=ghvault_path,
            logger=logger,
            strict=strict,
        )
        result = renderer.render(
            objects_by_group=build_objects,
            raw_sources=raw_sources,
        )
        total_written += result.files_written
        total_skipped += result.files_skipped

    logger.info(f"Files written: {total_written}")
    logger.info(f"Manual files skipped: {total_skipped}")
    logger.info("Build completed")
    return 0


def clean(config_path: str, verbose: bool = False, target: BuildTarget = "both") -> int:
    config = load_config(config_path)
    if verbose:
        config.setdefault("logging", {})["verbose"] = True
    logger = setup_logging(config)
    paths = ensure_project_paths(config)
    marker = marker_from_config(config)
    total = 0

    if target_includes_source(target):
        count = clean_generated_markdown(
            roots=[paths.vault_path / "kb", paths.vault_path / "ws"],
            marker=marker,
            logger=logger,
        )
        logger.info(f"Deleted generated source-vault Markdown files: {count}")
        total += count

    if target_includes_ghvault(target):
        ghvault_path = resolve_repo_path(config.get("ghvault", {}).get("path", "./ghvault"), "ghvault.path")
        count = clean_generated_markdown(
            roots=[ghvault_path],
            marker=marker,
            logger=logger,
        )
        logger.info(f"Deleted generated ghvault Markdown files: {count}")
        total += count

    logger.info(f"Deleted generated Markdown files: {total}")
    return 0


def doctor(config_path: str, verbose: bool = False, target: BuildTarget = "both") -> int:
    config_file = Path(config_path)
    if not config_file.exists():
        print(f"Config file not found: {config_file}")
        return 1

    config = load_config(config_path)
    if verbose:
        config.setdefault("logging", {})["verbose"] = True

    logger = setup_logging(config)
    paths = ensure_project_paths(config)

    required_templates = []
    if target_includes_source(target):
        required_templates.extend(
            [
                Path("templates/mitre/tactic.md.j2"),
                Path("templates/mitre/technique.md.j2"),
                Path("templates/mitre/mitigation.md.j2"),
                Path("templates/mitre/data-source.md.j2"),
                Path("templates/mitre/tool.md.j2"),
                Path("templates/mitre/index.md.j2"),
            ]
        )

        sources_config = config.get("sources", {})
        lolbins_config = sources_config.get("lolbins", sources_config.get("lolbas", {}))
        gtfobins_config = sources_config.get("gtfobins", {})
        payloads_config = sources_config.get("payloadsallthethings", {})
        internal_config = sources_config.get("internalallthethings", {})
        hacktricks_config = sources_config.get("hacktricks", {})
        redteaming_config = sources_config.get("redteamingtactics", {})

        if lolbins_config.get("enabled", False):
            required_templates.extend([Path("templates/lolbas/tool.md.j2"), Path("templates/lolbas/index.md.j2")])
        if gtfobins_config.get("enabled", False):
            required_templates.extend([Path("templates/gtfobins/tool.md.j2"), Path("templates/gtfobins/index.md.j2")])
        if payloads_config.get("enabled", False):
            required_templates.extend(
                [
                    Path("templates/payloadsallthethings/payload-topic.md.j2"),
                    Path("templates/payloadsallthethings/moved-reference.md.j2"),
                    Path("templates/payloadsallthethings/index.md.j2"),
                ]
            )
        if internal_config.get("enabled", False):
            required_templates.extend([Path("templates/internalallthethings/topic.md.j2"), Path("templates/internalallthethings/index.md.j2")])
        if hacktricks_config.get("enabled", False):
            required_templates.extend([Path("templates/hacktricks/topic.md.j2"), Path("templates/hacktricks/index.md.j2")])
        if redteaming_config.get("enabled", False):
            required_templates.extend([Path("templates/redteamingtactics/topic.md.j2"), Path("templates/redteamingtactics/index.md.j2")])

    missing = [str(path) for path in required_templates if not path.exists()]
    if missing:
        for item in missing:
            logger.error(f"Missing template: {item}")
        return 1

    sources_config = config.get("sources", {})
    mitre_config = sources_config.get("mitre", {})
    lolbins_config = sources_config.get("lolbins", sources_config.get("lolbas", {}))
    gtfobins_config = sources_config.get("gtfobins", {})
    payloads_config = sources_config.get("payloadsallthethings", {})
    internal_config = sources_config.get("internalallthethings", {})
    hacktricks_config = sources_config.get("hacktricks", {})
    redteaming_config = sources_config.get("redteamingtactics", {})

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
    if hacktricks_config.get("enabled", False) and not hacktricks_config.get("local_path"):
        logger.error("HackTricks source requires local_path")
        return 1
    if redteaming_config.get("enabled", False) and not redteaming_config.get("local_path"):
        logger.error("RedTeaming Tactics source requires local_path")
        return 1

    if target_includes_ghvault(target):
        ghvault_path = resolve_repo_path(config.get("ghvault", {}).get("path", "./ghvault"), "ghvault.path")
        logger.info(f"GitHub retrieval vault path: {ghvault_path}")

    logger.info("Doctor check passed")
    logger.info(f"Source vault path: {paths.vault_path}")
    logger.info(f"Cache path: {paths.cache_path}")
    logger.info(f"Log path: {paths.log_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Focus Locust vault outputs from local datasets.")
    parser.add_argument("command", choices=["build", "clean", "doctor"])
    parser.add_argument("--config", default="config.yml", help="Path to config.yml")
    parser.add_argument("--vault", default=None, help="Override vault output path for source or ghvault target")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose console logging")
    parser.add_argument(
        "--target",
        choices=["source", "ghvault", "both"],
        default="both",
        help="Render the source-first vault, the GitHub retrieval vault, or both outputs.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail the ghvault build when validation finds broken links or structural errors.",
    )
    args = parser.parse_args()

    if args.command == "build":
        return build(
            args.config,
            vault_override=args.vault,
            verbose=args.verbose,
            target=args.target,
            strict=args.strict,
        )
    if args.command == "clean":
        return clean(args.config, verbose=args.verbose, target=args.target)
    if args.command == "doctor":
        return doctor(args.config, verbose=args.verbose, target=args.target)

    raise ValueError(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
