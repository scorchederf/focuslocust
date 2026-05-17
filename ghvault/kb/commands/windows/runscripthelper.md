---
parsed_by: focuslocust
source: commands
type: generated
---
# Runscripthelper Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Runscripthelper.exe

Tool page: [Runscripthelper.exe](../../tools/windows/runscripthelper.exe.md)

### Bypass constrained language mode and execute Powershell script

```text
runscripthelper.exe surfacecheck \\?\{PATH_ABSOLUTE:.txt} {PATH_ABSOLUTE:folder}
```

Description:

Execute the PowerShell script with .txt extension

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Runscripthelper.yml` |
| Evidence | Command preserved from source parser. |
