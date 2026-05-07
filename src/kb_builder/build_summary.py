from __future__ import annotations

from collections import defaultdict
import json
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from .naming import slugify
from .paths import ProjectPaths
from .safe_write import safe_write_text


class FieldSummary:
    def __init__(self) -> None:
        self.count = 0
        self.types: set[str] = set()
        self.samples: list[str] = []

    def add(self, value: Any) -> None:
        self.count += 1
        self.types.add(type(value).__name__)
        sample = sample_value(value)
        if sample and sample not in self.samples and len(self.samples) < 3:
            self.samples.append(sample)


class ObjectField:
    def __init__(self, name: str, field: FieldSummary, values: list[str]) -> None:
        self.name = name
        self.types = ", ".join(sorted(field.types))
        self.count = field.count
        self.jinja = jinja_expression(name)
        self.values = values


def render_datasource_field_summary(
    sources: dict[str, list[dict[str, Any]]],
    marker: str,
    paths: ProjectPaths,
    logger=None,
) -> bool:
    lines = [
        "---",
        f"parsed_by: {marker}",
        "source: build",
        "type: datasource-field-summary",
        "---",
        "",
        "# Datasource Field Summary",
        "",
        "This file is generated during each build from raw datasource records.",
        "",
    ]

    for source_name, records in sorted(sources.items()):
        summary = summarize_records(records)
        lines.extend(
            [
                f"## {source_name}",
                "",
                f"Records inspected: {len(records)}",
                "",
                "| Field | Types | Count | Sample data |",
                "| --- | --- | ---: | --- |",
            ]
        )

        for field_name in sorted(summary):
            field = summary[field_name]
            samples = "<br>".join(escape_table_cell(sample) for sample in field.samples)
            lines.append(
                f"| `{escape_table_cell(field_name)}` | {escape_table_cell(', '.join(sorted(field.types)))} | {field.count} | {samples} |"
            )
        lines.append("")

    content = "\n".join(lines).rstrip() + "\n"
    return safe_write_text(
        paths.vault_path / "kb" / "_build" / "datasource-fields.md",
        content,
        marker=marker,
        logger=logger,
    )


def render_object_property_pages(
    objects_by_group: dict[str, list[Any]],
    marker: str,
    paths: ProjectPaths,
    logger=None,
) -> tuple[int, int]:
    env = Environment(
        loader=FileSystemLoader("templates"),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("build/object-properties.md.j2")

    written = 0
    skipped = 0

    for group_name, objects in sorted(objects_by_group.items()):
        obj = object_with_most_fields(objects)
        if not obj:
            continue

        raw = getattr(obj, "raw", {}) or {}
        fields = object_fields(raw)
        content = template.render(
            parsed_marker=marker,
            group_name=group_name,
            obj=obj,
            fields=fields,
        )
        target = (
            paths.vault_path
            / "kb"
            / "_build"
            / "objects"
            / group_name
            / f"example-{obj.id}-{slugify(obj.name)}.md"
        )
        if safe_write_text(target, content.rstrip() + "\n", marker=marker, logger=logger):
            written += 1
        else:
            skipped += 1

    return written, skipped


def object_with_most_fields(objects: list[Any]) -> Any | None:
    if not objects:
        return None

    return max(
        objects,
        key=lambda obj: len(object_fields(getattr(obj, "raw", {}) or {})),
    )


def object_fields(raw: dict[str, Any]) -> list[ObjectField]:
    summary = summarize_records([raw])
    fields = []
    for field_name in sorted(summary):
        values = [
            sample_value(value)
            for value in extract_field_values(raw, field_name)
            if value is not None and value != ""
        ]
        deduped_values = []
        for value in values:
            if value not in deduped_values and len(deduped_values) < 8:
                deduped_values.append(value)
        fields.append(ObjectField(field_name, summary[field_name], deduped_values))
    return fields


def summarize_records(records: list[dict[str, Any]]) -> dict[str, FieldSummary]:
    summary: dict[str, FieldSummary] = defaultdict(FieldSummary)
    for record in records:
        walk_fields(record, "", summary)
    return dict(summary)


def walk_fields(value: Any, prefix: str, summary: dict[str, FieldSummary]) -> None:
    if prefix:
        summary[prefix].add(value)

    if isinstance(value, dict):
        for key, child in value.items():
            if str(key).startswith("_"):
                continue
            child_path = f"{prefix}.{key}" if prefix else str(key)
            walk_fields(child, child_path, summary)
        return

    if isinstance(value, list):
        item_prefix = f"{prefix}[]" if prefix else "[]"
        for item in value:
            walk_fields(item, item_prefix, summary)


def extract_field_values(value: Any, path: str) -> list[Any]:
    current = [value]
    for part in path.split("."):
        next_values = []
        is_list_part = part.endswith("[]")
        key = part[:-2] if is_list_part else part

        for item in current:
            child = None
            if isinstance(item, dict):
                child = item.get(key)
            elif hasattr(item, key):
                child = getattr(item, key)

            if child is None:
                continue

            if is_list_part and isinstance(child, list):
                next_values.extend(child)
            else:
                next_values.append(child)

        current = next_values
    return current


def jinja_expression(path: str) -> str:
    if "[]" in path:
        return '{% for value in obj.raw | field_values("' + path + '") %}{{ value }}{% endfor %}'
    return '{{ obj.raw | field_value("' + path + '") }}'


def sample_value(value: Any) -> str:
    if value is None:
        return "null"

    if isinstance(value, str):
        return truncate(value.replace("\n", " "))

    if isinstance(value, (int, float, bool)):
        return str(value)

    if isinstance(value, list):
        return f"list[{len(value)}]"

    if isinstance(value, dict):
        keys = ", ".join(str(key) for key in list(value.keys())[:5])
        suffix = ", ..." if len(value) > 5 else ""
        return f"dict({keys}{suffix})"

    return truncate(json.dumps(value, default=str, sort_keys=True))


def truncate(value: str, limit: int = 140) -> str:
    if len(value) <= limit:
        return value
    return value[: limit - 3].rstrip() + "..."


def escape_table_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")
