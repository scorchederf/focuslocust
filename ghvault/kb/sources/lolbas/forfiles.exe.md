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

## Generated Concept Page

- [Forfiles.exe](../../tools/windows/forfiles.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | forfiles.exe |
| name | Forfiles.exe |
| type | tool |
| source | lolbas |
| url | https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@vector_sec'
  Person: Eric
- Handle: '@oddvarmoe'
  Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: forfiles /p c:\windows\system32 /m notepad.exe /c "{CMD}"
  Description: Executes specified command since there is a match for notepad.exe in the c:\windows\System32 folder.
  MitreID: T1202
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Use forfiles to start a new process to evade defensive counter measures
- Category: ADS
  Command: forfiles /p c:\windows\system32 /m notepad.exe /c "{PATH_ABSOLUTE}:evil.exe"
  Description: Executes the evil.exe Alternate Data Stream (AD) since there is a match for notepad.exe in the c:\windows\system32
    folder.
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Use forfiles to start a new process from a binary hidden in an alternate data stream
Created: 2018-05-25
Description: Selects and executes a command on a file or set of files. This command is useful for batch processing.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_forfiles.yml
Full_Path:
- Path: C:\Windows\System32\forfiles.exe
- Path: C:\Windows\SysWOW64\forfiles.exe
Name: Forfiles.exe
Resources:
- Link: https://twitter.com/vector_sec/status/896049052642533376
- Link: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
- Link: https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Forfiles.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_forfiles.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_forfiles.yml
```
