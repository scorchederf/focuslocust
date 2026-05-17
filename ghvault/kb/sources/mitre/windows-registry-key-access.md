---
parsed_by: focuslocust
source: mitre
type: generated
---
# Windows Registry Key Access

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0050` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows Registry Key Access](../../attack/data-sources/DC0050-windows-registry-key-access.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0050 |
| name | Windows Registry Key Access |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0050 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: The action of opening a specific Windows Registry key, typically to read its associated value. This activity
  can be used for system configuration, application settings retrieval, and security policies.
external_references:
- external_id: DC0050
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0050
id: x-mitre-data-component--ed0dd8aa-1677-4551-bb7d-8da767617e1b
modified: '2025-11-12T22:03:39.105Z'
name: Windows Registry Key Access
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
- channel: EventCode=4663, 4670, 4656
  name: WinEventLog:Security
- channel: EventCode=4657
  name: WinEventLog:Security
- channel: Behavioral rule for registry enumeration under credential-related paths
  name: EDR:hunting
- channel: Enumerate Winlogon subkeys for unknown or unsigned binaries
  name: Autoruns:RegistryScan
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
