---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Atbroker.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `atbroker.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Atbroker.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Atbroker.exe](../../tools/windows/atbroker.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | atbroker.exe |
| name | Atbroker.exe |
| type | tool |
| source | lolbas |
| url | http://www.hexacorn.com/blog/2016/07/22/beyond-good-ol-run-key-part-42/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@hexacorn'
  Person: Adam
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: ATBroker.exe /start malware
  Description: Start a registered Assistive Technology (AT).
  MitreID: T1218
  OperatingSystem: Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Executes code defined in registry for a new AT. Modifications must be made to the system registry to either register
    or modify an existing Assistive Technology (AT) service entry.
Created: 2018-05-25
Description: Helper binary for Assistive Technology (AT)
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_susp_atbroker.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/registry/registry_event/registry_event_susp_atbroker_change.yml
- IOC: Changes to HKCU\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\Configuration
- IOC: Changes to HKLM\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs
- IOC: Unknown AT starting C:\Windows\System32\ATBroker.exe /start malware
Full_Path:
- Path: C:\Windows\System32\Atbroker.exe
- Path: C:\Windows\SysWOW64\Atbroker.exe
Name: Atbroker.exe
Resources:
- Link: http://www.hexacorn.com/blog/2016/07/22/beyond-good-ol-run-key-part-42/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Atbroker.yml
```

## Detection / Analysis Notes

```text
IOC: Changes to HKCU\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\Configuration
```

```text
IOC: Changes to HKLM\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs
```

```text
IOC: Unknown AT starting C:\Windows\System32\ATBroker.exe /start malware
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_susp_atbroker.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/registry/registry_event/registry_event_susp_atbroker_change.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_susp_atbroker.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/registry/registry_event/registry_event_susp_atbroker_change.yml
- IOC: Changes to HKCU\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\Configuration
- IOC: Changes to HKLM\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs
- IOC: Unknown AT starting C:\Windows\System32\ATBroker.exe /start malware
```
