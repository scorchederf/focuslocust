---
parsed_by: focuslocust
source: mitre
type: generated
---
# Pre-OS Boot

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1542` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Pre-OS Boot](../../attack/techniques/T1542-pre-os-boot.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1542 |
| name | Pre-OS Boot |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1542 |

## Preserved Source Material

```yaml
created: '2019-11-13T14:44:49.439Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse Pre-OS Boot mechanisms as a way to establish persistence on a system. During the booting
  process of a computer, firmware and various startup services are loaded before the operating system. These programs control
  flow of execution before the operating system takes control.(Citation: Wikipedia Booting)


  Adversaries may overwrite data in boot drivers or firmware such as BIOS (Basic Input/Output System) and The Unified Extensible
  Firmware Interface (UEFI) to persist on systems at a layer below the operating system. This can be particularly difficult
  to detect as malware at this level will not be detected by host software-based defenses.'
external_references:
- external_id: T1542
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1542
- description: Wikipedia. (n.d.). Booting. Retrieved November 13, 2019.
  source_name: Wikipedia Booting
  url: https://en.wikipedia.org/wiki/Booting
id: attack-pattern--7f0ca133-88c4-40c6-a62f-b3083a7fbc2e
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2026-04-17T18:38:50.048Z'
name: Pre-OS Boot
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '2.0'
```
