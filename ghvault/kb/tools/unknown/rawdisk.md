---
parsed_by: focuslocust
source: mitre
type: generated
---
# RawDisk

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0364` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

RawDisk is a legitimate commercial driver from the EldoS Corporation that is used for interacting with files, disks, and partitions. The driver allows for direct modification of data on a local computer's hard drive. In some cases, the tool can enact these raw disk modifications from user-mode processes, circumventing Windows operating system security features.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/rawdisk.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1485 - Data Destruction](../../attack/techniques/T1485-data-destruction.md) | explicit | source | [RawDisk](https://attack.mitre.org/software/S0364) was used in [Shamoon](https://attack.mitre.org/software/S0140) to write to protected system locations such as the MBR and disk partitions in an effort to destroy data.(Citation: Palo Alto Shamoon Nov 2016)(Citation: Unit 42 Shamoon3 2018) |
| [T1561.001 - Disk Content Wipe](../../attack/techniques/T1561.001-disk-content-wipe.md) | explicit | source | [RawDisk](https://attack.mitre.org/software/S0364) has been used to directly access the hard disk to help overwrite arbitrarily sized portions of disk content.(Citation: Novetta Blockbuster Destructive Malware) |
| [T1561.002 - Disk Structure Wipe](../../attack/techniques/T1561.002-disk-structure-wipe.md) | explicit | source | [RawDisk](https://attack.mitre.org/software/S0364) was used in [Shamoon](https://attack.mitre.org/software/S0140) to help overwrite components of disk structure like the MBR and disk partitions.(Citation: Palo Alto Shamoon Nov 2016)(Citation: Unit 42 Shamoon3 2018) |

## Source Verification

[source record](../../sources/mitre/rawdisk.md)

## Evidence Excerpt

```text
created: '2019-03-25T12:30:40.919Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[RawDisk](https://attack.mitre.org/software/S0364) is a legitimate commercial driver from the EldoS Corporation
that is used for interacting with files, disks, and partitions. The driver allows for direct modification of data on a local
computer''s hard drive. In some cases, the tool can enact these raw disk modifications from user-mode processes, circumventing
Windows operating system security features.(Citation: EldoS RawDisk ITpro)(Citation: Novetta Blockbuster Destructive Malware)'
external_references:
- external_id: S0364
```
