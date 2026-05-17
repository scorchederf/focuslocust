---
parsed_by: focuslocust
source: lolbas
type: generated
---
# ComputerDefaults.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `computerdefaults.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/ComputerDefaults.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ComputerDefaults.exe](../../tools/windows/computerdefaults.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | computerdefaults.exe |
| name | ComputerDefaults.exe |
| type | tool |
| source | lolbas |
| url | https://gist.github.com/havoc3-3/812547525107bd138a1a839118a3a44b |

## Preserved Source Material

```yaml
Acknowledgement:
- Person: Eron Clarke
Author: Eron Clarke
Commands:
- Category: UAC Bypass
  Command: ComputerDefaults.exe
  Description: Upon execution, ComputerDefaults.exe checks two registry values at HKEY_CURRENT_USER\Software\Classes\ms-settings\Shell\open\command;
    if these are set by an attacker, the set command will be executed as a high-integrity process without a UAC prompt being
    displayed to the user. See 'resources' for which registry keys/values to set.
  MitreID: T1548.002
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Usecase: Execute a binary or script as a high-integrity process without a UAC prompt.
Created: 2024-09-24
Description: ComputerDefaults.exe is a Windows system utility for managing default applications for tasks like web browsing,
  emailing, and media playback.
Detection:
- IOC: Event ID 10
- IOC: A binary or script spawned as a child process of ComputerDefaults.exe
- IOC: Changes to HKEY_CURRENT_USER\Software\Classes\ms-settings\Shell\open\command
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_computerdefaults.yml
Full_Path:
- Path: C:\Windows\System32\ComputerDefaults.exe
- Path: C:\Windows\SysWOW64\ComputerDefaults.exe
Name: ComputerDefaults.exe
Resources:
- Link: https://gist.github.com/havoc3-3/812547525107bd138a1a839118a3a44b
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/ComputerDefaults.yml
```

## Detection / Analysis Notes

```text
IOC: A binary or script spawned as a child process of ComputerDefaults.exe
```

```text
IOC: Changes to HKEY_CURRENT_USER\Software\Classes\ms-settings\Shell\open\command
```

```text
IOC: Event ID 10
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_computerdefaults.yml
```

```text
- IOC: Event ID 10
- IOC: A binary or script spawned as a child process of ComputerDefaults.exe
- IOC: Changes to HKEY_CURRENT_USER\Software\Classes\ms-settings\Shell\open\command
- Sigma: https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_computerdefaults.yml
```
