---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Scriptrunner.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `scriptrunner.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Scriptrunner.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Execute binary through proxy binary to evade defensive counter measures

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/scriptrunner.md)
- Source verification: [source record](../../sources/lolbas/scriptrunner.exe.md)

## Aliases

- `Scriptrunner.exe`
- `scriptrunner.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: Scriptrunner.exe -appvscript {PATH:.exe} |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: ScriptRunner.exe -appvscript {PATH_SMB:.cmd} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/scriptrunner.exe.md)

## Source Verification

[source record](../../sources/lolbas/scriptrunner.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@nicktyrer'
Person: Nick Tyrer
Author: Oddvar Moe
Commands:
- Category: Execute
Command: Scriptrunner.exe -appvscript {PATH:.exe}
Description: Executes executable
```
