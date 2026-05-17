---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Zipfldr.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `zipfldr.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Zipfldr.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Zipfldr.dll](../../tools/windows/zipfldr.dll.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | zipfldr.dll |
| name | Zipfldr.dll |
| type | tool |
| source | lolbas |
| url | https://twitter.com/bohops/status/997896811904929792 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@moriarty_meng'
  Person: Moriarty (Execution)
- Handle: '@r0lan'
  Person: r0lan (Obfuscation)
Author: LOLBAS Team
Commands:
- Category: Execute
  Command: rundll32.exe zipfldr.dll,RouteTheCall {PATH:.exe}
  Description: Launch an executable payload by calling RouteTheCall.
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Launch an executable.
- Category: Execute
  Command: rundll32.exe zipfldr.dll,RouteTheCall file://^C^:^/^W^i^n^d^o^w^s^/^s^y^s^t^e^m^3^2^/^c^a^l^c^.^e^x^e
  Description: Launch an executable payload by calling RouteTheCall (obfuscated).
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Launch an executable.
Created: 2018-05-25
Description: Compressed Folder library
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
Full_Path:
- Path: c:\windows\system32\zipfldr.dll
- Path: c:\windows\syswow64\zipfldr.dll
Name: Zipfldr.dll
Resources:
- Link: https://twitter.com/moriarty_meng/status/977848311603380224
- Link: https://twitter.com/bohops/status/997896811904929792
- Link: https://windows10dll.nirsoft.net/zipfldr_dll.html
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Zipfldr.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```
