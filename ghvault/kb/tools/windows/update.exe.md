---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Update.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `update.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Update.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary to update the existing installed Nuget/squirrel package. Part of Microsoft Teams installation.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/update.md)
- Source verification: [source record](../../sources/lolbas/update.exe.md)

## Aliases

- `Update.exe`
- `update.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1070 - Indicator Removal](../../attack/techniques/T1070-indicator-removal.md) | explicit | source | Command metadata lists T1070: Update.exe --removeShortcut={PATH:.exe}-l=Startup |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: Update.exe --processStart {PATH:.exe} --process-start-args "{CMD:args}" |
| [T1547 - Boot or Logon Autostart Execution](../../attack/techniques/T1547-boot-or-logon-autostart-execution.md) | explicit | source | Command metadata lists T1547: Update.exe --createShortcut={PATH:.exe} -l=Startup |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/update.exe.md)

## Source Verification

[source record](../../sources/lolbas/update.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@reegun21'
Person: Reegun Richard Jayapaul (SpiderLabs, Trustwave)
- Handle: '@MrUn1k0d3r'
Person: Mr.Un1k0d3r
- Handle: '@Hexacorn'
Person: Adam
- Person: Jesus Galvez
```
