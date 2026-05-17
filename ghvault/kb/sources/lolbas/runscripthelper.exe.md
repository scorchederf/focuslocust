---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Runscripthelper.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `runscripthelper.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Runscripthelper.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Runscripthelper.exe](../../tools/windows/runscripthelper.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | runscripthelper.exe |
| name | Runscripthelper.exe |
| type | tool |
| source | lolbas |
| url | https://posts.specterops.io/bypassing-application-whitelisting-with-runscripthelper-exe-1906923658fc |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@mattifestation'
  Person: Matt Graeber
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: runscripthelper.exe surfacecheck \\?\{PATH_ABSOLUTE:.txt} {PATH_ABSOLUTE:folder}
  Description: Execute the PowerShell script with .txt extension
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
  Privileges: User
  Tags:
  - Execute: PowerShell
  Usecase: Bypass constrained language mode and execute Powershell script
Created: 2018-05-25
Description: Execute target PowerShell script
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_runscripthelper.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: Event ID 4104 - Microsoft-Windows-PowerShell/Operational
- IOC: Event ID 400 - Windows PowerShell
Full_Path:
- Path: C:\Windows\WinSxS\amd64_microsoft-windows-u..ed-telemetry-client_31bf3856ad364e35_10.0.16299.15_none_c2df1bba78111118\Runscripthelper.exe
- Path: C:\Windows\WinSxS\amd64_microsoft-windows-u..ed-telemetry-client_31bf3856ad364e35_10.0.16299.192_none_ad4699b571e00c4a\Runscripthelper.exe
Name: Runscripthelper.exe
Resources:
- Link: https://posts.specterops.io/bypassing-application-whitelisting-with-runscripthelper-exe-1906923658fc
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Runscripthelper.yml
```

## Detection / Analysis Notes

```text
BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
```

```text
IOC: Event ID 400 - Windows PowerShell
```

```text
IOC: Event ID 4104 - Microsoft-Windows-PowerShell/Operational
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_runscripthelper.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_runscripthelper.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: Event ID 4104 - Microsoft-Windows-PowerShell/Operational
- IOC: Event ID 400 - Windows PowerShell
```
