---
parsed_by: focuslocust
source: lolbas
type: generated
---
# AppCert.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `appcert.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Appcert.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AppCert.exe](../../tools/windows/appcert.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | appcert.exe |
| name | AppCert.exe |
| type | tool |
| source | lolbas |
| url | https://learn.microsoft.com/windows/win32/win_cert/using-the-windows-app-certification-kit |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
  Command: appcert.exe test -apptype desktop -setuppath {PATH_ABSOLUTE:.exe} -reportoutputpath {PATH_ABSOLUTE:.xml}
  Description: Execute an executable file via the Windows App Certification Kit command-line tool.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: Administrator
  Tags:
  - Execute: EXE
  Usecase: Performs execution of specified file, can be used as a defense evasion
- Category: Execute
  Command: appcert.exe test -apptype desktop -setuppath {PATH_ABSOLUTE:.msi} -setupcommandline /q -reportoutputpath {PATH_ABSOLUTE:.xml}
  Description: Install an MSI file via an msiexec instance spawned via appcert.exe as parent process.
  MitreID: T1218.007
  OperatingSystem: Windows
  Privileges: Administrator
  Tags:
  - Execute: MSI
  Usecase: Execute custom made MSI file with malicious code
Created: 2024-03-06
Description: Windows App Certification Kit command-line tool.
Full_Path:
- Path: C:\Program Files (x86)\Windows Kits\10\App Certification Kit\appcert.exe
- Path: C:\Program Files\Windows Kits\10\App Certification Kit\appcert.exe
Name: AppCert.exe
Resources:
- Link: https://learn.microsoft.com/windows/win32/win_cert/using-the-windows-app-certification-kit
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Appcert.yml
```
