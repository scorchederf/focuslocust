---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Bitsadmin.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `bitsadmin.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Bitsadmin.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Bitsadmin.exe](../../tools/windows/bitsadmin.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | bitsadmin.exe |
| name | Bitsadmin.exe |
| type | tool |
| source | lolbas |
| url | https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@mubix'
  Person: Rob Fuller
- Handle: '@carnal0wnage'
  Person: Chris Gates
- Handle: '@oddvarmoe'
  Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: ADS
  Command: bitsadmin /create 1 bitsadmin /addfile 1 c:\windows\system32\cmd.exe c:\data\playfolder\cmd.exe bitsadmin /SetNotifyCmdLine
    1 c:\data\playfolder\1.txt:cmd.exe NULL bitsadmin /RESUME 1 bitsadmin /complete 1
  Description: Create a bitsadmin job named 1, add cmd.exe to the job, configure the job to run the target command from an
    Alternate data stream, then resume and complete the job.
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Performs execution of specified file in the alternate data stream, can be used as a defensive evasion or persistence
    technique.
- Category: Download
  Command: bitsadmin /create 1 bitsadmin /addfile 1 https://live.sysinternals.com/autoruns.exe c:\data\playfolder\autoruns.exe
    bitsadmin /RESUME 1 bitsadmin /complete 1
  Description: Create a bitsadmin job named 1, add cmd.exe to the job, configure the job to run the target command, then resume
    and complete the job.
  MitreID: T1105
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Download file from Internet
- Category: Copy
  Command: bitsadmin /create 1 & bitsadmin /addfile 1 c:\windows\system32\cmd.exe c:\data\playfolder\cmd.exe & bitsadmin /RESUME
    1 & bitsadmin /Complete 1 & bitsadmin /reset
  Description: Command for copying cmd.exe to another folder
  MitreID: T1105
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
  Privileges: User
  Usecase: Copy file
- Category: Execute
  Command: bitsadmin /create 1 & bitsadmin /addfile 1 c:\windows\system32\cmd.exe c:\data\playfolder\cmd.exe & bitsadmin /SetNotifyCmdLine
    1 c:\data\playfolder\cmd.exe NULL & bitsadmin /RESUME 1 & bitsadmin /Reset
  Description: One-liner that creates a bitsadmin job named 1, add cmd.exe to the job, configure the job to run the target
    command, then resume and complete the job.
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
  Privileges: User
  Usecase: Execute binary file specified. Can be used as a defensive evasion.
Created: 2018-05-25
Description: Used for managing background intelligent transfer
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_bitsadmin_download.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/web/proxy_generic/proxy_ua_bitsadmin_susp_tld.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_bitsadmin_potential_persistence.yml
- Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/bitsadmin_download_file.yml
- IOC: Child process from bitsadmin.exe
- IOC: bitsadmin creates new files
- IOC: bitsadmin adds data to alternate data stream
Full_Path:
- Path: C:\Windows\System32\bitsadmin.exe
- Path: C:\Windows\SysWOW64\bitsadmin.exe
Name: Bitsadmin.exe
Resources:
- Link: https://www.slideshare.net/chrisgates/windows-attacks-at-is-the-new-black-26672679
- Link: https://www.youtube.com/watch?v=_8xJaaQlpBo
- Link: https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
- Link: https://www.soc-labs.top/en/detections/100
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Bitsadmin.yml
```

## Detection / Analysis Notes

```text
IOC: Child process from bitsadmin.exe
```

```text
IOC: bitsadmin adds data to alternate data stream
```

```text
IOC: bitsadmin creates new files
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/web/proxy_generic/proxy_ua_bitsadmin_susp_tld.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_bitsadmin_download.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_bitsadmin_potential_persistence.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/bitsadmin_download_file.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_bitsadmin_download.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/web/proxy_generic/proxy_ua_bitsadmin_susp_tld.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_bitsadmin_potential_persistence.yml
- Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/bitsadmin_download_file.yml
- IOC: Child process from bitsadmin.exe
- IOC: bitsadmin creates new files
- IOC: bitsadmin adds data to alternate data stream
```
