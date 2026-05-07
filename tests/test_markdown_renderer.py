from pathlib import Path

from src.kb_builder.sources.mitre import MitreSource
from src.kb_builder.paths import ProjectPaths
from src.kb_builder.render.markdown import MarkdownRenderer


class DummyLogger:
    def info(self, *args, **kwargs):
        pass

    def debug(self, *args, **kwargs):
        pass

    def warning(self, *args, **kwargs):
        pass


def test_table_cell_escapes_wikilink_pipe(tmp_path):
    renderer = MarkdownRenderer(
        config={"rendering": {"generated_marker": "focuslocust"}},
        paths=ProjectPaths(
            vault_path=tmp_path / "vault",
            cache_path=tmp_path / ".cache",
            log_path=tmp_path / ".logs",
        ),
        logger=DummyLogger(),
    )

    value = "[[kb/mitre/attack/techniques/T1649-steal-or-forge-authentication-certificates|T1649 - Steal or Forge Authentication Certificates]]"

    assert renderer._table_cell(value) == (
        "[[kb/mitre/attack/techniques/T1649-steal-or-forge-authentication-certificates\\|"
        "T1649 - Steal or Forge Authentication Certificates]]"
    )


def test_table_cell_replaces_newlines():
    renderer = MarkdownRenderer(
        config={"rendering": {"generated_marker": "focuslocust"}},
        paths=ProjectPaths(
            vault_path=Path("vault"),
            cache_path=Path(".cache"),
            log_path=Path(".logs"),
        ),
        logger=DummyLogger(),
    )

    assert renderer._table_cell("first\nsecond") == "first<br>second"


