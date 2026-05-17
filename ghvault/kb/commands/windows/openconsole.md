---
parsed_by: focuslocust
source: commands
type: generated
---
# OpenConsole Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## OpenConsole.exe

Tool page: [OpenConsole.exe](../../tools/windows/openconsole.exe.md)

### Use OpenConsole.exe as a proxy binary to evade defensive counter-measures

```text
OpenConsole.exe {PATH:.exe}
```

Description:

Execute specified process with OpenConsole.exe as parent process

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/OpenConsole.yml` |
| Evidence | Command preserved from source parser. |
