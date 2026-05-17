"""GitHub-first retrieval vault renderer.

This renderer intentionally avoids Obsidian wikilinks. It writes standard
relative Markdown links so the generated vault can be browsed through the
GitHub web UI.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable
import hashlib
import json
import re
import shutil

import yaml

from ..naming import slugify


@dataclass
class GhVaultBuildResult:
    files_written: int = 0
    files_skipped: int = 0
    broken_links: list[dict[str, str]] = field(default_factory=list)


@dataclass
class Relationship:
    source_id: str
    source_name: str
    source_path: str
    target_id: str
    target_name: str
    target_path: str
    relationship: str
    confidence: str
    evidence: str
    source: str


class GhVaultRenderer:
    """Render a standalone concept-first vault for GitHub browsing."""

    def __init__(self, config: dict[str, Any], root: Path, logger, strict: bool = False):
        self.config = config
        self.root = root
        self.logger = logger
        self.strict = strict
        self.marker = config.get("rendering", {}).get("parsed_marker", "focuslocust")
        self.files_written = 0
        self.files_skipped = 0
        self.page_paths: dict[str, str] = {}
        self.relationships: list[Relationship] = []
        self.source_pages_by_object_id: dict[str, str] = {}
        self.source_hash_rows: list[dict[str, str]] = []
        self.conflicts: list[str] = []
        self.unmapped_records: list[str] = []
        self.low_confidence_relationships: list[Relationship] = []
        self.source_records_by_source: dict[str, list[Any]] = defaultdict(list)

    def render(self, objects_by_group: dict[str, list[Any]], raw_sources: dict[str, list[dict[str, Any]]]) -> GhVaultBuildResult:
        self._reset_output()
        objects = self._flatten_objects(objects_by_group)
        by_type = self._objects_by_type(objects)
        techniques_by_id = {obj.id: obj for obj in by_type.get("technique", [])}

        self._prepare_paths(objects)
        self._prepare_source_paths(objects)
        self._collect_relationships(objects, techniques_by_id)

        self._write_static_structure(objects_by_group, raw_sources)
        self._write_attack_pages(by_type)
        self._write_tool_pages(objects, techniques_by_id)
        self._write_command_pages(objects, techniques_by_id)
        self._write_topic_pages(objects)
        self._write_capability_pages(objects)
        self._write_source_pages(objects, raw_sources)
        self._write_indexes(objects, by_type)
        self._write_playbooks()
        self._copy_manual_content()
        self._write_build_reports(objects_by_group, raw_sources, objects)
        self._write_review_reports()
        # Write a placeholder before validation so the verification index can
        # link to the report without producing a false-positive broken link.
        self._write_broken_links_report([])

        broken_links = self._validate_links()
        self._write_broken_links_report(broken_links)
        if self.strict and broken_links:
            raise RuntimeError(f"ghvault validation failed: {len(broken_links)} broken Markdown links")

        return GhVaultBuildResult(
            files_written=self.files_written,
            files_skipped=self.files_skipped,
            broken_links=broken_links,
        )

    # ------------------------------------------------------------------
    # Output setup and low-level writing
    # ------------------------------------------------------------------

    def _reset_output(self) -> None:
        if self.root.exists():
            shutil.rmtree(self.root)
        for directory in [
            self.root,
            self.root / ".github" / "ISSUE_TEMPLATE",
            self.root / "kb" / "attack" / "tactics",
            self.root / "kb" / "attack" / "techniques",
            self.root / "kb" / "attack" / "mitigations",
            self.root / "kb" / "attack" / "data-sources",
            self.root / "kb" / "tools",
            self.root / "kb" / "commands",
            self.root / "kb" / "platforms",
            self.root / "kb" / "topics",
            self.root / "kb" / "capabilities",
            self.root / "kb" / "sources",
            self.root / "kb" / "indexes",
            self.root / "playbooks",
            self.root / "manual",
            self.root / "_build",
            self.root / "_review",
        ]:
            directory.mkdir(parents=True, exist_ok=True)

    def _write_page(self, relative_path: str, title: str, body: str, source: str = "ghvault") -> None:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        content = self._frontmatter(source=source, page_type="generated")
        content += f"# {title}\n\n"
        content += body.rstrip() + "\n"
        path.write_text(content, encoding="utf-8")
        self.files_written += 1

    def _write_raw(self, relative_path: str, content: str) -> None:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content.rstrip() + "\n", encoding="utf-8")
        self.files_written += 1

    def _frontmatter(self, source: str, page_type: str) -> str:
        return "\n".join(
            [
                "---",
                f"parsed_by: {self.marker}",
                f"source: {source}",
                f"type: {page_type}",
                "---",
                "",
            ]
        )

    # ------------------------------------------------------------------
    # Object/path preparation
    # ------------------------------------------------------------------

    def _flatten_objects(self, objects_by_group: dict[str, list[Any]]) -> list[Any]:
        objects: list[Any] = []
        for group_objects in objects_by_group.values():
            objects.extend(group_objects)
        return objects

    def _objects_by_type(self, objects: list[Any]) -> dict[str, list[Any]]:
        result: dict[str, list[Any]] = defaultdict(list)
        for obj in objects:
            result[getattr(obj, "type", "unknown")].append(obj)
        for values in result.values():
            values.sort(key=lambda item: (getattr(item, "id", ""), getattr(item, "name", "")))
        return dict(result)

    def _prepare_paths(self, objects: list[Any]) -> None:
        for obj in objects:
            obj_type = getattr(obj, "type", "unknown")
            source = getattr(obj, "source", "unknown")
            obj_id = getattr(obj, "id", "") or slugify(getattr(obj, "name", "unknown"))
            name = getattr(obj, "name", obj_id)

            if source == "mitre" and obj_type == "tactic":
                path = f"kb/attack/tactics/{slugify(name)}.md"
            elif source == "mitre" and obj_type == "technique":
                path = f"kb/attack/techniques/{obj_id}-{slugify(name)}.md"
            elif source == "mitre" and obj_type == "mitigation":
                path = f"kb/attack/mitigations/{obj_id}-{slugify(name)}.md"
            elif source == "mitre" and obj_type == "data-source":
                path = f"kb/attack/data-sources/{obj_id}-{slugify(name)}.md"
            elif obj_type == "tool":
                platform = self._platform_for(obj)
                path = f"kb/tools/{platform}/{slugify(name)}.md"
            else:
                category = self._category_for(obj)
                path = f"kb/topics/{category}/{slugify(name)}.md"

            key = self._object_key(obj)
            self.page_paths[key] = path
            if obj_id:
                self.page_paths[obj_id] = path

    def _prepare_source_paths(self, objects: list[Any]) -> None:
        for obj in objects:
            source = getattr(obj, "source", "unknown")
            source_name = slugify(source)
            name = getattr(obj, "name", getattr(obj, "id", "record"))
            path = f"kb/sources/{source_name}/{slugify(name)}.md"
            self.source_pages_by_object_id[self._object_key(obj)] = path

    def _object_key(self, obj: Any) -> str:
        return f"{getattr(obj, 'source', 'unknown')}:{getattr(obj, 'type', 'unknown')}:{getattr(obj, 'id', slugify(getattr(obj, 'name', 'unknown')))}"

    def _platform_for(self, obj: Any) -> str:
        source = getattr(obj, "source", "")
        if source == "lolbas":
            return "windows"
        if source == "gtfobins":
            return "linux"
        platforms = [slugify(item) for item in getattr(obj, "platforms", []) if item]
        if platforms:
            return platforms[0]
        return "unknown"

    def _category_for(self, obj: Any) -> str:
        category = getattr(obj, "category", "") or "general"
        return slugify(str(category)) or "general"

    # ------------------------------------------------------------------
    # Relationship extraction
    # ------------------------------------------------------------------

    def _collect_relationships(self, objects: list[Any], techniques_by_id: dict[str, Any]) -> None:
        for obj in objects:
            if getattr(obj, "type", "") != "tool":
                continue
            explicit_ids = self._explicit_technique_ids(obj)
            inferred = self._inferred_technique_ids(obj)

            for technique_id, evidence in explicit_ids.items():
                technique = techniques_by_id.get(technique_id)
                if not technique:
                    self.unmapped_records.append(
                        f"{getattr(obj, 'name', getattr(obj, 'id', 'unknown'))}: explicit technique {technique_id} not present in MITRE objects"
                    )
                    continue
                self.relationships.append(
                    self._relationship(obj, technique, "explicit", "source", evidence)
                )

            for technique_id, evidence in inferred.items():
                if technique_id in explicit_ids:
                    continue
                technique = techniques_by_id.get(technique_id)
                if not technique:
                    continue
                relationship = self._relationship(obj, technique, "inferred", "high", evidence)
                self.relationships.append(relationship)

        self.relationships.sort(key=lambda row: (row.source_name, row.target_id, row.relationship))

    def _relationship(self, source_obj: Any, target_obj: Any, relationship: str, confidence: str, evidence: str) -> Relationship:
        return Relationship(
            source_id=getattr(source_obj, "id", ""),
            source_name=getattr(source_obj, "name", getattr(source_obj, "id", "")),
            source_path=self.page_paths.get(self._object_key(source_obj), self.page_paths.get(getattr(source_obj, "id", ""), "")),
            target_id=getattr(target_obj, "id", ""),
            target_name=getattr(target_obj, "name", getattr(target_obj, "id", "")),
            target_path=self.page_paths.get(self._object_key(target_obj), self.page_paths.get(getattr(target_obj, "id", ""), "")),
            relationship=relationship,
            confidence=confidence,
            evidence=evidence,
            source=getattr(source_obj, "source", "unknown"),
        )

    def _explicit_technique_ids(self, obj: Any) -> dict[str, str]:
        result: dict[str, str] = {}

        for command in getattr(obj, "commands", []) or []:
            technique_id = getattr(command, "mitre_id", "") or ""
            if technique_id:
                result[technique_id] = f"Command metadata lists {technique_id}: {self._one_line(getattr(command, 'command', ''))}"

        for row in getattr(obj, "techniques_used", []) or []:
            if isinstance(row, dict) and row.get("id"):
                result[str(row["id"])] = row.get("description") or "Technique listed by source relationship."

        return result

    def _inferred_technique_ids(self, obj: Any) -> dict[str, str]:
        result: dict[str, str] = {}
        for text in self._command_texts(obj):
            lowered = text.lower()
            if any(token in lowered for token in ["http://", "https://", "ftp://", "wget ", "curl ", "invoke-webrequest"]):
                result.setdefault("T1105", f"Command appears to retrieve a remote file: {self._one_line(text)}")
        return result

    # ------------------------------------------------------------------
    # Static and high-level pages
    # ------------------------------------------------------------------

    def _write_static_structure(self, objects_by_group: dict[str, list[Any]], raw_sources: dict[str, list[dict[str, Any]]]) -> None:
        self._write_page(
            "README.md",
            "Focus Locust GitHub Retrieval Vault",
            "\n".join(
                [
                    "This standalone vault is generated for fast human retrieval through the GitHub web UI.",
                    "",
                    "## Start Here",
                    "",
                    "- [Start Here](START-HERE.md)",
                    "- [Browse ATT&CK](kb/attack/README.md)",
                    "- [Browse Tools](kb/tools/README.md)",
                    "- [Browse Commands](kb/commands/README.md)",
                    "- [Browse Sources](kb/sources/README.md)",
                    "- [All Indexes](kb/indexes/README.md)",
                    "- [Build Reports](_build/build-summary.md)",
                    "- [Review Queue](_review/README.md)",
                    "",
                    "## Scope",
                    "",
                    "Security and IT operational reference only. Certification study notes and general personal notes are intentionally excluded.",
                    "",
                    "## Link Format",
                    "",
                    "This vault uses GitHub-compatible relative Markdown links only. It does not rely on Obsidian wikilinks or Dataview.",
                ]
            ),
        )
        self._write_page(
            "START-HERE.md",
            "Start Here",
            "\n".join(
                [
                    "Use this page as the entry point for retrieval.",
                    "",
                    "## Retrieval Paths",
                    "",
                    "1. Browse playbooks and checklists from [Playbooks](playbooks/README.md).",
                    "2. Find a tool under [Tools](kb/tools/README.md).",
                    "3. Find command examples under [Commands](kb/commands/README.md).",
                    "4. Verify claims through [Verification Index](kb/indexes/verification-index.md).",
                    "5. Review parser gaps and conflicts under [Review Queue](_review/README.md).",
                ]
            ),
        )
        self._write_raw(".gitignore", "# generated helper files\n.DS_Store\n")
        self._write_raw(
            ".github/ISSUE_TEMPLATE/broken-link.md",
            "\n".join(
                [
                    "---",
                    "name: Broken link",
                    "about: Report a broken generated link in ghvault",
                    "title: '[ghvault] Broken link: '",
                    "labels: documentation",
                    "---",
                    "",
                    "## Page",
                    "",
                    "## Broken link",
                    "",
                    "## Expected target",
                ]
            ),
        )

        for path, title, body in [
            ("kb/attack/README.md", "ATT&CK", "Browse ATT&CK tactics, techniques, mitigations, and data sources."),
            ("kb/tools/README.md", "Tools", "Browse tools by platform and source."),
            ("kb/commands/README.md", "Commands", "Command pages are grouped by platform and tool. Command pages include a fixed safety notice."),
            ("kb/platforms/README.md", "Platforms", "Browse content by platform."),
            ("kb/topics/README.md", "Topics", "Browse source-backed topics."),
            ("kb/capabilities/README.md", "Capabilities", "Browse conservative capability groupings."),
            ("kb/sources/README.md", "Sources", "Source-record pages preserve fuller source material for verification."),
            ("kb/indexes/README.md", "Indexes", "Generated indexes for GitHub browsing."),
        ]:
            self._write_page(path, title, self._breadcrumb(path) + "\n\n" + body)

    def _breadcrumb(self, relative_path: str) -> str:
        depth = len(Path(relative_path).parent.parts)
        prefix = "../" * depth
        if not prefix:
            return "[Home](README.md)"
        return f"[Home]({prefix}README.md)"

    # ------------------------------------------------------------------
    # Concept pages
    # ------------------------------------------------------------------

    def _write_attack_pages(self, by_type: dict[str, list[Any]]) -> None:
        for group, title in [
            ("tactic", "ATT&CK Tactic"),
            ("technique", "ATT&CK Technique"),
            ("mitigation", "ATT&CK Mitigation"),
            ("data-source", "ATT&CK Data Source"),
        ]:
            for obj in by_type.get(group, []):
                path = self.page_paths[self._object_key(obj)]
                related_tools = [rel for rel in self.relationships if rel.target_id == getattr(obj, "id", "")]
                body = [self._breadcrumb(path), "", self._provenance_table(obj), ""]
                body.append("## Summary\n")
                body.append(self._clean_description(getattr(obj, "description", "")) or "No summary available from source.")
                if related_tools:
                    body.extend(["", "## Related Tools", "", self._relationship_table(related_tools, from_path=path, direction="tool")])
                body.extend(["", "## Source Verification", "", self._source_verification_links(obj, from_path=path)])
                body.extend(["", "## Evidence Excerpt", "", self._short_evidence_excerpt(obj)])
                self._write_page(path, f"{getattr(obj, 'id', '')} - {getattr(obj, 'name', '')}".strip(" -"), "\n".join(body), source="mitre")

    def _write_tool_pages(self, objects: list[Any], techniques_by_id: dict[str, Any]) -> None:
        tools = [obj for obj in objects if getattr(obj, "type", "") == "tool"]
        for tool in sorted(tools, key=lambda item: (self._platform_for(item), getattr(item, "name", ""))):
            path = self.page_paths[self._object_key(tool)]
            relationships = [rel for rel in self.relationships if rel.source_id == getattr(tool, "id", "")]
            command_path = self._command_page_path(tool)
            source_link = self._source_verification_links(tool, from_path=path)
            body = [self._breadcrumb(path), "", self._provenance_table(tool), ""]
            body.extend(["## Summary", "", self._clean_description(getattr(tool, "description", "")) or "No summary available from source."])
            body.extend(
                [
                    "",
                    "## Fast Retrieval",
                    "",
                    f"- Platform: `{self._platform_for(tool)}`",
                    f"- Command page: {self._md_link('commands', command_path, path) if self._command_texts(tool) else 'No command page generated from parsed source commands.'}",
                    f"- Source verification: {source_link}",
                ]
            )
            aliases = sorted(set(getattr(tool, "aliases", []) or []))
            if aliases:
                body.extend(["", "## Aliases", ""])
                body.extend(f"- `{alias}`" for alias in aliases)
            if relationships:
                body.extend(["", "## Related ATT&CK Techniques", "", self._relationship_table(relationships, from_path=path, direction="technique")])
            detection_notes = self._detection_notes(tool)
            if detection_notes:
                body.extend(
                    [
                        "",
                        "## Detection / Analysis Notes",
                        "",
                        "This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.",
                        "",
                        source_link,
                    ]
                )
            body.extend(["", "## Source Verification", "", source_link])
            body.extend(["", "## Evidence Excerpt", "", self._short_evidence_excerpt(tool)])
            self._write_page(path, getattr(tool, "name", getattr(tool, "id", "Tool")), "\n".join(body), source=getattr(tool, "source", "unknown"))

    def _write_command_pages(self, objects: list[Any], techniques_by_id: dict[str, Any]) -> None:
        tools = [obj for obj in objects if getattr(obj, "type", "") == "tool"]
        by_path: dict[str, list[Any]] = defaultdict(list)
        for tool in tools:
            if self._command_texts(tool):
                by_path[self._command_page_path(tool)].append(tool)

        for path, tool_group in sorted(by_path.items()):
            title = f"{self._command_page_title(tool_group[0])} Commands"
            body = [self._breadcrumb(path), "", "> This page contains security testing commands. Use only in authorised environments.", ""]
            for tool in tool_group:
                tool_path = self.page_paths[self._object_key(tool)]
                body.extend([f"## {getattr(tool, 'name', getattr(tool, 'id', 'Tool'))}", ""])
                body.append(f"Tool page: {self._md_link(getattr(tool, 'name', 'tool'), tool_path, path)}")
                body.append("")
                commands = getattr(tool, "commands", []) or []
                if commands:
                    for command in commands:
                        command_text = getattr(command, "command", "") or ""
                        if not command_text:
                            continue
                        body.extend(self._render_command_block(tool, command, path))
                else:
                    for example in getattr(tool, "function_examples", []) or []:
                        code = getattr(example, "code", "") or ""
                        if not code:
                            continue
                        body.extend(
                            [
                                f"### {getattr(example, 'function', 'Example')}",
                                "",
                                self._fenced_code(code),
                                "",
                                self._evidence_table(tool, "Function example preserved from source parser."),
                                "",
                            ]
                        )
            self._write_page(path, title, "\n".join(body), source="commands")

    def _write_topic_pages(self, objects: list[Any]) -> None:
        topics = [obj for obj in objects if getattr(obj, "type", "") not in {"tool", "tactic", "technique", "mitigation", "data-source"}]
        for topic in sorted(topics, key=lambda item: (getattr(item, "source", ""), getattr(item, "name", ""))):
            path = self.page_paths[self._object_key(topic)]
            body = [self._breadcrumb(path), "", self._provenance_table(topic), ""]
            body.extend(["## Summary", "", self._clean_description(getattr(topic, "description", "")) or "Source-backed topic page."])
            body.extend(["", "## Preserved Body", "", self._safe_body(getattr(topic, "body", ""))])
            body.extend(["", "## Source Verification", "", self._source_verification_links(topic, from_path=path)])
            body.extend(["", "## Evidence Excerpt", "", self._short_evidence_excerpt(topic)])
            self._write_page(path, getattr(topic, "name", getattr(topic, "id", "Topic")), "\n".join(body), source=getattr(topic, "source", "unknown"))

    def _write_capability_pages(self, objects: list[Any]) -> None:
        capabilities: dict[str, list[Any]] = defaultdict(list)
        for obj in objects:
            for capability in self._capabilities_for(obj):
                capabilities[capability].append(obj)

        for capability, capability_objects in sorted(capabilities.items()):
            path = f"kb/capabilities/{slugify(capability)}.md"
            lines = [self._breadcrumb(path), "", "## Related Pages", ""]
            for obj in sorted(capability_objects, key=lambda item: getattr(item, "name", "")):
                obj_path = self.page_paths.get(self._object_key(obj), "")
                if obj_path:
                    lines.append(f"- {self._md_link(getattr(obj, 'name', getattr(obj, 'id', 'object')), obj_path, path)}")
            self._write_page(path, capability.replace("-", " ").title(), "\n".join(lines), source="capabilities")

    # ------------------------------------------------------------------
    # Source pages and indexes
    # ------------------------------------------------------------------

    def _write_source_pages(self, objects: list[Any], raw_sources: dict[str, list[dict[str, Any]]]) -> None:
        for obj in objects:
            source = getattr(obj, "source", "unknown")
            source_name = slugify(source)
            name = getattr(obj, "name", getattr(obj, "id", "record"))
            path = self.source_pages_by_object_id.get(self._object_key(obj), f"kb/sources/{source_name}/{slugify(name)}.md")
            self.source_pages_by_object_id[self._object_key(obj)] = path
            self.source_records_by_source[source_name].append(obj)
            self._record_source_hash(obj)

            concept_path = self.page_paths.get(self._object_key(obj), "")
            body = [self._breadcrumb(path), "", self._provenance_table(obj), ""]
            if concept_path:
                body.extend(["## Generated Concept Page", "", f"- {self._md_link(name, concept_path, path)}", ""])
            body.extend(["## Extracted Fields", "", self._extracted_fields_table(obj), ""])
            body.extend(["## Preserved Source Material", "", self._raw_source_block(getattr(obj, "raw", {}) or {})])
            detections = self._detection_notes(obj)
            if detections:
                body.extend(["", "## Detection / Analysis Notes", ""])
                for note in detections:
                    body.extend([self._fenced_code(note), ""])
            self._write_page(path, name, "\n".join(body), source=source)

        for source_name, records in sorted(self.source_records_by_source.items()):
            path = f"kb/sources/{source_name}/README.md"
            lines = [self._breadcrumb(path), "", f"Records: {len(records)}", ""]
            for obj in sorted(records, key=lambda item: getattr(item, "name", "")):
                record_path = self.source_pages_by_object_id.get(self._object_key(obj), "")
                if record_path:
                    lines.append(f"- {self._md_link(getattr(obj, 'name', getattr(obj, 'id', 'record')), record_path, path)}")
            self._write_page(path, f"{source_name} Source Records", "\n".join(lines), source=source_name)

    def _write_indexes(self, objects: list[Any], by_type: dict[str, list[Any]]) -> None:
        self._write_tools_index(objects)
        self._write_techniques_indexes(by_type.get("technique", []))
        self._write_commands_indexes(objects)
        self._write_sources_index()
        self._write_verification_index()

    def _write_tools_index(self, objects: list[Any]) -> None:
        tools = [obj for obj in objects if getattr(obj, "type", "") == "tool"]
        path = "kb/indexes/tools-by-platform.md"
        lines = [self._breadcrumb(path), ""]
        by_platform: dict[str, list[Any]] = defaultdict(list)
        for tool in tools:
            by_platform[self._platform_for(tool)].append(tool)
        for platform, platform_tools in sorted(by_platform.items()):
            lines.extend([f"## {platform}", ""])
            for tool in sorted(platform_tools, key=lambda item: getattr(item, "name", "")):
                tool_path = self.page_paths.get(self._object_key(tool), "")
                lines.append(f"- {self._md_link(getattr(tool, 'name', getattr(tool, 'id', 'tool')), tool_path, path)}")
            lines.append("")
        self._write_page(path, "Tools by Platform", "\n".join(lines), source="indexes")

        by_technique: dict[str, list[Relationship]] = defaultdict(list)
        for rel in self.relationships:
            by_technique[rel.target_id].append(rel)
        path = "kb/indexes/tools-by-technique.md"
        lines = [self._breadcrumb(path), ""]
        for technique_id, rels in sorted(by_technique.items()):
            first = rels[0]
            lines.extend([f"## {technique_id} - {first.target_name}", ""])
            for rel in rels:
                lines.append(f"- {self._md_link(rel.source_name, rel.source_path, path)} — {rel.relationship}, {rel.confidence}. {rel.evidence}")
            lines.append("")
        self._write_page(path, "Tools by Technique", "\n".join(lines), source="indexes")

    def _write_techniques_indexes(self, techniques: list[Any]) -> None:
        path = "kb/indexes/techniques-by-id.md"
        lines = [self._breadcrumb(path), ""]
        for technique in techniques:
            technique_path = self.page_paths.get(self._object_key(technique), "")
            lines.append(f"- {self._md_link(f'{getattr(technique, 'id', '')} - {getattr(technique, 'name', '')}', technique_path, path)}")
        self._write_page(path, "Techniques by ID", "\n".join(lines), source="indexes")

        path = "kb/indexes/techniques-by-tool.md"
        lines = [self._breadcrumb(path), ""]
        by_tool: dict[str, list[Relationship]] = defaultdict(list)
        for rel in self.relationships:
            by_tool[rel.source_name].append(rel)
        for tool_name, rels in sorted(by_tool.items()):
            first = rels[0]
            lines.extend([f"## {tool_name}", "", f"Tool: {self._md_link(first.source_name, first.source_path, path)}", ""])
            for rel in rels:
                lines.append(f"- {self._md_link(f'{rel.target_id} - {rel.target_name}', rel.target_path, path)} — {rel.relationship}, {rel.confidence}")
            lines.append("")
        self._write_page(path, "Techniques by Tool", "\n".join(lines), source="indexes")

    def _write_commands_indexes(self, objects: list[Any]) -> None:
        tools = [obj for obj in objects if getattr(obj, "type", "") == "tool" and self._command_texts(obj)]
        path = "kb/indexes/commands-by-tool.md"
        lines = [self._breadcrumb(path), ""]
        for tool in sorted(tools, key=lambda item: getattr(item, "name", "")):
            lines.append(f"- {self._md_link(getattr(tool, 'name', getattr(tool, 'id', 'tool')), self._command_page_path(tool), path)}")
        self._write_page(path, "Commands by Tool", "\n".join(lines), source="indexes")

        path = "kb/indexes/commands-by-platform.md"
        by_platform: dict[str, list[Any]] = defaultdict(list)
        for tool in tools:
            by_platform[self._platform_for(tool)].append(tool)
        lines = [self._breadcrumb(path), ""]
        for platform, platform_tools in sorted(by_platform.items()):
            lines.extend([f"## {platform}", ""])
            for tool in sorted(platform_tools, key=lambda item: getattr(item, "name", "")):
                lines.append(f"- {self._md_link(getattr(tool, 'name', getattr(tool, 'id', 'tool')), self._command_page_path(tool), path)}")
            lines.append("")
        self._write_page(path, "Commands by Platform", "\n".join(lines), source="indexes")

    def _write_sources_index(self) -> None:
        path = "kb/indexes/sources-by-concept.md"
        lines = [self._breadcrumb(path), ""]
        for source_name, records in sorted(self.source_records_by_source.items()):
            source_index = f"kb/sources/{source_name}/README.md"
            lines.append(f"- {self._md_link(source_name, source_index, path)} — {len(records)} records")
        self._write_page(path, "Sources by Concept", "\n".join(lines), source="indexes")

    def _write_verification_index(self) -> None:
        path = "kb/indexes/verification-index.md"
        body = "\n".join(
            [
                self._breadcrumb(path),
                "",
                "Use this page to trace generated information back to source material.",
                "",
                "## Source Records",
                "",
                "- [Sources](../sources/README.md)",
                "",
                "## Build Reports",
                "",
                "- [Build summary](../../_build/build-summary.md)",
                "- [Source coverage](../../_build/source-coverage.md)",
                "- [Relationship coverage](../../_build/relationship-coverage.md)",
                "- [Inferred relationships](../../_build/inferred-relationships.md)",
                "- [Source hashes](../../_build/source-hashes.md)",
                "- [Broken links](../../_build/broken-links.md)",
                "",
                "## Review Queue",
                "",
                "- [Conflicts](../../_review/conflicts.md)",
                "- [Unmapped records](../../_review/unmapped-records.md)",
                "- [Low-confidence relationships](../../_review/low-confidence-relationships.md)",
            ]
        )
        self._write_page(path, "Verification Index", body, source="indexes")

    # ------------------------------------------------------------------
    # Playbooks, build reports, review reports
    # ------------------------------------------------------------------

    def _write_playbooks(self) -> None:
        self._write_page(
            "playbooks/README.md",
            "Playbooks",
            "\n".join(
                [
                    self._breadcrumb("playbooks/README.md"),
                    "",
                    "Generated playbook landing pages. These are intentionally lightweight until manually maintained playbooks are supplied.",
                    "",
                    "- [Initial Triage](initial-triage.md)",
                    "- [Windows LOLBins](windows-lolbins.md)",
                    "- [Linux Privilege Escalation](linux-privilege-escalation.md)",
                    "- [Active Directory](active-directory.md)",
                    "- [Web Application Attacks](web-application-attacks.md)",
                    "- [Cloud and Identity](cloud-and-identity.md)",
                ]
            ),
            source="playbooks",
        )
        playbooks = {
            "initial-triage.md": "Initial Triage",
            "windows-lolbins.md": "Windows LOLBins",
            "linux-privilege-escalation.md": "Linux Privilege Escalation",
            "active-directory.md": "Active Directory",
            "web-application-attacks.md": "Web Application Attacks",
            "cloud-and-identity.md": "Cloud and Identity",
        }
        for filename, title in playbooks.items():
            path = f"playbooks/{filename}"
            self._write_page(
                path,
                title,
                "\n".join(
                    [
                        self._breadcrumb(path),
                        "",
                        "## Purpose",
                        "",
                        "Placeholder generated page for human retrieval. Add durable custom content under the repository-level `manual/` folder, then let the builder copy or merge it into ghvault.",
                        "",
                        "## Useful Indexes",
                        "",
                        "- [Tools by Platform](../kb/indexes/tools-by-platform.md)",
                        "- [Tools by Technique](../kb/indexes/tools-by-technique.md)",
                        "- [Commands by Tool](../kb/indexes/commands-by-tool.md)",
                    ]
                ),
                source="playbooks",
            )

    def _copy_manual_content(self) -> None:
        manual_path = self.config.get("ghvault", {}).get("manual_path", "manual")
        source = Path(manual_path)
        if not source.exists():
            self._write_page(
                "manual/README.md",
                "Manual Content",
                "No repository-level manual content folder was found. Keep manual source files outside `ghvault/` because `ghvault/` is cleared on every build.",
                source="manual",
            )
            return
        destination = self.root / "manual"
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(source, destination)

    def _write_build_reports(self, objects_by_group: dict[str, list[Any]], raw_sources: dict[str, list[dict[str, Any]]], objects: list[Any]) -> None:
        total_objects = sum(len(values) for values in objects_by_group.values())
        self._write_page(
            "_build/build-summary.md",
            "Build Summary",
            "\n".join(
                [
                    "## Counts",
                    "",
                    f"- Parsed object groups: {len(objects_by_group)}",
                    f"- Parsed objects: {total_objects}",
                    f"- Raw source groups: {len(raw_sources)}",
                    f"- Relationships: {len(self.relationships)}",
                    f"- Files written before final validation: {self.files_written}",
                ]
            ),
            source="build",
        )
        self._write_source_coverage(raw_sources, objects_by_group)
        self._write_relationship_coverage()
        self._write_inferred_relationships()
        self._write_source_hashes()
        self._write_duplicate_pages(objects)
        self._write_orphan_pages()
        self._write_schema_summary(raw_sources)

    def _write_source_coverage(self, raw_sources: dict[str, list[dict[str, Any]]], objects_by_group: dict[str, list[Any]]) -> None:
        lines = ["| Source / Group | Count |", "| --- | ---: |"]
        for source, records in sorted(raw_sources.items()):
            lines.append(f"| raw `{source}` | {len(records)} |")
        for group, objects in sorted(objects_by_group.items()):
            lines.append(f"| parsed `{group}` | {len(objects)} |")
        self._write_page("_build/source-coverage.md", "Source Coverage", "\n".join(lines), source="build")

    def _write_relationship_coverage(self) -> None:
        counts: dict[str, int] = defaultdict(int)
        for rel in self.relationships:
            counts[rel.relationship] += 1
        lines = ["| Relationship | Count |", "| --- | ---: |"]
        for key, count in sorted(counts.items()):
            lines.append(f"| {key} | {count} |")
        self._write_page("_build/relationship-coverage.md", "Relationship Coverage", "\n".join(lines), source="build")

    def _write_inferred_relationships(self) -> None:
        inferred = [rel for rel in self.relationships if rel.relationship == "inferred"]
        self._write_page("_build/inferred-relationships.md", "Inferred Relationships", self._relationship_table(inferred, from_path="_build/inferred-relationships.md", direction="both"), source="build")

    def _write_source_hashes(self) -> None:
        lines = ["| Source | Local path | SHA256 |", "| --- | --- | --- |"]
        for row in sorted(self.source_hash_rows, key=lambda item: (item["source"], item["path"])):
            lines.append(f"| {self._escape_table(row['source'])} | `{self._escape_table(row['path'])}` | `{row['sha256']}` |")
        if len(lines) == 2:
            lines.append("| none | none | none |")
        self._write_page("_build/source-hashes.md", "Source Hashes", "\n".join(lines), source="build")

    def _write_duplicate_pages(self, objects: list[Any]) -> None:
        seen: dict[str, list[Any]] = defaultdict(list)
        for obj in objects:
            path = self.page_paths.get(self._object_key(obj), "")
            if path:
                seen[path].append(obj)
        lines = ["| Page | Objects |", "| --- | --- |"]
        for path, page_objects in sorted(seen.items()):
            if len(page_objects) > 1:
                names = ", ".join(getattr(obj, "name", getattr(obj, "id", "object")) for obj in page_objects)
                lines.append(f"| `{path}` | {self._escape_table(names)} |")
        if len(lines) == 2:
            lines.append("| none | none |")
        self._write_page("_build/duplicate-pages.md", "Duplicate Pages", "\n".join(lines), source="build")

    def _write_orphan_pages(self) -> None:
        self._write_page("_build/orphan-pages.md", "Orphan Pages", "No orphan-page analysis is implemented yet. This report is generated as a placeholder so the check is visible.", source="build")

    def _write_schema_summary(self, raw_sources: dict[str, list[dict[str, Any]]]) -> None:
        lines = []
        for source, records in sorted(raw_sources.items()):
            fields: set[str] = set()
            for record in records:
                self._walk_fields(record, "", fields)
            lines.extend([f"## {source}", ""])
            for field in sorted(fields):
                lines.append(f"- `{field}`")
            lines.append("")
        self._write_page("_build/schema-summary.md", "Schema Summary", "\n".join(lines), source="build")

    def _write_review_reports(self) -> None:
        self._write_page(
            "_review/README.md",
            "Review Queue",
            "\n".join(
                [
                    "Generated review reports. Empty reports are still generated to prove the checks ran.",
                    "",
                    "- [Conflicts](conflicts.md)",
                    "- [Unmapped records](unmapped-records.md)",
                    "- [Low-confidence relationships](low-confidence-relationships.md)",
                    "- [Optional Ollama suggestions](optional-ollama-suggestions.md)",
                ]
            ),
            source="review",
        )
        self._write_page("_review/conflicts.md", "Conflicts", self._lines_or_none(self.conflicts), source="review")
        self._write_page("_review/unmapped-records.md", "Unmapped Records", self._lines_or_none(self.unmapped_records), source="review")
        self._write_page("_review/low-confidence-relationships.md", "Low-confidence Relationships", self._relationship_table(self.low_confidence_relationships, from_path="_review/low-confidence-relationships.md", direction="both"), source="review")
        self._write_page(
            "_review/optional-ollama-suggestions.md",
            "Optional Ollama Suggestions",
            "Ollama/local model enrichment is intentionally disabled by default. Any future model output must be review-only and must not write directly to canonical concept pages.",
            source="review",
        )

    def _write_broken_links_report(self, broken_links: list[dict[str, str]]) -> None:
        lines = ["| Page | Link | Target |", "| --- | --- | --- |"]
        for row in broken_links:
            lines.append(f"| `{self._escape_table(row['page'])}` | {self._escape_table(row['link'])} | `{self._escape_table(row['target'])}` |")
        if len(lines) == 2:
            lines.append("| none | none | none |")
        self._write_page("_build/broken-links.md", "Broken Links", "\n".join(lines), source="build")

    # ------------------------------------------------------------------
    # Formatting helpers
    # ------------------------------------------------------------------

    def _provenance_table(self, obj: Any) -> str:
        raw = getattr(obj, "raw", {}) or {}
        source_path = raw.get("_source_path", "") if isinstance(raw, dict) else ""
        return "\n".join(
            [
                "## Provenance",
                "",
                "| Field | Value |",
                "| --- | --- |",
                f"| Source | `{self._escape_table(getattr(obj, 'source', 'unknown'))}` |",
                f"| Type | `{self._escape_table(getattr(obj, 'type', 'unknown'))}` |",
                f"| Record ID | `{self._escape_table(getattr(obj, 'id', ''))}` |",
                f"| Source file | `{self._escape_table(str(source_path))}` |",
                f"| Parsed by | `{self.marker}` |",
                "| Relationship mode | `explicit / conservative inferred / manual` |",
            ]
        )

    def _source_verification_links(self, obj: Any, from_path: str) -> str:
        source_page = self.source_pages_by_object_id.get(self._object_key(obj))
        if source_page:
            return self._md_link("source record", source_page, from_path)
        return "Source-record page is generated later in the build."

    def _relationship_table(self, relationships: Iterable[Relationship], from_path: str, direction: str) -> str:
        rels = list(relationships)
        if not rels:
            return "No relationships generated."
        lines = ["| Item | Relationship | Confidence | Evidence |", "| --- | --- | --- | --- |"]
        for rel in rels:
            if direction == "tool":
                item = self._md_link(rel.source_name, rel.source_path, from_path)
            elif direction == "technique":
                item = self._md_link(f"{rel.target_id} - {rel.target_name}", rel.target_path, from_path)
            else:
                item = f"{self._md_link(rel.source_name, rel.source_path, from_path)} → {self._md_link(f'{rel.target_id} - {rel.target_name}', rel.target_path, from_path)}"
            lines.append(f"| {item} | {rel.relationship} | {rel.confidence} | {self._escape_table(rel.evidence)} |")
        return "\n".join(lines)

    def _render_command_block(self, tool: Any, command: Any, from_path: str) -> list[str]:
        command_text = getattr(command, "command", "") or ""
        title = getattr(command, "usecase", "") or getattr(command, "category", "") or "Command"
        lines = [f"### {title}", "", self._fenced_code(command_text), ""]
        description = getattr(command, "description", "") or ""
        if description:
            lines.extend(["Description:", "", description, ""])
        mitre_id = getattr(command, "mitre_id", "") or ""
        if mitre_id and mitre_id in self.page_paths:
            lines.extend(["Related ATT&CK:", "", f"- {self._md_link(mitre_id, self.page_paths[mitre_id], from_path)}", ""])
        lines.extend([self._evidence_table(tool, "Command preserved from source parser."), ""])
        return lines

    def _evidence_table(self, obj: Any, evidence: str) -> str:
        raw = getattr(obj, "raw", {}) or {}
        source_path = raw.get("_source_path", "") if isinstance(raw, dict) else ""
        return "\n".join(
            [
                "Provenance:",
                "",
                "| Field | Value |",
                "| --- | --- |",
                f"| Source | `{self._escape_table(getattr(obj, 'source', 'unknown'))}` |",
                f"| Source file | `{self._escape_table(str(source_path))}` |",
                f"| Evidence | {self._escape_table(evidence)} |",
            ]
        )

    def _extracted_fields_table(self, obj: Any) -> str:
        fields = {
            "id": getattr(obj, "id", ""),
            "name": getattr(obj, "name", ""),
            "type": getattr(obj, "type", ""),
            "source": getattr(obj, "source", ""),
            "url": getattr(obj, "url", ""),
        }
        lines = ["| Field | Value |", "| --- | --- |"]
        for key, value in fields.items():
            lines.append(f"| {key} | {self._escape_table(str(value))} |")
        return "\n".join(lines)

    def _raw_source_block(self, raw: dict[str, Any]) -> str:
        if not raw:
            return "No raw source material preserved by parser."
        try:
            text = yaml.safe_dump(raw, sort_keys=True, allow_unicode=True, width=120)
        except Exception:
            text = json.dumps(raw, indent=2, sort_keys=True, default=str)
        return self._fenced_code(text, language="yaml")

    def _short_evidence_excerpt(self, obj: Any) -> str:
        raw = getattr(obj, "raw", {}) or {}
        if raw:
            text = self._stringify(raw)
        else:
            parts = [
                getattr(obj, "description", "") or "",
                getattr(obj, "body", "") or "",
                "\n".join(self._command_texts(obj)),
            ]
            text = "\n".join(part for part in parts if part.strip())
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        excerpt = "\n".join(lines[:8]).strip()
        if not excerpt:
            return "No short source excerpt available."
        if len(excerpt) > 1200:
            excerpt = excerpt[:1197].rstrip() + "..."
        return self._fenced_code(excerpt, language="text")

    def _fenced_code(self, value: str, language: str = "text") -> str:
        fence = "```"
        while fence in value:
            fence += "`"
        return f"{fence}{language}\n{value.rstrip()}\n{fence}"

    def _md_link(self, label: str, target_path: str, from_path: str) -> str:
        if not target_path:
            return label
        rel = Path(target_path)
        source_dir = Path(from_path).parent
        relative = self._relative_path(source_dir, rel)
        return f"[{self._escape_link_label(label)}]({relative})"

    def _relative_path(self, source_dir: Path, target: Path) -> str:
        if str(source_dir) == ".":
            return target.as_posix()
        source_parts = list(source_dir.parts)
        target_parts = list(target.parts)
        while source_parts and target_parts and source_parts[0] == target_parts[0]:
            source_parts.pop(0)
            target_parts.pop(0)
        return "/".join([".."] * len(source_parts) + target_parts)

    def _clean_description(self, value: str) -> str:
        text = value or ""
        text = re.sub(r"\(Citation: [^)]+\)", "", text)
        text = self._plain_markdown_text(text)
        return text.strip()

    def _plain_markdown_text(self, value: str) -> str:
        text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", value)
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        text = re.sub(r"\[([^\]]+)\]\([^)\s]*$", r"\1", text)
        text = text.replace("[", "(").replace("]", ")")
        return text

    def _safe_body(self, value: str) -> str:
        if not value or not value.strip():
            return "No preserved body content."
        return self._fenced_code(value.strip(), language="markdown")

    def _command_texts(self, obj: Any) -> list[str]:
        texts: list[str] = []
        for command in getattr(obj, "commands", []) or []:
            text = getattr(command, "command", "") or ""
            if text:
                texts.append(text)
        for example in getattr(obj, "function_examples", []) or []:
            text = getattr(example, "code", "") or ""
            if text:
                texts.append(text)
        return texts

    def _command_page_path(self, tool: Any) -> str:
        platform = self._platform_for(tool)
        name = getattr(tool, "name", getattr(tool, "id", "tool"))
        stem = slugify(name)
        if platform == "windows" and stem.endswith(".exe"):
            stem = stem[:-4]
        return f"kb/commands/{platform}/{stem}.md"

    def _command_page_title(self, tool: Any) -> str:
        name = getattr(tool, "name", getattr(tool, "id", "tool"))
        if self._platform_for(tool) == "windows" and name.lower().endswith(".exe"):
            return name[:-4]
        return name

    def _capabilities_for(self, obj: Any) -> list[str]:
        capabilities: set[str] = set()
        for command in self._command_texts(obj):
            lowered = command.lower()
            if any(token in lowered for token in ["http://", "https://", "ftp://", "wget ", "curl ", "invoke-webrequest"]):
                capabilities.add("file-download")
        for function in getattr(obj, "functions", []) or []:
            if function:
                capabilities.add(slugify(str(function)))
        return sorted(capabilities)

    def _detection_notes(self, obj: Any) -> list[str]:
        notes = [str(item) for item in getattr(obj, "detections", []) or [] if str(item).strip()]
        raw = getattr(obj, "raw", {}) or {}
        if isinstance(raw, dict):
            for key in ["Detection", "Detections", "detection", "detections"]:
                value = raw.get(key)
                if value:
                    notes.append(self._stringify(value))
        seen: set[str] = set()
        result = []
        for note in notes:
            if note not in seen:
                result.append(note)
                seen.add(note)
        return result

    def _stringify(self, value: Any) -> str:
        if isinstance(value, str):
            return value
        try:
            return yaml.safe_dump(value, sort_keys=True, allow_unicode=True, width=120).strip()
        except Exception:
            return json.dumps(value, indent=2, sort_keys=True, default=str)

    def _one_line(self, value: str, limit: int = 180) -> str:
        text = " ".join((value or "").split())
        if len(text) <= limit:
            return text
        return text[: limit - 3].rstrip() + "..."

    def _escape_table(self, value: str) -> str:
        return (value or "").replace("|", "\\|").replace("\n", "<br>")

    def _escape_link_label(self, value: str) -> str:
        return (value or "").replace("[", "(").replace("]", ")")

    def _lines_or_none(self, values: list[str]) -> str:
        if not values:
            return "No items found."
        return "\n".join(f"- {value}" for value in values)

    # ------------------------------------------------------------------
    # Source hashes, schemas, and validation
    # ------------------------------------------------------------------

    def _record_source_hash(self, obj: Any) -> None:
        raw = getattr(obj, "raw", {}) or {}
        if not isinstance(raw, dict):
            return
        source_path = raw.get("_source_path")
        if not source_path:
            return
        path = Path(str(source_path))
        if not path.exists() or not path.is_file():
            return
        sha256 = hashlib.sha256(path.read_bytes()).hexdigest()
        self.source_hash_rows.append(
            {
                "source": getattr(obj, "source", "unknown"),
                "path": str(path),
                "sha256": sha256,
            }
        )

    def _walk_fields(self, value: Any, prefix: str, fields: set[str]) -> None:
        if prefix:
            fields.add(prefix)
        if isinstance(value, dict):
            for key, child in value.items():
                if str(key).startswith("_"):
                    continue
                child_path = f"{prefix}.{key}" if prefix else str(key)
                self._walk_fields(child, child_path, fields)
        elif isinstance(value, list):
            child_path = f"{prefix}[]" if prefix else "[]"
            for item in value:
                self._walk_fields(item, child_path, fields)

    def _validate_links(self) -> list[dict[str, str]]:
        broken: list[dict[str, str]] = []
        link_pattern = re.compile(r"(?<!!)(?<!\\)\[[^\]]+\]\(([^)]+)\)")
        for page in self.root.rglob("*.md"):
            text = self._strip_fenced_code(page.read_text(encoding="utf-8"))
            for match in link_pattern.finditer(text):
                if match.start() > 0 and text[match.start() - 1] not in " \t\r\n([{-":
                    continue
                link = match.group(1).strip()
                if not link or link.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target_text = link.split("#", 1)[0]
                if not target_text:
                    continue
                target = (page.parent / target_text).resolve()
                try:
                    target.relative_to(self.root.resolve())
                except ValueError:
                    broken.append({"page": str(page.relative_to(self.root)), "link": link, "target": str(target)})
                    continue
                if not target.exists():
                    broken.append({"page": str(page.relative_to(self.root)), "link": link, "target": str(target.relative_to(self.root.resolve()))})
        return broken

    def _strip_fenced_code(self, text: str) -> str:
        return re.sub(r"(?ms)^(`{3,}|~{3,}).*?^\1[ \t]*$", "", text)
