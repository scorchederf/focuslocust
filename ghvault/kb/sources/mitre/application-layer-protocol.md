---
parsed_by: focuslocust
source: mitre
type: generated
---
# Application Layer Protocol

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1071` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Application Layer Protocol](../../attack/techniques/T1071-application-layer-protocol.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1071 |
| name | Application Layer Protocol |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1071 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:56.776Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may communicate using OSI application layer protocols to avoid detection/network filtering by blending\
  \ in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within\
  \ the protocol traffic between the client and server. \n\nAdversaries may utilize many different protocols, including those\
  \ used for web browsing, transferring files, electronic mail, DNS, or publishing/subscribing. For connections that occur\
  \ internally within an enclave (such as those between a proxy or pivot node and other nodes), commonly used protocols are\
  \ SMB, SSH, or RDP.(Citation: Mandiant APT29 Eye Spy Email Nov 22) "
external_references:
- external_id: T1071
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1071
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
- description: 'Mandiant. (2022, May 2). UNC3524: Eye Spy on Your Email. Retrieved August 17, 2023.'
  source_name: Mandiant APT29 Eye Spy Email Nov 22
  url: https://www.mandiant.com/resources/blog/unc3524-eye-spy-email
id: attack-pattern--355be19c-ffc9-46d5-8d50-d6a036c675b6
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:48:38.368Z'
name: Application Layer Protocol
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Duane Michael
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
- Network Devices
- ESXi
x_mitre_version: '2.4'
```
