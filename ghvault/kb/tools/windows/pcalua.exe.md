---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pcalua.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pcalua.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pcalua.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Program Compatibility Assistant

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/pcalua.md)
- Source verification: [source record](../../sources/lolbas/pcalua.exe.md)

## Aliases

- `Pcalua.exe`
- `pcalua.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: pcalua.exe -a {PATH_ABSOLUTE:.cpl} -c Java |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/pcalua.exe.md)

## Source Verification

[source record](../../sources/lolbas/pcalua.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@kylehanslovan'
Person: Kyle Hanslovan
- Handle: '@0rbz_'
Person: Fab
Author: Oddvar Moe
Commands:
- Category: Execute
```
