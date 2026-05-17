---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1542 - Pre-OS Boot

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

## Summary

Adversaries may abuse Pre-OS Boot mechanisms as a way to establish persistence on a system. During the booting process of a computer, firmware and various startup services are loaded before the operating system. These programs control flow of execution before the operating system takes control.

Adversaries may overwrite data in boot drivers or firmware such as BIOS (Basic Input/Output System) and The Unified Extensible Firmware Interface (UEFI) to persist on systems at a layer below the operating system. This can be particularly difficult to detect as malware at this level will not be detected by host software-based defenses.

## Source Verification

[source record](../../sources/mitre/pre-os-boot.md)

## Evidence Excerpt

```text
created: '2019-11-13T14:44:49.439Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse Pre-OS Boot mechanisms as a way to establish persistence on a system. During the booting
process of a computer, firmware and various startup services are loaded before the operating system. These programs control
flow of execution before the operating system takes control.(Citation: Wikipedia Booting)
Adversaries may overwrite data in boot drivers or firmware such as BIOS (Basic Input/Output System) and The Unified Extensible
Firmware Interface (UEFI) to persist on systems at a layer below the operating system. This can be particularly difficult
to detect as malware at this level will not be detected by host software-based defenses.'
```
