---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Wab.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wab.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wab.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows address book manager

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/wab.md)
- Source verification: [source record](../../sources/lolbas/wab.exe.md)

## Aliases

- `Wab.exe`
- `wab.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: wab.exe |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/wab.exe.md)

## Source Verification

[source record](../../sources/lolbas/wab.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@Hexacorn'
Person: Adam
Author: Oddvar Moe
Commands:
- Category: Execute
Command: wab.exe
Description: Change HKLM\Software\Microsoft\WAB\DLLPath and execute DLL of choice
```
