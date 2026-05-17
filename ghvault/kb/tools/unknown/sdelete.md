---
parsed_by: focuslocust
source: mitre
type: generated
---
# SDelete

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0195` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

SDelete is an application that securely deletes data in a way that makes it unrecoverable. It is part of the Microsoft Sysinternals suite of tools.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/sdelete.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1070.004 - File Deletion](../../attack/techniques/T1070.004-file-deletion.md) | explicit | source | [SDelete](https://attack.mitre.org/software/S0195) deletes data in a way that makes it unrecoverable.(Citation: Microsoft SDelete July 2016) |
| [T1485 - Data Destruction](../../attack/techniques/T1485-data-destruction.md) | explicit | source | [SDelete](https://attack.mitre.org/software/S0195) deletes data in a way that makes it unrecoverable.(Citation: Microsoft SDelete July 2016) |

## Source Verification

[source record](../../sources/mitre/sdelete.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[SDelete](https://attack.mitre.org/software/S0195) is an application that securely deletes data in a way that
makes it unrecoverable. It is part of the Microsoft Sysinternals suite of tools. (Citation: Microsoft SDelete July 2016)'
external_references:
- external_id: S0195
source_name: mitre-attack
url: https://attack.mitre.org/software/S0195
```
