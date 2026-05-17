---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Launch-VsDevShell.ps1

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `launch-vsdevshell.ps1` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Launch-VsDevShell.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Launch-VsDevShell.ps1](../../tools/windows/launch-vsdevshell.ps1.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | launch-vsdevshell.ps1 |
| name | Launch-VsDevShell.ps1 |
| type | tool |
| source | lolbas |
| url | https://twitter.com/nas_bench/status/1535981653239255040 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@nas_bench'
  Person: Nasreddine Bencherchali
Author: Nasreddine Bencherchali
Commands:
- Category: Execute
  Command: powershell -ep RemoteSigned -f .\Launch-VsDevShell.ps1 -VsWherePath {PATH_ABSOLUTE:.exe}
  Description: Execute binaries from the context of the signed script using the "VsWherePath" flag.
  MitreID: T1216
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Proxy execution
- Category: Execute
  Command: powershell -ep RemoteSigned -f .\Launch-VsDevShell.ps1 -VsInstallationPath "/../../../../../; {PATH:.exe} ;"
  Description: Execute binaries and commands from the context of the signed script using the "VsInstallationPath" flag.
  MitreID: T1216
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Proxy execution
Created: 2022-06-13
Description: Locates and imports a Developer PowerShell module and calls the Enter-VsDevShell cmdlet
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_launch_vsdevshell.yml
Full_Path:
- Path: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\Launch-VsDevShell.ps1
- Path: C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\Tools\Launch-VsDevShell.ps1
Name: Launch-VsDevShell.ps1
Resources:
- Link: https://twitter.com/nas_bench/status/1535981653239255040
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Launch-VsDevShell.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_launch_vsdevshell.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_launch_vsdevshell.yml
```
