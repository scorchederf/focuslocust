from __future__ import annotations

from pathlib import Path
import re
from typing import Any

from ..models import ExternalReference, PayloadTopic
from ..naming import slugify
from ..paths import resolve_repo_path


class PayloadsAllTheThingsSource:
    """
    Loader/parser for PayloadsAllTheThings Markdown topics.

    PayloadsAllTheThings is treated as topic/reference Markdown, not as a tool
    dataset and not as one payload per note.
    """

    INTERNAL_MOVE_MARKER = ":warning: Content of this page has been moved to [InternalAllTheThings"

    def __init__(self, config: dict[str, Any], logger):
        self.config = config
        self.logger = logger

    def load(self) -> list[dict[str, Any]]:
        local_path = self.config.get("local_path")
        if not local_path:
            raise ValueError(
                "PayloadsAllTheThings source requires sources.payloadsallthethings.local_path"
            )

        path = resolve_repo_path(local_path, "sources.payloadsallthethings.local_path")
        files = self._markdown_files(path)
        self.logger.info(f"Loading PayloadsAllTheThings Markdown files: {len(files)}")

        records: list[dict[str, Any]] = []
        for file_path in files:
            relative_path = file_path.relative_to(path)
            text = file_path.read_text(encoding="utf-8")
            records.append(
                {
                    "_source_path": str(file_path),
                    "_relative_path": relative_path.as_posix(),
                    "_body": text.strip(),
                }
            )

        return records

    def parse(self, records: list[dict[str, Any]]) -> list[PayloadTopic]:
        topics: list[PayloadTopic] = []
        for record in records:
            topic = self._parse_topic(record)
            if topic:
                topics.append(topic)

        categories_with_index = {
            topic.category for topic in topics if topic.is_category_index
        }
        for topic in topics:
            topic.has_category_index = topic.category in categories_with_index

        topics.sort(
            key=lambda item: (
                item.category.lower(),
                not item.is_category_index,
                item.relative_path.lower(),
            )
        )
        self.logger.info(f"Parsed PayloadsAllTheThings topics: {len(topics)}")
        return topics

    def _markdown_files(self, path: Path) -> list[Path]:
        if path.is_file():
            return [path]

        if not path.is_dir():
            raise FileNotFoundError(f"PayloadsAllTheThings local_path not found: {path}")

        files = []
        for item in path.rglob("*.md"):
            if not item.is_file():
                continue
            relative_parts = item.relative_to(path).parts
            if self._skip_path(relative_parts):
                continue
            files.append(item)

        return sorted(files)

    def _skip_path(self, parts: tuple[str, ...]) -> bool:
        if not parts:
            return True
        if len(parts) == 1:
            return True
        return any(part.startswith((".", "_")) for part in parts)

    def _parse_topic(self, record: dict[str, Any]) -> PayloadTopic | None:
        relative_path = str(record.get("_relative_path") or "").strip()
        body = str(record.get("_body") or "").strip()
        if not relative_path or not body:
            return None
        if self.INTERNAL_MOVE_MARKER in body:
            return None

        path = Path(relative_path)
        category = path.parts[0] if path.parts else ""
        title = self._title(body, path)
        is_category_index = path.name.lower() == "readme.md"
        topic_id = f"patt-{slugify(relative_path.removesuffix('.md'))}"
        page_slug = slugify(category) if is_category_index else slugify(path.stem)
        output_dir = "/".join(slugify(part) for part in path.parts[:-1])
        output_path = f"kb/payloads/{output_dir}/{page_slug}.md" if output_dir else f"kb/payloads/{page_slug}.md"
        source_url = self._source_url(relative_path)
        moved_to = self._moved_to(body)

        return PayloadTopic(
            id=topic_id,
            source="payloadsallthethings",
            type="payload-topic",
            name=title,
            description=self._description(body, title, moved_to),
            path=output_path,
            url=source_url,
            aliases=sorted(set(filter(None, [title, topic_id]))),
            tags=self._tags(category, moved_to),
            raw=record,
            external_references=[
                ExternalReference(source_name="payloadsallthethings", url=source_url)
            ],
            category=category,
            relative_path=relative_path,
            headings=self._headings(body),
            body=self._body_content(body),
            moved_to=moved_to,
            is_category_index=is_category_index,
        )

    def _title(self, body: str, path: Path) -> str:
        match = re.search(r"^#\s+(.+?)\s*$", body, flags=re.MULTILINE)
        if match:
            return match.group(1).strip()
        if path.name.lower() == "readme.md" and path.parts:
            return path.parts[-2]
        return path.stem

    def _headings(self, body: str) -> list[str]:
        headings = []
        for match in re.finditer(r"^#{2,6}\s+(.+?)\s*$", body, flags=re.MULTILINE):
            heading = match.group(1).strip()
            if heading:
                headings.append(heading)
        return headings

    def _body_without_title(self, body: str) -> str:
        return re.sub(r"^#\s+.+?\s*\n+", "", body, count=1, flags=re.MULTILINE).strip()

    def _body_content(self, body: str) -> str:
        content = self._body_without_title(body)
        return self._remove_summary_section(content)

    def _remove_summary_section(self, body: str) -> str:
        pattern = re.compile(
            r"(^##\s+Summary\s*$\n?)(.*?)(?=^##\s+|\Z)",
            flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
        )
        return pattern.sub("", body).strip()

    def _description(self, body: str, title: str, moved_to: str) -> str:
        if moved_to:
            return f"PayloadsAllTheThings moved reference for {title}."

        for line in body.splitlines():
            text = line.strip()
            if not text or text.startswith("#") or text.lower() == "## summary":
                continue
            text = re.sub(r"^>\s*", "", text)
            text = re.sub(r"[*_`]", "", text)
            if text:
                return text[:240]

        return f"PayloadsAllTheThings topic for {title}."

    def _moved_to(self, body: str) -> str:
        match = re.search(r"Content of this page has been moved to \[[^\]]+\]\(([^)]+)\)", body)
        return match.group(1).strip() if match else ""

    def _source_url(self, relative_path: str) -> str:
        encoded = "/".join(part.replace(" ", "%20") for part in relative_path.split("/"))
        return f"https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/{encoded}"

    def _tags(self, category: str, moved_to: str) -> list[str]:
        tags = {
            "payloadsallthethings",
            "payloadsallthethings/topic",
            f"payloadsallthethings/category/{slugify(category)}",
        }
        if moved_to:
            tags.add("payloadsallthethings/moved")
        return sorted(tags)
