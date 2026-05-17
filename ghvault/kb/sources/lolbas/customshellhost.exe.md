---
parsed_by: focuslocust
source: lolbas
type: generated
---
# CustomShellHost.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `customshellhost.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/CustomShellHost.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CustomShellHost.exe](../../tools/windows/customshellhost.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | customshellhost.exe |
| name | CustomShellHost.exe |
| type | tool |
| source | lolbas |
| url | https://docs.microsoft.com/en-us/windows/configuration/kiosk-shelllauncher |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@YoSignals'
  Person: John Carroll
Author: Wietze Beukema
Commands:
- Category: Execute
  Command: CustomShellHost.exe
  Description: Executes explorer.exe (with command-line argument /NoShellRegistrationCheck) if present in the current working
    folder.
  MitreID: T1218
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Can be used to evade defensive counter-measures
Created: 2021-11-14
Description: A host process that is used by custom shells when using Windows in Kiosk mode.
Detection:
- IOC: CustomShellHost.exe is unlikely to run on normal workstations
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_lolbin_customshellhost.yml
Full_Path:
- Path: C:\Windows\System32\CustomShellHost.exe
Name: CustomShellHost.exe
Resources:
- Link: https://twitter.com/YoSignals/status/1381353520088113154
- Link: https://docs.microsoft.com/en-us/windows/configuration/kiosk-shelllauncher
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/CustomShellHost.yml
```

## Detection / Analysis Notes

```text
IOC: CustomShellHost.exe is unlikely to run on normal workstations
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_lolbin_customshellhost.yml
```

```text
- IOC: CustomShellHost.exe is unlikely to run on normal workstations
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_lolbin_customshellhost.yml
```
