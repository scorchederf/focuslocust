from pathlib import Path

import yaml

from src.kb_builder.paths import ProjectPaths
from src.kb_builder.render.markdown import MarkdownRenderer
from src.kb_builder.sources.payloadsallthethings import PayloadsAllTheThingsSource


class DummyLogger:
    def info(self, *args, **kwargs):
        pass

    def warning(self, *args, **kwargs):
        pass

    def debug(self, *args, **kwargs):
        pass


def test_payloads_source_parses_topic_markdown(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "payloads"
    topic_dir = data_dir / "Command Injection"
    topic_dir.mkdir(parents=True)
    (topic_dir / "README.md").write_text(
        """# Command Injection

> Execute arbitrary commands through an unsafe application parameter.

## Summary

- [Tools](#tools)

## Tools

- commix
""",
        encoding="utf-8",
    )

    source = PayloadsAllTheThingsSource(config={"local_path": "payloads"}, logger=DummyLogger())
    topics = source.parse(source.load())

    assert len(topics) == 1
    assert topics[0].id == "patt-command-injection-readme"
    assert topics[0].name == "Command Injection"
    assert topics[0].category == "Command Injection"
    assert topics[0].path == "kb/payloads/command-injection/command-injection.md"
    assert topics[0].headings == ["Summary", "Tools"]
    assert "## Summary" not in topics[0].body
    assert "[Tools](#tools)" not in topics[0].body
    assert "## Tools" in topics[0].body
    assert topics[0].is_category_index is True
    assert topics[0].has_category_index is True


def test_payloads_source_skips_internalallthethings_moved_reference(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "payloads"
    topic_dir = data_dir / "Methodology and Resources"
    topic_dir.mkdir(parents=True)
    (topic_dir / "Reverse Shell Cheatsheet.md").write_text(
        """# Reverse Shell Cheatsheet

:warning: Content of this page has been moved to [InternalAllTheThings/cheatsheet/shell-reverse](https://example.test/moved/)
""",
        encoding="utf-8",
    )

    source = PayloadsAllTheThingsSource(config={"local_path": "payloads"}, logger=DummyLogger())
    topics = source.parse(source.load())

    assert topics == []


def test_render_payloads_writes_topic_and_index(tmp_path, monkeypatch):
    repo_root = Path.cwd()
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "payloads"
    topic_dir = data_dir / "File Inclusion"
    topic_dir.mkdir(parents=True)
    (topic_dir / "Wrappers.md").write_text(
        """# Inclusion Using Wrappers

## Summary

- [Wrapper php://filter](#wrapper-phpfilter)

## Wrapper php://filter

```powershell
php://filter/convert.base64-encode/resource=index.php
```
""",
        encoding="utf-8",
    )

    source = PayloadsAllTheThingsSource(config={"local_path": "payloads"}, logger=DummyLogger())
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

    written, skipped = renderer.render_payloadsallthethings(topics)

    assert written == 2
    assert skipped == 0

    topic_note = (tmp_path / "vault/kb/payloads/file-inclusion/wrappers.md").read_text(encoding="utf-8")
    assert "parsed_by: focuslocust" in topic_note
    assert "source: payloadsallthethings" in topic_note
    assert "# Inclusion Using Wrappers" in topic_note
    assert "php://filter/convert.base64-encode/resource=index.php" in topic_note
    assert "## Summary" not in topic_note
    frontmatter = yaml.safe_load(topic_note.split("---", 2)[1])
    assert frontmatter["category"] == "File Inclusion"

    index = (tmp_path / "vault/kb/indexes/payloadsallthethings.md").read_text(encoding="utf-8")
    assert "[[kb/payloads/file-inclusion/wrappers|Inclusion Using Wrappers]]" in index


def test_payloads_index_indents_subsections_under_category_page(tmp_path, monkeypatch):
    repo_root = Path.cwd()
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "payloads"
    topic_dir = data_dir / "Account Takeover"
    topic_dir.mkdir(parents=True)
    (topic_dir / "README.md").write_text(
        """# Account Takeover

## Summary

- [MFA Bypasses](#mfa-bypasses)

## Methodology
""",
        encoding="utf-8",
    )
    (topic_dir / "mfa-bypass.md").write_text(
        """# MFA Bypasses

## Push Fatigue
""",
        encoding="utf-8",
    )

    source = PayloadsAllTheThingsSource(config={"local_path": "payloads"}, logger=DummyLogger())
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

    renderer.render_payloadsallthethings(topics)

    index = (tmp_path / "vault/kb/indexes/payloadsallthethings.md").read_text(encoding="utf-8")
    assert "## Account Takeover" in index
    assert "- [[kb/payloads/account-takeover/account-takeover|Account Takeover]]" in index
    assert "  - [[kb/payloads/account-takeover/mfa-bypass|MFA Bypasses]]" in index
    assert index.index("account-takeover|Account Takeover") < index.index("mfa-bypass|MFA Bypasses")
