---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pixtool.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pixtool.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Pixtool.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Pixtool.exe](../../tools/windows/pixtool.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pixtool.exe |
| name | Pixtool.exe |
| type | tool |
| source | lolbas |
| url | https://devblogs.microsoft.com/pix/pixtool/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
  Command: pixtool.exe launch {PATH_ABSOLUTE:.exe}
  Description: Launches an executable via PIX command-line utility.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Executes an executable under a trusted, Microsoft signed binary.
Created: 2025-09-21
Description: Command line utility for taking and analyzing PIX GPU captures.
Full_Path:
- Path: C:\Program Files\Microsoft PIX\pixtool.exe
- Path: C:\Program Files (x86)\Microsoft PIX\pixtool.exe
Name: Pixtool.exe
Resources:
- Link: https://devblogs.microsoft.com/pix/pixtool/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Pixtool.yml
```
