---
parsed_by: focuslocust
source: commands
type: generated
---
# AgentExecutor Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## AgentExecutor.exe

Tool page: [AgentExecutor.exe](../../tools/windows/agentexecutor.exe.md)

### Execute unsigned powershell scripts

```text
AgentExecutor.exe -powershell "{PATH_ABSOLUTE:.ps1}" "{PATH_ABSOLUTE:.1.log}" "{PATH_ABSOLUTE:.2.log}" "{PATH_ABSOLUTE:.3.log}" 60000 "C:\Windows\SysWOW64\WindowsPowerShell\v1.0" 0 1
```

Description:

Spawns powershell.exe and executes a provided powershell script with ExecutionPolicy Bypass argument

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Agentexecutor.yml` |
| Evidence | Command preserved from source parser. |

### Execute a provided EXE

```text
AgentExecutor.exe -powershell "{PATH_ABSOLUTE:.ps1}" "{PATH_ABSOLUTE:.1.log}" "{PATH_ABSOLUTE:.2.log}" "{PATH_ABSOLUTE:.3.log}" 60000 "{PATH_ABSOLUTE:folder}" 0 1
```

Description:

If we place a binary named powershell.exe in the specified folder path, agentexecutor.exe will execute it successfully

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Agentexecutor.yml` |
| Evidence | Command preserved from source parser. |
