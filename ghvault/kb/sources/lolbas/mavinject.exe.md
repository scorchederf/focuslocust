---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Mavinject.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `mavinject.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mavinject.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Mavinject.exe](../../tools/windows/mavinject.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mavinject.exe |
| name | Mavinject.exe |
| type | tool |
| source | lolbas |
| url | https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@gN3mes1s'
  Person: Giuseppe N3mes1s
- Handle: '@oddvarmoe'
  Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: MavInject.exe 3110 /INJECTRUNNING {PATH_ABSOLUTE:.dll}
  Description: Inject evil.dll into a process with PID 3110.
  MitreID: T1218.013
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Inject dll file into running process
- Category: ADS
  Command: Mavinject.exe 4172 /INJECTRUNNING {PATH_ABSOLUTE}:file.dll
  Description: Inject file.dll stored as an Alternate Data Stream (ADS) into a process with PID 4172
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Inject dll file into running process
Created: 2018-05-25
Description: Used by App-v in Windows
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_mavinject_process_injection.yml
- IOC: mavinject.exe should not run unless APP-v is in use on the workstation
Full_Path:
- Path: C:\Windows\System32\mavinject.exe
- Path: C:\Windows\SysWOW64\mavinject.exe
Name: Mavinject.exe
Resources:
- Link: https://twitter.com/gN3mes1s/status/941315826107510784
- Link: https://twitter.com/Hexcorn/status/776122138063409152
- Link: https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mavinject.yml
```

## Detection / Analysis Notes

```text
IOC: mavinject.exe should not run unless APP-v is in use on the workstation
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_mavinject_process_injection.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_mavinject_process_injection.yml
- IOC: mavinject.exe should not run unless APP-v is in use on the workstation
```
