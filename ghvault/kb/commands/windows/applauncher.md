---
parsed_by: focuslocust
source: commands
type: generated
---
# AppLauncher Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## AppLauncher.exe

Tool page: [AppLauncher.exe](../../tools/windows/applauncher.exe.md)

### Executes an executable under a trusted, Microsoft signed binary.

```text
AppLauncher.exe {PATH_ABSOLUTE:.exe}
```

Description:

Launches an executable via User Experience Virtualization tool.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/AppLauncher.yml` |
| Evidence | Command preserved from source parser. |
