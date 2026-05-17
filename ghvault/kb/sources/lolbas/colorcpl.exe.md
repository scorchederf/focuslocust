---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Colorcpl.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `colorcpl.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Colorcpl.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Colorcpl.exe](../../tools/windows/colorcpl.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | colorcpl.exe |
| name | Colorcpl.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/eral4m/status/1480468728324231172 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@eral4m'
  Person: eral4m
Author: Arjan Onwezen
Commands:
- Category: Copy
  Command: colorcpl {PATH}
  Description: Copies the referenced file to C:\Windows\System32\spool\drivers\color\.
  MitreID: T1036.005
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Copies file(s) to a subfolder of a generally trusted folder (c:\Windows\System32), which can be used to hide files
    or make them blend into the environment.
Created: 2023-06-26
Description: Binary that handles color management
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_colorcpl.yml
- IOC: colorcpl.exe writing files
Full_Path:
- Path: C:\Windows\System32\colorcpl.exe
- Path: C:\Windows\SysWOW64\colorcpl.exe
Name: Colorcpl.exe
Resources:
- Link: https://twitter.com/eral4m/status/1480468728324231172
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Colorcpl.yml
```

## Detection / Analysis Notes

```text
IOC: colorcpl.exe writing files
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_colorcpl.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_colorcpl.yml
- IOC: colorcpl.exe writing files
```
