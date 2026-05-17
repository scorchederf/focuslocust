---
parsed_by: focuslocust
source: commands
type: generated
---
# Rasautou Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Rasautou.exe

Tool page: [Rasautou.exe](../../tools/windows/rasautou.exe.md)

### Execute DLL code

```text
rasautou -d {PATH:.dll} -p export_name -a a -e e
```

Description:

Loads the target .DLL specified in -d and executes the export specified in -p. Options removed in Windows 10.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rasautou.yml` |
| Evidence | Command preserved from source parser. |
