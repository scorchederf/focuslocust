from __future__ import annotations

import posixpath
from pathlib import Path
import re
from typing import Any
from urllib.parse import unquote

from ..models import ExternalReference, RedTeamingTopic
from ..naming import slugify
from ..paths import resolve_repo_path


class RedTeamingTacticsSource:
    """
    Loader/parser for ired.team Red Teaming Tactics and Techniques Markdown.

    The source is treated as GitBook topic/reference Markdown, preserving each
    source Markdown page as one generated note.
    """

    FRONTMATTER_PATTERN = re.compile(r"\A---\s*\n.*?\n---\s*\n?", flags=re.DOTALL)
    GITBOOK_DIRECTIVE_PATTERN = re.compile(r"^\s*\{%\s*.*?%\}\s*$\n?", flags=re.MULTILINE)
    MARKDOWN_ANGLE_IMAGE_PATTERN = re.compile(r"!\[((?:\\.|[^\]])*)\]\(<([^>]+)>\)")
    MARKDOWN_PLAIN_IMAGE_PATTERN = re.compile(r"!\[((?:\\.|[^\]])*)\]\(([^)\n]+)\)")
    HTML_IMAGE_PATTERN = re.compile(
        r"<img\b(?=[^>]*\bsrc=[\"']([^\"']*\.gitbook/assets/[^\"']+)[\"'])[^>]*>",
        flags=re.IGNORECASE,
    )
    HTML_ALT_PATTERN = re.compile(r"\balt=[\"']([^\"']*)[\"']", flags=re.IGNORECASE)

    def __init__(self, config: dict[str, Any], logger):
        self.config = config
        self.logger = logger

    def load(self) -> list[dict[str, Any]]:
        local_path = self.config.get("local_path")
        if not local_path:
            raise ValueError(
                "RedTeaming Tactics source requires sources.redteamingtactics.local_path"
            )

        path = resolve_repo_path(local_path, "sources.redteamingtactics.local_path")
        files = self._markdown_files(path)
        self.logger.info(f"Loading RedTeaming Tactics Markdown files: {len(files)}")

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

    def parse(self, records: list[dict[str, Any]]) -> list[RedTeamingTopic]:
        topics: list[RedTeamingTopic] = []
        for record in records:
            topic = self._parse_topic(record)
            if topic:
                topics.append(topic)

        categories_with_index = {
            topic.category for topic in topics if topic.is_category_index
        }
        for topic in topics:
            topic.has_category_index = topic.category in categories_with_index

        direct_children = self._direct_children_by_directory(topics)
        for topic in topics:
            if topic.is_category_index:
                directory = posixpath.dirname(topic.relative_path)
                topic.child_topics = direct_children.get(directory, [])

        topics.sort(
            key=lambda item: (
                item.category.lower(),
                not item.is_category_index,
                item.relative_path.lower(),
            )
        )
        self.logger.info(f"Parsed RedTeaming Tactics topics: {len(topics)}")
        return topics

    def _direct_children_by_directory(self, topics: list[RedTeamingTopic]) -> dict[str, list[dict[str, str]]]:
        children: dict[str, list[dict[str, str]]] = {}
        for parent in topics:
            if not parent.is_category_index:
                continue

            parent_dir = posixpath.dirname(parent.relative_path)
            rows = []
            for topic in topics:
                if topic.relative_path == parent.relative_path:
                    continue
                if self._parent_directory(topic.relative_path) != parent_dir:
                    continue
                rows.append(
                    {
                        "name": topic.name,
                        "path": topic.path.removesuffix(".md"),
                    }
                )
            children[parent_dir] = sorted(rows, key=lambda row: row["name"].lower())
        return children

    def _parent_directory(self, relative_path: str) -> str:
        directory = posixpath.dirname(relative_path)
        if posixpath.basename(relative_path).lower() == "readme.md":
            return posixpath.dirname(directory)
        return directory

    def _markdown_files(self, path: Path) -> list[Path]:
        if path.is_file():
            return [path]

        if not path.is_dir():
            raise FileNotFoundError(f"RedTeaming Tactics local_path not found: {path}")

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
        if parts[0].lower() == ".gitbook":
            return True
        return any(part.startswith((".", "_")) for part in parts)

    def _parse_topic(self, record: dict[str, Any]) -> RedTeamingTopic | None:
        relative_path = str(record.get("_relative_path") or "").strip()
        raw_body = str(record.get("_body") or "").strip()
        body = self._remove_frontmatter(raw_body)
        if not relative_path or not body:
            return None

        path = Path(relative_path)
        category = path.parts[0] if path.parts else ""
        title = self._title(body, path)
        is_category_index = path.name.lower() == "readme.md"
        topic_id = f"rtt-{slugify(relative_path.removesuffix('.md'))}"
        page_slug = slugify(path.parts[-2]) if is_category_index and len(path.parts) > 1 else slugify(path.stem)
        output_dir = "/".join(slugify(part) for part in path.parts[:-1])
        output_path = f"kb/redteaming/{output_dir}/{page_slug}.md" if output_dir else f"kb/redteaming/{page_slug}.md"
        source_url = self._source_url(relative_path)

        body_content, asset_filenames = self._body_content(body, output_path)
        parsed_record = dict(record)
        parsed_record["_asset_filenames"] = asset_filenames

        return RedTeamingTopic(
            id=topic_id,
            source="redteamingtactics",
            type="redteaming-topic",
            name=title,
            description=self._description(body, title),
            path=output_path,
            url=source_url,
            aliases=sorted(set(filter(None, [title, topic_id]))),
            tags=self._tags(category),
            raw=parsed_record,
            external_references=[
                ExternalReference(source_name="redteamingtactics", url=source_url)
            ],
            category=category,
            relative_path=relative_path,
            headings=self._headings(body),
            body=body_content,
            is_category_index=is_category_index,
        )

    def _remove_frontmatter(self, body: str) -> str:
        return self.FRONTMATTER_PATTERN.sub("", body).strip()

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
        return re.sub(r"^#\s+.+?\s*(?:\n+|\Z)", "", body, count=1, flags=re.MULTILINE).strip()

    def _body_content(self, body: str, output_path: str) -> tuple[str, list[str]]:
        content = self._body_without_title(body)
        content = self._remove_summary_section(content)
        content = self._remove_gitbook_directives(content)
        return self._rewrite_asset_links(content, output_path)

    def _remove_summary_section(self, body: str) -> str:
        pattern = re.compile(
            r"(^##\s+Summary\s*$\n?)(.*?)(?=^##\s+|\Z)",
            flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
        )
        return pattern.sub("", body).strip()

    def _remove_gitbook_directives(self, body: str) -> str:
        return self.GITBOOK_DIRECTIVE_PATTERN.sub("", body).strip()

    def _rewrite_asset_links(self, body: str, output_path: str) -> tuple[str, list[str]]:
        asset_filenames: list[str] = []
        note_dir = posixpath.dirname(output_path)

        def replace_markdown_angle_image(match: re.Match[str]) -> str:
            alt_text = match.group(1)
            target = match.group(2).strip()
            rewritten, asset_filename = self._rewrite_asset_target(target, note_dir)
            if not rewritten:
                return match.group(0)
            if asset_filename:
                asset_filenames.append(asset_filename)
            return f"![{alt_text}](<{rewritten}>)"

        def replace_markdown_plain_image(match: re.Match[str]) -> str:
            alt_text = match.group(1)
            target = match.group(2).strip()
            rewritten, asset_filename = self._rewrite_asset_target(target, note_dir)
            if not rewritten:
                return match.group(0)
            if asset_filename:
                asset_filenames.append(asset_filename)
            return f"![{alt_text}](<{rewritten}>)"

        def replace_html_image(match: re.Match[str]) -> str:
            target = match.group(1).strip()
            alt_match = self.HTML_ALT_PATTERN.search(match.group(0))
            alt_text = alt_match.group(1).strip() if alt_match else ""
            rewritten, asset_filename = self._rewrite_asset_target(target, note_dir)
            if not rewritten:
                return match.group(0)
            if asset_filename:
                asset_filenames.append(asset_filename)
            return f"![{alt_text}](<{rewritten}>)"

        body = self.HTML_IMAGE_PATTERN.sub(replace_html_image, body)
        body = self.MARKDOWN_ANGLE_IMAGE_PATTERN.sub(replace_markdown_angle_image, body)
        body = self.MARKDOWN_PLAIN_IMAGE_PATTERN.sub(replace_markdown_plain_image, body)
        return body.strip(), sorted(set(asset_filenames))

    def _rewrite_asset_target(self, target: str, note_dir: str) -> tuple[str, str]:
        if re.match(r"^[a-z][a-z0-9+.-]*://", target, flags=re.IGNORECASE):
            return "", ""

        unquoted = unquote(target).replace("\\_", "_")
        marker = ".gitbook/assets/"
        if marker not in unquoted:
            return "", ""

        asset_filename = unquoted.split(marker, 1)[1].strip()
        if not asset_filename or "/" in asset_filename or "\\" in asset_filename:
            return "", ""

        asset_path = f"kb/redteaming/_assets/{asset_filename}"
        return posixpath.relpath(asset_path, note_dir), asset_filename

    def _description(self, body: str, title: str) -> str:
        for line in body.splitlines():
            text = line.strip()
            if (
                not text
                or text.startswith("#")
                or text.lower() == "## summary"
                or text.startswith("{%")
            ):
                continue
            text = re.sub(r"^>\s*", "", text)
            text = re.sub(r"[*_`]", "", text)
            if text:
                return text[:240]

        return f"RedTeaming Tactics topic for {title}."

    def _source_url(self, relative_path: str) -> str:
        encoded = "/".join(part.replace(" ", "%20") for part in relative_path.split("/"))
        return f"https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/{encoded}"

    def _tags(self, category: str) -> list[str]:
        return sorted(
            {
                "redteamingtactics",
                "redteamingtactics/topic",
                f"redteamingtactics/category/{slugify(category)}",
            }
        )
