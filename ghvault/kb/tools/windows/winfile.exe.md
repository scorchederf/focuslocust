---
parsed_by: focuslocust
source: lolbas
type: generated
---
# winfile.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `winfile.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/winfile.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows File Manager executable

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/winfile.md)
- Source verification: [source record](../../sources/lolbas/winfile.exe.md)

## Aliases

- `winfile.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: winfile.exe {PATH:.exe} |

## Source Verification

[source record](../../sources/lolbas/winfile.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
Command: winfile.exe {PATH:.exe}
Description: Execute an executable file with WinFile as a parent process.
```
