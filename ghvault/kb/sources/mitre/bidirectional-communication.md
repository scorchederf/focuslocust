---
parsed_by: focuslocust
source: mitre
type: generated
---
# Bidirectional Communication

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1102.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Bidirectional Communication](../../attack/techniques/T1102.002-bidirectional-communication.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1102.002 |
| name | Bidirectional Communication |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1102/002 |

## Preserved Source Material

```yaml
created: '2020-03-14T22:34:03.024Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may use an existing, legitimate external Web service as a means for sending commands to and receiving\
  \ output from a compromised system over the Web service channel. Compromised systems may leverage popular websites and social\
  \ media to host command and control (C2) instructions. Those infected systems can then send the output from those commands\
  \ back over that Web service channel. The return traffic may occur in a variety of ways, depending on the Web service being\
  \ utilized. For example, the return traffic may take the form of the compromised system posting a comment on a forum, issuing\
  \ a pull request to development project, updating a document hosted on a Web service, or by sending a Tweet. \n\nPopular\
  \ websites and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that\
  \ hosts within a network are already communicating with them prior to a compromise. Using common services, such as those\
  \ offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly\
  \ use SSL/TLS encryption, giving adversaries an added level of protection. "
external_references:
- external_id: T1102.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1102/002
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
id: attack-pattern--be055942-6e63-49d7-9fa1-9cb7d8a8f3f4
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:49:18.602Z'
name: Bidirectional Communication
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
