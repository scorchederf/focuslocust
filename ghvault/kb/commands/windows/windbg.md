---
parsed_by: focuslocust
source: commands
type: generated
---
# WinDbg Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## WinDbg.exe

Tool page: [WinDbg.exe](../../tools/windows/windbg.exe.md)

### Executes an executable under a trusted microsoft signed binary.

```text
windbg.exe -g {CMD}
```

Description:

Launches a command line through the debugging process; optionally add `-G` to exit the debugger automatically.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/WinDbg.yml` |
| Evidence | Command preserved from source parser. |
