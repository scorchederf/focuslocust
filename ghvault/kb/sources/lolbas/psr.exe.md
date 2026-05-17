---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Psr.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `psr.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Psr.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Psr.exe](../../tools/windows/psr.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | psr.exe |
| name | Psr.exe |
| type | tool |
| source | lolbas |
| url | https://social.technet.microsoft.com/wiki/contents/articles/51722.windows-problem-steps-recorder-psr-quick-and-easy-documenting-of-your-steps-and-procedures.aspx |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@L3m0nada'
  Person: Leon Rodenko
Author: Leon Rodenko
Commands:
- Category: Reconnaissance
  Command: psr.exe /start /output {PATH_ABSOLUTE:.zip} /sc 1 /gui 0
  Description: Record a user screen without creating a GUI. You should use "psr.exe /stop" to stop recording and create output
    file.
  MitreID: T1113
  OperatingSystem: since Windows 7 (client) / Windows 2008 R2
  Privileges: User
  Usecase: Can be used to take screenshots of the user environment
Created: 2020-06-27
Description: Windows Problem Steps Recorder, used to record screen and clicks.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_psr_capture_screenshots.yml
- IOC: psr.exe spawned
- IOC: suspicious activity when running with "/gui 0" flag
Full_Path:
- Path: c:\windows\system32\psr.exe
- Path: c:\windows\syswow64\psr.exe
Name: Psr.exe
Resources:
- Link: https://social.technet.microsoft.com/wiki/contents/articles/51722.windows-problem-steps-recorder-psr-quick-and-easy-documenting-of-your-steps-and-procedures.aspx
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Psr.yml
```

## Detection / Analysis Notes

```text
IOC: psr.exe spawned
```

```text
IOC: suspicious activity when running with "/gui 0" flag
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_psr_capture_screenshots.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_psr_capture_screenshots.yml
- IOC: psr.exe spawned
- IOC: suspicious activity when running with "/gui 0" flag
```
