---
parsed_by: focuslocust
source: mitre
type: generated
---
# Local Data Staging

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1074.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Local Data Staging](../../attack/techniques/T1074.001-local-data-staging.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1074.001 |
| name | Local Data Staging |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1074/001 |

## Preserved Source Material

```yaml
created: '2020-03-13T21:13:10.467Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may stage collected data in a central location or directory on the local system prior to Exfiltration.
  Data may be kept in separate files or combined into one file through techniques such as [Archive Collected Data](https://attack.mitre.org/techniques/T1560).
  Interactive command shells may be used, and common functionality within [cmd](https://attack.mitre.org/software/S0106) and
  bash may be used to copy data into a staging location.


  Adversaries may also stage collected data in various available formats/locations of a system, including local storage databases/repositories
  or the Windows Registry.(Citation: Prevailion DarkWatchman 2021)'
external_references:
- external_id: T1074.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1074/001
- description: 'Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved
    January 10, 2022.'
  source_name: Prevailion DarkWatchman 2021
  url: https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/
id: attack-pattern--1c34f7aa-9341-4a48-bfab-af22e51aca6c
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:48:28.868Z'
name: Local Data Staging
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Massimiliano Romano, BT Security
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Windows
x_mitre_version: '1.2'
```
