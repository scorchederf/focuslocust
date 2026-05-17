---
parsed_by: focuslocust
source: mitre
type: generated
---
# esentutl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0404` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

esentutl is a command-line tool that provides database utilities for the Windows Extensible Storage Engine.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/esentutl.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.003 - NTDS](../../attack/techniques/T1003.003-ntds.md) | explicit | source | [esentutl](https://attack.mitre.org/software/S0404) can copy `ntds.dit` using the Volume Shadow Copy service.(Citation: LOLBAS Esentutl)(Citation: Cary Esentutl) |
| [T1005 - Data from Local System](../../attack/techniques/T1005-data-from-local-system.md) | explicit | source | [esentutl](https://attack.mitre.org/software/S0404) can be used to collect data from local file systems.(Citation: Red Canary 2021 Threat Detection Report March 2021) |
| [T1006 - Direct Volume Access](../../attack/techniques/T1006-direct-volume-access.md) | explicit | source | [esentutl](https://attack.mitre.org/software/S0404) can use the Volume Shadow Copy service to copy locked files such as `ntds.dit`.(Citation: LOLBAS Esentutl)(Citation: Cary Esentutl) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [esentutl](https://attack.mitre.org/software/S0404) can be used to copy files from a given URL.(Citation: LOLBAS Esentutl) |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | [esentutl](https://attack.mitre.org/software/S0404) can be used to read and write alternate data streams.(Citation: LOLBAS Esentutl) |
| [T1570 - Lateral Tool Transfer](../../attack/techniques/T1570-lateral-tool-transfer.md) | explicit | source | [esentutl](https://attack.mitre.org/software/S0404) can be used to copy files to/from a remote share.(Citation: LOLBAS Esentutl) |

## Source Verification

[source record](../../sources/mitre/esentutl.md)

## Evidence Excerpt

```text
created: '2019-09-03T18:25:36.963Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[esentutl](https://attack.mitre.org/software/S0404) is a command-line tool that provides database utilities
for the Windows Extensible Storage Engine.(Citation: Microsoft Esentutl)'
external_references:
- external_id: S0404
source_name: mitre-attack
url: https://attack.mitre.org/software/S0404
```
