---
parsed_by: focuslocust
source: mitre
type: generated
---
# Match Legitimate Resource Name or Location

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1036.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Match Legitimate Resource Name or Location](../../attack/techniques/T1036.005-match-legitimate-resource-name-or-location.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1036.005 |
| name | Match Legitimate Resource Name or Location |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1036/005 |

## Preserved Source Material

```yaml
created: '2020-02-10T20:43:10.239Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may match or approximate the name or location of legitimate files, Registry keys, or other resources\
  \ when naming/placing them. This is done for the sake of evading defenses and observation. \n\nThis may be done by placing\
  \ an executable in a commonly trusted directory (ex: under System32) or giving it the name of a legitimate, trusted program\
  \ (ex: `svchost.exe`). Alternatively, a Windows Registry key may be given a close approximation to a key used by a legitimate\
  \ program. In containerized environments, a threat actor may create a resource in a trusted namespace or one that matches\
  \ the naming convention of a container pod or cluster.(Citation: Aquasec Kubernetes Backdoor 2023)"
external_references:
- external_id: T1036.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1036/005
- description: Michael Katchinskiy and Assaf Morag. (2023, April 21). First-Ever Attack Leveraging Kubernetes RBAC to Backdoor
    Clusters. Retrieved March 24, 2025.
  source_name: Aquasec Kubernetes Backdoor 2023
  url: https://www.aquasec.com/blog/leveraging-kubernetes-rbac-to-backdoor-clusters/
id: attack-pattern--1c4e5d32-1fe9-4116-9d9d-59e3925bd6a2
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:39:41.881Z'
name: Match Legitimate Resource Name or Location
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Vishwas Manral, McAfee
- Yossi Weizman, Azure Defender Research Team
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Containers
- ESXi
- Linux
- macOS
- Windows
x_mitre_version: '3.0'
```
