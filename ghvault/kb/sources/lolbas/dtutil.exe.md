---
parsed_by: focuslocust
source: lolbas
type: generated
---
# dtutil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `dtutil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dtutil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [dtutil.exe](../../tools/windows/dtutil.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dtutil.exe |
| name | dtutil.exe |
| type | tool |
| source | lolbas |
| url | https://learn.microsoft.com/en-us/sql/integration-services/dtutil-utility?view=sql-server-ver16 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Copy
  Command: dtutil.exe /FILE {PATH_ABSOLUTE:.source.ext} /COPY FILE;{PATH_ABSOLUTE:.dest.ext}
  Description: Copy file from source to destination
  MitreID: T1105
  OperatingSystem: Windows
  Privileges: Administrator
  Usecase: Use to copies the source file to the destination file
Created: 2024-06-17
Description: Microsoft command line utility used to manage SQL Server Integration Services packages.
Full_Path:
- Path: C:\Program Files\Microsoft SQL Server\<version>\DTS\Binn\dtutil.exe
- Path: C:\Program Files (x86)\Microsoft SQL Server\<version>\DTS\Binn\dtutil.exe
Name: dtutil.exe
Resources:
- Link: https://learn.microsoft.com/en-us/sql/integration-services/dtutil-utility?view=sql-server-ver16
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dtutil.yml
```
