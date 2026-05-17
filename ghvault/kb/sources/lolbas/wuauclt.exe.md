---
parsed_by: focuslocust
source: lolbas
type: generated
---
# wuauclt.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wuauclt.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wuauclt.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [wuauclt.exe](../../tools/windows/wuauclt.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | wuauclt.exe |
| name | wuauclt.exe |
| type | tool |
| source | lolbas |
| url | https://dtm.uk/wuauclt/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@dtmsecurity'
  Person: David Middlehurst
Author: David Middlehurst
Commands:
- Category: Execute
  Command: wuauclt.exe /UpdateDeploymentProvider {PATH_ABSOLUTE:.dll} /RunHandlerComServer
  Description: Loads and executes DLL code on attach.
  MitreID: T1218
  OperatingSystem: Windows 10
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Execute dll via attach/detach methods
Created: 2020-09-23
Description: Windows Update Client
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/network_connection/net_connection_win_wuauclt_network_connection.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_wuauclt.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_wuauclt_execution.yml
- IOC: wuauclt run with a parameter of a DLL path
- IOC: Suspicious wuauclt Internet/network connections
Full_Path:
- Path: C:\Windows\System32\wuauclt.exe
- Path: C:\Windows\UUS\amd64\wuauclt.exe
Name: wuauclt.exe
Resources:
- Link: https://dtm.uk/wuauclt/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wuauclt.yml
```

## Detection / Analysis Notes

```text
IOC: Suspicious wuauclt Internet/network connections
```

```text
IOC: wuauclt run with a parameter of a DLL path
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/network_connection/net_connection_win_wuauclt_network_connection.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_wuauclt.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_wuauclt_execution.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/network_connection/net_connection_win_wuauclt_network_connection.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_wuauclt.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_wuauclt_execution.yml
- IOC: wuauclt run with a parameter of a DLL path
- IOC: Suspicious wuauclt Internet/network connections
```
