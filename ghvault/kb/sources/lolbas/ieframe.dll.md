---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ieframe.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ieframe.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Ieframe.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Ieframe.dll](../../tools/windows/ieframe.dll.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ieframe.dll |
| name | Ieframe.dll |
| type | tool |
| source | lolbas |
| url | http://www.hexacorn.com/blog/2018/03/15/running-programs-via-proxy-jumping-on-a-edr-bypass-trampoline-part-5/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@bohops'
  Person: Jimmy
- Handle: '@hexacorn'
  Person: Adam
Author: LOLBAS Team
Code_Sample:
- Code: https://gist.githubusercontent.com/bohops/89d7b11fa32062cfe31be9fdb18f050e/raw/1206a613a6621da21e7fd164b80a7ff01c5b64ab/calc.url
Commands:
- Category: Execute
  Command: rundll32.exe ieframe.dll,OpenURL {PATH_ABSOLUTE:.url}
  Description: Launch an executable payload via proxy through a(n) URL (information) file by calling OpenURL.
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: URL
  Usecase: Load an executable payload by calling a .url file with or without quotes. The .url file extension can be renamed.
Created: 2018-05-25
Description: Internet Browser DLL for translating HTML code.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
Full_Path:
- Path: c:\windows\system32\ieframe.dll
- Path: c:\windows\syswow64\ieframe.dll
Name: Ieframe.dll
Resources:
- Link: http://www.hexacorn.com/blog/2018/03/15/running-programs-via-proxy-jumping-on-a-edr-bypass-trampoline-part-5/
- Link: https://bohops.com/2018/03/17/abusing-exported-functions-and-exposed-dcom-interfaces-for-pass-thru-command-execution-and-lateral-movement/
- Link: https://twitter.com/bohops/status/997690405092290561
- Link: https://windows10dll.nirsoft.net/ieframe_dll.html
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Ieframe.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```
