---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Setupapi.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `setupapi.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Setupapi.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Setupapi.dll](../../tools/windows/setupapi.dll.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | setupapi.dll |
| name | Setupapi.dll |
| type | tool |
| source | lolbas |
| url | https://github.com/huntresslabs/evading-autoruns |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@KyleHanslovan'
  Person: Kyle Hanslovan (COM Scriptlet)
- Handle: '@HuntressLabs'
  Person: Huntress Labs (COM Scriptlet)
- Handle: '@subTee'
  Person: Casey Smith (COM Scriptlet)
- Handle: '@ItsReallyNick'
  Person: Nick Carr (Threat Intel)
Author: LOLBAS Team
Code_Sample:
- Code: https://raw.githubusercontent.com/huntresslabs/evading-autoruns/master/shady.inf
- Code: https://gist.github.com/enigma0x3/469d82d1b7ecaf84f4fb9e6c392d25ba#file-backdoor-minimalist-sct
- Code: https://gist.githubusercontent.com/enigma0x3/469d82d1b7ecaf84f4fb9e6c392d25ba/raw/6cb52b88bcc929f5555cd302d9ed848b7e407052/Backdoor-Minimalist.sct
- Code: https://gist.githubusercontent.com/bohops/0cc6586f205f3691e04a1ebf1806aabd/raw/baf7b29891bb91e76198e30889fbf7d6642e8974/calc_exe.inf
Commands:
- Category: AWL Bypass
  Command: rundll32.exe setupapi.dll,InstallHinfSection DefaultInstall 128 {PATH_ABSOLUTE:.inf}
  Description: Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information
    file directive (section name specified).
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: INF
  Usecase: Run local or remote script(let) code through INF file specification.
- Category: Execute
  Command: rundll32.exe setupapi.dll,InstallHinfSection DefaultInstall 128 {PATH_ABSOLUTE:.inf}
  Description: Launch an executable file via the InstallHinfSection function and .inf file section directive.
  MitreID: T1218.011
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: INF
  Usecase: Load an executable payload.
Created: 2018-05-25
Description: Windows Setup Application Programming Interface
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_rundll32_setupapi_installhinfsection.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___setupapi.yml
Full_Path:
- Path: c:\windows\system32\setupapi.dll
- Path: c:\windows\syswow64\setupapi.dll
Name: Setupapi.dll
Resources:
- Link: https://github.com/huntresslabs/evading-autoruns
- Link: https://twitter.com/pabraeken/status/994742106852941825
- Link: https://windows10dll.nirsoft.net/setupapi_dll.html
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Setupapi.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_rundll32_setupapi_installhinfsection.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___setupapi.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_rundll32_setupapi_installhinfsection.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___setupapi.yml
```
