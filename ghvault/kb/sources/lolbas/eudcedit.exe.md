---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Eudcedit.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `eudcedit.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Eudcedit.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Eudcedit.exe](../../tools/windows/eudcedit.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | eudcedit.exe |
| name | Eudcedit.exe |
| type | tool |
| source | lolbas |
| url | https://medium.com/@matanb707/windows-fonts-exploitation-in-2025-bypassing-uac-with-eudcedit-915599705639 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@Bl4ckShad3'
  Person: Matan Bahar
Author: Matan Bahar
Commands:
- Category: UAC Bypass
  Command: eudcedit
  Description: Once executed, the Private Charecter Editor will be opened - click OK, then click File -> Font Links. In the
    next window choose the option "Link with Selected Fonts" and click on Save As, then in the opened enter the command you
    want to execute.
  MitreID: T1548.002
  OperatingSystem: Windows 10, Windows 11
  Privileges: Administrator
  Tags:
  - Execute: CMD
  - Application: GUI
  Usecase: Execute a binary or script as a high-integrity process without a UAC prompt.
Created: 2025-08-07
Description: Private Character Editor Windows Utility
Detection:
- IOC: Processes spawned by eudcedit.exe.
Full_Path:
- Path: c:\windows\system32\eudcedit.exe
- Path: c:\windows\syswow64\eudcedit.exe
Name: Eudcedit.exe
Resources:
- Link: https://medium.com/@matanb707/windows-fonts-exploitation-in-2025-bypassing-uac-with-eudcedit-915599705639
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Eudcedit.yml
```

## Detection / Analysis Notes

```text
IOC: Processes spawned by eudcedit.exe.
```

```text
- IOC: Processes spawned by eudcedit.exe.
```
