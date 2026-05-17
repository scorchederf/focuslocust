---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Forfiles.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `forfiles.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Forfiles.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Selects and executes a command on a file or set of files. This command is useful for batch processing.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/forfiles.md)
- Source verification: [source record](../../sources/lolbas/forfiles.exe.md)

## Aliases

- `Forfiles.exe`
- `forfiles.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: forfiles /p c:\windows\system32 /m notepad.exe /c "{CMD}" |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: forfiles /p c:\windows\system32 /m notepad.exe /c "{PATH_ABSOLUTE}:evil.exe" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/forfiles.exe.md)

## Source Verification

[source record](../../sources/lolbas/forfiles.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@vector_sec'
Person: Eric
- Handle: '@oddvarmoe'
Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: Execute
```
