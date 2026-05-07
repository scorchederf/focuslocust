from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExternalReference:
    source_name: str
    url: str = ""
    external_id: str = ""


@dataclass
class KBObject:
    id: str
    source: str
    type: str
    name: str
    description: str = ""
    path: str = ""
    url: str = ""
    aliases: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    links: list[str] = field(default_factory=list)
    reference_notes: list[dict[str, str]] = field(default_factory=list)
    raw: dict[str, Any] = field(default_factory=dict)
    external_references: list[ExternalReference] = field(default_factory=list)


@dataclass
class MitreObject(KBObject):
    tactics: list[str] = field(default_factory=list)
    platforms: list[str] = field(default_factory=list)
    data_sources: list[str] = field(default_factory=list)
    permissions_required: list[str] = field(default_factory=list)
    procedure_examples: list[dict[str, str]] = field(default_factory=list)
    mitigations: list[dict[str, str]] = field(default_factory=list)
    related_techniques: list[dict[str, str]] = field(default_factory=list)
    subtechniques: list[dict[str, str]] = field(default_factory=list)
    techniques_used: list[dict[str, str]] = field(default_factory=list)
    parent_technique_id: str = ""


@dataclass
class LolbasCommand:
    command: str = ""
    description: str = ""
    usecase: str = ""
    category: str = ""
    privileges: str = ""
    mitre_id: str = ""
    operating_system: str = ""


@dataclass
class LolbasTool(KBObject):
    functions: list[str] = field(default_factory=list)
    commands: list[LolbasCommand] = field(default_factory=list)
    paths: list[str] = field(default_factory=list)
    detections: list[str] = field(default_factory=list)
    resources: list[str] = field(default_factory=list)
    acknowledgements: list[str] = field(default_factory=list)
