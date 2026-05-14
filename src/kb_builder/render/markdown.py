from __future__ import annotations

from collections import defaultdict
import json
from pathlib import Path
import re
import shutil
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from ..models import (
    GtfobinsTool,
    HackTricksTopic,
    InternalTopic,
    LolbasTool,
    MitreObject,
    PayloadTopic,
    RedTeamingTopic,
)
from ..naming import strip_md
from ..paths import ProjectPaths
from ..render.links import wikilink
from ..safe_write import safe_write_text


class MarkdownRenderer:
    def __init__(self, config: dict[str, Any], paths: ProjectPaths, logger):
        self.config = config
        self.paths = paths
        self.logger = logger
        rendering_config = config.get("rendering", {})
        self.marker = rendering_config.get("parsed_marker", "focuslocust")

        self.env = Environment(
            loader=FileSystemLoader("templates"),
            undefined=StrictUndefined,
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.env.filters["parse_description"] = self._parse_description
        self.env.filters["strip_md"] = strip_md
        self.env.filters["table_cell"] = self._table_cell
        self.env.filters["index_link"] = self._index_link
        self.env.filters["field_values"] = self._field_values
        self.env.filters["field_value"] = self._field_value
        self.env.filters["yaml_quote"] = self._yaml_quote

    def render_mitre(self, objects: list[MitreObject]) -> tuple[int, int]:
        link_map = self._build_link_map(objects)
        enriched = self._enrich_links(objects, link_map)

        written = 0
        skipped = 0

        for obj in enriched:
            template_name = f"mitre/{obj.type}.md.j2"
            content = self.env.get_template(template_name).render(
                obj=obj,
                parsed_marker=self.marker,
                link_map=link_map,
            )
            content = self._normalize_markdown(content)
            target = self.paths.vault_path / obj.path

            if safe_write_text(target, content, marker=self.marker, logger=self.logger):
                written += 1
            else:
                skipped += 1

        index_written, index_skipped = self._render_indexes(enriched, link_map)
        written += index_written
        skipped += index_skipped

        return written, skipped

    def render_lolbas(self, tools: list[LolbasTool]) -> tuple[int, int]:
        written = 0
        skipped = 0

        for tool in tools:
            content = self.env.get_template("lolbas/tool.md.j2").render(
                obj=tool,
                parsed_marker=self.marker,
            )
            content = self._normalize_markdown(content)
            if safe_write_text(self.paths.vault_path / tool.path, content, marker=self.marker, logger=self.logger):
                written += 1
            else:
                skipped += 1

        index = self.env.get_template("lolbas/index.md.j2").render(
            title="LOLBAS Tools",
            objects=tools,
            parsed_marker=self.marker,
        )
        index = self._normalize_markdown(index)
        if safe_write_text(
            self.paths.vault_path / "kb/indexes/lolbas.md",
            index,
            marker=self.marker,
            logger=self.logger,
        ):
            written += 1
        else:
            skipped += 1

        return written, skipped

    def render_gtfobins(self, tools: list[GtfobinsTool]) -> tuple[int, int]:
        written = 0
        skipped = 0

        for tool in tools:
            content = self.env.get_template("gtfobins/tool.md.j2").render(
                obj=tool,
                parsed_marker=self.marker,
            )
            content = self._normalize_markdown(content)
            if safe_write_text(self.paths.vault_path / tool.path, content, marker=self.marker, logger=self.logger):
                written += 1
            else:
                skipped += 1

        index = self.env.get_template("gtfobins/index.md.j2").render(
            title="GTFOBins Tools",
            objects=tools,
            parsed_marker=self.marker,
        )
        index = self._normalize_markdown(index)
        if safe_write_text(
            self.paths.vault_path / "kb/indexes/gtfobins.md",
            index,
            marker=self.marker,
            logger=self.logger,
        ):
            written += 1
        else:
            skipped += 1

        return written, skipped

    def render_payloadsallthethings(self, topics: list[PayloadTopic]) -> tuple[int, int]:
        written = 0
        skipped = 0

        for topic in topics:
            template_name = (
                "payloadsallthethings/moved-reference.md.j2"
                if topic.moved_to
                else "payloadsallthethings/payload-topic.md.j2"
            )
            content = self.env.get_template(template_name).render(
                obj=topic,
                parsed_marker=self.marker,
            )
            content = self._normalize_markdown(content)
            if safe_write_text(self.paths.vault_path / topic.path, content, marker=self.marker, logger=self.logger):
                written += 1
            else:
                skipped += 1

        index = self.env.get_template("payloadsallthethings/index.md.j2").render(
            title="PayloadsAllTheThings",
            objects=topics,
            parsed_marker=self.marker,
        )
        index = self._normalize_markdown(index)
        if safe_write_text(
            self.paths.vault_path / "kb/indexes/payloadsallthethings.md",
            index,
            marker=self.marker,
            logger=self.logger,
        ):
            written += 1
        else:
            skipped += 1

        return written, skipped

    def render_internalallthethings(self, topics: list[InternalTopic]) -> tuple[int, int]:
        written = 0
        skipped = 0

        for topic in topics:
            content = self.env.get_template("internalallthethings/topic.md.j2").render(
                obj=topic,
                parsed_marker=self.marker,
            )
            content = self._normalize_markdown(content)
            if safe_write_text(self.paths.vault_path / topic.path, content, marker=self.marker, logger=self.logger):
                written += 1
            else:
                skipped += 1

        index = self.env.get_template("internalallthethings/index.md.j2").render(
            title="InternalAllTheThings",
            objects=topics,
            parsed_marker=self.marker,
        )
        index = self._normalize_markdown(index)
        if safe_write_text(
            self.paths.vault_path / "kb/indexes/internalallthethings.md",
            index,
            marker=self.marker,
            logger=self.logger,
        ):
            written += 1
        else:
            skipped += 1

        return written, skipped

    def render_hacktricks(self, topics: list[HackTricksTopic]) -> tuple[int, int]:
        written = 0
        skipped = 0

        for topic in topics:
            content = self.env.get_template("hacktricks/topic.md.j2").render(
                obj=topic,
                parsed_marker=self.marker,
            )
            content = self._normalize_markdown(content)
            if safe_write_text(self.paths.vault_path / topic.path, content, marker=self.marker, logger=self.logger):
                written += 1
            else:
                skipped += 1

        index = self.env.get_template("hacktricks/index.md.j2").render(
            title="HackTricks",
            objects=topics,
            parsed_marker=self.marker,
        )
        index = self._normalize_markdown(index)
        if safe_write_text(
            self.paths.vault_path / "kb/indexes/hacktricks.md",
            index,
            marker=self.marker,
            logger=self.logger,
        ):
            written += 1
        else:
            skipped += 1

        return written, skipped

    def render_redteamingtactics(self, topics: list[RedTeamingTopic]) -> tuple[int, int]:
        written = 0
        skipped = 0

        for topic in topics:
            self._copy_redteaming_assets(topic)
            content = self.env.get_template("redteamingtactics/topic.md.j2").render(
                obj=topic,
                parsed_marker=self.marker,
            )
            content = self._normalize_markdown(content)
            if safe_write_text(self.paths.vault_path / topic.path, content, marker=self.marker, logger=self.logger):
                written += 1
            else:
                skipped += 1

        index = self.env.get_template("redteamingtactics/index.md.j2").render(
            title="RedTeaming Tactics and Techniques",
            objects=topics,
            parsed_marker=self.marker,
        )
        index = self._normalize_markdown(index)
        if safe_write_text(
            self.paths.vault_path / "kb/indexes/redteamingtactics.md",
            index,
            marker=self.marker,
            logger=self.logger,
        ):
            written += 1
        else:
            skipped += 1

        return written, skipped

    def _copy_redteaming_assets(self, topic: RedTeamingTopic) -> None:
        asset_filenames = topic.raw.get("_asset_filenames", [])
        source_path = topic.raw.get("_source_path", "")
        if not asset_filenames or not source_path:
            return

        relative_parts = Path(topic.relative_path).parts
        if not relative_parts:
            return

        source_root = Path(source_path).parents[len(relative_parts) - 1]
        source_asset_dir = source_root / ".gitbook" / "assets"
        target_asset_dir = self.paths.vault_path / "kb/redteaming/_assets"
        target_asset_dir.mkdir(parents=True, exist_ok=True)

        for asset_filename in asset_filenames:
            source_asset = source_asset_dir / asset_filename
            target_asset = target_asset_dir / asset_filename
            if not source_asset.is_file() or target_asset.exists():
                continue
            shutil.copy2(source_asset, target_asset)

    def _build_link_map(self, objects: list[MitreObject]) -> dict[str, str]:
        link_map = {}
        for obj in objects:
            link_map[obj.id] = strip_md(obj.path)
        return link_map

    def _enrich_links(
        self,
        objects: list[MitreObject],
        link_map: dict[str, str],
    ) -> list[MitreObject]:
        technique_rows_by_tactic: dict[str, list[dict[str, str]]] = defaultdict(list)
        object_by_id = {obj.id: obj for obj in objects}

        for obj in objects:
            obj.aliases = [obj.id]
            obj.reference_notes = self._reference_notes(obj)

            if obj.type == "technique":
                for tactic_slug in obj.tactics:
                    technique_rows_by_tactic[tactic_slug].append(self._table_row(obj, link_map))
                obj.procedure_examples = [
                    self._procedure_row_with_link(row, object_by_id, link_map)
                    for row in obj.procedure_examples
                ]
                obj.mitigations = [
                    self._row_with_link(row, object_by_id, link_map)
                    for row in obj.mitigations
                ]
                obj.subtechniques = [
                    self._table_row(other, link_map)
                    for other in objects
                    if other.type == "technique" and other.parent_technique_id == obj.id
                ]

            if obj.type == "mitigation":
                obj.related_techniques = [
                    self._row_with_link(row, object_by_id, link_map)
                    for row in obj.related_techniques
                ]

            if obj.type == "tool":
                obj.techniques_used = [
                    self._row_with_link(row, object_by_id, link_map)
                    for row in obj.techniques_used
                ]

        for obj in objects:
            if obj.type == "tactic":
                slug = obj.name.lower().replace(" ", "-")
                obj.related_techniques = sorted(
                    technique_rows_by_tactic.get(slug, []),
                    key=lambda row: row["id"],
                )

        for obj in objects:
            obj.tags = self._tags_for(obj)

        return objects

    def _table_row(self, obj: MitreObject, link_map: dict[str, str]) -> dict[str, str]:
        return {
            "id": obj.id,
            "name": obj.name,
            "description": obj.description,
            "link": wikilink(link_map[obj.id], obj.id),
            "reference_notes": obj.reference_notes,
        }

    def _row_with_link(
        self,
        row: dict[str, str],
        object_by_id: dict[str, MitreObject],
        link_map: dict[str, str],
    ) -> dict[str, str]:
        linked = dict(row)
        if "reference_notes" not in linked and row.get("external_references"):
            linked["reference_notes"] = self._reference_notes_from_external_references(row["external_references"])

        if row["id"] in link_map:
            linked["link"] = wikilink(link_map[row["id"]], row["id"])
            if "reference_notes" not in linked and row["id"] in object_by_id:
                linked["reference_notes"] = object_by_id[row["id"]].reference_notes
            return linked

        linked["link"] = row["id"]
        obj = object_by_id.get(row["id"])
        if obj:
            linked["link"] = wikilink(link_map[obj.id], obj.id)
            if "reference_notes" not in linked:
                linked["reference_notes"] = obj.reference_notes
        else:
            linked.setdefault("reference_notes", [])
        return linked

    def _procedure_row_with_link(
        self,
        row: dict[str, str],
        object_by_id: dict[str, MitreObject],
        link_map: dict[str, str],
    ) -> dict[str, str]:
        linked = self._row_with_link(row, object_by_id, link_map)
        if linked["link"] != row["id"]:
            return linked

        if row.get("source_type") == "malware" and row.get("url"):
            linked["link"] = f"[{row['id']}]({row['url']})"

        return linked

    def _reference_notes(self, obj: MitreObject) -> list[dict[str, str]]:
        return self._reference_notes_from_external_references(obj.external_references)

    def _reference_notes_from_external_references(self, external_references) -> list[dict[str, str]]:
        notes = []
        seen = set()
        for ref in external_references:
            if ref.source_name == "mitre-attack":
                continue
            if ref.source_name in seen:
                continue
            seen.add(ref.source_name)
            notes.append(
                {
                    "id": str(len(notes) + 1),
                    "source_name": ref.source_name,
                    "url": ref.url,
                }
            )
        return notes

    def _tags_for(self, obj: MitreObject) -> list[str]:
        domain = self.config.get("sources", {}).get("mitre", {}).get("domain", "enterprise-attack")
        tags = [self._tag("attack", "domain", domain)]

        if obj.type == "tactic":
            tags.append("attack/type/tactic")
        elif obj.type == "mitigation":
            tags.append("attack/type/mitigation")
        elif obj.type == "data-source":
            tags.append("attack/type/data_source")
        elif obj.type == "tool":
            tags.extend(["attack/software/tool", "attack/type/software"])
        elif obj.type == "technique":
            is_subtechnique = bool(obj.parent_technique_id)
            tags.append("attack/type/subtechnique" if is_subtechnique else "attack/type/technique")
            if is_subtechnique:
                tags.append("attack/subtechnique")
            tags.extend(self._tag("attack", "tactic", tactic) for tactic in obj.tactics)
            tags.extend(self._tag("platform", platform) for platform in obj.platforms)
            tags.extend(self._tag("attack", "permission", permission) for permission in obj.permissions_required)
            if obj.procedure_examples:
                tags.append("attack/has_procedures")
            if obj.mitigations:
                tags.append("attack/mitigated")
            if obj.subtechniques:
                tags.append("attack/has_subtechniques")

        return sorted(set(tags))

    def _tag(self, *parts: str) -> str:
        return "/".join(self._tag_value(part) for part in parts if part)

    def _tag_value(self, value: str) -> str:
        value = value.lower().replace("&", "and")
        value = re.sub(r"[^a-z0-9]+", "_", value)
        return value.strip("_")

    def _parse_description(
        self,
        description: str,
        reference_notes: list[dict[str, str]] | None = None,
        link_map: dict[str, str] | None = None,
    ) -> str:
        reference_notes = reference_notes or []
        link_map = link_map or {}

        description = (description or "").replace("\n", "<br>")
        description = description.replace("</code>", "`").replace("<code>", "`")

        for ref in reference_notes:
            source_name = re.escape(ref["source_name"])
            description = re.sub(fr"\(Citation: {source_name}\)", f'[^{ref["id"]}] ', description)

        description = re.sub(
            r"\[([^\]]+)\]\(https://attack\.mitre\.org/(?:tactics|techniques|mitigations|datasources|software)/([^)/#]+)(?:/([^)/#]+))?/?\)",
            lambda match: self._description_link(match, link_map),
            description,
        )
        description = re.sub(r"\[([^\]]+)\]\(https?://[^)]+\)", r"\1", description)
        description = re.sub(r"https?://\S+", "", description)
        return description

    def _description_link(self, match: re.Match, link_map: dict[str, str]) -> str:
        attack_id = f"{match.group(2)}.{match.group(3)}" if match.group(3) else match.group(2)
        if attack_id not in link_map:
            return match.group(1)
        return wikilink(link_map[attack_id], match.group(1))

    def _table_cell(self, value: str) -> str:
        return (value or "").replace("|", "\\|").replace("\n", "<br>")

    def _yaml_quote(self, value) -> str:
        return json.dumps("" if value is None else str(value))

    def _field_values(self, value, path: str) -> list[str]:
        values = self._extract_field_values(value, path)
        return [str(item) for item in values if item is not None and item != ""]

    def _field_value(self, value, path: str) -> str:
        values = self._field_values(value, path)
        return values[0] if values else ""

    def _extract_field_values(self, value, path: str):
        current = [value]
        for part in path.split("."):
            next_values = []
            is_list_part = part.endswith("[]")
            key = part[:-2] if is_list_part else part

            for item in current:
                if isinstance(item, dict):
                    child = item.get(key)
                else:
                    child = getattr(item, key, None)

                if child is None:
                    continue

                if is_list_part:
                    if isinstance(child, list):
                        next_values.extend(child)
                    else:
                        next_values.append(child)
                else:
                    next_values.append(child)

            current = next_values

        return current

    def _index_link(self, obj: MitreObject, link_map: dict[str, str]) -> str:
        return wikilink(link_map[obj.id], f"{obj.id} - {obj.name}")

    def _normalize_markdown(self, content: str) -> str:
        content = re.sub(r"([^\n])\n(## )", r"\1\n\n\2", content)
        content = re.sub(r"\n{3,}", "\n\n", content)
        return content.rstrip() + "\n"

    def _render_indexes(
        self,
        objects: list[MitreObject],
        link_map: dict[str, str],
    ) -> tuple[int, int]:
        written = 0
        skipped = 0

        tactics = sorted([o for o in objects if o.type == "tactic"], key=lambda o: o.id)
        techniques = sorted([o for o in objects if o.type == "technique"], key=lambda o: o.id)
        mitigations = sorted([o for o in objects if o.type == "mitigation"], key=lambda o: o.id)
        data_sources = sorted([o for o in objects if o.type == "data-source"], key=lambda o: o.id)
        tools = sorted([o for o in objects if o.type == "tool"], key=lambda o: o.id)

        index_specs = [
            ("kb/mitre/attack/indexes/all-tactics.md", "Tactics", tactics),
            ("kb/mitre/attack/indexes/all-techniques.md", "Techniques", techniques),
            ("kb/mitre/attack/indexes/all-mitigations.md", "Mitigations", mitigations),
            ("kb/mitre/attack/indexes/all-data-sources.md", "Data Sources", data_sources),
            ("kb/mitre/attack/indexes/all-software.md", "Software", tools),
        ]

        for path, title, index_objects in index_specs:
            body = self.env.get_template("mitre/index.md.j2").render(
                title=title,
                objects=index_objects,
                link_map=link_map,
                source="mitre",
                parsed_marker=self.marker,
            )
            body = self._normalize_markdown(body)
            if safe_write_text(self.paths.vault_path / path, body, marker=self.marker, logger=self.logger):
                written += 1
            else:
                skipped += 1

        by_tactic = self._render_by_tactic(techniques, link_map)
        if safe_write_text(
            self.paths.vault_path / "kb/mitre/attack/indexes/by-tactic.md",
            by_tactic,
            marker=self.marker,
            logger=self.logger,
        ):
            written += 1
        else:
            skipped += 1

        by_platform = self._render_by_platform(techniques, link_map)
        if safe_write_text(
            self.paths.vault_path / "kb/mitre/attack/indexes/by-platform.md",
            by_platform,
            marker=self.marker,
            logger=self.logger,
        ):
            written += 1
        else:
            skipped += 1

        main_index = self._render_main_index(tactics, techniques, mitigations, data_sources, tools, link_map)
        if safe_write_text(
            self.paths.vault_path / "kb/indexes/mitre.md",
            main_index,
            marker=self.marker,
            logger=self.logger,
        ):
            written += 1
        else:
            skipped += 1

        references_index = self._render_references_index(objects)
        if safe_write_text(
            self.paths.vault_path / "kb/mitre/attack/indexes/all-references.md",
            references_index,
            marker=self.marker,
            logger=self.logger,
        ):
            written += 1
        else:
            skipped += 1

        return written, skipped

    def _render_main_index(
        self,
        tactics: list[MitreObject],
        techniques: list[MitreObject],
        mitigations: list[MitreObject],
        data_sources: list[MitreObject],
        tools: list[MitreObject],
        link_map: dict[str, str],
    ) -> str:
        lines = [
            "---",
            f"parsed_by: {self.marker}",
            "source: mitre",
            "type: index",
            "tags:",
            "    - attack/type/index",
            "---",
            "",
            "# MITRE ATT&CK",
            "",
        ]

        sections = [
            ("Tactics", tactics),
            ("Mitigations", mitigations),
            ("Data Sources", data_sources),
            ("Software", tools),
        ]
        for title, objects in sections:
            if not objects:
                continue
            lines.append(f"- {title}")
            for obj in sorted(objects, key=lambda item: item.id):
                lines.append(f"  - {self._index_link(obj, link_map)}")

        parent_techniques = sorted(
            [technique for technique in techniques if not technique.parent_technique_id],
            key=lambda item: item.id,
        )
        if parent_techniques:
            lines.append("- Techniques")
            for technique in parent_techniques:
                lines.append(f"  - {self._index_link(technique, link_map)}")
                subtechniques = sorted(
                    [subt for subt in techniques if subt.parent_technique_id == technique.id],
                    key=lambda item: item.id,
                )
                for subtechnique in subtechniques:
                    lines.append(f"    - {self._index_link(subtechnique, link_map)}")

        return "\n".join(lines).rstrip() + "\n"

    def _render_references_index(self, objects: list[MitreObject]) -> str:
        references: dict[tuple[str, str], set[str]] = defaultdict(set)
        for obj in objects:
            for ref in obj.external_references:
                if ref.source_name == "mitre-attack":
                    continue
                key = (ref.source_name, ref.url)
                references[key].add(f"{obj.id} - {obj.name}")

        lines = [
            "---",
            f"parsed_by: {self.marker}",
            "source: mitre",
            "type: reference-index",
            "---",
            "",
            "# References",
            "",
        ]

        for (source_name, url), used_by in sorted(references.items(), key=lambda item: item[0][0].lower()):
            if url:
                lines.append(f"- [{source_name}]({url})")
            else:
                lines.append(f"- {source_name}")
            for item in sorted(used_by):
                lines.append(f"  - {item}")

        return "\n".join(lines).rstrip() + "\n"

    def _render_by_tactic(self, techniques: list[MitreObject], link_map: dict[str, str]) -> str:
        groups: dict[str, list[MitreObject]] = defaultdict(list)
        for obj in techniques:
            for tactic in obj.tactics:
                groups[tactic].append(obj)

        lines = [
            "---",
            f"parsed_by: {self.marker}",
            "source: mitre",
            "type: index",
            "---",
            "",
            "## Techniques by tactic",
            "",
        ]

        for tactic in sorted(groups):
            lines.append(f"## {tactic.replace('-', ' ').title()}")
            lines.append("")
            for obj in sorted(groups[tactic], key=lambda item: item.id):
                lines.append(f"- {self._index_link(obj, link_map)}")
            lines.append("")

        return "\n".join(lines).rstrip() + "\n"

    def _render_by_platform(self, techniques: list[MitreObject], link_map: dict[str, str]) -> str:
        groups: dict[str, list[MitreObject]] = defaultdict(list)
        for obj in techniques:
            for platform in obj.platforms:
                groups[platform].append(obj)

        lines = [
            "---",
            f"parsed_by: {self.marker}",
            "source: mitre",
            "type: index",
            "---",
            "",
            "## Techniques by platform",
            "",
        ]

        for platform in sorted(groups):
            lines.append(f"## {platform}")
            lines.append("")
            for obj in sorted(groups[platform], key=lambda item: item.id):
                lines.append(f"- {self._index_link(obj, link_map)}")
            lines.append("")

        return "\n".join(lines).rstrip() + "\n"
