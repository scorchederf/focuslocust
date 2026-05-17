---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Regedit.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `regedit.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regedit.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Regedit.exe](../../tools/windows/regedit.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | regedit.exe |
| name | Regedit.exe |
| type | tool |
| source | lolbas |
| url | https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@oddvarmoe'
  Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: ADS
  Command: regedit /E {PATH_ABSOLUTE}:regfile.reg HKEY_CURRENT_USER\MyCustomRegKey
  Description: Export the target Registry key to the specified .REG file.
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Hide registry data in alternate data stream
- Category: ADS
  Command: regedit {PATH_ABSOLUTE}:regfile.reg
  Description: Import the target .REG file into the Registry.
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Import hidden registry data from alternate data stream
Created: 2018-05-25
Description: Used by Windows to manipulate registry
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_regedit_import_keys_ads.yml
- IOC: regedit.exe reading and writing to alternate data stream
- IOC: regedit.exe should normally not be executed by end-users
Full_Path:
- Path: C:\Windows\regedit.exe
Name: Regedit.exe
Resources:
- Link: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regedit.yml
```

## Detection / Analysis Notes

```text
IOC: regedit.exe reading and writing to alternate data stream
```

```text
IOC: regedit.exe should normally not be executed by end-users
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_regedit_import_keys_ads.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_regedit_import_keys_ads.yml
- IOC: regedit.exe reading and writing to alternate data stream
- IOC: regedit.exe should normally not be executed by end-users
```
