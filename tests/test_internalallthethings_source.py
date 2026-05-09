from pathlib import Path

import yaml

from src.kb_builder.paths import ProjectPaths
from src.kb_builder.render.markdown import MarkdownRenderer
from src.kb_builder.sources.internalallthethings import InternalAllTheThingsSource


class DummyLogger:
    def info(self, *args, **kwargs):
        pass

    def warning(self, *args, **kwargs):
        pass

    def debug(self, *args, **kwargs):
        pass


def test_internal_source_parses_topic_markdown(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "internal"
    topic_dir = data_dir / "redteam" / "access"
    topic_dir.mkdir(parents=True)
    (topic_dir / "initial-access.md").write_text(
        """# Initial Access

> Files used to establish an initial foothold.

## Summary

- [Payload](#payload)

## Payload

- LNK
""",
        encoding="utf-8",
    )

    source = InternalAllTheThingsSource(config={"local_path": "internal"}, logger=DummyLogger())
    topics = source.parse(source.load())

    assert len(topics) == 1
    assert topics[0].id == "iatt-redteam-access-initial-access"
    assert topics[0].name == "Initial Access"
    assert topics[0].category == "redteam"
    assert topics[0].path == "kb/internal/redteam/access/initial-access.md"
    assert "## Summary" not in topics[0].body
    assert "[Payload](#payload)" not in topics[0].body
    assert "## Payload" in topics[0].body


def test_render_internal_writes_topic_and_index(tmp_path, monkeypatch):
    repo_root = Path.cwd()
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "internal"
    topic_dir = data_dir / "devops"
    topic_dir.mkdir(parents=True)
    (topic_dir / "README.md").write_text(
        """# DevOps

## Summary

- [Package Managers](#package-managers)

## Overview
""",
        encoding="utf-8",
    )
    (topic_dir / "package-managers.md").write_text(
        """# Package Managers

## npm

Token and package notes.
""",
        encoding="utf-8",
    )

    source = InternalAllTheThingsSource(config={"local_path": "internal"}, logger=DummyLogger())
    topics = source.parse(source.load())
    monkeypatch.chdir(repo_root)
    renderer = MarkdownRenderer(
        config={"rendering": {"parsed_marker": "focuslocust"}},
        paths=ProjectPaths(
            vault_path=tmp_path / "vault",
            cache_path=tmp_path / ".cache",
            log_path=tmp_path / ".logs",
        ),
        logger=DummyLogger(),
    )

    written, skipped = renderer.render_internalallthethings(topics)

    assert written == 3
    assert skipped == 0

    topic_note = (tmp_path / "vault/kb/internal/devops/package-managers.md").read_text(encoding="utf-8")
    assert "parsed_by: focuslocust" in topic_note
    assert "source: internalallthethings" in topic_note
    assert "# Package Managers" in topic_note
    assert "Token and package notes." in topic_note
    frontmatter = yaml.safe_load(topic_note.split("---", 2)[1])
    assert frontmatter["category"] == "devops"

    index = (tmp_path / "vault/kb/indexes/internalallthethings.md").read_text(encoding="utf-8")
    assert "## Devops" in index
    assert "- [[kb/internal/devops/devops|DevOps]]" in index
    assert "  - [[kb/internal/devops/package-managers|Package Managers]]" in index
