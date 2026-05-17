---
parsed_by: focuslocust
source: lolbas
type: generated
---
# At.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `at.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/At.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Schedule periodic tasks

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/at.md)
- Source verification: [source record](../../sources/lolbas/at.exe.md)

## Aliases

- `At.exe`
- `at.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1053.002 - At](../../attack/techniques/T1053.002-at.md) | explicit | source | Command metadata lists T1053.002: C:\Windows\System32\at.exe 09:00 /interactive /every:m,t,w,th,f,s,su {CMD} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/at.exe.md)

## Source Verification

[source record](../../sources/lolbas/at.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: null
Person: Freddie Barr-Smith
- Handle: null
Person: Riccardo Spolaor
- Handle: null
Person: Mariano Graziano
- Handle: null
```
