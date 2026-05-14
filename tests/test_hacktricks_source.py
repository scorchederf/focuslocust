from pathlib import Path

import yaml

from src.kb_builder.paths import ProjectPaths
from src.kb_builder.render.markdown import MarkdownRenderer
from src.kb_builder.sources.hacktricks import HackTricksSource


class DummyLogger:
    def info(self, *args, **kwargs):
        pass

    def warning(self, *args, **kwargs):
        pass

    def debug(self, *args, **kwargs):
        pass


def test_hacktricks_source_parses_topic_markdown(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "hacktricks"
    topic_dir = data_dir / "pentesting-web" / "sql-injection"
    topic_dir.mkdir(parents=True)
    (topic_dir / "README.md").write_text(
        """# SQL Injection

{{#include ../../banners/hacktricks-training.md}}

## Summary

- [Entry point detection](#entry-point-detection)

## Entry point detection

Use quotes.
""",
        encoding="utf-8",
    )

    source = HackTricksSource(config={"local_path": "hacktricks"}, logger=DummyLogger())
    topics = source.parse(source.load())

    assert len(topics) == 1
    assert topics[0].id == "hacktricks-pentesting-web-sql-injection-readme"
    assert topics[0].name == "SQL Injection"
    assert topics[0].category == "pentesting-web"
    assert topics[0].path == "kb/hacktricks/pentesting-web/sql-injection/sql-injection.md"
    assert "hacktricks-training.md" not in topics[0].body
    assert "{{#include" not in topics[0].body
    assert "## Summary" not in topics[0].body
    assert "[Entry point detection](#entry-point-detection)" not in topics[0].body
    assert "## Entry point detection" in topics[0].body


def test_render_hacktricks_writes_topic_and_index(tmp_path, monkeypatch):
    repo_root = Path.cwd()
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "hacktricks"
    topic_dir = data_dir / "generic-methodologies-and-resources"
    topic_dir.mkdir(parents=True)
    (topic_dir / "README.md").write_text(
        """# Generic Methodologies

## Summary

- [Pentesting Methodology](#pentesting-methodology)

## Overview
""",
        encoding="utf-8",
    )
    (topic_dir / "pentesting-methodology.md").write_text(
        """# Pentesting Methodology

## Scope

Define target scope.
""",
        encoding="utf-8",
    )

    source = HackTricksSource(config={"local_path": "hacktricks"}, logger=DummyLogger())
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

    written, skipped = renderer.render_hacktricks(topics)

    assert written == 3
    assert skipped == 0

    topic_note = (
        tmp_path / "vault/kb/hacktricks/generic-methodologies-and-resources/pentesting-methodology.md"
    ).read_text(encoding="utf-8")
    assert "parsed_by: focuslocust" in topic_note
    assert "source: hacktricks" in topic_note
    assert "# Pentesting Methodology" in topic_note
    assert "Define target scope." in topic_note
    frontmatter = yaml.safe_load(topic_note.split("---", 2)[1])
    assert frontmatter["category"] == "generic-methodologies-and-resources"

    index = (tmp_path / "vault/kb/indexes/hacktricks.md").read_text(encoding="utf-8")
    assert "## Generic Methodologies And Resources" in index
    assert "- [[kb/hacktricks/generic-methodologies-and-resources/generic-methodologies-and-resources|Generic Methodologies]]" in index
    assert "  - [[kb/hacktricks/generic-methodologies-and-resources/pentesting-methodology|Pentesting Methodology]]" in index


def test_hacktricks_source_skips_banner_pages(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "hacktricks"
    banner_dir = data_dir / "banners"
    banner_dir.mkdir(parents=True)
    (banner_dir / "hacktricks-training.md").write_text(
        """# HackTricks Training

Banner content.
""",
        encoding="utf-8",
    )
    topic_dir = data_dir / "pentesting-web"
    topic_dir.mkdir()
    (topic_dir / "README.md").write_text(
        """# Web

{{#include ../banners/hacktricks-training.md}}

## Content
""",
        encoding="utf-8",
    )

    source = HackTricksSource(config={"local_path": "hacktricks"}, logger=DummyLogger())
    topics = source.parse(source.load())

    assert len(topics) == 1
    assert topics[0].category == "pentesting-web"
    assert "hacktricks-training.md" not in topics[0].body
