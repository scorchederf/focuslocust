---
parsed_by: focuslocust
source: lolbas
type: generated
---
# AppLauncher.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `applauncher.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/AppLauncher.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AppLauncher.exe](../../tools/windows/applauncher.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | applauncher.exe |
| name | AppLauncher.exe |
| type | tool |
| source | lolbas |
| url | https://learn.microsoft.com/en-us/microsoft-desktop-optimization-pack/ue-v/uev-getting-started |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
  Command: AppLauncher.exe {PATH_ABSOLUTE:.exe}
  Description: Launches an executable via User Experience Virtualization tool.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Executes an executable under a trusted, Microsoft signed binary.
Created: 2025-09-21
Description: User Experience Virtualization tool that launches applications under monitoring to capture and synchronize user
  settings.
Full_Path:
- Path: C:\Program Files\Windows Kits\10\Microsoft User Experience Virtualization\Management\AppLauncher.exe
- Path: C:\Program Files (x86)\Windows Kits\10\Microsoft User Experience Virtualization\Management\AppLauncher.exe
Name: AppLauncher.exe
Resources:
- Link: https://learn.microsoft.com/en-us/microsoft-desktop-optimization-pack/ue-v/uev-getting-started
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/AppLauncher.yml
```
