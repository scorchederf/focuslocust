---
parsed_by: focuslocust
source: lolbas
type: generated
---
# ntdsutil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ntdsutil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Ntdsutil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Command line utility used to export Active Directory.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/ntdsutil.md)
- Source verification: [source record](../../sources/lolbas/ntdsutil.exe.md)

## Aliases

- `ntdsutil.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.003 - NTDS](../../attack/techniques/T1003.003-ntds.md) | explicit | source | Command metadata lists T1003.003: ntdsutil.exe "ac i ntds" "ifm" "create full c:\" q q |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/ntdsutil.exe.md)

## Source Verification

[source record](../../sources/lolbas/ntdsutil.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@PyroTek3'
Person: Sean Metcalf
Author: Tony Lambert
Commands:
- Category: Dump
Command: ntdsutil.exe "ac i ntds" "ifm" "create full c:\" q q
Description: Dump NTDS.dit into folder
```
