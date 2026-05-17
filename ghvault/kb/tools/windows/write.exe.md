---
parsed_by: focuslocust
source: lolbas
type: generated
---
# write.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `write.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/write.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Write

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/write.md)
- Source verification: [source record](../../sources/lolbas/write.exe.md)

## Aliases

- `write.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: write.exe |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/write.exe.md)

## Source Verification

[source record](../../sources/lolbas/write.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Person: Michal Belzak
Author: Michal Belzak
Commands:
- Category: Execute
Command: write.exe
Description: Executes a binary provided in default value of `HKCU\Software\Microsoft\Windows\CurrentVersion\App Paths\wordpad.exe`.
MitreID: T1218
```
