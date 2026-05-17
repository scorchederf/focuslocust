---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Nmcap.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `nmcap.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Nmcap.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Nmcap.exe](../../tools/windows/nmcap.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | nmcap.exe |
| name | Nmcap.exe |
| type | tool |
| source | lolbas |
| url | https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/network-monitor-3 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Reconnaissance
  Command: nmcap.exe /network * /capture /file {PATH_ABSOLUTE:.cap}
  Description: 'Start capture on all network adapters and save to specified .cap (circular) file.

    Optionally, one can add:

    - `/TerminateWhen /TimeAfter 30 seconds` to auto-terminate after a relative times (e.g. 30 seconds);

    - `/TerminateWhen /Time 04:52:00 AM 9/17/2025` to auto-terminate after a specific date/time;

    - `/TerminateWhen /KeyPress x` to terminate when a specific key is pressed.

    '
  MitreID: T1040
  OperatingSystem: Windows
  Privileges: Administrator
  Usecase: Capture network traffic on windows to collect sensitive data.
Created: 2025-09-16
Description: Command-line packet capture utility from Microsoft Network Monitor 3.x.
Full_Path:
- Path: C:\Program Files\Microsoft Network Monitor 3\nmcap.exe
- Path: C:\Program Files (x86)\Microsoft Network Monitor 3\nmcap.exe
Name: Nmcap.exe
Resources:
- Link: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/network-monitor-3
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Nmcap.yml
```
