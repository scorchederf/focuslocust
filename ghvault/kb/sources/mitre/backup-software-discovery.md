---
parsed_by: focuslocust
source: mitre
type: generated
---
# Backup Software Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1518.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Backup Software Discovery](../../attack/techniques/T1518.002-backup-software-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1518.002 |
| name | Backup Software Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1518/002 |

## Preserved Source Material

```yaml
created: '2025-05-22T18:57:47.616Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may attempt to get a listing of backup software or configurations that are installed on a system.\
  \ Adversaries may use this information to shape follow-on behaviors, such as [Data Destruction](https://attack.mitre.org/techniques/T1485),\
  \ [Inhibit System Recovery](https://attack.mitre.org/techniques/T1490), or [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486).\
  \  \n\nCommands that can be used to obtain security software information are [netsh](https://attack.mitre.org/software/S0108),\
  \ `reg query` with [Reg](https://attack.mitre.org/software/S0075), `dir` with [cmd](https://attack.mitre.org/software/S0106),\
  \ and [Tasklist](https://attack.mitre.org/software/S0057), but other indicators of discovery behavior may be more specific\
  \ to the type of software or security system the adversary is looking for, such as Veeam, Acronis, Dropbox, or Paragon.(Citation:\
  \ Symantec Play Ransomware 2023)"
external_references:
- external_id: T1518.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1518/002
- description: Symantec Threat Hunter Team. (2023, April 19). Play Ransomware Group Using New Custom Data-Gathering Tools.
    Retrieved May 22, 2025.
  source_name: Symantec Play Ransomware 2023
  url: https://www.security.com/threat-intelligence/play-ransomware-volume-shadow-copy
id: attack-pattern--4a6cfdae-1417-40c7-a84e-f59d21c58266
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-22T03:53:48.786Z'
name: Backup Software Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Florian Heigl
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
- macOS
- Linux
x_mitre_version: '1.0'
```
