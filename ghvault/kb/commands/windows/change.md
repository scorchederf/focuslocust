---
parsed_by: focuslocust
source: commands
type: generated
---
# Change Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Change.exe

Tool page: [Change.exe](../../tools/windows/change.exe.md)

### Execute an arbitrary executable via trusted system executable.

```text
change.exe user
```

Description:

Once executed, `change.exe` will execute `chgusr.exe` in the same folder. Thus, if `change.exe` is copied to a folder and an arbitrary executable is renamed to `chgusr.exe`, `change.exe` will spawn it. Instead of `user`, it is also possible to use `port` or `logon` as command-line option.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Change.yml` |
| Evidence | Command preserved from source parser. |
