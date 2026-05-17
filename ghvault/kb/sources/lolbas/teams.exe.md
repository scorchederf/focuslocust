---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Teams.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `teams.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Teams.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Teams.exe](../../tools/windows/teams.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | teams.exe |
| name | Teams.exe |
| type | tool |
| source | lolbas |
| url | https://l--k.uk/2022/01/16/microsoft-teams-and-other-electron-apps-as-lolbins/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Person: Andrew Kisliakov
- Handle: '@mrd0x'
  Person: mr.d0x
Author: Andrew Kisliakov
Code_Sample:
- Code: https://github.com/lltltk/LOLBAS-research/tree/master/Teams
Commands:
- Category: Execute
  Command: teams.exe
  Description: Generate JavaScript payload and package.json, and save to "%LOCALAPPDATA%\\Microsoft\\Teams\\current\\app\\"
    before executing.
  MitreID: T1218.015
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: Node.JS
  Usecase: Execute JavaScript code
- Category: Execute
  Command: teams.exe
  Description: Generate JavaScript payload and package.json, archive in ASAR file and save to "%LOCALAPPDATA%\\Microsoft\\Teams\\current\\app.asar"
    before executing.
  MitreID: T1218.015
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: Node.JS
  Usecase: Execute JavaScript code
- Category: Execute
  Command: teams.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&"
  Description: Teams spawns cmd.exe as a child process of teams.exe and executes the ping command
  MitreID: T1218.015
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Executes a process under a trusted Microsoft signed binary
Created: 2022-01-17
Description: Electron runtime binary which runs the Teams application
Detection:
- IOC: '%LOCALAPPDATA%\Microsoft\Teams\current\app directory created'
- IOC: '%LOCALAPPDATA%\Microsoft\Teams\current\app.asar file created/modified by non-Teams installer/updater'
- Sigma: https://github.com/SigmaHQ/sigma/blob/43277f26fc1c81fc98fc79147b711189e901b757/rules/windows/process_creation/proc_creation_win_susp_electron_exeuction_proxy.yml
Full_Path:
- Path: C:\Users\<username>\AppData\Local\Microsoft\Teams\current\Teams.exe
Name: Teams.exe
Resources:
- Link: https://l--k.uk/2022/01/16/microsoft-teams-and-other-electron-apps-as-lolbins/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Teams.yml
```

## Detection / Analysis Notes

```text
IOC: %LOCALAPPDATA%\Microsoft\Teams\current\app directory created
```

```text
IOC: %LOCALAPPDATA%\Microsoft\Teams\current\app.asar file created/modified by non-Teams installer/updater
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/43277f26fc1c81fc98fc79147b711189e901b757/rules/windows/process_creation/proc_creation_win_susp_electron_exeuction_proxy.yml
```

```text
- IOC: '%LOCALAPPDATA%\Microsoft\Teams\current\app directory created'
- IOC: '%LOCALAPPDATA%\Microsoft\Teams\current\app.asar file created/modified by non-Teams installer/updater'
- Sigma: https://github.com/SigmaHQ/sigma/blob/43277f26fc1c81fc98fc79147b711189e901b757/rules/windows/process_creation/proc_creation_win_susp_electron_exeuction_proxy.yml
```
