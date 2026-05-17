---
parsed_by: focuslocust
source: mitre
type: generated
---
# One-Way Communication

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1102.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [One-Way Communication](../../attack/techniques/T1102.003-one-way-communication.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1102.003 |
| name | One-Way Communication |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1102/003 |

## Preserved Source Material

```yaml
created: '2020-03-14T22:45:52.963Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use an existing, legitimate external Web service as a means for sending commands to a compromised
  system without receiving return output over the Web service channel. Compromised systems may leverage popular websites and
  social media to host command and control (C2) instructions. Those infected systems may opt to send the output from those
  commands back over a different C2 channel, including to another distinct Web service. Alternatively, compromised systems
  may return no output at all in cases where adversaries want to send instructions to systems and do not want a response.


  Popular websites and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood
  that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those
  offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly
  use SSL/TLS encryption, giving adversaries an added level of protection.'
external_references:
- external_id: T1102.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1102/003
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
id: attack-pattern--9c99724c-a483-4d60-ad9d-7f004e42e8e8
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:49:08.849Z'
name: One-Way Communication
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
