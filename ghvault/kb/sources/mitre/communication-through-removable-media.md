---
parsed_by: focuslocust
source: mitre
type: generated
---
# Communication Through Removable Media

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1092` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Communication Through Removable Media](../../attack/techniques/T1092-communication-through-removable-media.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1092 |
| name | Communication Through Removable Media |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1092 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:09.379Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries can perform command and control between compromised hosts on potentially disconnected networks using
  removable media to transfer commands from system to system.(Citation: ESET Sednit USBStealer 2014) Both systems would need
  to be compromised, with the likelihood that an Internet-connected system was compromised first and the second through lateral
  movement by [Replication Through Removable Media](https://attack.mitre.org/techniques/T1091). Commands and files would be
  relayed from the disconnected system to the Internet-connected system to which the adversary has direct access.'
external_references:
- external_id: T1092
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1092
- description: Calvet, J. (2014, November 11). Sednit Espionage Group Attacking Air-Gapped Networks. Retrieved January 4,
    2017.
  source_name: ESET Sednit USBStealer 2014
  url: http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/
id: attack-pattern--64196062-5210-42c3-9a02-563a0d1797ef
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:48:52.106Z'
name: Communication Through Removable Media
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
x_mitre_version: '1.0'
```
