---
parsed_by: focuslocust
source: lolbas
type: generated
---
# wbemtest.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wbemtest.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wbemtest.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [wbemtest.exe](../../tools/windows/wbemtest.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | wbemtest.exe |
| name | wbemtest.exe |
| type | tool |
| source | lolbas |
| url | https://saulpanders.github.io/2025/01/20/lolbas-wbemtest.html |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@saulpanders'
  Person: Paul Sanders
Author: saulpanders
Commands:
- Category: Execute
  Command: wbemtest.exe
  Description: Execute arbitary commands through WMI through a GUI managment interface for Web Based Enterprise Management
    testing (WBEM). Uses WMI to Create and instance of a Win32_Process WMI class with a commandline argument of the target
    command to spawn. Spawns a GUI so it requires interactive access. For a demo, see link to blog in resources.
  MitreID: T1047
  OperatingSystem: Windows 10, Windows 11
  Privileges: Any
  Tags:
  - Application: GUI
  - Execute: CMD
  Usecase: Execute arbitrary commands through WMI classes
Created: 2025-04-22
Description: WMI/WBEM Test Binary
Detection:
- IOC: wbemtest.exe binary spawned
Full_Path:
- Path: c:\windows\system32\wbem\wbemtest.exe
Name: wbemtest.exe
Resources:
- Link: https://saulpanders.github.io/2025/01/20/lolbas-wbemtest.html
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wbemtest.yml
```

## Detection / Analysis Notes

```text
IOC: wbemtest.exe binary spawned
```

```text
- IOC: wbemtest.exe binary spawned
```
