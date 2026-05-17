---
parsed_by: focuslocust
source: lolbas
type: generated
---
# At.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `at.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/At.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [At.exe](../../tools/windows/at.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | at.exe |
| name | At.exe |
| type | tool |
| source | lolbas |
| url | https://freddiebarrsmith.com/at.txt |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: null
  Person: Freddie Barr-Smith
- Handle: null
  Person: Riccardo Spolaor
- Handle: null
  Person: Mariano Graziano
- Handle: null
  Person: Xabier Ugarte-Pedrero
Author: Freddie Barr-Smith
Commands:
- Category: Execute
  Command: C:\Windows\System32\at.exe 09:00 /interactive /every:m,t,w,th,f,s,su {CMD}
  Description: Create a recurring task to execute every day at a specific time.
  MitreID: T1053.002
  OperatingSystem: Windows 7 or older
  Privileges: Local Admin
  Tags:
  - Execute: CMD
  Usecase: Create a recurring task, to eg. to keep reverse shell session(s) alive
Created: 2019-09-20
Description: Schedule periodic tasks
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_at_interactive_execution.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/network/zeek/zeek_smb_converted_win_atsvc_task.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/builtin/security/win_security_atsvc_task.yml
- IOC: C:\Windows\System32\Tasks\At1 (substitute 1 with subsequent number of at job)
- IOC: C:\Windows\Tasks\At1.job
- IOC: Registry Key - Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree\At1.
Full_Path:
- Path: C:\WINDOWS\System32\At.exe
- Path: C:\WINDOWS\SysWOW64\At.exe
Name: At.exe
Resources:
- Link: https://freddiebarrsmith.com/at.txt
- Link: https://sushant747.gitbooks.io/total-oscp-guide/privilege_escalation_windows.html
- Link: https://www.secureworks.com/blog/where-you-at-indicators-of-lateral-movement-using-at-exe-on-windows-7-systems
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/At.yml
```

## Detection / Analysis Notes

```text
IOC: C:\Windows\System32\Tasks\At1 (substitute 1 with subsequent number of at job)
```

```text
IOC: C:\Windows\Tasks\At1.job
```

```text
IOC: Registry Key - Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree\At1.
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/network/zeek/zeek_smb_converted_win_atsvc_task.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/builtin/security/win_security_atsvc_task.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_at_interactive_execution.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_at_interactive_execution.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/network/zeek/zeek_smb_converted_win_atsvc_task.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/builtin/security/win_security_atsvc_task.yml
- IOC: C:\Windows\System32\Tasks\At1 (substitute 1 with subsequent number of at job)
- IOC: C:\Windows\Tasks\At1.job
- IOC: Registry Key - Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree\At1.
```
