---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Remote.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `remote.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Remote.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Remote.exe](../../tools/windows/remote.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | remote.exe |
| name | Remote.exe |
| type | tool |
| source | lolbas |
| url | https://blog.thecybersecuritytutor.com/Exeuction-AWL-Bypass-Remote-exe-LOLBin/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@mrd0x'
  Person: mr.d0x
Author: mr.d0x
Commands:
- Category: AWL Bypass
  Command: Remote.exe /s {PATH:.exe} anythinghere
  Description: Spawns specified executable as a child process of remote.exe
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Executes a process under a trusted Microsoft signed binary
- Category: Execute
  Command: Remote.exe /s {PATH:.exe} anythinghere
  Description: Spawns specified executable as a child process of remote.exe
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Executes a process under a trusted Microsoft signed binary
- Category: Execute
  Command: Remote.exe /s {PATH_SMB:.exe} anythinghere
  Description: Run a remote file
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: EXE
  - Execute: Remote
  Usecase: Executing a remote binary without saving file to disk
Created: 2021-06-01
Description: Debugging tool included with Windows Debugging Tools
Detection:
- IOC: remote.exe process spawns
- Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/process_creation/proc_creation_win_lolbin_remote.yml
Full_Path:
- Path: C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\remote.exe
- Path: C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\remote.exe
Name: Remote.exe
Resources:
- Link: https://blog.thecybersecuritytutor.com/Exeuction-AWL-Bypass-Remote-exe-LOLBin/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Remote.yml
```

## Detection / Analysis Notes

```text
IOC: remote.exe process spawns
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/process_creation/proc_creation_win_lolbin_remote.yml
```

```text
- IOC: remote.exe process spawns
- Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/process_creation/proc_creation_win_lolbin_remote.yml
```
