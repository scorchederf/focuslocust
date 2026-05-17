---
parsed_by: focuslocust
source: mitre
type: generated
---
# Junk Data

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1001.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Junk Data](../../attack/techniques/T1001.001-junk-data.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1001.001 |
| name | Junk Data |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1001/001 |

## Preserved Source Material

```yaml
created: '2020-03-15T00:30:25.444Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may add junk data to protocols used for command and control to make detection more difficult.(Citation:
  FireEye SUNBURST Backdoor December 2020) By adding random or meaningless data to the protocols used for command and control,
  adversaries can prevent trivial methods for decoding, deciphering, or otherwise analyzing the traffic. Examples may include
  appending/prepending data with junk characters or writing junk characters between significant characters. '
external_references:
- external_id: T1001.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1001/001
- description: FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple
    Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.
  source_name: FireEye SUNBURST Backdoor December 2020
  url: https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
id: attack-pattern--f7c0689c-4dbd-489b-81be-7cb7c7079ade
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:49:38.011Z'
name: Junk Data
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
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
x_mitre_version: '1.1'
```
