---
parsed_by: focuslocust
source: commands
type: generated
---
# winfile Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## winfile.exe

Tool page: [winfile.exe](../../tools/windows/winfile.exe.md)

### Performs execution of specified file, can be used as a defense evasion

```text
winfile.exe {PATH:.exe}
```

Description:

Execute an executable file with WinFile as a parent process.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/winfile.yml` |
| Evidence | Command preserved from source parser. |
