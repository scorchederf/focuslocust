---
parsed_by: focuslocust
source: commands
type: generated
---
# Ie4uinit Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Ie4uinit.exe

Tool page: [Ie4uinit.exe](../../tools/windows/ie4uinit.exe.md)

### Get code execution by copy files to another location

```text
ie4uinit.exe -BaseSettings
```

Description:

Executes commands from a specially prepared ie4uinit.inf file.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ie4uinit.yml` |
| Evidence | Command preserved from source parser. |
