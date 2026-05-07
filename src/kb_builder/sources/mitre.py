from __future__ import annotations

from collections import defaultdict
from typing import Any

from ..models import ExternalReference, MitreObject
from ..naming import make_id_slug_filename


class MitreSource:
    def __init__(self, config: dict[str, Any], logger):
        self.config = config
        self.logger = logger

    def parse(self, data: dict[str, Any]) -> list[MitreObject]:
        objects = data.get("objects", [])
        self.logger.info(f"Loaded STIX objects: {len(objects)}")

        id_to_attack_id: dict[str, str] = {}
        id_to_name: dict[str, str] = {}
        id_to_description: dict[str, str] = {}
        id_to_stix_type: dict[str, str] = {}
        id_to_url: dict[str, str] = {}
        relationships = []
        relationship_refs_by_attack_id: dict[str, list[ExternalReference]] = defaultdict(list)

        for item in objects:
            if self._skip(item):
                continue

            attack_id, attack_url = self._attack_external(item)
            if attack_id:
                id_to_attack_id[item.get("id", "")] = attack_id
                id_to_name[item.get("id", "")] = item.get("name", "")
                id_to_description[item.get("id", "")] = item.get("description", "")
                id_to_stix_type[item.get("id", "")] = item.get("type", "")
                id_to_url[item.get("id", "")] = attack_url

            if item.get("type") == "relationship":
                relationships.append(item)

        mitigations_by_technique: dict[str, list[dict[str, str]]] = defaultdict(list)
        techniques_by_mitigation: dict[str, list[dict[str, str]]] = defaultdict(list)
        procedure_examples_by_technique: dict[str, list[dict[str, str]]] = defaultdict(list)
        techniques_by_tool: dict[str, list[dict[str, str]]] = defaultdict(list)

        for rel in relationships:
            rel_type = rel.get("relationship_type")
            source_ref = rel.get("source_ref")
            target_ref = rel.get("target_ref")

            source_attack_id = id_to_attack_id.get(source_ref, "")
            target_attack_id = id_to_attack_id.get(target_ref, "")
            source_name = id_to_name.get(source_ref, source_attack_id)
            target_name = id_to_name.get(target_ref, target_attack_id)
            description = rel.get("description", "")

            if rel_type == "mitigates" and target_attack_id and source_attack_id:
                rel_refs = self._external_references(rel)
                relationship_refs_by_attack_id[source_attack_id].extend(rel_refs)
                relationship_refs_by_attack_id[target_attack_id].extend(rel_refs)
                mitigations_by_technique[target_attack_id].append(
                    {
                        "id": source_attack_id,
                        "name": source_name,
                        "description": description or id_to_description.get(source_ref, ""),
                        "external_references": rel_refs,
                    }
                )
                techniques_by_mitigation[source_attack_id].append(
                    {
                        "id": target_attack_id,
                        "name": target_name,
                        "description": description or id_to_description.get(target_ref, ""),
                        "external_references": rel_refs,
                    }
                )
            elif (
                rel_type == "uses"
                and target_attack_id.startswith("T")
                and source_attack_id.startswith("S")
            ):
                rel_refs = self._external_references(rel)
                relationship_refs_by_attack_id[source_attack_id].extend(rel_refs)
                relationship_refs_by_attack_id[target_attack_id].extend(rel_refs)
                procedure_examples_by_technique[target_attack_id].append(
                    {
                        "id": source_attack_id,
                        "name": source_name,
                        "description": description or id_to_description.get(source_ref, ""),
                        "external_references": rel_refs,
                        "source_type": id_to_stix_type.get(source_ref, ""),
                        "url": id_to_url.get(source_ref, ""),
                    }
                )
                if id_to_stix_type.get(source_ref) == "tool":
                    techniques_by_tool[source_attack_id].append(
                        {
                            "id": target_attack_id,
                            "name": target_name,
                            "description": description or id_to_description.get(target_ref, ""),
                            "external_references": rel_refs,
                        }
                    )

        parsed: list[MitreObject] = []

        include_tactics = self.config.get("include_tactics", True)
        include_techniques = self.config.get("include_techniques", True)
        include_subtechniques = self.config.get("include_subtechniques", True)
        include_mitigations = self.config.get("include_mitigations", True)
        include_data_sources = self.config.get("include_data_sources", True)
        include_tools = self.config.get("include_tools", True)

        counts = defaultdict(int)

        for item in objects:
            if self._skip(item):
                continue

            stix_type = item.get("type")

            if stix_type == "x-mitre-tactic" and include_tactics:
                obj = self._parse_basic(item, "tactic")
                if obj:
                    self._add_relationship_refs(obj, relationship_refs_by_attack_id)
                    obj.path = self._path_for(obj)
                    parsed.append(obj)
                    counts["tactics"] += 1

            elif stix_type == "attack-pattern":
                is_subtechnique = bool(item.get("x_mitre_is_subtechnique", False))

                if is_subtechnique and not include_subtechniques:
                    continue

                if not is_subtechnique and not include_techniques:
                    continue

                obj = self._parse_basic(item, "technique")
                if obj:
                    self._add_relationship_refs(obj, relationship_refs_by_attack_id)
                    obj.tactics = self._kill_chain_phases(item)
                    obj.platforms = item.get("x_mitre_platforms", []) or []
                    obj.data_sources = item.get("x_mitre_data_sources", []) or []
                    obj.permissions_required = item.get("x_mitre_permissions_required", []) or []
                    obj.procedure_examples = sorted(
                        procedure_examples_by_technique.get(obj.id, []),
                        key=lambda row: row["id"],
                    )
                    if is_subtechnique and "." in obj.id:
                        obj.parent_technique_id = obj.id.rsplit(".", 1)[0]
                    obj.mitigations = sorted(
                        mitigations_by_technique.get(obj.id, []),
                        key=lambda row: row["id"],
                    )
                    obj.path = self._path_for(obj)
                    parsed.append(obj)
                    counts["techniques"] += 1

            elif stix_type == "course-of-action" and include_mitigations:
                obj = self._parse_basic(item, "mitigation")
                if obj:
                    self._add_relationship_refs(obj, relationship_refs_by_attack_id)
                    obj.related_techniques = sorted(
                        techniques_by_mitigation.get(obj.id, []),
                        key=lambda row: row["id"],
                    )
                    obj.path = self._path_for(obj)
                    parsed.append(obj)
                    counts["mitigations"] += 1

            elif stix_type in {"x-mitre-data-source", "x-mitre-data-component"} and include_data_sources:
                obj = self._parse_basic(item, "data-source")
                if obj:
                    self._add_relationship_refs(obj, relationship_refs_by_attack_id)
                    obj.path = self._path_for(obj)
                    parsed.append(obj)
                    counts["data_sources"] += 1

            elif stix_type == "tool" and include_tools:
                obj = self._parse_basic(item, "tool")
                if obj:
                    self._add_relationship_refs(obj, relationship_refs_by_attack_id)
                    obj.techniques_used = sorted(
                        techniques_by_tool.get(obj.id, []),
                        key=lambda row: row["id"],
                    )
                    obj.path = self._path_for(obj)
                    parsed.append(obj)
                    counts["tools"] += 1

        self.logger.info(f"Parsed tactics: {counts['tactics']}")
        self.logger.info(f"Parsed techniques/sub-techniques: {counts['techniques']}")
        self.logger.info(f"Parsed mitigations: {counts['mitigations']}")
        self.logger.info(f"Parsed data sources: {counts['data_sources']}")
        self.logger.info(f"Parsed tools: {counts['tools']}")

        return parsed

    def _parse_basic(self, item: dict[str, Any], obj_type: str) -> MitreObject | None:
        attack_id, attack_url = self._attack_external(item)
        if not attack_id:
            self.logger.debug(f"Skipping {item.get('id')} because no ATT&CK external ID was found")
            return None

        refs = self._external_references(item)

        return MitreObject(
            id=attack_id,
            source="mitre",
            type=obj_type,
            name=self._display_name(item.get("name", attack_id)),
            description=item.get("description", ""),
            url=attack_url,
            external_references=refs,
            raw=item,
        )

    def _attack_external(self, item: dict[str, Any]) -> tuple[str, str]:
        for ref in item.get("external_references", []):
            if ref.get("source_name") == "mitre-attack":
                return ref.get("external_id", ""), ref.get("url", "")
        return "", ""

    def _external_references(self, item: dict[str, Any]) -> list[ExternalReference]:
        return [
            ExternalReference(
                source_name=ref.get("source_name", ""),
                url=ref.get("url", ""),
                external_id=ref.get("external_id", ""),
            )
            for ref in item.get("external_references", [])
            if ref.get("url") or ref.get("external_id")
        ]

    def _add_relationship_refs(
        self,
        obj: MitreObject,
        relationship_refs_by_attack_id: dict[str, list[ExternalReference]],
    ) -> None:
        seen = {(ref.source_name, ref.url, ref.external_id) for ref in obj.external_references}
        for ref in relationship_refs_by_attack_id.get(obj.id, []):
            key = (ref.source_name, ref.url, ref.external_id)
            if key not in seen:
                obj.external_references.append(ref)
                seen.add(key)

    def _skip(self, item: dict[str, Any]) -> bool:
        return bool(item.get("revoked", False) or item.get("x_mitre_deprecated", False))

    def _display_name(self, name: str) -> str:
        return name.replace("/", "／")

    def _kill_chain_phases(self, item: dict[str, Any]) -> list[str]:
        phases = []
        for phase in item.get("kill_chain_phases", []) or []:
            name = phase.get("phase_name")
            if name:
                phases.append(name)
        return sorted(set(phases))

    def _path_for(self, obj: MitreObject) -> str:
        filename = make_id_slug_filename(obj.id, obj.name)
        base = "kb/mitre/attack"

        if obj.type == "tactic":
            return f"{base}/tactics/{filename}"

        if obj.type == "technique":
            return f"{base}/techniques/{filename}"

        if obj.type == "mitigation":
            return f"{base}/mitigations/{filename}"

        if obj.type == "data-source":
            return f"{base}/data-sources/{filename}"

        if obj.type == "tool":
            return f"{base}/software/{filename}"

        return f"{base}/{filename}"
