---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Msconfig.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msconfig.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msconfig.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Msconfig.exe](../../tools/windows/msconfig.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msconfig.exe |
| name | Msconfig.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/pabraeken/status/991314564896690177 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@pabraeken'
  Person: Pierre-Alexandre Braeken
Author: Oddvar Moe
Code_Sample:
- Code: https://raw.githubusercontent.com/LOLBAS-Project/LOLBAS/master/OSBinaries/Payload/mscfgtlc.xml
Commands:
- Category: Execute
  Command: Msconfig.exe -5
  Description: Executes command embeded in crafted c:\windows\system32\mscfgtlc.xml.
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
  Privileges: Administrator
  Tags:
  - Execute: CMD
  Usecase: Code execution using Msconfig.exe
Created: 2018-05-25
Description: MSConfig is a troubleshooting tool which is used to temporarily disable or re-enable software, device drivers
  or Windows services that run during startup process to help the user determine the cause of a problem with Windows
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_uac_bypass_msconfig_gui.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/file/file_event/file_event_win_uac_bypass_msconfig_gui.yml
- IOC: mscfgtlc.xml changes in system32 folder
Full_Path:
- Path: C:\Windows\System32\msconfig.exe
Name: Msconfig.exe
Resources:
- Link: https://twitter.com/pabraeken/status/991314564896690177
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msconfig.yml
```

## Detection / Analysis Notes

```text
IOC: mscfgtlc.xml changes in system32 folder
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/file/file_event/file_event_win_uac_bypass_msconfig_gui.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_uac_bypass_msconfig_gui.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_uac_bypass_msconfig_gui.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/file/file_event/file_event_win_uac_bypass_msconfig_gui.yml
- IOC: mscfgtlc.xml changes in system32 folder
```
