---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ieadvpack.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ieadvpack.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Ieadvpack.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Ieadvpack.dll](../../tools/windows/ieadvpack.dll.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ieadvpack.dll |
| name | Ieadvpack.dll |
| type | tool |
| source | lolbas |
| url | https://bohops.com/2018/03/10/leveraging-inf-sct-fetch-execute-techniques-for-bypass-evasion-persistence-part-2/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@bohops'
  Person: Jimmy (LaunchINFSection)
- Handle: '@0rbz_'
  Person: Fabrizio (RegisterOCX - DLL)
- Handle: '@pabraeken'
  Person: Pierre-Alexandre Braeken (RegisterOCX - CMD)
Author: LOLBAS Team
Code_Sample:
- Code: https://github.com/LOLBAS-Project/LOLBAS-Project.github.io/blob/master/_lolbas/Libraries/Payload/Ieadvpack.inf
- Code: https://github.com/LOLBAS-Project/LOLBAS-Project.github.io/blob/master/_lolbas/Libraries/Payload/Ieadvpack_calc.sct
Commands:
- Category: AWL Bypass
  Command: rundll32.exe ieadvpack.dll,LaunchINFSection {PATH_ABSOLUTE:.inf},DefaultInstall_SingleUser,1,
  Description: Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information
    file directive (section name specified).
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: INF
  Usecase: Run local or remote script(let) code through INF file specification.
- Category: AWL Bypass
  Command: rundll32.exe ieadvpack.dll,LaunchINFSection {PATH_ABSOLUTE:.inf},,1,
  Description: Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information
    file directive (DefaultInstall section implied).
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: INF
  Usecase: Run local or remote script(let) code through INF file specification.
- Category: Execute
  Command: rundll32.exe ieadvpack.dll,RegisterOCX {PATH:.dll}
  Description: Launch a DLL payload by calling the RegisterOCX function.
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Load a DLL payload.
- Category: Execute
  Command: rundll32.exe ieadvpack.dll,RegisterOCX {PATH:.exe}
  Description: Launch an executable by calling the RegisterOCX function.
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Run an executable payload.
- Category: Execute
  Command: rundll32 ieadvpack.dll, RegisterOCX {CMD}
  Description: Launch command line by calling the RegisterOCX function.
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Run an executable payload.
Created: 2018-05-25
Description: INF installer for Internet Explorer. Has much of the same functionality as advpack.dll.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___advpack.yml
Full_Path:
- Path: c:\windows\system32\ieadvpack.dll
- Path: c:\windows\syswow64\ieadvpack.dll
Name: Ieadvpack.dll
Resources:
- Link: https://bohops.com/2018/03/10/leveraging-inf-sct-fetch-execute-techniques-for-bypass-evasion-persistence-part-2/
- Link: https://twitter.com/pabraeken/status/991695411902599168
- Link: https://twitter.com/0rbz_/status/974472392012689408
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Ieadvpack.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___advpack.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___advpack.yml
```
