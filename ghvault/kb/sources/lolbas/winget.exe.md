---
parsed_by: focuslocust
source: lolbas
type: generated
---
# winget.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `winget.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Winget.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [winget.exe](../../tools/windows/winget.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | winget.exe |
| name | winget.exe |
| type | tool |
| source | lolbas |
| url | https://docs.microsoft.com/en-us/windows/package-manager/winget/#production-recommended |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@saulpanders'
  Person: Paul
- Person: Konrad 'unrooted' Klawikowski
- Person: Fredrik H. Brathen
Author: Paul Sanders
Code_Sample:
- Code: https://gist.github.com/saulpanders/00e1177602a8c01a3a8bfa932b3886b0
Commands:
- Category: Execute
  Command: winget.exe install --manifest {PATH:.yml}
  Description: 'Downloads a file from the web address specified in .yml file and executes it on the system. Local manifest
    setting must be enabled in winget for it to work: `winget settings --enable LocalManifestFiles`'
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: Local Administrator - required to enable local manifest setting
  Tags:
  - Execute: Remote
  - Execute: EXE
  Usecase: Download and execute an arbitrary file from the internet
- Category: Download
  Command: winget.exe install --accept-package-agreements -s msstore {name or ID}
  Description: 'Download and install any software from the Microsoft Store using its name or Store ID, even if the Microsoft
    Store App itself is blocked on the machine. For example, use "Sysinternals Suite" or `9p7knl5rwt25` for obtaining ProcDump,
    PsExec via the Sysinternals Suite. Note: a Microsoft account is required for this.'
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Usecase: Download and install software from Microsoft Store, even if Microsoft Store App is blocked
- Category: AWL Bypass
  Command: winget.exe install --accept-package-agreements -s msstore {name or ID}
  Description: 'Download and install any software from the Microsoft Store using its name or Store ID, even if the Microsoft
    Store App itself is blocked on the machine, and even if AppLocker is active on the machine. For example, use "Sysinternals
    Suite" or `9p7knl5rwt25` for obtaining ProcDump, PsExec via the Sysinternals Suite. Note: a Microsoft account is required
    for this.'
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Usecase: Download and install software from Microsoft Store, even if Microsoft Store App is blocked, and AppLocker is activated
    on the machine
Created: 2022-01-03
Description: Windows Package Manager tool
Detection:
- IOC: winget.exe spawned with local manifest file
- IOC: Sysmon Event ID 1 - Process Creation
- Analysis: https://saulpanders.github.io/2022/01/02/New-Year-New-LOLBAS.html
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_winget_local_install_via_manifest.yml
Full_Path:
- Path: C:\Users\user\AppData\Local\Microsoft\WindowsApps\winget.exe
Name: winget.exe
Resources:
- Link: https://saulpanders.github.io/2022/01/02/New-Year-New-LOLBAS.html
- Link: https://docs.microsoft.com/en-us/windows/package-manager/winget/#production-recommended
- Link: https://www.youtube.com/watch?v=zuL7x4Wltto
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Winget.yml
```

## Detection / Analysis Notes

```text
Analysis: https://saulpanders.github.io/2022/01/02/New-Year-New-LOLBAS.html
```

```text
IOC: Sysmon Event ID 1 - Process Creation
```

```text
IOC: winget.exe spawned with local manifest file
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_winget_local_install_via_manifest.yml
```

```text
- IOC: winget.exe spawned with local manifest file
- IOC: Sysmon Event ID 1 - Process Creation
- Analysis: https://saulpanders.github.io/2022/01/02/New-Year-New-LOLBAS.html
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_winget_local_install_via_manifest.yml
```
