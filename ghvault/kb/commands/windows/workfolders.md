---
parsed_by: focuslocust
source: commands
type: generated
---
# WorkFolders Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## WorkFolders.exe

Tool page: [WorkFolders.exe](../../tools/windows/workfolders.exe.md)

### Can be used to evade defensive countermeasures or to hide as a persistence mechanism

```text
WorkFolders
```

Description:

Execute `control.exe` in the current working directory

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/WorkFolders.yml` |
| Evidence | Command preserved from source parser. |

### Proxy execution of a malicious payload via App Paths registry hijacking.

```text
WorkFolders
```

Description:

`WorkFolders` attempts to execute `control.exe`. By modifying the default value of the App Paths registry key for `control.exe` in `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\control.exe`, an attacker can achieve proxy execution.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/WorkFolders.yml` |
| Evidence | Command preserved from source parser. |
