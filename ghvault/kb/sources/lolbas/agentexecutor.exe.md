---
parsed_by: focuslocust
source: lolbas
type: generated
---
# AgentExecutor.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `agentexecutor.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Agentexecutor.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AgentExecutor.exe](../../tools/windows/agentexecutor.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | agentexecutor.exe |
| name | AgentExecutor.exe |
| type | tool |
| source | lolbas |
| url |  |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@lefterispan'
  Person: Eleftherios Panos
Author: Eleftherios Panos
Commands:
- Category: Execute
  Command: AgentExecutor.exe -powershell "{PATH_ABSOLUTE:.ps1}" "{PATH_ABSOLUTE:.1.log}" "{PATH_ABSOLUTE:.2.log}" "{PATH_ABSOLUTE:.3.log}"
    60000 "C:\Windows\SysWOW64\WindowsPowerShell\v1.0" 0 1
  Description: Spawns powershell.exe and executes a provided powershell script with ExecutionPolicy Bypass argument
  MitreID: T1218
  OperatingSystem: Windows 10
  Privileges: User
  Tags:
  - Execute: PowerShell
  Usecase: Execute unsigned powershell scripts
- Category: Execute
  Command: AgentExecutor.exe -powershell "{PATH_ABSOLUTE:.ps1}" "{PATH_ABSOLUTE:.1.log}" "{PATH_ABSOLUTE:.2.log}" "{PATH_ABSOLUTE:.3.log}"
    60000 "{PATH_ABSOLUTE:folder}" 0 1
  Description: If we place a binary named powershell.exe in the specified folder path, agentexecutor.exe will execute it successfully
  MitreID: T1218
  OperatingSystem: Windows 10
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Execute a provided EXE
Created: 2020-07-23
Description: Intune Management Extension included on Intune Managed Devices
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_agentexecutor.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_agentexecutor_susp_usage.yml
Full_Path:
- Path: C:\Program Files (x86)\Microsoft Intune Management Extension\AgentExecutor.exe
Name: AgentExecutor.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Agentexecutor.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_agentexecutor.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_agentexecutor_susp_usage.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_agentexecutor.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_agentexecutor_susp_usage.yml
```
