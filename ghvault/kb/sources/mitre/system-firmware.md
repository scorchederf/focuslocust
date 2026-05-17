---
parsed_by: focuslocust
source: mitre
type: generated
---
# System Firmware

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1542.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [System Firmware](../../attack/techniques/T1542.001-system-firmware.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1542.001 |
| name | System Firmware |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1542/001 |

## Preserved Source Material

```yaml
created: '2019-12-19T19:43:34.507Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may modify system firmware to persist on systems.The BIOS (Basic Input/Output System) and The Unified
  Extensible Firmware Interface (UEFI) or Extensible Firmware Interface (EFI) are examples of system firmware that operate
  as the software interface between the operating system and hardware of a computer.(Citation: Wikipedia BIOS)(Citation: Wikipedia
  UEFI)(Citation: About UEFI)


  System firmware like BIOS and (U)EFI underly the functionality of a computer and may be modified by an adversary to perform
  or assist in malicious activity. Capabilities exist to overwrite the system firmware, which may give sophisticated adversaries
  a means to install malicious firmware updates as a means of persistence on a system that may be difficult to detect.'
external_references:
- external_id: T1542.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1542/001
- description: UEFI Forum. (n.d.). About UEFI Forum. Retrieved January 5, 2016.
  source_name: About UEFI
  url: http://www.uefi.org/about
- description: Wikipedia. (2017, July 10). Unified Extensible Firmware Interface. Retrieved July 11, 2017.
  source_name: Wikipedia UEFI
  url: https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface
- description: Wikipedia. (n.d.). BIOS. Retrieved January 5, 2016.
  source_name: Wikipedia BIOS
  url: https://en.wikipedia.org/wiki/BIOS
id: attack-pattern--16ab6452-c3c1-497c-a47d-206018ca1ada
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2026-04-17T18:38:49.546Z'
name: System Firmware
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Jean-Ian Boutin, ESET
- McAfee
- Ryan Becwar
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Network Devices
- Windows
x_mitre_version: '2.0'
```
