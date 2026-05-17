---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ntsd.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ntsd.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Ntsd.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Ntsd.exe](../../tools/windows/ntsd.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ntsd.exe |
| name | Ntsd.exe |
| type | tool |
| source | lolbas |
| url | https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/cdb-command-line-options |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
  Command: ntsd.exe -g {CMD}
  Description: Launches command through the debugging process; optionally add `-G` to exit the debugger automatically.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Executes an executable under a trusted microsoft signed binary.
Created: 2025-07-16
Description: Symbolic Debugger for Windows.
Full_Path:
- Path: C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\ntsd.exe
- Path: C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\ntsd.exe
- Path: C:\Program Files (x86)\Windows Kits\10\Debuggers\arm\ntsd.exe
- Path: C:\Program Files (x86)\Windows Kits\10\Debuggers\arm64\ntsd.exe
Name: Ntsd.exe
Resources:
- Link: https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/cdb-command-line-options
- Link: https://strontic.github.io/xcyclopedia/library/ntsd.exe-629EA12D527237B9CD945AC44C2DE80D.html
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Ntsd.yml
```
