---
parsed_by: focuslocust
source: lolbas
type: generated
---
# SQLToolsPS.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `sqltoolsps.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Sqltoolsps.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Tool included with Microsoft SQL that loads SQL Server cmdlts. A replacement for sqlps.exe. Successor to sqlps.exe in SQL Server 2016+.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/sqltoolsps.md)
- Source verification: [source record](../../sources/lolbas/sqltoolsps.exe.md)

## Aliases

- `SQLToolsPS.exe`
- `sqltoolsps.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: SQLToolsPS.exe -noprofile -command Start-Process {PATH:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/sqltoolsps.exe.md)

## Source Verification

[source record](../../sources/lolbas/sqltoolsps.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@pabraeken'
Person: Pierre-Alexandre Braeken
Author: Oddvar Moe
Commands:
- Category: Execute
Command: SQLToolsPS.exe -noprofile -command Start-Process {PATH:.exe}
Description: Run a SQL Server PowerShell mini-console without Module and ScriptBlock Logging.
```
