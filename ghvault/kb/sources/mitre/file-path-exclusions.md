---
parsed_by: focuslocust
source: mitre
type: generated
---
# File／Path Exclusions

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1564.012` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [File／Path Exclusions](../../attack/techniques/T1564.012-file-path-exclusions.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1564.012 |
| name | File／Path Exclusions |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1564/012 |

## Preserved Source Material

```yaml
created: '2024-03-29T16:59:10.374Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to hide their file-based artifacts by writing them to specific folders or file names
  excluded from antivirus (AV) scanning and other defensive capabilities. AV and other file-based scanners often include exclusions
  to optimize performance as well as ease installation and legitimate use of applications. These exclusions may be contextual
  (e.g., scans are only initiated in response to specific triggering events/alerts), but are also often hardcoded strings
  referencing specific folders and/or files assumed to be trusted and legitimate.(Citation: Microsoft File Folder Exclusions)


  Adversaries may abuse these exclusions to hide their file-based artifacts. For example, rather than  tampering with tool
  settings to add a new exclusion (i.e., [Disable or Modify Tools](https://attack.mitre.org/techniques/T1685)), adversaries
  may drop their file-based payloads in default or otherwise well-known exclusions. Adversaries may also use [Security Software
  Discovery](https://attack.mitre.org/techniques/T1518/001) and other [Discovery](https://attack.mitre.org/tactics/TA0007)/[Reconnaissance](https://attack.mitre.org/tactics/TA0043)
  activities to both discover and verify existing exclusions in a victim environment.'
external_references:
- external_id: T1564.012
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1564/012
- description: Microsoft. (2024, February 27). Contextual file and folder exclusions. Retrieved March 29, 2024.
  source_name: Microsoft File Folder Exclusions
  url: https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus
id: attack-pattern--09b008a9-b4eb-462a-a751-a0eb58050cd9
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-16T19:21:42.768Z'
name: File/Path Exclusions
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
