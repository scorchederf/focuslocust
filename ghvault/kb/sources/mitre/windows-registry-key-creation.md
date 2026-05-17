---
parsed_by: focuslocust
source: mitre
type: generated
---
# Windows Registry Key Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0056` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows Registry Key Creation](../../attack/data-sources/DC0056-windows-registry-key-creation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0056 |
| name | Windows Registry Key Creation |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0056 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Initial construction of a new registry key within the Windows operating system. '
external_references:
- external_id: DC0056
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0056
id: x-mitre-data-component--7f70fae7-a68d-4730-a83a-f260b9606129
modified: '2025-11-12T22:03:39.105Z'
name: Windows Registry Key Creation
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: EventCode=12
  name: WinEventLog:Sysmon
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
