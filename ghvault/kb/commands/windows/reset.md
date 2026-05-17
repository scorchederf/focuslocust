---
parsed_by: focuslocust
source: commands
type: generated
---
# Reset Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Reset.exe

Tool page: [Reset.exe](../../tools/windows/reset.exe.md)

### Execute an arbitrary executable via trusted system executable.

```text
reset.exe session
```

Description:

Once executed, `reset.exe` will execute `rwinsta.exe` in the same folder. Thus, if `reset.exe` is copied to a folder and an arbitrary executable is renamed to `rwinsta.exe`, `reset.exe` will spawn it.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Reset.yml` |
| Evidence | Command preserved from source parser. |
