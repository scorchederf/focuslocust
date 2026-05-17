---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Conhost.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `conhost.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Conhost.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Conhost.exe](../../tools/windows/conhost.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | conhost.exe |
| name | Conhost.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/Wietze/status/1511397781159751680 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@hexacorn'
  Person: Adam
- Handle: '@wietze'
  Person: Wietze
Author: Wietze Beukema
Commands:
- Category: Execute
  Command: conhost.exe {CMD}
  Description: Execute a command line with conhost.exe as parent process
  MitreID: T1202
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Use conhost.exe as a proxy binary to evade defensive counter-measures
- Category: Execute
  Command: conhost.exe --headless {CMD}
  Description: Execute a command line with conhost.exe as parent process
  MitreID: T1202
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Specify --headless parameter to hide child process window (if applicable)
Created: 2022-04-05
Description: Console Window host
Detection:
- IOC: conhost.exe spawning unexpected processes
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_conhost_susp_child_process.yml
Full_Path:
- Path: c:\windows\system32\conhost.exe
Name: Conhost.exe
Resources:
- Link: https://www.hexacorn.com/blog/2020/05/25/how-to-con-your-host/
- Link: https://twitter.com/Wietze/status/1511397781159751680
- Link: https://twitter.com/embee_research/status/1559410767564181504
- Link: https://twitter.com/ankit_anubhav/status/1561683123816972288
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Conhost.yml
```

## Detection / Analysis Notes

```text
IOC: conhost.exe spawning unexpected processes
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_conhost_susp_child_process.yml
```

```text
- IOC: conhost.exe spawning unexpected processes
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_conhost_susp_child_process.yml
```
