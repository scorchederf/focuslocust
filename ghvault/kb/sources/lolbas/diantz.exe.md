---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Diantz.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `diantz.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Diantz.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Diantz.exe](../../tools/windows/diantz.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | diantz.exe |
| name | Diantz.exe |
| type | tool |
| source | lolbas |
| url | https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/diantz |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@tim8288'
  Person: Tamir Yehuda
- Handle: '@vakninhai'
  Person: Hai Vaknin
Author: Tamir Yehuda
Commands:
- Category: ADS
  Command: diantz.exe {PATH_ABSOLUTE:.exe} {PATH_ABSOLUTE}:targetFile.cab
  Description: Compress a file (first argument) into a CAB file stored in the Alternate Data Stream (ADS) of the target file.
  MitreID: T1564.004
  OperatingSystem: Windows XP, Windows vista, Windows 7, Windows 8, Windows 8.1.
  Privileges: User
  Tags:
  - Type: Compression
  Usecase: Hide data compressed into an Alternate Data Stream.
- Category: Download
  Command: diantz.exe {PATH_SMB:.exe} {PATH_ABSOLUTE:.cab}
  Description: Download and compress a remote file and store it in a CAB file on local machine.
  MitreID: T1105
  OperatingSystem: Windows Server 2012, Windows Server 2012R2, Windows Server 2016, Windows Server 2019
  Privileges: User
  Tags:
  - Type: Compression
  Usecase: Download and compress into a cab file.
- Category: Execute
  Command: diantz /f {PATH:.ddf}
  Description: Execute diantz directives as defined in the specified Diamond Definition File (.ddf); see resources for the
    format specification.
  MitreID: T1036
  OperatingSystem: Windows Server 2012, Windows Server 2012R2, Windows Server 2016, Windows Server 2019
  Privileges: User
  Tags:
  - Type: Compression
  Usecase: Bypass command-line based detections
Created: 2020-08-08
Description: Binary that package existing files into a cabinet (.cab) file
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_diantz_ads.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_diantz_remote_cab.yml
- IOC: diantz storing data into alternate data streams.
- IOC: diantz getting a file from a remote machine or the internet.
Full_Path:
- Path: c:\windows\system32\diantz.exe
- Path: c:\windows\syswow64\diantz.exe
Name: Diantz.exe
Resources:
- Link: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/diantz
- Link: https://ss64.com/nt/makecab-directives.html
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Diantz.yml
```

## Detection / Analysis Notes

```text
IOC: diantz getting a file from a remote machine or the internet.
```

```text
IOC: diantz storing data into alternate data streams.
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_diantz_ads.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_diantz_remote_cab.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_diantz_ads.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_diantz_remote_cab.yml
- IOC: diantz storing data into alternate data streams.
- IOC: diantz getting a file from a remote machine or the internet.
```
