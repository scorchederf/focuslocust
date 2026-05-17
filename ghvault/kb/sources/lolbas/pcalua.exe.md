---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pcalua.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pcalua.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pcalua.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Pcalua.exe](../../tools/windows/pcalua.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pcalua.exe |
| name | Pcalua.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/KyleHanslovan/status/912659279806640128 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@kylehanslovan'
  Person: Kyle Hanslovan
- Handle: '@0rbz_'
  Person: Fab
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: pcalua.exe -a {PATH:.exe}
  Description: Open the target .EXE using the Program Compatibility Assistant.
  MitreID: T1202
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Proxy execution of binary
- Category: Execute
  Command: pcalua.exe -a {PATH_SMB:.dll}
  Description: Open the target .DLL file with the Program Compatibilty Assistant.
  MitreID: T1202
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
  Privileges: User
  Tags:
  - Execute: DLL
  - Execute: Remote
  Usecase: Proxy execution of remote dll file
- Category: Execute
  Command: pcalua.exe -a {PATH_ABSOLUTE:.cpl} -c Java
  Description: Open the target .CPL file with the Program Compatibility Assistant.
  MitreID: T1202
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Execution of CPL files
Created: 2018-05-25
Description: Program Compatibility Assistant
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_pcalua.yml
Full_Path:
- Path: C:\Windows\System32\pcalua.exe
Name: Pcalua.exe
Resources:
- Link: https://twitter.com/KyleHanslovan/status/912659279806640128
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pcalua.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_pcalua.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_pcalua.yml
```
