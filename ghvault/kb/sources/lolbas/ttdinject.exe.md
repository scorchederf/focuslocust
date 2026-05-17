---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ttdinject.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ttdinject.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ttdinject.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Ttdinject.exe](../../tools/windows/ttdinject.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ttdinject.exe |
| name | Ttdinject.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/Oddvarmoe/status/1196333160470138880 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@oddvarmoe'
  Person: Oddvar Moe
- Handle: '@m_nad0'
  Person: Maxime Nadeau
Author: Maxime Nadeau
Commands:
- Category: Execute
  Command: TTDInject.exe /ClientParams "7 tmp.run 0 0 0 0 0 0 0 0 0 0" /Launch "{PATH:.exe}"
  Description: Execute a program using ttdinject.exe. Requires administrator privileges. A log file will be created in tmp.run.
    The log file can be changed, but the length (7) has to be updated.
  MitreID: T1127
  OperatingSystem: Windows 10 2004 and above, Windows 11
  Privileges: Administrator
  Tags:
  - Execute: EXE
  Usecase: Spawn process using other binary
- Category: Execute
  Command: ttdinject.exe /ClientScenario TTDRecorder /ddload 0 /ClientParams "7 tmp.run 0 0 0 0 0 0 0 0 0 0" /launch "{PATH:.exe}"
  Description: Execute a program using ttdinject.exe. Requires administrator privileges. A log file will be created in tmp.run.
    The log file can be changed, but the length (7) has to be updated.
  MitreID: T1127
  OperatingSystem: Windows 10 1909 and below
  Privileges: Administrator
  Tags:
  - Execute: EXE
  Usecase: Spawn process using other binary
Created: 2020-05-12
Description: Used by Windows 1809 and newer to Debug Time Travel (Underlying call of tttracer.exe)
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/create_remote_thread/create_remote_thread_win_ttdinjec.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/7ea6ed3db65e0bd812b051d9bb4fffd27c4c4d0a/rules/windows/process_creation/proc_creation_win_lolbin_ttdinject.yml
- IOC: Parent child relationship. Ttdinject.exe parent for executed command
- IOC: Multiple queries made to the IFEO registry key of an untrusted executable (Ex. "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image
    File Execution Options\payload.exe") from the ttdinject.exe process
Full_Path:
- Path: C:\Windows\System32\ttdinject.exe
- Path: C:\Windows\Syswow64\ttdinject.exe
Name: Ttdinject.exe
Resources:
- Link: https://twitter.com/Oddvarmoe/status/1196333160470138880
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ttdinject.yml
```

## Detection / Analysis Notes

```text
IOC: Multiple queries made to the IFEO registry key of an untrusted executable (Ex. "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\payload.exe") from the ttdinject.exe process
```

```text
IOC: Parent child relationship. Ttdinject.exe parent for executed command
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/create_remote_thread/create_remote_thread_win_ttdinjec.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/7ea6ed3db65e0bd812b051d9bb4fffd27c4c4d0a/rules/windows/process_creation/proc_creation_win_lolbin_ttdinject.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/create_remote_thread/create_remote_thread_win_ttdinjec.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/7ea6ed3db65e0bd812b051d9bb4fffd27c4c4d0a/rules/windows/process_creation/proc_creation_win_lolbin_ttdinject.yml
- IOC: Parent child relationship. Ttdinject.exe parent for executed command
- IOC: Multiple queries made to the IFEO registry key of an untrusted executable (Ex. "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image
    File Execution Options\payload.exe") from the ttdinject.exe process
```
