---
parsed_by: focuslocust
source: mitre
type: generated
---
# Data Obfuscation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Data Obfuscation](../../attack/techniques/T1001-data-obfuscation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1001 |
| name | Data Obfuscation |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1001 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:18.931Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may obfuscate command and control traffic to make it more difficult to detect.(Citation: Bitdefender
  FunnyDream Campaign November 2020) Command and control (C2) communications are hidden (but not necessarily encrypted) in
  an attempt to make the content more difficult to discover or decipher and to make the communication less conspicuous and
  hide commands from being seen. This encompasses many methods, such as adding junk data to protocol traffic, using steganography,
  or impersonating legitimate protocols. '
external_references:
- external_id: T1001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1001
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
- description: Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions.
    Retrieved September 19, 2022.
  source_name: Bitdefender FunnyDream Campaign November 2020
  url: https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf
id: attack-pattern--ad255bfe-a9e6-4b52-a258-8d3462abe842
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:49:13.380Z'
name: Data Obfuscation
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
- ESXi
- Linux
- macOS
- Windows
x_mitre_version: '1.2'
```
