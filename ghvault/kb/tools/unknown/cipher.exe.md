---
parsed_by: focuslocust
source: mitre
type: generated
---
# cipher.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S1205` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

cipher.exe is a native Microsoft utility that manages encryption of directories and files on NTFS (New Technology File System) partitions by using the Encrypting File System (EFS).

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/cipher.exe.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1561.001 - Disk Content Wipe](../../attack/techniques/T1561.001-disk-content-wipe.md) | explicit | source | [cipher.exe](https://attack.mitre.org/software/S1205) can be used to overwrite deleted data in specified folders.(Citation: Nearest Neighbor Volexity) |

## Source Verification

[source record](../../sources/mitre/cipher.exe.md)

## Evidence Excerpt

```text
created: '2025-02-25T17:31:00.202Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[cipher.exe](https://attack.mitre.org/software/S1205) is a native Microsoft utility that manages encryption
of directories and files on NTFS (New Technology File System) partitions by using the Encrypting File System (EFS).(Citation:
cipher.exe)'
external_references:
- external_id: S1205
source_name: mitre-attack
```
