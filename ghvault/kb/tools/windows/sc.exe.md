---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Sc.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `sc.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Sc.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used by Windows to manage services

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/sc.md)
- Source verification: [source record](../../sources/lolbas/sc.exe.md)

## Aliases

- `Sc.exe`
- `sc.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: sc config {ExistingServiceName} binPath="\"c:\\ADS\\file.txt:cmd.exe\" /c echo works > \"c:\ADS\works.txt\"" & sc start {ExistingServiceName} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/sc.exe.md)

## Source Verification

[source record](../../sources/lolbas/sc.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@oddvarmoe'
Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: ADS
Command: sc create evilservice binPath="\"c:\\ADS\\file.txt:cmd.exe\" /c echo works > \"c:\ADS\works.txt\"" DisplayName=
"evilservice" start= auto\ & sc start evilservice
```
