---
parsed_by: focuslocust
source: lolbas
type: generated
---
# wbemtest.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wbemtest.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wbemtest.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

WMI/WBEM Test Binary

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/wbemtest.md)
- Source verification: [source record](../../sources/lolbas/wbemtest.exe.md)

## Aliases

- `wbemtest.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1047 - Windows Management Instrumentation](../../attack/techniques/T1047-windows-management-instrumentation.md) | explicit | source | Command metadata lists T1047: wbemtest.exe |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/wbemtest.exe.md)

## Source Verification

[source record](../../sources/lolbas/wbemtest.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@saulpanders'
Person: Paul Sanders
Author: saulpanders
Commands:
- Category: Execute
Command: wbemtest.exe
Description: Execute arbitary commands through WMI through a GUI managment interface for Web Based Enterprise Management
```
