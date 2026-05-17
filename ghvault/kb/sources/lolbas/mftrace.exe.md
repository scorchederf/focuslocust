---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Mftrace.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `mftrace.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Mftrace.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Mftrace.exe](../../tools/windows/mftrace.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mftrace.exe |
| name | Mftrace.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/0rbz_/status/988911181422186496 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@0rbz_'
  Person: fabrizio
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: Mftrace.exe {PATH:.exe}
  Description: Launch specified executable as a subprocess of Mftrace.exe.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Local execution of cmd.exe as a subprocess of Mftrace.exe.
Created: 2018-05-25
Description: Trace log generation tool for Media Foundation Tools.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_mftrace.yml
Full_Path:
- Path: C:\Program Files (x86)\Windows Kits\10\bin\10.0.16299.0\x86\mftrace.exe
- Path: C:\Program Files (x86)\Windows Kits\10\bin\10.0.16299.0\x64\mftrace.exe
- Path: C:\Program Files (x86)\Windows Kits\10\bin\x86\mftrace.exe
- Path: C:\Program Files (x86)\Windows Kits\10\bin\x64\mftrace.exe
Name: Mftrace.exe
Resources:
- Link: https://twitter.com/0rbz_/status/988911181422186496
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Mftrace.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_mftrace.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_mftrace.yml
```
