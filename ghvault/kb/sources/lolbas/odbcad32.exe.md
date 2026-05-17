---
parsed_by: focuslocust
source: lolbas
type: generated
---
# odbcad32.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `odbcad32.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/odbcad32.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [odbcad32.exe](../../tools/windows/odbcad32.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | odbcad32.exe |
| name | odbcad32.exe |
| type | tool |
| source | lolbas |
| url | https://medium.com/@thebinaryhashira/living-off-the-land-and-living-above-uac-6a66738d225c |

## Preserved Source Material

```yaml
Acknowledgement:
- Person: amonitoring
- Handle: '@eki_erk'
  Person: Ekitji
Author: Ekitji
Commands:
- Category: UAC Bypass
  Command: odbcad32.exe
  Description: Launch odbcad32.exe GUI, click 'Tracing' tab, click 'Browsing' button, enter abitrary command in the File Dialog's
    path, press enter.
  MitreID: T1548.002
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  - Application: GUI
  Usecase: Execute a binary as a high-integrity process without a UAC prompt.
Created: 2025-09-04
Description: ODBC Data Source Administrator to manage User/System DSNs and ODBC drivers.
Detection:
- IOC: odbcad32.exe spawning unexpected child processes.
Full_Path:
- Path: c:\windows\system32\odbcad32.exe
- Path: c:\windows\syswow64\odbcad32.exe
Name: odbcad32.exe
Resources:
- Link: https://medium.com/@thebinaryhashira/living-off-the-land-and-living-above-uac-6a66738d225c
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/odbcad32.yml
```

## Detection / Analysis Notes

```text
IOC: odbcad32.exe spawning unexpected child processes.
```

```text
- IOC: odbcad32.exe spawning unexpected child processes.
```
