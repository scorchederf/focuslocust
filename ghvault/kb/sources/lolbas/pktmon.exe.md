---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pktmon.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pktmon.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pktmon.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Pktmon.exe](../../tools/windows/pktmon.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pktmon.exe |
| name | Pktmon.exe |
| type | tool |
| source | lolbas |
| url | https://binar-x79.com/windows-10-secret-sniffer/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Person: Derek Johnson
Author: Derek Johnson
Commands:
- Category: Reconnaissance
  Command: pktmon.exe start --etw
  Description: Will start a packet capture and store log file as PktMon.etl. Use pktmon.exe stop
  MitreID: T1040
  OperatingSystem: Windows 10 1809 and later, Windows 11
  Privileges: Administrator
  Usecase: use this a built in network sniffer on windows 10 to capture senstive traffic
- Category: Reconnaissance
  Command: pktmon.exe filter add -p 445
  Description: Select Desired ports for packet capture
  MitreID: T1040
  OperatingSystem: Windows 10 1809 and later, Windows 11
  Privileges: Administrator
  Usecase: Look for interesting traffic such as telent or FTP
Created: 2020-08-12
Description: Capture Network Packets on the windows 10 with October 2018 Update or later.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_pktmon.yml
- IOC: .etl files found on system
Full_Path:
- Path: c:\windows\system32\pktmon.exe
- Path: c:\windows\syswow64\pktmon.exe
Name: Pktmon.exe
Resources:
- Link: https://binar-x79.com/windows-10-secret-sniffer/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pktmon.yml
```

## Detection / Analysis Notes

```text
IOC: .etl files found on system
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_pktmon.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_pktmon.yml
- IOC: .etl files found on system
```
