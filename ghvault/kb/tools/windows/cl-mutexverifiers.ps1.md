---
parsed_by: focuslocust
source: lolbas
type: generated
---
# CL_Mutexverifiers.ps1

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cl-mutexverifiers.ps1` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/CL_mutexverifiers.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Proxy execution with CL_Mutexverifiers.ps1

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/cl-mutexverifiers.ps1.md)
- Source verification: [source record](../../sources/lolbas/cl-mutexverifiers.ps1.md)

## Aliases

- `CL_Mutexverifiers.ps1`
- `cl-mutexverifiers.ps1`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1216 - System Script Proxy Execution](../../attack/techniques/T1216-system-script-proxy-execution.md) | explicit | source | Command metadata lists T1216: . C:\Windows\diagnostics\system\AERO\CL_Mutexverifiers.ps1 \nrunAfterCancelProcess {PATH:.ps1} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/cl-mutexverifiers.ps1.md)

## Source Verification

[source record](../../sources/lolbas/cl-mutexverifiers.ps1.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@pabraeken'
Person: Pierre-Alexandre Braeken
Author: Oddvar Moe
Commands:
- Category: Execute
Command: . C:\Windows\diagnostics\system\AERO\CL_Mutexverifiers.ps1   \nrunAfterCancelProcess {PATH:.ps1}
Description: Import the PowerShell Diagnostic CL_Mutexverifiers script and call runAfterCancelProcess to launch an executable.
```
