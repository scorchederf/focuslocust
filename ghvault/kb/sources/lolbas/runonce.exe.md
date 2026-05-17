---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Runonce.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `runonce.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Runonce.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Runonce.exe](../../tools/windows/runonce.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | runonce.exe |
| name | Runonce.exe |
| type | tool |
| source | lolbas |
| url | https://cmatskas.com/configure-a-runonce-task-on-windows/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@pabraeken'
  Person: Pierre-Alexandre Braeken
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: Runonce.exe /AlternateShellStartup
  Description: Executes a Run Once Task that has been configured in the registry.
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: Administrator
  Tags:
  - Execute: CMD
  Usecase: Persistence, bypassing defensive counter measures
Created: 2018-05-25
Description: Executes a Run Once Task that has been configured in the registry
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/registry/registry_event/registry_event_runonce_persistence.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_runonce_execution.yml
- Elastic: https://github.com/elastic/detection-rules/blob/2926e98c5d998706ef7e248a63fb0367c841f685/rules/windows/persistence_run_key_and_startup_broad.toml
- IOC: Registy key add - HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\YOURKEY
Full_Path:
- Path: C:\Windows\System32\runonce.exe
- Path: C:\Windows\SysWOW64\runonce.exe
Name: Runonce.exe
Resources:
- Link: https://twitter.com/pabraeken/status/990717080805789697
- Link: https://cmatskas.com/configure-a-runonce-task-on-windows/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Runonce.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/2926e98c5d998706ef7e248a63fb0367c841f685/rules/windows/persistence_run_key_and_startup_broad.toml
```

```text
IOC: Registy key add - HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\YOURKEY
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_runonce_execution.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/registry/registry_event/registry_event_runonce_persistence.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/registry/registry_event/registry_event_runonce_persistence.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_runonce_execution.yml
- Elastic: https://github.com/elastic/detection-rules/blob/2926e98c5d998706ef7e248a63fb0367c841f685/rules/windows/persistence_run_key_and_startup_broad.toml
- IOC: Registy key add - HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\YOURKEY
```
