---
parsed_by: focuslocust
source: lolbas
type: generated
---
# DumpMinitool.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `dumpminitool.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/DumpMinitool.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [DumpMinitool.exe](../../tools/windows/dumpminitool.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dumpminitool.exe |
| name | DumpMinitool.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/mrd0x/status/1511415432888131586 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@mrd0x'
  Person: mr.d0x
Author: mr.d0x
Commands:
- Category: Dump
  Command: DumpMinitool.exe --file {PATH_ABSOLUTE} --processId 1132 --dumpType Full
  Description: Creates a memory dump of the lsass process
  MitreID: T1003.001
  OperatingSystem: Windows 10, Windows 11
  Privileges: Administrator
  Usecase: Create memory dump and parse it offline
Created: 2022-01-20
Description: Dump tool part Visual Studio 2022
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_dumpminitool_execution.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_dumpminitool_susp_execution.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_devinit_lolbin_usage.yml
Full_Path:
- Path: C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\Extensions\TestPlatform\Extensions\DumpMinitool.exe
Name: DumpMinitool.exe
Resources:
- Link: https://twitter.com/mrd0x/status/1511415432888131586
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/DumpMinitool.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_devinit_lolbin_usage.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_dumpminitool_execution.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_dumpminitool_susp_execution.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_dumpminitool_execution.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_dumpminitool_susp_execution.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_devinit_lolbin_usage.yml
```
