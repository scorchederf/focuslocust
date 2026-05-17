---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Regini.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `regini.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regini.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Regini.exe](../../tools/windows/regini.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | regini.exe |
| name | Regini.exe |
| type | tool |
| source | lolbas |
| url | https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@elisalem9'
  Person: Eli Salem
Author: Oddvar Moe
Commands:
- Category: ADS
  Command: regini.exe {PATH}:hidden.ini
  Description: Write registry keys from data inside the Alternate data stream.
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Write to registry
Created: 2020-07-03
Description: Used to manipulate the registry
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regini_ads.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regini_execution.yml
- IOC: regini.exe reading from ADS
Full_Path:
- Path: C:\Windows\System32\regini.exe
- Path: C:\Windows\SysWOW64\regini.exe
Name: Regini.exe
Resources:
- Link: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regini.yml
```

## Detection / Analysis Notes

```text
IOC: regini.exe reading from ADS
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regini_ads.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regini_execution.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regini_ads.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regini_execution.yml
- IOC: regini.exe reading from ADS
```
