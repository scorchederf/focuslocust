---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Msbuild.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msbuild.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msbuild.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used to compile and execute code

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/msbuild.md)
- Source verification: [source record](../../sources/lolbas/msbuild.exe.md)

## Aliases

- `Msbuild.exe`
- `msbuild.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1036 - Masquerading](../../attack/techniques/T1036-masquerading.md) | explicit | source | Command metadata lists T1036: msbuild.exe @{PATH:.rsp} |
| [T1127.001 - MSBuild](../../attack/techniques/T1127.001-msbuild.md) | explicit | source | Command metadata lists T1127.001: msbuild.exe {PATH:.proj} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/msbuild.exe.md)

## Source Verification

[source record](../../sources/lolbas/msbuild.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
- Handle: '@Cneelis'
Person: Cn33liz
- Handle: '@bohops'
Person: Jimmy
Author: Oddvar Moe
```
