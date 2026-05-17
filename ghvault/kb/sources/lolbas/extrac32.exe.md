---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Extrac32.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `extrac32.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Extrac32.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Extrac32.exe](../../tools/windows/extrac32.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | extrac32.exe |
| name | Extrac32.exe |
| type | tool |
| source | lolbas |
| url | https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@egre55'
  Person: egre55
- Handle: '@oddvarmoe'
  Person: Oddvar Moe
- Handle: '@VakninHai'
  Person: Hai Vaknin(Lux
- Handle: '@tim8288'
  Person: Tamir Yehuda
Author: Oddvar Moe
Commands:
- Category: ADS
  Command: extrac32 {PATH_ABSOLUTE:.cab} {PATH_ABSOLUTE}:file.exe
  Description: Extracts the source CAB file into an Alternate Data Stream (ADS) of the target file.
  MitreID: T1564.004
  OperatingSystem: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Type: Compression
  Usecase: Extract data from cab file and hide it in an alternate data stream.
- Category: ADS
  Command: extrac32 {PATH_ABSOLUTE:.cab} {PATH_ABSOLUTE}:file.exe
  Description: Extracts the source CAB file on an unc path into an Alternate Data Stream (ADS) of the target file.
  MitreID: T1564.004
  OperatingSystem: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Type: Compression
  Usecase: Extract data from cab file and hide it in an alternate data stream.
- Category: Download
  Command: extrac32 /Y /C {PATH_SMB} {PATH_ABSOLUTE}
  Description: Copy the source file to the destination file and overwrite it.
  MitreID: T1105
  OperatingSystem: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Download file from UNC/WEBDav
- Category: Copy
  Command: extrac32.exe /C {PATH_ABSOLUTE:.source.exe} {PATH_ABSOLUTE:.dest.exe}
  Description: Command for copying file from one folder to another
  MitreID: T1105
  OperatingSystem: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Copy file
Created: 2018-05-25
Description: Extract to ADS, copy or overwrite a file with Extrac32.exe
Detection:
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_misc_lolbin_connecting_to_the_internet.toml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_extrac32.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_extrac32_ads.yml
Full_Path:
- Path: C:\Windows\System32\extrac32.exe
- Path: C:\Windows\SysWOW64\extrac32.exe
Name: Extrac32.exe
Resources:
- Link: https://oddvar.moe/2018/04/11/putting-data-in-alternate-data-streams-and-how-to-execute-it-part-2/
- Link: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
- Link: https://twitter.com/egre55/status/985994639202283520
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Extrac32.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_misc_lolbin_connecting_to_the_internet.toml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_extrac32.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_extrac32_ads.yml
```

```text
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_misc_lolbin_connecting_to_the_internet.toml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_extrac32.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_extrac32_ads.yml
```
