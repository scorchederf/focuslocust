---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Url.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `url.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Url.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Url.dll](../../tools/windows/url.dll.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | url.dll |
| name | Url.dll |
| type | tool |
| source | lolbas |
| url | https://bohops.com/2018/03/17/abusing-exported-functions-and-exposed-dcom-interfaces-for-pass-thru-command-execution-and-lateral-movement/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@hexacorn'
  Person: Adam (OpenURL)
- Handle: '@bohops'
  Person: Jimmy (OpenURL)
- Handle: '@DissectMalware'
  Person: Malwrologist (FileProtocolHandler - HTA)
- Handle: '@r0lan'
  Person: r0lan (Obfuscation)
Author: LOLBAS Team
Commands:
- Category: Execute
  Command: rundll32.exe url.dll,OpenURL {PATH_ABSOLUTE:.hta}
  Description: Launch a HTML application payload by calling OpenURL.
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: HTA
  Usecase: Invoke an HTML Application via mshta.exe (Default Handler).
- Category: Execute
  Command: rundll32.exe url.dll,OpenURL {PATH_ABSOLUTE:.url}
  Description: Launch an executable payload via proxy through a .url (information) file by calling OpenURL.
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: URL
  Usecase: Load an executable payload by calling a .url file.
- Category: Execute
  Command: rundll32.exe url.dll,OpenURL file://^C^:^/^W^i^n^d^o^w^s^/^s^y^s^t^e^m^3^2^/^c^a^l^c^.^e^x^e
  Description: Launch an executable by calling OpenURL.
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Load an executable payload by specifying the file protocol handler (obfuscated).
- Category: Execute
  Command: rundll32.exe url.dll,FileProtocolHandler {PATH_ABSOLUTE:.exe}
  Description: Launch an executable by calling FileProtocolHandler.
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Launch an executable.
- Category: Execute
  Command: rundll32.exe url.dll,FileProtocolHandler file://^C^:^/^W^i^n^d^o^w^s^/^s^y^s^t^e^m^3^2^/^c^a^l^c^.^e^x^e
  Description: Launch an executable by calling FileProtocolHandler.
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Load an executable payload by specifying the file protocol handler (obfuscated).
- Category: Execute
  Command: rundll32.exe url.dll,FileProtocolHandler file:///C:/test/test.hta
  Description: Launch a HTML application payload by calling FileProtocolHandler.
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: HTA
  Usecase: Invoke an HTML Application via mshta.exe (Default Handler).
Created: 2018-05-25
Description: Internet Shortcut Shell Extension DLL.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
Full_Path:
- Path: c:\windows\system32\url.dll
- Path: c:\windows\syswow64\url.dll
Name: Url.dll
Resources:
- Link: https://bohops.com/2018/03/17/abusing-exported-functions-and-exposed-dcom-interfaces-for-pass-thru-command-execution-and-lateral-movement/
- Link: https://twitter.com/DissectMalware/status/995348436353470465
- Link: https://twitter.com/bohops/status/974043815655956481
- Link: https://twitter.com/yeyint_mth/status/997355558070927360
- Link: https://twitter.com/Hexacorn/status/974063407321223168
- Link: https://windows10dll.nirsoft.net/url_dll.html
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Url.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```
