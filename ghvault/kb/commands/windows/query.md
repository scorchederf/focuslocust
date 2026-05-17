---
parsed_by: focuslocust
source: commands
type: generated
---
# Query Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Query.exe

Tool page: [Query.exe](../../tools/windows/query.exe.md)

### Execute an arbitrary executable via trusted system executable.

```text
query.exe user
```

Description:

Once executed, `query.exe` will execute `quser.exe` in the same folder. Thus, if `query.exe` is copied to a folder and an arbitrary executable is renamed to `quser.exe`, `query.exe` will spawn it. Instead of `user`, it is also possible to use `session`, `termsession` or `process` as command-line option.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Query.yml` |
| Evidence | Command preserved from source parser. |
