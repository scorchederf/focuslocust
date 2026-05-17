---
parsed_by: focuslocust
source: mitre
type: generated
---
# Steganography

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1001.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Steganography](../../attack/techniques/T1001.002-steganography.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1001.002 |
| name | Steganography |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1001/002 |

## Preserved Source Material

```yaml
created: '2020-03-15T00:37:58.963Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use steganographic techniques to hide command and control traffic to make detection efforts
  more difficult. Steganographic techniques can be used to hide data in digital messages that are transferred between systems.
  This hidden information can be used for command and control of compromised systems. In some cases, the passing of files
  embedded using steganography, such as image or document files, can be used for command and control. '
external_references:
- external_id: T1001.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1001/002
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
id: attack-pattern--eec23884-3fa1-4d8a-ac50-6f104d51e235
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:49:35.060Z'
name: Steganography
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
- ESXi
x_mitre_version: '1.1'
```
