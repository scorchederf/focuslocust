---
parsed_by: focuslocust
source: mitre
type: generated
---
# Peripheral Device Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1120` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Peripheral Device Discovery](../../attack/techniques/T1120-peripheral-device-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1120 |
| name | Peripheral Device Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1120 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:28.471Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to gather information about attached peripheral devices and components connected to
  a computer system.(Citation: Peripheral Discovery Linux)(Citation: Peripheral Discovery macOS) Peripheral devices could
  include auxiliary resources that support a variety of functionalities such as keyboards, printers, cameras, smart card readers,
  or removable storage. The information may be used to enhance their awareness of the system and network environment or may
  be used for further actions.'
external_references:
- external_id: T1120
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1120
- description: Shahriar Shovon. (2018, March). List USB Devices Linux. Retrieved March 11, 2022.
  source_name: Peripheral Discovery Linux
  url: https://linuxhint.com/list-usb-devices-linux/
- description: SS64. (n.d.). system_profiler. Retrieved March 11, 2022.
  source_name: Peripheral Discovery macOS
  url: https://ss64.com/osx/system_profiler.html
id: attack-pattern--348f1eef-964b-4eb6-bb53-69b3dcb0c643
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:48:37.563Z'
name: Peripheral Device Discovery
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
x_mitre_version: '1.4'
```
