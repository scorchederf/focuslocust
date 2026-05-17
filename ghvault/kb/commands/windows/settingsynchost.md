---
parsed_by: focuslocust
source: commands
type: generated
---
# SettingSyncHost Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## SettingSyncHost.exe

Tool page: [SettingSyncHost.exe](../../tools/windows/settingsynchost.exe.md)

### Can be used to evade defensive countermeasures or to hide as a persistence mechanism

```text
SettingSyncHost -LoadAndRunDiagScript {PATH:.exe}
```

Description:

Execute file specified in %COMSPEC%

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/SettingSyncHost.yml` |
| Evidence | Command preserved from source parser. |

### Can be used to evade defensive countermeasures or to hide as a persistence mechanism. Additionally, effectively act as a -WindowStyle Hidden option (as there is in PowerShell) for any arbitrary batch file.

```text
SettingSyncHost -LoadAndRunDiagScriptNoCab {PATH:.bat}
```

Description:

Execute a batch script in the background (no window ever pops up) which can be subverted to running arbitrary programs by setting the current working directory to %TMP% and creating files such as reg.bat/reg.exe in that directory thereby causing them to execute instead of the ones in C:\Windows\System32.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/SettingSyncHost.yml` |
| Evidence | Command preserved from source parser. |
