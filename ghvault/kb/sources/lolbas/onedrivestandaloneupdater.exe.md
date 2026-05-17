---
parsed_by: focuslocust
source: lolbas
type: generated
---
# OneDriveStandaloneUpdater.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `onedrivestandaloneupdater.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/OneDriveStandaloneUpdater.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [OneDriveStandaloneUpdater.exe](../../tools/windows/onedrivestandaloneupdater.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | onedrivestandaloneupdater.exe |
| name | OneDriveStandaloneUpdater.exe |
| type | tool |
| source | lolbas |
| url | https://github.com/LOLBAS-Project/LOLBAS/pull/153 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@elliotkillick'
  Person: Elliot Killick
Author: Elliot Killick
Commands:
- Category: Download
  Command: OneDriveStandaloneUpdater
  Description: Download a file from the web address specified in `HKCU\Software\Microsoft\OneDrive\UpdateOfficeConfig\UpdateRingSettingURLFromOC`.
    `ODSUUpdateXMLUrlFromOC` and `UpdateXMLUrlFromOC` must be equal to non-empty string values in that same registry key.
    `UpdateOfficeConfigTimestamp` is a UNIX epoch time which must be set to a large QWORD such as 99999999999 (in decimal)
    to indicate the URL cache is good. The downloaded file will be in `%localappdata%\OneDrive\StandaloneUpdater\PreSignInSettingsConfig.json`.
  MitreID: T1105
  OperatingSystem: Windows 10
  Privileges: User
  Usecase: Download a file from the Internet without executing any anomalous executables with suspicious arguments
Created: 2021-08-22
Description: OneDrive Standalone Updater
Detection:
- IOC: HKCU\Software\Microsoft\OneDrive\UpdateOfficeConfig\UpdateRingSettingURLFromOC being set to a suspicious non-Microsoft
    controlled URL
- IOC: Reports of downloading from suspicious URLs in %localappdata%\OneDrive\setup\logs\StandaloneUpdate_*.log files
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/registry/registry_set/registry_set_lolbin_onedrivestandaloneupdater.yml
Full_Path:
- Path: C:\Users\<username>\AppData\Local\Microsoft\OneDrive\OneDriveStandaloneUpdater.exe
- Path: C:\Program Files\Microsoft OneDrive\OneDriveStandaloneUpdater.exe
- Path: C:\Program Files (x86)\Microsoft OneDrive\OneDriveStandaloneUpdater.exe
Name: OneDriveStandaloneUpdater.exe
Resources:
- Link: https://github.com/LOLBAS-Project/LOLBAS/pull/153
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/OneDriveStandaloneUpdater.yml
```

## Detection / Analysis Notes

```text
IOC: HKCU\Software\Microsoft\OneDrive\UpdateOfficeConfig\UpdateRingSettingURLFromOC being set to a suspicious non-Microsoft controlled URL
```

```text
IOC: Reports of downloading from suspicious URLs in %localappdata%\OneDrive\setup\logs\StandaloneUpdate_*.log files
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/registry/registry_set/registry_set_lolbin_onedrivestandaloneupdater.yml
```

```text
- IOC: HKCU\Software\Microsoft\OneDrive\UpdateOfficeConfig\UpdateRingSettingURLFromOC being set to a suspicious non-Microsoft
    controlled URL
- IOC: Reports of downloading from suspicious URLs in %localappdata%\OneDrive\setup\logs\StandaloneUpdate_*.log files
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/registry/registry_set/registry_set_lolbin_onedrivestandaloneupdater.yml
```
