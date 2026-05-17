---
parsed_by: focuslocust
source: mitre
type: generated
---
# Exfiltration Over C2 Channel

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1041` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Exfiltration Over C2 Channel](../../attack/techniques/T1041-exfiltration-over-c2-channel.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1041 |
| name | Exfiltration Over C2 Channel |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1041 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:41.804Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Adversaries may steal data by exfiltrating it over an existing command and control channel. Stolen data is encoded
  into the normal communications channel using the same protocol as command and control communications.
external_references:
- external_id: T1041
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1041
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
id: attack-pattern--92d7da27-2d91-488e-a00c-059dc162766d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: exfiltration
modified: '2025-10-24T17:49:06.675Z'
name: Exfiltration Over C2 Channel
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- William Cain
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Windows
x_mitre_version: '2.3'
```
