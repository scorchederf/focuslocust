---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Vshadow.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `vshadow.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Vshadow.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Vshadow.exe](../../tools/windows/vshadow.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | vshadow.exe |
| name | Vshadow.exe |
| type | tool |
| source | lolbas |
| url | https://learn.microsoft.com/en-us/windows/win32/vss/vshadow-tool-and-sample |

## Preserved Source Material

```yaml
Acknowledgement:
- Person: Ayberk Halaç
Author: Ayberk Halaç
Commands:
- Category: Execute
  Command: 'vshadow.exe -nw -exec={PATH_ABSOLUTE:.exe} C:'
  Description: Executes specified executable from vshadow.exe.
  MitreID: T1202
  OperatingSystem: Windows 10, Windows 11
  Privileges: Administrator
  Tags:
  - Execute: EXE
  Usecase: Performs execution of specified executable file.
Created: 2023-09-06
Description: VShadow is a command-line tool that can be used to create and manage volume shadow copies.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_vshadow_exec.yml
- IOC: vshadow.exe usage with -exec parameter
Full_Path:
- Path: C:\Program Files (x86)\Windows Kits\10\bin\<version>\x64\vshadow.exe
Name: Vshadow.exe
Resources:
- Link: https://learn.microsoft.com/en-us/windows/win32/vss/vshadow-tool-and-sample
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Vshadow.yml
```

## Detection / Analysis Notes

```text
IOC: vshadow.exe usage with -exec parameter
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_vshadow_exec.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_vshadow_exec.yml
- IOC: vshadow.exe usage with -exec parameter
```
