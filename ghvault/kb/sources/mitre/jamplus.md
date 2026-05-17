---
parsed_by: focuslocust
source: mitre
type: generated
---
# JamPlus

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1127.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [JamPlus](../../attack/techniques/T1127.003-jamplus.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1127.003 |
| name | JamPlus |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1127/003 |

## Preserved Source Material

```yaml
created: '2025-03-21T13:36:48.710Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use `JamPlus` to proxy the execution of a malicious script. `JamPlus` is a build utility tool
  for code and data build systems. It works with several popular compilers and can be used for generating workspaces in code
  editors such as Visual Studio.(Citation: JamPlus manual)


  Adversaries may abuse the `JamPlus` build utility to execute malicious scripts via a `.jam` file, which describes the build
  process and required dependencies. Because the malicious script is executed from a reputable developer tool, it may subvert
  application control security systems such as Smart App Control.(Citation: Cyble)(Citation: Elastic Security Labs)'
external_references:
- external_id: T1127.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1127/003
- description: 'Cyble. (2024, September 9). Reputation Hijacking with JamPlus: A Maneuver to Bypass Smart App Control (SAC).
    Retrieved March 21, 2025.'
  source_name: Cyble
  url: https://cyble.com/blog/reputation-hijacking-with-jamplus-a-maneuver-to-bypass-smart-app-control-sac/
- description: Joe Desimone. (2024, August 5). Dismantling Smart App Control. Retrieved March 21, 2025.
  source_name: Elastic Security Labs
  url: https://www.elastic.co/security-labs/dismantling-smart-app-control
- description: 'Perforce Software, Inc.. (n.d.). JamPlus manual: Quick Start Guide. Retrieved March 21, 2025.'
  source_name: JamPlus manual
  url: https://jamplus.github.io/jamplus/quick_start.html
id: attack-pattern--7d356151-a69d-404e-896b-71618952702a
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2026-04-15T22:45:43.373Z'
name: JamPlus
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
- Windows
x_mitre_remote_support: false
x_mitre_version: '2.0'
```
