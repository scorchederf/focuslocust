---
parsed_by: focuslocust
source: mitre
type: generated
---
# Web Protocols

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1071.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Web Protocols](../../attack/techniques/T1071.001-web-protocols.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1071.001 |
| name | Web Protocols |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1071/001 |

## Preserved Source Material

```yaml
created: '2020-03-15T16:13:46.151Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may communicate using application layer protocols associated with web traffic to avoid detection/network\
  \ filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands,\
  \ will be embedded within the protocol traffic between the client and server. \n\nProtocols such as HTTP/S(Citation: CrowdStrike\
  \ Putter Panda) and WebSocket(Citation: Brazking-Websockets) that carry web traffic may be very common in environments.\
  \ HTTP/S packets have many fields and headers in which data can be concealed. An adversary may abuse these protocols to\
  \ communicate with systems under their control within a victim network while also mimicking normal, expected traffic. "
external_references:
- external_id: T1071.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1071/001
- description: 'Crowdstrike Global Intelligence Team. (2014, June 9). CrowdStrike Intelligence Report: Putter Panda. Retrieved
    January 22, 2016.'
  source_name: CrowdStrike Putter Panda
  url: http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
- description: Shahar Tavor. (n.d.). BrazKing Android Malware Upgraded and Targeting Brazilian Banks. Retrieved March 24,
    2023.
  source_name: Brazking-Websockets
  url: https://securityintelligence.com/posts/brazking-android-malware-upgraded-targeting-brazilian-banks/
id: attack-pattern--df8b2a25-8bdf-4856-953c-a04372b1c161
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:49:29.591Z'
name: Web Protocols
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- TruKno
- Don Le, Stifel Financial
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.5'
```
