from pathlib import Path

import yaml

from src.kb_builder.paths import ProjectPaths
from src.kb_builder.render.markdown import MarkdownRenderer
from src.kb_builder.sources.redteamingtactics import RedTeamingTacticsSource


class DummyLogger:
    def info(self, *args, **kwargs):
        pass

    def warning(self, *args, **kwargs):
        pass

    def debug(self, *args, **kwargs):
        pass


def test_redteaming_source_parses_topic_markdown(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "redteaming"
    topic_dir = data_dir / "offensive-security" / "defense-evasion"
    topic_dir.mkdir(parents=True)
    (topic_dir / "t1027-obfuscated-powershell-invocations.md").write_text(
        """---
description: Obfuscated PowerShell notes.
---

# Obfuscated PowerShell Invocations

## Summary

- [Examples](#examples)

{% hint style="warning" %}
Lab only.
{% endhint %}

## Examples

{% code title="attacker@victim" %}
```powershell
whoami
```
{% endcode %}

![](<../../.gitbook/assets/Screenshot Example.png>)

![Head of SEH fs:\\[0\\]](<../../.gitbook/assets/escaped-alt.png>)

![](<../../.gitbook/assets/image (532).png>)

<img src="../../.gitbook/assets/html-image.png" alt="HTML image" data-size="original">

Use encoded commands.
""",
        encoding="utf-8",
    )

    source = RedTeamingTacticsSource(config={"local_path": "redteaming"}, logger=DummyLogger())
    topics = source.parse(source.load())

    assert len(topics) == 1
    assert topics[0].id == "rtt-offensive-security-defense-evasion-t1027-obfuscated-powershell-invocations"
    assert topics[0].name == "Obfuscated PowerShell Invocations"
    assert topics[0].category == "offensive-security"
    assert topics[0].path == "kb/redteaming/offensive-security/defense-evasion/t1027-obfuscated-powershell-invocations.md"
    assert "description:" not in topics[0].body
    assert "## Summary" not in topics[0].body
    assert "[Examples](#examples)" not in topics[0].body
    assert "{% hint" not in topics[0].body
    assert "{% endhint" not in topics[0].body
    assert "{% code" not in topics[0].body
    assert "{% endcode" not in topics[0].body
    assert "```powershell" in topics[0].body
    assert "![ ]" not in topics[0].body
    assert "](<../../_assets/Screenshot Example.png>)" in topics[0].body
    assert "![Head of SEH fs:\\[0\\]](<../../_assets/escaped-alt.png>)" in topics[0].body
    assert "![](<../../_assets/image (532).png>)" in topics[0].body
    assert "![HTML image](<../../_assets/html-image.png>)" in topics[0].body
    assert topics[0].raw["_asset_filenames"] == [
        "Screenshot Example.png",
        "escaped-alt.png",
        "html-image.png",
        "image (532).png",
    ]
    assert "## Examples" in topics[0].body


def test_render_redteaming_writes_topic_and_index(tmp_path, monkeypatch):
    repo_root = Path.cwd()
    monkeypatch.chdir(tmp_path)
    data_dir = tmp_path / "redteaming"
    topic_dir = data_dir / "offensive-security" / "lateral-movement"
    topic_dir.mkdir(parents=True)
    asset_dir = data_dir / ".gitbook" / "assets"
    asset_dir.mkdir(parents=True)
    (data_dir / ".gitbook" / "README.md").write_text("# Skip asset docs\n", encoding="utf-8")
    (asset_dir / "lateral move.png").write_bytes(b"image-bytes")
    (topic_dir / "README.md").write_text(
        """# Lateral Movement

## Summary

- [Overview](#overview)
""",
        encoding="utf-8",
    )
    (topic_dir / "wmi-via-newscheduledtask.md").write_text(
        """# WMI via NewScheduledTask

![](../../.gitbook/assets/lateral%20move.png)

## Execution

Create a scheduled task through WMI.
""",
        encoding="utf-8",
    )
    subtopic_dir = topic_dir / "remote-desktop"
    subtopic_dir.mkdir()
    (subtopic_dir / "README.md").write_text(
        """# Remote Desktop

## RDP
""",
        encoding="utf-8",
    )

    source = RedTeamingTacticsSource(config={"local_path": "redteaming"}, logger=DummyLogger())
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

    written, skipped = renderer.render_redteamingtactics(topics)

    assert written == 4
    assert skipped == 0

    topic_note = (
        tmp_path / "vault/kb/redteaming/offensive-security/lateral-movement/wmi-via-newscheduledtask.md"
    ).read_text(encoding="utf-8")
    assert "parsed_by: focuslocust" in topic_note
    assert "source: redteamingtactics" in topic_note
    assert "# WMI via NewScheduledTask" in topic_note
    assert "](<../../_assets/lateral move.png>)" in topic_note
    assert "Create a scheduled task through WMI." in topic_note
    frontmatter = yaml.safe_load(topic_note.split("---", 2)[1])
    assert frontmatter["category"] == "offensive-security"
    assert (tmp_path / "vault/kb/redteaming/_assets/lateral move.png").read_bytes() == b"image-bytes"

    index_note = (
        tmp_path / "vault/kb/redteaming/offensive-security/lateral-movement/lateral-movement.md"
    ).read_text(encoding="utf-8")
    assert "\n## Content\n" not in index_note
    assert index_note.count("# Lateral Movement") == 1
    assert "## Subpages" in index_note
    assert "- [[kb/redteaming/offensive-security/lateral-movement/wmi-via-newscheduledtask|WMI via NewScheduledTask]]" in index_note
    assert "- [[kb/redteaming/offensive-security/lateral-movement/remote-desktop/remote-desktop|Remote Desktop]]" in index_note

    index = (tmp_path / "vault/kb/indexes/redteamingtactics.md").read_text(encoding="utf-8")
    assert "## Offensive Security" in index
    assert "- [[kb/redteaming/offensive-security/lateral-movement/lateral-movement|Lateral Movement]]" in index
    assert "  - [[kb/redteaming/offensive-security/lateral-movement/wmi-via-newscheduledtask|WMI via NewScheduledTask]]" in index
