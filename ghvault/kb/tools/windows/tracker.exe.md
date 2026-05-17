---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Tracker.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `tracker.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Tracker.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Tool included with Microsoft .Net Framework.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/tracker.md)
- Source verification: [source record](../../sources/lolbas/tracker.exe.md)

## Aliases

- `Tracker.exe`
- `tracker.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: Tracker.exe /d {PATH:.dll} /c C:\Windows\write.exe |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/tracker.exe.md)

## Source Verification

[source record](../../sources/lolbas/tracker.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subTee'
Person: Casey Smith
Author: Oddvar Moe
Commands:
- Category: Execute
Command: Tracker.exe /d {PATH:.dll} /c C:\Windows\write.exe
Description: Use tracker.exe to proxy execution of an arbitrary DLL into another process. Since tracker.exe is also signed
```
