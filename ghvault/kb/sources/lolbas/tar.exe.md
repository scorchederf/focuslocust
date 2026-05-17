---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Tar.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `tar.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Tar.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Tar.exe](../../tools/windows/tar.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tar.exe |
| name | Tar.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/Cyber_Sorcery/status/1619819249886969856 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@Cyber_Sorcery'
  Person: Brian Lucero
- Person: Avester Fahimipour
Author: Brian Lucero
Commands:
- Category: ADS
  Command: tar -cf {PATH}:ads {PATH_ABSOLUTE:folder}
  Description: Compress one or more files to an alternate data stream (ADS).
  MitreID: T1564.004
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Type: Compression
  Usecase: Can be used to evade defensive countermeasures, or to hide as part of a persistence mechanism
- Category: ADS
  Command: tar -xf {PATH}:ads
  Description: Decompress a compressed file from an alternate data stream (ADS).
  MitreID: T1564.004
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Type: Compression
  Usecase: Can be used to evade defensive countermeasures, or to hide as part of a persistence mechanism
- Category: Copy
  Command: tar -xf {PATH_SMB:.tar}
  Description: Extracts archive.tar from the remote (internal) host to the current host.
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Type: Compression
  Usecase: Copy files
Created: 2023-01-30
Description: Used by Windows to extract and create archives.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_tar_compression.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_tar_extraction.yml
- IOC: tar.exe extracting files from a remote host within the environment
- IOC: Abnormal processes spawning tar.exe
- IOC: tar.exe interacting with alternate data streams (ADS)
Full_Path:
- Path: C:\Windows\System32\tar.exe
- Path: C:\Windows\SysWOW64\tar.exe
Name: Tar.exe
Resources:
- Link: https://twitter.com/Cyber_Sorcery/status/1619819249886969856
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Tar.yml
```

## Detection / Analysis Notes

```text
IOC: Abnormal processes spawning tar.exe
```

```text
IOC: tar.exe extracting files from a remote host within the environment
```

```text
IOC: tar.exe interacting with alternate data streams (ADS)
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_tar_compression.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_tar_extraction.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_tar_compression.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_tar_extraction.yml
- IOC: tar.exe extracting files from a remote host within the environment
- IOC: Abnormal processes spawning tar.exe
- IOC: tar.exe interacting with alternate data streams (ADS)
```
