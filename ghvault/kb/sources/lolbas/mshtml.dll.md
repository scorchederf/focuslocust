---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Mshtml.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `mshtml.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Mshtml.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Mshtml.dll](../../tools/windows/mshtml.dll.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mshtml.dll |
| name | Mshtml.dll |
| type | tool |
| source | lolbas |
| url | https://twitter.com/pabraeken/status/998567549670477824 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@pabraeken'
  Person: Pierre-Alexandre Braeken
Author: LOLBAS Team
Commands:
- Category: Execute
  Command: rundll32.exe Mshtml.dll,PrintHTML {PATH_ABSOLUTE:.hta}
  Description: 'Invoke an HTML Application via mshta.exe (note: pops a security warning and a print dialogue box).'
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: HTA
  Usecase: Launch an HTA application.
Created: 2018-05-25
Description: Microsoft HTML Viewer
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
Full_Path:
- Path: c:\windows\system32\mshtml.dll
- Path: c:\windows\syswow64\mshtml.dll
Name: Mshtml.dll
Resources:
- Link: https://twitter.com/pabraeken/status/998567549670477824
- Link: https://windows10dll.nirsoft.net/mshtml_dll.html
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Mshtml.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```
