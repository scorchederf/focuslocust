---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ie4uinit.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ie4uinit.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ie4uinit.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Ie4uinit.exe](../../tools/windows/ie4uinit.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ie4uinit.exe |
| name | Ie4uinit.exe |
| type | tool |
| source | lolbas |
| url | https://bohops.com/2018/03/10/leveraging-inf-sct-fetch-execute-techniques-for-bypass-evasion-persistence-part-2/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@bohops'
  Person: Jimmy
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: ie4uinit.exe -BaseSettings
  Description: Executes commands from a specially prepared ie4uinit.inf file.
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: INF
  Usecase: Get code execution by copy files to another location
Created: 2018-05-25
Description: Executes commands from a specially prepared ie4uinit.inf file.
Detection:
- IOC: ie4uinit.exe copied outside of %windir%
- IOC: ie4uinit.exe loading an inf file (ieuinit.inf) from outside %windir%
- Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/process_creation/proc_creation_win_lolbin_ie4uinit.yml
Full_Path:
- Path: c:\windows\system32\ie4uinit.exe
- Path: c:\windows\sysWOW64\ie4uinit.exe
- Path: c:\windows\system32\ieuinit.inf
- Path: c:\windows\sysWOW64\ieuinit.inf
Name: Ie4uinit.exe
Resources:
- Link: https://bohops.com/2018/03/10/leveraging-inf-sct-fetch-execute-techniques-for-bypass-evasion-persistence-part-2/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ie4uinit.yml
```

## Detection / Analysis Notes

```text
IOC: ie4uinit.exe copied outside of %windir%
```

```text
IOC: ie4uinit.exe loading an inf file (ieuinit.inf) from outside %windir%
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/process_creation/proc_creation_win_lolbin_ie4uinit.yml
```

```text
- IOC: ie4uinit.exe copied outside of %windir%
- IOC: ie4uinit.exe loading an inf file (ieuinit.inf) from outside %windir%
- Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/process_creation/proc_creation_win_lolbin_ie4uinit.yml
```
