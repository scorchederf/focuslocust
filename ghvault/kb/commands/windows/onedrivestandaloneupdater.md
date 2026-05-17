---
parsed_by: focuslocust
source: commands
type: generated
---
# OneDriveStandaloneUpdater Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## OneDriveStandaloneUpdater.exe

Tool page: [OneDriveStandaloneUpdater.exe](../../tools/windows/onedrivestandaloneupdater.exe.md)

### Download a file from the Internet without executing any anomalous executables with suspicious arguments

```text
OneDriveStandaloneUpdater
```

Description:

Download a file from the web address specified in `HKCU\Software\Microsoft\OneDrive\UpdateOfficeConfig\UpdateRingSettingURLFromOC`. `ODSUUpdateXMLUrlFromOC` and `UpdateXMLUrlFromOC` must be equal to non-empty string values in that same registry key. `UpdateOfficeConfigTimestamp` is a UNIX epoch time which must be set to a large QWORD such as 99999999999 (in decimal) to indicate the URL cache is good. The downloaded file will be in `%localappdata%\OneDrive\StandaloneUpdater\PreSignInSettingsConfig.json`.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/OneDriveStandaloneUpdater.yml` |
| Evidence | Command preserved from source parser. |
