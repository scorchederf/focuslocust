---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Rundll32.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `rundll32.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rundll32.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used by Windows to execute dll files

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/rundll32.md)
- Source verification: [source record](../../sources/lolbas/rundll32.exe.md)

## Aliases

- `Rundll32.exe`
- `rundll32.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.011 - Rundll32](../../attack/techniques/T1218.011-rundll32.md) | explicit | source | Command metadata lists T1218.011: rundll32.exe -sta {CLSID} |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: rundll32 "{PATH}:ADSDLL.dll",DllMain |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/rundll32.exe.md)

## Source Verification

[source record](../../sources/lolbas/rundll32.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
- Handle: '@oddvarmoe'
Person: Oddvar Moe
- Handle: '@bohops'
Person: Jimmy
- Handle: '@404death'
```
