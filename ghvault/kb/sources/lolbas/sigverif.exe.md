---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Sigverif.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `sigverif.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Sigverif.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Sigverif.exe](../../tools/windows/sigverif.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | sigverif.exe |
| name | Sigverif.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/0gtweet/status/1457676633809330184 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@0gtweet'
  Person: Grzegorz Tworek
- Handle: '@Hexacorn'
  Person: Adam
Author: Moshe Kaplan
Commands:
- Category: Execute
  Command: sigverif.exe
  Description: Launch sigverif.exe GUI, click 'Advanced', specify arbitrary executable path as 'log file name', then click
    'View Log' to execute the binary.
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  - Application: GUI
  Usecase: Execute arbitrary programs through a trusted Microsoft-signed binary to bypass application whitelisting.
Created: 2021-11-08
Description: File Signature Verification utility to verify digital signatures of files
Detection:
- IOC: sigverif.exe spawning unexpected child processes
Full_Path:
- Path: C:\Windows\System32\sigverif.exe
- Path: C:\Windows\SysWOW64\sigverif.exe
Name: Sigverif.exe
Resources:
- Link: https://twitter.com/0gtweet/status/1457676633809330184
- Link: https://www.hexacorn.com/blog/2018/04/27/i-shot-the-sigverif-exe-the-gui-based-lolbin/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Sigverif.yml
```

## Detection / Analysis Notes

```text
IOC: sigverif.exe spawning unexpected child processes
```

```text
- IOC: sigverif.exe spawning unexpected child processes
```
