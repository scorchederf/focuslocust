from __future__ import annotations

from collections import defaultdict
import re
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from ..models import MitreObject
from ..naming import strip_md
from ..paths import ProjectPaths
from ..render.links import wikilink
from ..safe_write import safe_write_text


class MarkdownRenderer:
    def __init__(self, config: dict[str, Any], paths: ProjectPaths, logger):
        self.config = config
        self.paths = paths
        self.logger = logger
        self.marker = config.get("rendering", {}).get("generated_marker", "focuslocust")

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

    def render_mitre(self, objects: list[MitreObject]) -> tuple[int, int]:
        link_map = self._build_link_map(objects)
        enriched = self._enrich_links(objects, link_map)

        written = 0
        skipped = 0

        for obj in enriched:
            template_name = f"mitre/{obj.type}.md.j2"
            content = self.env.get_template(template_name).render(
                obj=obj,
                generated_marker=self.marker,
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
                generated_marker=self.marker,
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
            f"generated_by: {self.marker}",
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
            f"generated_by: {self.marker}",
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
            f"generated_by: {self.marker}",
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
            f"generated_by: {self.marker}",
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
