---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Findstr.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `findstr.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Findstr.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Findstr.exe](../../tools/windows/findstr.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | findstr.exe |
| name | Findstr.exe |
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
  Command: findstr /V /L W3AllLov3LolBas {PATH_ABSOLUTE:.exe} > {PATH_ABSOLUTE}:file.exe
  Description: Searches for the string W3AllLov3LolBas, since it does not exist (/V) the specified .exe file is written to
    an Alternate Data Stream (ADS) of the specified target file.
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Add a file to an alternate data stream to hide from defensive counter measures
- Category: ADS
  Command: findstr /V /L W3AllLov3LolBas {PATH_SMB:.exe} > {PATH_ABSOLUTE}:file.exe
  Description: Searches for the string W3AllLov3LolBas, since it does not exist (/V) file.exe is written to an Alternate Data
    Stream (ADS) of the file.txt file.
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Add a file to an alternate data stream from a webdav server to hide from defensive counter measures
- Category: Credentials
  Command: findstr /S /I cpassword \\sysvol\policies\*.xml
  Description: Search for stored password in Group Policy files stored on SYSVOL.
  MitreID: T1552.001
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Find credentials stored in cpassword attrbute
- Category: Download
  Command: findstr /V /L W3AllLov3LolBas {PATH_SMB:.exe} > {PATH_ABSOLUTE:.exe}
  Description: Searches for the string W3AllLov3LolBas, since it does not exist (/V) file.exe is downloaded to the target
    file.
  MitreID: T1105
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Download/Copy file from webdav server
Created: 2018-05-25
Description: Write to ADS, discover, or download files with Findstr.exe
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_findstr.yml
Full_Path:
- Path: C:\Windows\System32\findstr.exe
- Path: C:\Windows\SysWOW64\findstr.exe
Name: Findstr.exe
Resources:
- Link: https://oddvar.moe/2018/04/11/putting-data-in-alternate-data-streams-and-how-to-execute-it-part-2/
- Link: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Findstr.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_findstr.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_findstr.yml
```
