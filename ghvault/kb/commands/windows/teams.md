---
parsed_by: focuslocust
source: commands
type: generated
---
# Teams Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Teams.exe

Tool page: [Teams.exe](../../tools/windows/teams.exe.md)

### Execute JavaScript code

```text
teams.exe
```

Description:

Generate JavaScript payload and package.json, and save to "%LOCALAPPDATA%\\Microsoft\\Teams\\current\\app\\" before executing.

Related ATT&CK:

- [T1218.015](../../attack/techniques/T1218.015-electron-applications.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Teams.yml` |
| Evidence | Command preserved from source parser. |

### Execute JavaScript code

```text
teams.exe
```

Description:

Generate JavaScript payload and package.json, archive in ASAR file and save to "%LOCALAPPDATA%\\Microsoft\\Teams\\current\\app.asar" before executing.

Related ATT&CK:

- [T1218.015](../../attack/techniques/T1218.015-electron-applications.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Teams.yml` |
| Evidence | Command preserved from source parser. |

### Executes a process under a trusted Microsoft signed binary

```text
teams.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&"
```

Description:

Teams spawns cmd.exe as a child process of teams.exe and executes the ping command

Related ATT&CK:

- [T1218.015](../../attack/techniques/T1218.015-electron-applications.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Teams.yml` |
| Evidence | Command preserved from source parser. |
