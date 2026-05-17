---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Msdeploy.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msdeploy.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msdeploy.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Msdeploy.exe](../../tools/windows/msdeploy.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msdeploy.exe |
| name | Msdeploy.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/pabraeken/status/995837734379032576 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@pabraeken'
  Person: Pierre-Alexandre Braeken
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: msdeploy.exe -verb:sync -source:RunCommand -dest:runCommand="{PATH_ABSOLUTE:.bat}"
  Description: Launch .bat file via msdeploy.exe.
  MitreID: T1218
  OperatingSystem: Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11, Windows Server
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Local execution of batch file using msdeploy.exe.
- Category: AWL Bypass
  Command: msdeploy.exe -verb:sync -source:RunCommand -dest:runCommand="{PATH_ABSOLUTE:.bat}"
  Description: Launch .bat file via msdeploy.exe.
  MitreID: T1218
  OperatingSystem: Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11, Windows Server
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Local execution of batch file using msdeploy.exe.
- Category: Copy
  Command: msdeploy.exe -verb:sync -source:filePath={PATH_ABSOLUTE:.source.ext} -dest:filePath={PATH_ABSOLUTE:.dest.ext}
  Description: Copy file from source to destination.
  MitreID: T1105
  OperatingSystem: Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11, Windows Server
  Privileges: User
  Usecase: Copy file.
Created: 2018-05-25
Description: Microsoft tool used to deploy Web Applications.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_msdeploy.yml
Full_Path:
- Path: C:\Program Files\IIS\Microsoft Web Deploy V2\msdeploy.exe
- Path: C:\Program Files (x86)\IIS\Microsoft Web Deploy V2\msdeploy.exe
- Path: C:\Program Files\IIS\Microsoft Web Deploy V3\msdeploy.exe
- Path: C:\Program Files (x86)\IIS\Microsoft Web Deploy V3\msdeploy.exe
- Path: C:\Program Files\IIS\Microsoft Web Deploy V4\msdeploy.exe
- Path: C:\Program Files (x86)\IIS\Microsoft Web Deploy V4\msdeploy.exe
- Path: C:\Program Files\IIS\Microsoft Web Deploy V5\msdeploy.exe
- Path: C:\Program Files (x86)\IIS\Microsoft Web Deploy V5\msdeploy.exe
Name: Msdeploy.exe
Resources:
- Link: https://twitter.com/pabraeken/status/995837734379032576
- Link: https://twitter.com/pabraeken/status/999090532839313408
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msdeploy.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_msdeploy.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_msdeploy.yml
```
