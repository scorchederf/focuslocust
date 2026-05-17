---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Mmc.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `mmc.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mmc.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Load snap-ins to locally and remotely manage Windows systems

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/mmc.md)
- Source verification: [source record](../../sources/lolbas/mmc.exe.md)

## Aliases

- `Mmc.exe`
- `mmc.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.014 - MMC](../../attack/techniques/T1218.014-mmc.md) | explicit | source | Command metadata lists T1218.014: mmc.exe -Embedding {PATH_ABSOLUTE:.msc} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/mmc.exe.md)

## Source Verification

[source record](../../sources/lolbas/mmc.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@bohops'
Person: Jimmy
- Handle: '@clavoillotte'
Person: clem
- Person: Fredrik H. Brathen
Author: '@bohops'
Commands:
```
