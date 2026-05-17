---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Powershell.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `powershell.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/HonorableMentions/PowerShell.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Powershell.exe is a a task-based command-line shell built on .NET.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/powershell.md)
- Source verification: [source record](../../sources/lolbas/powershell.exe.md)

## Aliases

- `Powershell.exe`
- `powershell.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1059.001 - PowerShell](../../attack/techniques/T1059.001-powershell.md) | explicit | source | Command metadata lists T1059.001: powershell.exe -ep bypass -ec IgBXAGUAIAA8ADMAIABMAE8ATABCAEEAUwAiAA== |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/powershell.exe.md)

## Source Verification

[source record](../../sources/lolbas/powershell.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@alltheoffensivecyberers'
Person: Everyone
Author: Everyone
Commands:
- Category: Execute
Command: powershell.exe -ep bypass -file c:\path\to\a\script.ps1
Description: Set the execution policy to bypass and execute a PowerShell script without warning
```
