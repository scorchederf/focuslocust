---
parsed_by: focuslocust
source: commands
type: generated
---
# CustomShellHost Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## CustomShellHost.exe

Tool page: [CustomShellHost.exe](../../tools/windows/customshellhost.exe.md)

### Can be used to evade defensive counter-measures

```text
CustomShellHost.exe
```

Description:

Executes explorer.exe (with command-line argument /NoShellRegistrationCheck) if present in the current working folder.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/CustomShellHost.yml` |
| Evidence | Command preserved from source parser. |
