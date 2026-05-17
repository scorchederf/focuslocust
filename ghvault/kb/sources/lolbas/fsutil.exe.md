---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Fsutil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `fsutil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Fsutil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Fsutil.exe](../../tools/windows/fsutil.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | fsutil.exe |
| name | Fsutil.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/0gtweet/status/1720724516324704404 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@elliotkillick'
  Person: Elliot Killick
- Handle: '@bohops'
  Person: Jimmy
- Handle: '@0gtweet'
  Person: Grzegorz Tworek
Author: Elliot Killick
Commands:
- Category: Tamper
  Command: fsutil.exe file setZeroData offset=0 length=9999999999 {PATH_ABSOLUTE}
  Description: Zero out a file
  MitreID: T1485
  OperatingSystem: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10
  Privileges: User
  Usecase: Can be used to forensically erase a file
- Category: Tamper
  Command: 'fsutil.exe usn deletejournal /d c:'
  Description: Delete the USN journal volume to hide file creation activity
  MitreID: T1485
  OperatingSystem: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10
  Privileges: User
  Usecase: Can be used to hide file creation activity
- Category: Execute
  Command: fsutil.exe trace decode
  Description: Executes a pre-planted binary named netsh.exe from the current directory.
  MitreID: T1218
  OperatingSystem: Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Spawn a pre-planted executable from fsutil.exe.
Created: 2021-08-16
Description: File System Utility
Detection:
- IOC: fsutil.exe should not be run on a normal workstation
- IOC: file setZeroData (not case-sensitive) in the process arguments
- IOC: Sysmon Event ID 1
- IOC: Execution of process fsutil.exe with trace decode could be suspicious
- IOC: Non-Windows netsh.exe execution
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_susp_fsutil_usage.yml
Full_Path:
- Path: C:\Windows\System32\fsutil.exe
- Path: C:\Windows\SysWOW64\fsutil.exe
Name: Fsutil.exe
Resources:
- Link: https://twitter.com/0gtweet/status/1720724516324704404
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Fsutil.yml
```

## Detection / Analysis Notes

```text
IOC: Execution of process fsutil.exe with trace decode could be suspicious
```

```text
IOC: Non-Windows netsh.exe execution
```

```text
IOC: Sysmon Event ID 1
```

```text
IOC: file setZeroData (not case-sensitive) in the process arguments
```

```text
IOC: fsutil.exe should not be run on a normal workstation
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_susp_fsutil_usage.yml
```

```text
- IOC: fsutil.exe should not be run on a normal workstation
- IOC: file setZeroData (not case-sensitive) in the process arguments
- IOC: Sysmon Event ID 1
- IOC: Execution of process fsutil.exe with trace decode could be suspicious
- IOC: Non-Windows netsh.exe execution
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_susp_fsutil_usage.yml
```
