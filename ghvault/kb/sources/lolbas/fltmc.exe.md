---
parsed_by: focuslocust
source: lolbas
type: generated
---
# fltMC.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `fltmc.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/FltMC.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [fltMC.exe](../../tools/windows/fltmc.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | fltmc.exe |
| name | fltMC.exe |
| type | tool |
| source | lolbas |
| url | https://www.darkoperator.com/blog/2018/10/5/operating-offensively-against-sysmon |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@Carlos_Perez'
  Person: Carlos Perez
Author: John Lambert
Commands:
- Category: Tamper
  Command: fltMC.exe unload SysmonDrv
  Description: Unloads a driver used by security agents
  MitreID: T1562.001
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: Admin
  Usecase: Defense evasion
Created: 2021-09-18
Description: Filter Manager Control Program used by Windows
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_fltmc_unload_driver_sysmon.yml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_via_filter_manager.toml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/unload_sysmon_filter_driver.yml
- IOC: 4688 events with fltMC.exe
Full_Path:
- Path: C:\Windows\System32\fltMC.exe
Name: fltMC.exe
Resources:
- Link: https://www.darkoperator.com/blog/2018/10/5/operating-offensively-against-sysmon
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/FltMC.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_via_filter_manager.toml
```

```text
IOC: 4688 events with fltMC.exe
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_fltmc_unload_driver_sysmon.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/unload_sysmon_filter_driver.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_fltmc_unload_driver_sysmon.yml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_via_filter_manager.toml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/unload_sysmon_filter_driver.yml
- IOC: 4688 events with fltMC.exe
```
