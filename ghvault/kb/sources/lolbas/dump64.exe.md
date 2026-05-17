---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Dump64.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `dump64.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dump64.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Dump64.exe](../../tools/windows/dump64.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dump64.exe |
| name | Dump64.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/mrd0x/status/1460597833917251595 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@mrd0x'
  Person: mr.d0x
Author: mr.d0x
Commands:
- Category: Dump
  Command: dump64.exe {PID} out.dmp
  Description: Creates a memory dump of the LSASS process.
  MitreID: T1003.001
  OperatingSystem: Windows 10, Windows 11
  Privileges: Administrator
  Usecase: Create memory dump and parse it offline to retrieve credentials.
Created: 2021-11-16
Description: Memory dump tool that comes with Microsoft Visual Studio
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_dump64.yml
- IOC: As a Windows SDK binary, execution on a system may be suspicious
Full_Path:
- Path: C:\Program Files (x86)\Microsoft Visual Studio\Installer\Feedback\dump64.exe
Name: Dump64.exe
Resources:
- Link: https://twitter.com/mrd0x/status/1460597833917251595
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dump64.yml
```

## Detection / Analysis Notes

```text
IOC: As a Windows SDK binary, execution on a system may be suspicious
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_dump64.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_dump64.yml
- IOC: As a Windows SDK binary, execution on a system may be suspicious
```
