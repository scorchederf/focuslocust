---
parsed_by: focuslocust
source: mitre
type: generated
---
# Diskpart

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S9002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Diskpart](../../tools/unknown/diskpart.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | S9002 |
| name | Diskpart |
| type | tool |
| source | mitre |
| url | https://attack.mitre.org/software/S9002 |

## Preserved Source Material

```yaml
created: '2026-01-26T18:36:33.410Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "[Diskpart](https://attack.mitre.org/software/S9002) is a Windows command-line utility that is used to manage\
  \ the computer’s drives, which includes disks, partitions, volumes and virtual hard disks.(Citation: Microsoft_diskpart_Feb2023)\
  \  \n\nAdversaries may abuse [Diskpart](https://attack.mitre.org/software/S9002) to perform discovery and destructive actions\
  \ on a system’s storage. For example, adversaries have been observed using [Diskpart](https://attack.mitre.org/software/S9002)\
  \ to conduct [Discovery](https://attack.mitre.org/tactics/TA0007) techniques to enumerate disks and volumes to gather information\
  \ about the host environment, and to execute commands such as `clean all` to remove partition information and overwrite\
  \ data across disks, resulting in data destruction.(Citation: Trendmicro_RansomHub_Dec2024)"
external_references:
- external_id: S9002
  source_name: mitre-attack
  url: https://attack.mitre.org/software/S9002
- description: Microsoft. (2023, February 3). diskpart. Retrieved March 17, 2025.
  source_name: Microsoft_diskpart_Feb2023
  url: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskpart
- description: Trend Research. (2024, December 20). RansomHub. Retrieved December 23, 2025.
  source_name: Trendmicro_RansomHub_Dec2024
  url: https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-ransomhub
id: tool--080f872e-f1a3-4d42-bb00-9eb55949f6a9
modified: '2026-04-23T02:11:05.517Z'
name: Diskpart
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: tool
x_mitre_aliases:
- Diskpart
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Liran Ravich, CardinalOps
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.0'
```
