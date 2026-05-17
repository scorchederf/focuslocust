---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Schtasks.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `schtasks.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Schtasks.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Schtasks.exe](../../tools/windows/schtasks.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | schtasks.exe |
| name | Schtasks.exe |
| type | tool |
| source | lolbas |
| url | https://isc.sans.edu/forums/diary/Adding+Persistence+Via+Scheduled+Tasks/23633/ |

## Preserved Source Material

```yaml
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: schtasks /create /sc minute /mo 1 /tn "Reverse shell" /tr "{CMD}"
  Description: Create a recurring task to execute every minute.
  MitreID: T1053.005
  OperatingSystem: Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Create a recurring task to keep reverse shell session(s) alive
- Category: Execute
  Command: schtasks /create /s targetmachine /tn "MyTask" /tr "{CMD}" /sc daily
  Description: Create a scheduled task on a remote computer for persistence/lateral movement
  MitreID: T1053.005
  OperatingSystem: Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: Administrator
  Tags:
  - Execute: CMD
  Usecase: Create a remote task to run daily relative to the the time of creation
Created: 2018-05-25
Description: Schedule periodic tasks
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_schtasks_creation.yml
- Elastic: https://github.com/elastic/detection-rules/blob/ef7548f04c4341e0d1a172810330d59453f46a21/rules/windows/persistence_local_scheduled_task_creation.toml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/schtasks_scheduling_job_on_remote_system.yml
- IOC: Suspicious task creation events
Full_Path:
- Path: c:\windows\system32\schtasks.exe
- Path: c:\windows\syswow64\schtasks.exe
Name: Schtasks.exe
Resources:
- Link: https://isc.sans.edu/forums/diary/Adding+Persistence+Via+Scheduled+Tasks/23633/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Schtasks.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/ef7548f04c4341e0d1a172810330d59453f46a21/rules/windows/persistence_local_scheduled_task_creation.toml
```

```text
IOC: Suspicious task creation events
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_schtasks_creation.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/schtasks_scheduling_job_on_remote_system.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_schtasks_creation.yml
- Elastic: https://github.com/elastic/detection-rules/blob/ef7548f04c4341e0d1a172810330d59453f46a21/rules/windows/persistence_local_scheduled_task_creation.toml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/schtasks_scheduling_job_on_remote_system.yml
- IOC: Suspicious task creation events
```
