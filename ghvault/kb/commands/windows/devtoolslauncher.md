---
parsed_by: focuslocust
source: commands
type: generated
---
# Devtoolslauncher Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Devtoolslauncher.exe

Tool page: [Devtoolslauncher.exe](../../tools/windows/devtoolslauncher.exe.md)

### Execute any binary with given arguments and it will call `developertoolssvc.exe`. `developertoolssvc` is actually executing the binary.

```text
devtoolslauncher.exe LaunchForDeploy {PATH_ABSOLUTE:.exe} "{CMD:args}" test
```

Description:

The above binary will execute other binary.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Devtoolslauncher.yml` |
| Evidence | Command preserved from source parser. |

### Execute any binary with given arguments.

```text
devtoolslauncher.exe LaunchForDebug {PATH_ABSOLUTE:.exe} "{CMD:args}" test
```

Description:

The above binary will execute other binary.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Devtoolslauncher.yml` |
| Evidence | Command preserved from source parser. |
