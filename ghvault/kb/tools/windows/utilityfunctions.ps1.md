---
parsed_by: focuslocust
source: lolbas
type: generated
---
# UtilityFunctions.ps1

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `utilityfunctions.ps1` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/UtilityFunctions.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

PowerShell Diagnostic Script

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/utilityfunctions.ps1.md)
- Source verification: [source record](../../sources/lolbas/utilityfunctions.ps1.md)

## Aliases

- `UtilityFunctions.ps1`
- `utilityfunctions.ps1`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1216 - System Script Proxy Execution](../../attack/techniques/T1216-system-script-proxy-execution.md) | explicit | source | Command metadata lists T1216: powershell.exe -ep bypass -command "set-location -path c:\windows\diagnostics\system\networking; import-module .\UtilityFunctions.ps1; RegSnapin ..\..\..\..\temp\unsigned.dll;[P... |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/utilityfunctions.ps1.md)

## Source Verification

[source record](../../sources/lolbas/utilityfunctions.ps1.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@nickvangilder'
Person: Nick VanGilder
Author: Jimmy (@bohops)
Commands:
- Category: Execute
Command: powershell.exe -ep bypass -command "set-location -path c:\windows\diagnostics\system\networking; import-module
.\UtilityFunctions.ps1; RegSnapin ..\..\..\..\temp\unsigned.dll;[Program.Class]::Main()"
```
