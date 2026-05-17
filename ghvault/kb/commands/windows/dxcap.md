---
parsed_by: focuslocust
source: commands
type: generated
---
# Dxcap Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Dxcap.exe

Tool page: [Dxcap.exe](../../tools/windows/dxcap.exe.md)

### Local execution of a process as a subprocess of dxcap.exe

```text
Dxcap.exe -c {PATH_ABSOLUTE:.exe}
```

Description:

Launch specified executable as a subprocess of dxcap.exe. Note that you should have write permissions in the current working directory for the command to succeed; alternatively, add '-file c:\path\to\writable\location.ext' as first argument.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dxcap.yml` |
| Evidence | Command preserved from source parser. |

### Execute an arbitrary executable via trusted system executable.

```text
dxcap.exe -usage
```

Description:

Once executed, `dxcap.exe` will execute `xperf.exe` in the same folder. Thus, if `dxcap.exe` is copied to a folder and an arbitrary executable is renamed to `xperf.exe`, `dxcap.exe` will spawn it.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dxcap.yml` |
| Evidence | Command preserved from source parser. |
