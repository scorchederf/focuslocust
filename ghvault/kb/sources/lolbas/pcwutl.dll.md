---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pcwutl.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pcwutl.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Pcwutl.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Pcwutl.dll](../../tools/windows/pcwutl.dll.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pcwutl.dll |
| name | Pcwutl.dll |
| type | tool |
| source | lolbas |
| url | https://twitter.com/harr0ey/status/989617817849876488 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@harr0ey'
  Person: Matt harr0ey
Author: LOLBAS Team
Commands:
- Category: Execute
  Command: rundll32.exe pcwutl.dll,LaunchApplication {PATH:.exe}
  Description: Launch executable by calling the LaunchApplication function.
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Launch an executable.
Created: 2018-05-25
Description: Microsoft HTML Viewer
Detection:
- Analysis: https://redcanary.com/threat-detection-report/techniques/rundll32/
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
Full_Path:
- Path: c:\windows\system32\pcwutl.dll
- Path: c:\windows\syswow64\pcwutl.dll
Name: Pcwutl.dll
Resources:
- Link: https://twitter.com/harr0ey/status/989617817849876488
- Link: https://windows10dll.nirsoft.net/pcwutl_dll.html
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Pcwutl.yml
```

## Detection / Analysis Notes

```text
Analysis: https://redcanary.com/threat-detection-report/techniques/rundll32/
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```

```text
- Analysis: https://redcanary.com/threat-detection-report/techniques/rundll32/
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```
