---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Replace.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `replace.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Replace.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Replace.exe](../../tools/windows/replace.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | replace.exe |
| name | Replace.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/elceef/status/986334113941655553 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@elceef'
  Person: elceef
Author: Oddvar Moe
Commands:
- Category: Copy
  Command: replace.exe {PATH_ABSOLUTE:.cab} {PATH_ABSOLUTE:folder} /A
  Description: Copy .cab file to destination
  MitreID: T1105
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Copy files
- Category: Download
  Command: replace.exe {PATH_SMB:.exe} {PATH_ABSOLUTE:folder} /A
  Description: Download/Copy executable to specified folder
  MitreID: T1105
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Download file
Created: 2018-05-25
Description: Used to replace file with another file
Detection:
- IOC: Replace.exe retrieving files from remote server
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_replace.yml
Full_Path:
- Path: C:\Windows\System32\replace.exe
- Path: C:\Windows\SysWOW64\replace.exe
Name: Replace.exe
Resources:
- Link: https://twitter.com/elceef/status/986334113941655553
- Link: https://twitter.com/elceef/status/986842299861782529
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Replace.yml
```

## Detection / Analysis Notes

```text
IOC: Replace.exe retrieving files from remote server
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_replace.yml
```

```text
- IOC: Replace.exe retrieving files from remote server
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_replace.yml
```
