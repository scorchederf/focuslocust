from src.kb_builder.sources.mitre import MitreSource


class DummyLogger:
    def info(self, *args, **kwargs):
        pass

    def debug(self, *args, **kwargs):
        pass

    def warning(self, *args, **kwargs):
        pass


def parser():
    return MitreSource(
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


def test_parse_technique():
    data = {
        "objects": [
            {
                "type": "attack-pattern",
                "id": "attack-pattern--1",
                "name": "Security Account Manager",
                "description": "SAM dumping.",
                "external_references": [
                    {
                        "source_name": "mitre-attack",
                        "external_id": "T1003.002",
                        "url": "https://attack.mitre.org/techniques/T1003/002/",
                    }
                ],
                "kill_chain_phases": [{"phase_name": "credential-access"}],
                "x_mitre_platforms": ["Windows"],
                "x_mitre_data_sources": ["Process: Process Creation"],
            }
        ]
    }

    objects = parser().parse(data)

    assert len(objects) == 1
    assert objects[0].id == "T1003.002"
    assert objects[0].name == "Security Account Manager"
    assert objects[0].path == "kb/mitre/attack/techniques/T1003.002-security-account-manager.md"


def test_revoked_object_skipped():
    data = {
        "objects": [
            {
                "type": "attack-pattern",
                "id": "attack-pattern--1",
                "name": "Old Technique",
                "revoked": True,
                "external_references": [
                    {"source_name": "mitre-attack", "external_id": "T9999"}
                ],
            }
        ]
    }

    assert parser().parse(data) == []


def test_deprecated_object_skipped():
    data = {
        "objects": [
            {
                "type": "attack-pattern",
                "id": "attack-pattern--1",
                "name": "Old Technique",
                "x_mitre_deprecated": True,
                "external_references": [
                    {"source_name": "mitre-attack", "external_id": "T9999"}
                ],
            }
        ]
    }

    assert parser().parse(data) == []


def test_parse_tactic():
    data = {
        "objects": [
            {
                "type": "x-mitre-tactic",
                "id": "x-mitre-tactic--1",
                "name": "Credential Access",
                "description": "Stealing credentials.",
                "external_references": [
                    {"source_name": "mitre-attack", "external_id": "TA0006"}
                ],
            }
        ]
    }

    objects = parser().parse(data)

    assert len(objects) == 1
    assert objects[0].id == "TA0006"
    assert objects[0].path == "kb/mitre/attack/tactics/TA0006-credential-access.md"


def test_parse_mitigation():
    data = {
        "objects": [
            {
                "type": "course-of-action",
                "id": "course-of-action--1",
                "name": "Password Policies",
                "description": "Use password policies.",
                "external_references": [
                    {"source_name": "mitre-attack", "external_id": "M1027"}
                ],
            }
        ]
    }

    objects = parser().parse(data)

    assert len(objects) == 1
    assert objects[0].id == "M1027"
    assert objects[0].path == "kb/mitre/attack/mitigations/M1027-password-policies.md"


def test_parse_data_component_as_data_source_note():
    data = {
        "objects": [
            {
                "type": "x-mitre-data-component",
                "id": "x-mitre-data-component--1",
                "name": "Process Creation",
                "description": "Process starts.",
                "external_references": [
                    {"source_name": "mitre-attack", "external_id": "DC0001"}
                ],
            }
        ]
    }

    objects = parser().parse(data)

    assert len(objects) == 1
    assert objects[0].id == "DC0001"
    assert objects[0].type == "data-source"
    assert objects[0].path == "kb/mitre/attack/data-sources/DC0001-process-creation.md"


def test_display_name_normalises_slashes():
    data = {
        "objects": [
            {
                "type": "attack-pattern",
                "id": "attack-pattern--1",
                "name": "/etc/passwd and /etc/shadow",
                "external_references": [
                    {"source_name": "mitre-attack", "external_id": "T1003.008"}
                ],
            }
        ]
    }

    objects = parser().parse(data)

    assert objects[0].name == "／etc／passwd and ／etc／shadow"


def test_parse_tool():
    data = {
        "objects": [
            {
                "type": "tool",
                "id": "tool--1",
                "name": "Mimikatz",
                "description": "Credential tool.",
                "external_references": [
                    {"source_name": "mitre-attack", "external_id": "S0002"}
                ],
            }
        ]
    }

    objects = parser().parse(data)

    assert len(objects) == 1
    assert objects[0].id == "S0002"
    assert objects[0].type == "tool"
    assert objects[0].path == "kb/mitre/attack/software/S0002-mimikatz.md"


def test_malware_is_not_generated():
    data = {
        "objects": [
            {
                "type": "malware",
                "id": "malware--1",
                "name": "Example Malware",
                "description": "No page.",
                "external_references": [
                    {"source_name": "mitre-attack", "external_id": "S9999"}
                ],
            }
        ]
    }

    assert parser().parse(data) == []
