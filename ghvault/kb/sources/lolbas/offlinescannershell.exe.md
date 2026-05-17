---
parsed_by: focuslocust
source: lolbas
type: generated
---
# OfflineScannerShell.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `offlinescannershell.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/OfflineScannerShell.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [OfflineScannerShell.exe](../../tools/windows/offlinescannershell.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | offlinescannershell.exe |
| name | OfflineScannerShell.exe |
| type | tool |
| source | lolbas |
| url |  |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@elliotkillick'
  Person: Elliot Killick
Author: Elliot Killick
Commands:
- Category: Execute
  Command: OfflineScannerShell
  Description: Execute mpclient.dll library in the current working directory
  MitreID: T1218
  OperatingSystem: Windows 10, Windows 11
  Privileges: Administrator
  Tags:
  - Execute: DLL
  Usecase: Can be used to evade defensive countermeasures or to hide as a persistence mechanism
Created: 2021-08-16
Description: Windows Defender Offline Shell
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/process_creation/proc_creation_win_lolbas_offlinescannershell.yml
- IOC: OfflineScannerShell.exe should not be run on a normal workstation
Full_Path:
- Path: C:\Program Files\Windows Defender\Offline\OfflineScannerShell.exe
Name: OfflineScannerShell.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/OfflineScannerShell.yml
```

## Detection / Analysis Notes

```text
IOC: OfflineScannerShell.exe should not be run on a normal workstation
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/process_creation/proc_creation_win_lolbas_offlinescannershell.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/bea6f18d350d9c9fdc067f93dde0e9b11cc22dc2/rules/windows/process_creation/proc_creation_win_lolbas_offlinescannershell.yml
- IOC: OfflineScannerShell.exe should not be run on a normal workstation
```
