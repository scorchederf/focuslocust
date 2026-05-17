---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Syssetup.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `syssetup.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Syssetup.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Syssetup.dll](../../tools/windows/syssetup.dll.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | syssetup.dll |
| name | Syssetup.dll |
| type | tool |
| source | lolbas |
| url | https://twitter.com/bohops/status/975549525938135040 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@pabraeken'
  Person: Pierre-Alexandre Braeken (Execute)
- Handle: '@harr0ey'
  Person: Matt harr0ey (Execute)
- Handle: '@bohops'
  Person: Jimmy (Scriptlet)
Author: LOLBAS Team
Code_Sample:
- Code: https://raw.githubusercontent.com/huntresslabs/evading-autoruns/master/shady.inf
- Code: https://gist.github.com/enigma0x3/469d82d1b7ecaf84f4fb9e6c392d25ba#file-backdoor-minimalist-sct
- Code: https://gist.github.com/homjxi0e/87b29da0d4f504cb675bb1140a931415
Commands:
- Category: AWL Bypass
  Command: rundll32 syssetup.dll,SetupInfObjectInstallAction DefaultInstall 128 {PATH_ABSOLUTE:.inf}
  Description: Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information
    file directive (section name specified).
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: INF
  Usecase: Run local or remote script(let) code through INF file specification (Note May pop an error window).
- Category: Execute
  Command: rundll32 syssetup.dll,SetupInfObjectInstallAction DefaultInstall 128 {PATH_ABSOLUTE:.inf}
  Description: Launch an executable file via the SetupInfObjectInstallAction function and .inf file section directive.
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: INF
  Usecase: Load an executable payload.
Created: 2018-05-25
Description: Windows NT System Setup
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___syssetup.yml
Full_Path:
- Path: c:\windows\system32\syssetup.dll
- Path: c:\windows\syswow64\syssetup.dll
Name: Syssetup.dll
Resources:
- Link: https://twitter.com/pabraeken/status/994392481927258113
- Link: https://twitter.com/harr0ey/status/975350238184697857
- Link: https://twitter.com/bohops/status/975549525938135040
- Link: https://windows10dll.nirsoft.net/syssetup_dll.html
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Syssetup.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___syssetup.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___syssetup.yml
```
