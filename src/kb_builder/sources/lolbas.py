from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from ..models import ExternalReference, LolbasCommand, LolbasTool
from ..naming import slugify
from ..paths import resolve_repo_path


class LolbasSource:
    """
    Loader/parser for LOLBAS/LOLBins-style YAML sources.

    Design notes:
    - Preserve the complete source YAML in `tool.raw`.
    - Populate normalized fields for common vault/index use.
    - Avoid discarding LOLBAS-specific nested data such as:
      - Code_Sample[].Code
      - Commands[].Tags[]
      - Detection[].Sigma / Elastic / Splunk / IOC / BlockRule
      - Acknowledgement[].Person / Handle
    """

    def __init__(self, config: dict[str, Any], logger):
        self.config = config
        self.logger = logger

    def load(self) -> list[dict[str, Any]]:
        local_path = self.config.get("local_path")
        if not local_path:
            raise ValueError("LOLBAS/LOLBins source requires sources.lolbins.local_path")

        path = resolve_repo_path(local_path, "sources.lolbins.local_path")
        files = self._yaml_files(path)
        self.logger.info(f"Loading LOLBAS YAML files: {len(files)}")

        records: list[dict[str, Any]] = []
        for file_path in files:
            data = yaml.safe_load(file_path.read_text(encoding="utf-8")) or {}
            if isinstance(data, dict):
                data.setdefault("_source_path", str(file_path))
                records.append(data)

        return records

    def parse(self, records: list[dict[str, Any]]) -> list[LolbasTool]:
        tools: list[LolbasTool] = []
        for record in records:
            tool = self._parse_tool(record)
            if tool:
                tools.append(tool)

        tools.sort(key=lambda item: item.id)
        self.logger.info(f"Parsed LOLBAS tools: {len(tools)}")
        return tools

    def _yaml_files(self, path: Path) -> list[Path]:
        if path.is_file():
            return [path]

        if not path.is_dir():
            raise FileNotFoundError(f"LOLBAS/LOLBins local_path not found: {path}")

        files = [
            item
            for item in path.rglob("*")
            if item.is_file() and item.suffix.lower() in {".yml", ".yaml"}
        ]
        return sorted(files)

    def _parse_tool(self, record: dict[str, Any]) -> LolbasTool | None:
        name = str(record.get("Name") or record.get("name") or "").strip()
        if not name:
            self.logger.warning(
                f"Skipping LOLBAS record without Name: {record.get('_source_path', '')}"
            )
            return None

        tool_id = slugify(name)

        commands = self._commands(record.get("Commands") or record.get("commands") or [])
        resources = self._links_from_key(
            record.get("Resources") or record.get("resources") or [],
            "Link",
        )
        paths = self._links_from_key(
            record.get("Full_Path")
            or record.get("FullPath")
            or record.get("Paths")
            or [],
            "Path",
        )
        code_samples = self._links_from_key(
            record.get("Code_Sample")
            or record.get("CodeSample")
            or record.get("Code_Samples")
            or [],
            "Code",
        )
        detections_by_type = self._detections_by_type(
            record.get("Detection") or record.get("Detections") or []
        )
        acknowledgement_strings = self._acknowledgements(
            record.get("Acknowledgement") or record.get("Acknowledgements") or []
        )

        tool = LolbasTool(
            id=tool_id,
            source="lolbas",
            type="tool",
            name=name,
            description=str(
                record.get("Description") or record.get("description") or ""
            ).strip(),
            url=self._first_url(resources),
            aliases=sorted(set(filter(None, [name, tool_id]))),
            tags=self._tool_tags(record, commands),
            raw=record,
            external_references=[
                ExternalReference(source_name="lolbas-resource", url=url)
                for url in resources
                if url.startswith(("http://", "https://"))
            ],
        )

        # Normalized fields expected by the generic vault renderer.
        tool.functions = sorted({command.category for command in commands if command.category})
        tool.commands = commands
        tool.paths = paths
        tool.resources = resources
        tool.acknowledgements = acknowledgement_strings
        tool.detections = self._flatten_detections(detections_by_type)
        tool.path = f"kb/lolbas/tools/{tool_id}.md"

        # Optional dynamic attributes.
        # These are safe if your models allow extra attributes. If your model uses
        # strict pydantic/dataclasses slots, remove these and rely on tool.raw in
        # the template instead.
        try:
            tool.code_samples = code_samples
            tool.detections_by_type = detections_by_type
        except Exception:
            pass

        return tool

    def _commands(self, values: Any) -> list[LolbasCommand]:
        commands: list[LolbasCommand] = []

        for value in values if isinstance(values, list) else []:
            if not isinstance(value, dict):
                continue

            command = LolbasCommand(
                command=str(value.get("Command") or "").strip(),
                description=str(value.get("Description") or "").strip(),
                usecase=str(value.get("Usecase") or value.get("UseCase") or "").strip(),
                category=str(value.get("Category") or "").strip(),
                privileges=str(value.get("Privileges") or "").strip(),
                mitre_id=str(value.get("MitreID") or value.get("MitreId") or "").strip(),
                operating_system=str(value.get("OperatingSystem") or "").strip(),
            )

            # Optional dynamic attribute for LOLBAS command tags.
            # Template should still prefer raw access for maximum compatibility.
            try:
                command.tags = self._command_tags(value.get("Tags") or [])
            except Exception:
                pass

            commands.append(command)

        return commands

    def _command_tags(self, values: Any) -> dict[str, list[str]]:
        """
        Converts LOLBAS command tags like:
            Tags:
              - Execute: HTA
              - Execute: Remote
              - Download: INetCache

        Into:
            {
              "Execute": ["HTA", "Remote"],
              "Download": ["INetCache"]
            }
        """
        result: dict[str, list[str]] = {}

        if not isinstance(values, list):
            return result

        for value in values:
            if not isinstance(value, dict):
                continue

            for key, item in value.items():
                if item is None:
                    continue
                result.setdefault(str(key).strip(), []).append(str(item).strip())

        return {
            key: sorted(set(filter(None, items)))
            for key, items in result.items()
            if key
        }

    def _links_from_key(self, values: Any, key: str) -> list[str]:
        """
        Extracts a list of strings from a list of dictionaries using a preferred key.

        Handles common LOLBAS forms:
            Resources[].Link
            Full_Path[].Path
            Code_Sample[].Code
        """
        result: list[str] = []

        if isinstance(values, str) and values.strip():
            return [values.strip()]

        if not isinstance(values, list):
            return result

        for value in values:
            if isinstance(value, str) and value.strip():
                result.append(value.strip())
            elif isinstance(value, dict):
                item = value.get(key)
                if item:
                    result.append(str(item).strip())

        return sorted(set(filter(None, result)))

    def _detections_by_type(self, values: Any) -> dict[str, list[str]]:
        """
        Preserves LOLBAS detection subtypes:
            Detection[].Sigma
            Detection[].Elastic
            Detection[].Splunk
            Detection[].IOC
            Detection[].BlockRule
        """
        result: dict[str, list[str]] = {}

        if isinstance(values, str) and values.strip():
            return {"Detection": [values.strip()]}

        if not isinstance(values, list):
            return result

        for value in values:
            if isinstance(value, str) and value.strip():
                result.setdefault("Detection", []).append(value.strip())
            elif isinstance(value, dict):
                for key, item in value.items():
                    if item is None:
                        continue
                    key_text = str(key).strip()
                    item_text = str(item).strip()
                    if key_text and item_text:
                        result.setdefault(key_text, []).append(item_text)

        return {
            key: sorted(set(filter(None, items)))
            for key, items in result.items()
            if key
        }

    def _flatten_detections(self, detections_by_type: dict[str, list[str]]) -> list[str]:
        result: list[str] = []
        for key in sorted(detections_by_type):
            for value in detections_by_type[key]:
                result.append(f"{key}: {value}")
        return result

    def _acknowledgements(self, values: Any) -> list[str]:
        result: list[str] = []

        if isinstance(values, str) and values.strip():
            return [values.strip()]

        if not isinstance(values, list):
            return result

        for value in values:
            if isinstance(value, str) and value.strip():
                result.append(value.strip())
            elif isinstance(value, dict):
                person = str(value.get("Person") or "").strip()
                handle = str(value.get("Handle") or "").strip()

                if person and handle:
                    result.append(f"{person} ({handle})")
                elif person:
                    result.append(person)
                elif handle:
                    result.append(handle)

        return sorted(set(filter(None, result)))

    def _tool_tags(
        self,
        record: dict[str, Any],
        commands: list[LolbasCommand],
    ) -> list[str]:
        tags = {"lolbas/tool", "platform/windows"}

        for command in commands:
            if command.category:
                tags.add(f"lolbas/category/{slugify(command.category)}")
            if command.mitre_id:
                tags.add(f"attack/{command.mitre_id.lower()}")

        # Include any top-level LOLBAS tags if present.
        raw_tags = record.get("Tags") or record.get("tags") or []
        if isinstance(raw_tags, list):
            for tag in raw_tags:
                if isinstance(tag, str) and tag.strip():
                    tags.add(slugify(tag.strip()))

        return sorted(tags)

    def _strings(self, values: Any) -> list[str]:
        """
        Backwards-compatible generic string extractor.

        Kept for callers that still use it elsewhere. Prefer source-specific
        helpers above for Resources, Full_Path, Code_Sample, Detection, and
        Acknowledgement.
        """
        if isinstance(values, str):
            return [values.strip()] if values.strip() else []

        if not isinstance(values, list):
            return []

        result: list[str] = []
        preferred_keys = (
            "Path",
            "Link",
            "Url",
            "URL",
            "Name",
            "Person",
            "Handle",
            "Code",
            "Sigma",
            "Elastic",
            "Splunk",
            "IOC",
            "BlockRule",
        )

        for value in values:
            if isinstance(value, str) and value.strip():
                result.append(value.strip())
            elif isinstance(value, dict):
                for key in preferred_keys:
                    text = value.get(key)
                    if text:
                        result.append(str(text).strip())
                        break

        return sorted(set(filter(None, result)))

    def _first_url(self, values: list[str]) -> str:
        for value in values:
            if value.startswith(("http://", "https://")):
                return value
        return ""