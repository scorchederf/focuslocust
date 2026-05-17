---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Wab.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wab.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wab.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Wab.exe](../../tools/windows/wab.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | wab.exe |
| name | Wab.exe |
| type | tool |
| source | lolbas |
| url | http://www.hexacorn.com/blog/2018/05/01/wab-exe-as-a-lolbin/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@Hexacorn'
  Person: Adam
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: wab.exe
  Description: Change HKLM\Software\Microsoft\WAB\DLLPath and execute DLL of choice
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: Administrator
  Tags:
  - Execute: DLL
  Usecase: Execute dll file. Bypass defensive counter measures
Created: 2018-05-25
Description: Windows address book manager
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/registry/registry_set/registry_set_wab_dllpath_reg_change.yml
- IOC: WAB.exe should normally never be used
Full_Path:
- Path: C:\Program Files\Windows Mail\wab.exe
- Path: C:\Program Files (x86)\Windows Mail\wab.exe
Name: Wab.exe
Resources:
- Link: https://twitter.com/Hexacorn/status/991447379864932352
- Link: http://www.hexacorn.com/blog/2018/05/01/wab-exe-as-a-lolbin/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wab.yml
```

## Detection / Analysis Notes

```text
IOC: WAB.exe should normally never be used
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/registry/registry_set/registry_set_wab_dllpath_reg_change.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/registry/registry_set/registry_set_wab_dllpath_reg_change.yml
- IOC: WAB.exe should normally never be used
```
