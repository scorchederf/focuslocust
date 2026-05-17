---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pester.bat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pester.bat` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/pester.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Pester.bat](../../tools/windows/pester.bat.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pester.bat |
| name | Pester.bat |
| type | tool |
| source | lolbas |
| url | https://twitter.com/Oddvarmoe/status/993383596244258816 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@p0w3rsh3ll'
  Person: Emin Atac
- Handle: '@_st0pp3r_'
  Person: Stamatis Chatzimangou
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: Pester.bat [/help|?|-?|/?] "$null; {CMD}"
  Description: Execute code using Pester. The third parameter can be anything. The fourth is the payload.
  MitreID: T1216
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Proxy execution
- Category: Execute
  Command: Pester.bat ;{PATH:.exe}
  Description: Execute code using Pester. Example here executes specified executable.
  MitreID: T1216
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Proxy execution
Created: 2018-05-25
Description: Used as part of the Powershell pester
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_pester_1.yml
Full_Path:
- Path: c:\Program Files\WindowsPowerShell\Modules\Pester\<VERSION>\bin\Pester.bat
Name: Pester.bat
Resources:
- Link: https://twitter.com/Oddvarmoe/status/993383596244258816
- Link: https://twitter.com/_st0pp3r_/status/1560072680887525378
- Link: https://twitter.com/_st0pp3r_/status/1560072680887525378
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/pester.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_pester_1.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_pester_1.yml
```
