---
parsed_by: focuslocust
source: commands
type: generated
---
# Launch-VsDevShell.ps1 Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Launch-VsDevShell.ps1

Tool page: [Launch-VsDevShell.ps1](../../tools/windows/launch-vsdevshell.ps1.md)

### Proxy execution

```text
powershell -ep RemoteSigned -f .\Launch-VsDevShell.ps1 -VsWherePath {PATH_ABSOLUTE:.exe}
```

Description:

Execute binaries from the context of the signed script using the "VsWherePath" flag.

Related ATT&CK:

- [T1216](../../attack/techniques/T1216-system-script-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Launch-VsDevShell.yml` |
| Evidence | Command preserved from source parser. |

### Proxy execution

```text
powershell -ep RemoteSigned -f .\Launch-VsDevShell.ps1 -VsInstallationPath "/../../../../../; {PATH:.exe} ;"
```

Description:

Execute binaries and commands from the context of the signed script using the "VsInstallationPath" flag.

Related ATT&CK:

- [T1216](../../attack/techniques/T1216-system-script-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Launch-VsDevShell.yml` |
| Evidence | Command preserved from source parser. |
