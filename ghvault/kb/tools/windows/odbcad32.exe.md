---
parsed_by: focuslocust
source: lolbas
type: generated
---
# odbcad32.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `odbcad32.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/odbcad32.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

ODBC Data Source Administrator to manage User/System DSNs and ODBC drivers.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/odbcad32.md)
- Source verification: [source record](../../sources/lolbas/odbcad32.exe.md)

## Aliases

- `odbcad32.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | Command metadata lists T1548.002: odbcad32.exe |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/odbcad32.exe.md)

## Source Verification

[source record](../../sources/lolbas/odbcad32.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Person: amonitoring
- Handle: '@eki_erk'
Person: Ekitji
Author: Ekitji
Commands:
- Category: UAC Bypass
Command: odbcad32.exe
```
