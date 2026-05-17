---
parsed_by: focuslocust
source: mitre
type: generated
---
# Data from Network Shared Drive

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1039` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Data from Network Shared Drive](../../attack/techniques/T1039-data-from-network-shared-drive.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1039 |
| name | Data from Network Shared Drive |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1039 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:41.022Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Adversaries may search network shares on computers they have compromised to find files of interest. Sensitive
  data can be collected from remote systems via shared network drives (host shared directory, network file server, etc.) that
  are accessible from the current system prior to Exfiltration. Interactive command shells may be in use, and common functionality
  within [cmd](https://attack.mitre.org/software/S0106) may be used to gather information.
external_references:
- external_id: T1039
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1039
id: attack-pattern--ae676644-d2d2-41b7-af7e-9bed1b55898c
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:49:13.555Z'
name: Data from Network Shared Drive
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- David Tayouri
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.5'
```