def test_render_mitre_smoke_with_indexes_references_and_relationships(tmp_path):
    data = {
        "objects": [
            {
                "type": "x-mitre-tactic",
                "id": "x-mitre-tactic--credential-access",
                "name": "Credential Access",
                "description": "Steal credentials.",
                "external_references": [
                    {
                        "source_name": "mitre-attack",
                        "external_id": "TA0006",
                        "url": "https://attack.mitre.org/tactics/TA0006/",
                    }
                ],
            },
            {
                "type": "attack-pattern",
                "id": "attack-pattern--parent",
                "name": "OS Credential Dumping",
                "description": "Dump credentials.",
                "external_references": [
                    {
                        "source_name": "mitre-attack",
                        "external_id": "T1003",
                        "url": "https://attack.mitre.org/techniques/T1003/",
                    }
                ],
                "kill_chain_phases": [{"phase_name": "credential-access"}],
                "x_mitre_is_subtechnique": False,
                "x_mitre_platforms": ["Windows"],
            },
            {
                "type": "attack-pattern",
                "id": "attack-pattern--child",
                "name": "Security Account Manager",
                "description": "Use [parent](https://attack.mitre.org/techniques/T1003/) and [Mimikatz](https://attack.mitre.org/software/S0002/) and cite.(Citation: Example Ref)",
                "external_references": [
                    {
                        "source_name": "mitre-attack",
                        "external_id": "T1003.002",
                        "url": "https://attack.mitre.org/techniques/T1003/002/",
                    },
                    {
                        "source_name": "Example Ref",
                        "url": "https://example.test/ref",
                    },
                ],
                "kill_chain_phases": [{"phase_name": "credential-access"}],
                "x_mitre_is_subtechnique": True,
                "x_mitre_platforms": ["Windows"],
            },
            {
                "type": "course-of-action",
                "id": "course-of-action--mitigation",
                "name": "Password Policies",
                "description": "Use passwords.",
                "external_references": [
                    {
                        "source_name": "mitre-attack",
                        "external_id": "M1027",
                        "url": "https://attack.mitre.org/mitigations/M1027/",
                    }
                ],
            },
            {
                "type": "x-mitre-data-component",
                "id": "x-mitre-data-component--process",
                "name": "Process Creation",
                "description": "Process starts.",
                "external_references": [
                    {
                        "source_name": "mitre-attack",
                        "external_id": "DC0001",
                        "url": "https://attack.mitre.org/datacomponents/DC0001/",
                    }
                ],
            },
            {
                "type": "tool",
                "id": "tool--mimikatz",
                "name": "Mimikatz",
                "description": "Credential tool.",
                "external_references": [
                    {
                        "source_name": "mitre-attack",
                        "external_id": "S0002",
                        "url": "https://attack.mitre.org/software/S0002/",
                    }
                ],
            },
            {
                "type": "intrusion-set",
                "id": "intrusion-set--apt32",
                "name": "APT32",
                "description": "Threat group.",
                "external_references": [
                    {
                        "source_name": "mitre-attack",
                        "external_id": "G0050",
                        "url": "https://attack.mitre.org/groups/G0050/",
                    }
                ],
            },
            {
                "type": "campaign",
                "id": "campaign--example",
                "name": "Example Campaign",
                "description": "Campaign.",
                "external_references": [
                    {
                        "source_name": "mitre-attack",
                        "external_id": "C9999",
                        "url": "https://attack.mitre.org/campaigns/C9999/",
                    }
                ],
            },
            {
                "type": "malware",
                "id": "malware--example",
                "name": "Example Malware",
                "description": "Malware.",
                "external_references": [
                    {
                        "source_name": "mitre-attack",
                        "external_id": "S9999",
                        "url": "https://attack.mitre.org/software/S9999/",
                    }
                ],
            },
            {
                "type": "relationship",
                "id": "relationship--uses",
                "relationship_type": "uses",
                "source_ref": "tool--mimikatz",
                "target_ref": "attack-pattern--child",
                "description": "Mimikatz dumps SAM.(Citation: Procedure Ref)",
                "external_references": [
                    {
                        "source_name": "Procedure Ref",
                        "url": "https://example.test/procedure",
                    }
                ],
            },
            {
                "type": "relationship",
                "id": "relationship--group-uses",
                "relationship_type": "uses",
                "source_ref": "intrusion-set--apt32",
                "target_ref": "attack-pattern--child",
                "description": "APT32 dumped credentials.",
                "external_references": [
                    {
                        "source_name": "Group Procedure Ref",
                        "url": "https://example.test/group-procedure",
                    }
                ],
            },
            {
                "type": "relationship",
                "id": "relationship--campaign-uses",
                "relationship_type": "uses",
                "source_ref": "campaign--example",
                "target_ref": "attack-pattern--child",
                "description": "Campaign should not be rendered as a procedure example.",
            },
            {
                "type": "relationship",
                "id": "relationship--malware-uses",
                "relationship_type": "uses",
                "source_ref": "malware--example",
                "target_ref": "attack-pattern--child",
                "description": "Example Malware dumped credentials.",
            },
            {
                "type": "relationship",
                "id": "relationship--mitigates",
                "relationship_type": "mitigates",
                "source_ref": "course-of-action--mitigation",
                "target_ref": "attack-pattern--child",
                "description": "Mitigates with [[bad|pipe]].(Citation: Relationship Ref)",
                "external_references": [
                    {
                        "source_name": "Relationship Ref",
                        "url": "https://example.test/relationship",
                    }
                ],
            },
        ]
    }
    source = MitreSource(
        config={
            "include_tactics": True,
            "include_techniques": True,
            "include_subtechniques": True,
            "include_mitigations": True,
            "include_data_sources": True,
            "include_tools": True,
        },
        logger=DummyLogger(),
    )
    objects = source.parse(data)
    renderer = MarkdownRenderer(
        config={
            "sources": {"mitre": {"domain": "enterprise-attack"}},
            "rendering": {"generated_marker": "focuslocust"},
        },
        paths=ProjectPaths(
            vault_path=tmp_path / "vault",
            cache_path=tmp_path / ".cache",
            log_path=tmp_path / ".logs",
        ),
        logger=DummyLogger(),
    )

    written, skipped = renderer.render_mitre(objects)

    assert written == 15
    assert skipped == 0

    child = (tmp_path / "vault/kb/mitre/attack/techniques/T1003.002-security-account-manager.md").read_text(
        encoding="utf-8"
    )
    assert "## Parent Technique" not in child
    assert "## Procedure Examples" in child
    assert "    - attack/has_procedures" in child
    assert "APT32 dumped credentials" not in child
    assert "| [[kb/mitre/attack/software/S0002-mimikatz\\|S0002]] | Mimikatz | Mimikatz dumps SAM.[^1]  |" in child
    assert "| [S9999](https://attack.mitre.org/software/S9999/) | Example Malware | Example Malware dumped credentials. |" in child
    assert "Campaign should not be rendered as a procedure example" not in child
    assert "[[kb/mitre/attack/software/S0002-mimikatz|Mimikatz]]" in child
    assert "[Procedure Ref](https://example.test/procedure)" in child
    assert "[^1]" in child
    assert "(Citation:" not in child

    parent = (tmp_path / "vault/kb/mitre/attack/techniques/T1003-os-credential-dumping.md").read_text(
        encoding="utf-8"
    )
    assert "## Sub-techniques" in parent
    assert "[[kb/mitre/attack/techniques/T1003.002-security-account-manager\\|T1003.002]]" in parent

    tool = (tmp_path / "vault/kb/mitre/attack/software/S0002-mimikatz.md").read_text(encoding="utf-8")
    assert "type: tool" in tool
    assert "    - attack/software/tool" in tool
    assert "    - attack/type/software" in tool
    assert "## Techniques Used" in tool
    assert "[[kb/mitre/attack/techniques/T1003.002-security-account-manager\\|T1003.002]]" in tool
    assert "[Procedure Ref](https://example.test/procedure)" in tool

    mitigation = (tmp_path / "vault/kb/mitre/attack/mitigations/M1027-password-policies.md").read_text(
        encoding="utf-8"
    )
    assert "[[bad\\|pipe]]" in mitigation
    assert "[^1]" in mitigation
    assert "[Relationship Ref](https://example.test/relationship)" in mitigation
    assert "(Citation: Relationship Ref)" not in mitigation

    index = (tmp_path / "vault/kb/indexes/mitre.md").read_text(encoding="utf-8")
    assert "- Techniques" in index
    assert "- Software" in index
    assert "  - [[kb/mitre/attack/software/S0002-mimikatz|S0002 - Mimikatz]]" in index
    assert "    - [[kb/mitre/attack/techniques/T1003.002-security-account-manager|T1003.002 - Security Account Manager]]" in index

    references = (tmp_path / "vault/kb/mitre/attack/indexes/all-references.md").read_text(encoding="utf-8")
    assert "# References" in references
    assert "[Example Ref](https://example.test/ref)" in references
    assert "[Procedure Ref](https://example.test/procedure)" in references
    assert "[Relationship Ref](https://example.test/relationship)" in references
