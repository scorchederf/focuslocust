---
parsed_by: focuslocust
source: mitre
type: generated
---
# Data Transfer Size Limits

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1030` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Data Transfer Size Limits](../../attack/techniques/T1030-data-transfer-size-limits.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1030 |
| name | Data Transfer Size Limits |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1030 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:34.523Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: An adversary may exfiltrate data in fixed size chunks instead of whole files or limit packet sizes below certain
  thresholds. This approach may be used to avoid triggering network data transfer threshold alerts.
external_references:
- external_id: T1030
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1030
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
id: attack-pattern--c3888c54-775d-4b2f-b759-75a2ececcbfd
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: exfiltration
modified: '2025-10-24T17:49:20.770Z'
name: Data Transfer Size Limits
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
- ESXi
x_mitre_version: '1.1'
```
