---
parsed_by: focuslocust
source: commands
type: generated
---
# SQLToolsPS Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## SQLToolsPS.exe

Tool page: [SQLToolsPS.exe](../../tools/windows/sqltoolsps.exe.md)

### Execute PowerShell command.

```text
SQLToolsPS.exe -noprofile -command Start-Process {PATH:.exe}
```

Description:

Run a SQL Server PowerShell mini-console without Module and ScriptBlock Logging.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Sqltoolsps.yml` |
| Evidence | Command preserved from source parser. |
