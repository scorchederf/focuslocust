---
parsed_by: focuslocust
source: commands
type: generated
---
# Sqlps Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Sqlps.exe

Tool page: [Sqlps.exe](../../tools/windows/sqlps.exe.md)

### Execute PowerShell commands without ScriptBlock logging.

```text
Sqlps.exe -noprofile
```

Description:

Run a SQL Server PowerShell mini-console without Module and ScriptBlock Logging.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Sqlps.yml` |
| Evidence | Command preserved from source parser. |
