---
parsed_by: focuslocust
source: mitre
type: generated
---
# Windows Registry Key Deletion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0045` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows Registry Key Deletion](../../attack/data-sources/DC0045-windows-registry-key-deletion.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0045 |
| name | Windows Registry Key Deletion |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0045 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The removal of a registry key within the Windows operating system.\n\n*Data Collection Measures:*\n\n- Windows\
  \ Event Logs\n    - Event ID 4658 - Registry Key Handle Closed: Captures when a handle to a registry key is closed, which\
  \ may indicate deletion.\n    - Event ID 4660 - Object Deleted: Logs when a registry key is deleted.\n- Sysmon (System Monitor)\
  \ for Windows\n    - Sysmon Event ID 12 - Registry Key Deleted: Logs when a registry key is removed.\n    - Sysmon Event\
  \ ID 13 - Registry Value Deleted: Captures removal of specific registry values.\n- Endpoint Detection and Response (EDR)\
  \ Solutions\n    - Monitor registry deletions for suspicious behavior."
external_references:
- external_id: DC0045
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0045
id: x-mitre-data-component--1177a4c5-31c8-400c-8544-9071166afa0e
modified: '2025-10-21T15:10:28.402Z'
name: Windows Registry Key Deletion
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- ics-attack
- enterprise-attack
x_mitre_log_sources:
- channel: None
  name: Windows Registry
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
