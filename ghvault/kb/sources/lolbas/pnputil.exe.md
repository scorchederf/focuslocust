---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pnputil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pnputil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pnputil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Pnputil.exe](../../tools/windows/pnputil.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pnputil.exe |
| name | Pnputil.exe |
| type | tool |
| source | lolbas |
| url |  |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@LuxNoBulIshit'
  Person: Hai Vaknin(Lux)
- Handle: '@aloneliassaf'
  Person: Avihay eldad
Author: Hai vaknin (lux)
Code_Sample:
- Code: https://github.com/LuxNoBulIshit/test.inf/blob/main/inf
Commands:
- Category: Execute
  Command: pnputil.exe -i -a {PATH_ABSOLUTE:.inf}
  Description: Used for installing drivers
  MitreID: T1547
  OperatingSystem: Windows 7, Windows 10, Windows 11
  Privileges: Administrator
  Tags:
  - Execute: INF
  Usecase: Add malicious driver
Created: 2020-12-25
Description: Used for installing drivers
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_susp_driver_installed_by_pnputil.yml
Full_Path:
- Path: C:\Windows\system32\pnputil.exe
Name: Pnputil.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pnputil.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_susp_driver_installed_by_pnputil.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_susp_driver_installed_by_pnputil.yml
```
