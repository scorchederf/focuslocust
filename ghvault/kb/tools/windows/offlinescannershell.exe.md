---
parsed_by: focuslocust
source: lolbas
type: generated
---
# OfflineScannerShell.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `offlinescannershell.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/OfflineScannerShell.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Defender Offline Shell

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/offlinescannershell.md)
- Source verification: [source record](../../sources/lolbas/offlinescannershell.exe.md)

## Aliases

- `OfflineScannerShell.exe`
- `offlinescannershell.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: OfflineScannerShell |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/offlinescannershell.exe.md)

## Source Verification

[source record](../../sources/lolbas/offlinescannershell.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@elliotkillick'
Person: Elliot Killick
Author: Elliot Killick
Commands:
- Category: Execute
Command: OfflineScannerShell
Description: Execute mpclient.dll library in the current working directory
```
