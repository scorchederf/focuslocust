---
parsed_by: focuslocust
source: lolbas
type: generated
---
# iscsicpl.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `iscsicpl.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Iscsicpl.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [iscsicpl.exe](../../tools/windows/iscsicpl.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iscsicpl.exe |
| name | iscsicpl.exe |
| type | tool |
| source | lolbas |
| url | https://github.com/hackerhouse-opensource/iscsicpl_bypassUAC |

## Preserved Source Material

```yaml
Acknowledgement:
- Person: hacker.house
- Handle: '@eki_erk'
  Person: Ekitji
Author: Ekitji
Commands:
- Category: UAC Bypass
  Command: c:\windows\syswow64\iscsicpl.exe
  Description: c:\windows\syswow64\iscsicpl.exe has a DLL injection through `C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\ISCSIEXE.dll`,
    resulting in UAC bypass.
  MitreID: T1548.002
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Execute a custom DLL via a trusted high-integrity process without a UAC prompt.
- Category: UAC Bypass
  Command: iscsicpl.exe
  Description: Both `c:\windows\system32\iscsicpl.exe` and `c:\windows\system64\iscsicpl.exe` have UAC bypass through launching
    iscicpl.exe, then navigating into the Configuration tab, clicking Report, then launching your custom command.
  MitreID: T1548.002
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  - Application: GUI
  Usecase: Execute a binary or script as a high-integrity process without a UAC prompt.
Created: 2025-08-17
Description: Microsoft iSCSI Initiator Control Panel tool
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_uac_bypass_iscsicpl.yml
- IOC: C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\ISCSIEXE.dll
- IOC: Suspicious child process to iscsicpl.exe like cmd, powershell etc.
Full_Path:
- Path: c:\windows\system32\iscsicpl.exe
- Path: c:\windows\syswow64\iscsicpl.exe
Name: iscsicpl.exe
Resources:
- Link: https://learn.microsoft.com/en-us/windows-server/storage/iscsi/iscsi-initiator-portal
- Link: https://github.com/hackerhouse-opensource/iscsicpl_bypassUAC
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Iscsicpl.yml
```

## Detection / Analysis Notes

```text
IOC: C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\ISCSIEXE.dll
```

```text
IOC: Suspicious child process to iscsicpl.exe like cmd, powershell etc.
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_uac_bypass_iscsicpl.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_uac_bypass_iscsicpl.yml
- IOC: C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\ISCSIEXE.dll
- IOC: Suspicious child process to iscsicpl.exe like cmd, powershell etc.
```
