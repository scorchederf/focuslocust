---
parsed_by: focuslocust
source: lolbas
type: generated
---
# SettingSyncHost.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `settingsynchost.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/SettingSyncHost.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Host Process for Setting Synchronization

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/settingsynchost.md)
- Source verification: [source record](../../sources/lolbas/settingsynchost.exe.md)

## Aliases

- `SettingSyncHost.exe`
- `settingsynchost.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: SettingSyncHost -LoadAndRunDiagScriptNoCab {PATH:.bat} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/settingsynchost.exe.md)

## Source Verification

[source record](../../sources/lolbas/settingsynchost.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@hexacorn'
Person: Adam
- Handle: '@elliotkillick'
Person: Elliot Killick
Author: Elliot Killick
Commands:
- Category: Execute
```
