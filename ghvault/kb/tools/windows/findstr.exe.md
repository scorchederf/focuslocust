---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Findstr.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `findstr.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Findstr.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Write to ADS, discover, or download files with Findstr.exe

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/findstr.md)
- Source verification: [source record](../../sources/lolbas/findstr.exe.md)

## Aliases

- `Findstr.exe`
- `findstr.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: findstr /V /L W3AllLov3LolBas {PATH_SMB:.exe} > {PATH_ABSOLUTE:.exe} |
| [T1552.001 - Credentials In Files](../../attack/techniques/T1552.001-credentials-in-files.md) | explicit | source | Command metadata lists T1552.001: findstr /S /I cpassword \\sysvol\policies\*.xml |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: findstr /V /L W3AllLov3LolBas {PATH_SMB:.exe} > {PATH_ABSOLUTE}:file.exe |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/findstr.exe.md)

## Source Verification

[source record](../../sources/lolbas/findstr.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@oddvarmoe'
Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: ADS
Command: findstr /V /L W3AllLov3LolBas {PATH_ABSOLUTE:.exe} > {PATH_ABSOLUTE}:file.exe
Description: Searches for the string W3AllLov3LolBas, since it does not exist (/V) the specified .exe file is written to
```
