---
parsed_by: focuslocust
source: mitre
type: generated
---
# Network Share Access

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0102` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Share Access](../../attack/data-sources/DC0102-network-share-access.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0102 |
| name | Network Share Access |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0102 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.275Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Opening a network share, which makes the contents available to the requestor (ex: Windows EID 5140 or 5145)'
external_references:
- external_id: DC0102
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0102
id: x-mitre-data-component--f5468e67-51c7-4756-9b4f-65707708e7fa
modified: '2025-11-12T22:03:39.105Z'
name: Network Share Access
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
  name: Network Share
- channel: EventCode=31001
  name: WinEventLog:Microsoft-Windows-SMBClient/Security
- channel: EventCode=5140
  name: WinEventLog:Security
- channel: EventCode=5145
  name: WinEventLog:Security
- channel: Access to SYSVOL share from non-admin user or unusual endpoints
  name: WinEventLog:Microsoft-Windows-SMBServer
- channel: smb_files.log
  name: NSM:Flow
- channel: FileUploaded, FileAccessed
  name: m365:unified
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
