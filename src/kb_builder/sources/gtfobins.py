from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from ..models import ExternalReference, GtfobinsFunction, GtfobinsTool
from ..naming import slugify
from ..paths import resolve_repo_path


class GtfobinsSource:
    """
    Loader/parser for GTFOBins Markdown files.

    GTFOBins entries are Markdown documents with YAML front matter. The parser
    preserves that front matter in `tool.raw` and keeps the Markdown body for
    source-specific rendering.
    """

    def __init__(self, config: dict[str, Any], logger):
        self.config = config
        self.logger = logger

    def load(self) -> list[dict[str, Any]]:
        local_path = self.config.get("local_path")
        if not local_path:
            raise ValueError("GTFOBins source requires sources.gtfobins.local_path")

        path = resolve_repo_path(local_path, "sources.gtfobins.local_path")
        files = self._markdown_files(path)
        self.logger.info(f"Loading GTFOBins Markdown files: {len(files)}")

        records: list[dict[str, Any]] = []
        for file_path in files:
            frontmatter, body = self._read_frontmatter(file_path)
            frontmatter.setdefault("_source_path", str(file_path))
            frontmatter.setdefault("_body", body)
            frontmatter.setdefault("_name", file_path.stem)
            records.append(frontmatter)

        return records

    def parse(self, records: list[dict[str, Any]]) -> list[GtfobinsTool]:
        tools: list[GtfobinsTool] = []
        for record in records:
            tool = self._parse_tool(record)
            if tool:
                tools.append(tool)

        tools.sort(key=lambda item: item.id)
        self.logger.info(f"Parsed GTFOBins tools: {len(tools)}")
        return tools

    def _markdown_files(self, path: Path) -> list[Path]:
        if path.is_file():
            return [path]

        if not path.is_dir():
            raise FileNotFoundError(f"GTFOBins local_path not found: {path}")

        files = [
            item
            for item in path.rglob("*")
            if item.is_file() and item.suffix.lower() in {"", ".md"}
        ]
        return sorted(files)

    def _read_frontmatter(self, path: Path) -> tuple[dict[str, Any], str]:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            return {}, text.strip()

        parts = text.split("---", 2)
        if len(parts) < 2:
            return {}, text.strip()

        data = yaml.safe_load(parts[1]) or {}
        if not isinstance(data, dict):
            data = {}

        body = parts[2].strip() if len(parts) > 2 else ""
        return data, body

    def _parse_tool(self, record: dict[str, Any]) -> GtfobinsTool | None:
        name = str(record.get("name") or record.get("Name") or record.get("_name") or "").strip()
        if not name:
            self.logger.warning(
                f"Skipping GTFOBins record without name: {record.get('_source_path', '')}"
            )
            return None

        tool_id = slugify(name)
        function_examples = self._function_examples(record.get("functions") or {})
        functions = sorted({example.function for example in function_examples if example.function})
        url = f"https://gtfobins.github.io/gtfobins/{tool_id}/"

        return GtfobinsTool(
            id=tool_id,
            source="gtfobins",
            type="tool",
            name=name,
            description=self._description(record, functions),
            url=url,
            aliases=sorted(set(filter(None, [name, tool_id]))),
            tags=self._tool_tags(functions),
            raw=record,
            external_references=[ExternalReference(source_name="gtfobins", url=url)],
            functions=functions,
            function_examples=function_examples,
            path=f"kb/gtfobins/tools/{tool_id}.md",
        )

    def _function_examples(self, functions: Any) -> list[GtfobinsFunction]:
        examples: list[GtfobinsFunction] = []
        if not isinstance(functions, dict):
            return examples

        for function_name, values in sorted(functions.items()):
            function_text = str(function_name).strip()
            if isinstance(values, dict):
                values = [values]
            if not isinstance(values, list):
                continue

            for value in values:
                if isinstance(value, str):
                    examples.append(GtfobinsFunction(function=function_text, code=value.strip()))
                elif isinstance(value, dict):
                    examples.append(
                        GtfobinsFunction(
                            function=function_text,
                            code=str(value.get("code") or "").strip(),
                            description=str(value.get("description") or value.get("comment") or "").strip(),
                        )
                    )

        return examples

    def _description(self, record: dict[str, Any], functions: list[str]) -> str:
        description = str(record.get("description") or record.get("Description") or "").strip()
        if description:
            return description

        name = str(record.get("_name") or "").strip()
        if functions:
            return f"GTFOBins entry for {name} covering {', '.join(functions)}."

        return f"GTFOBins entry for {name}."

    def _tool_tags(self, functions: list[str]) -> list[str]:
        tags = {"gtfobins/tool", "platform/linux"}
        for function in functions:
            tags.add(f"gtfobins/function/{slugify(function)}")
        return sorted(tags)
