---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Verclsid.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `verclsid.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Verclsid.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Verclsid.exe](../../tools/windows/verclsid.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | verclsid.exe |
| name | Verclsid.exe |
| type | tool |
| source | lolbas |
| url | https://bohops.com/2018/08/18/abusing-the-com-registry-structure-part-2-loading-techniques-for-evasion-and-persistence/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@NickTyrer'
  Person: Nick Tyrer
Author: '@bohops'
Commands:
- Category: Execute
  Command: verclsid.exe /S /C {CLSID}
  Description: Used to verify a COM object before it is instantiated by Windows Explorer
  MitreID: T1218.012
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: COM
  Usecase: Run a COM object created in registry to evade defensive counter measures
Created: 2018-12-04
Description: Used to verify a COM object before it is instantiated by Windows Explorer
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_verclsid_runs_com.yml
- Splunk: https://github.com/splunk/security_content/blob/a1afa0fa605639cbef7d528dec46ce7c8112194a/detections/endpoint/verclsid_clsid_execution.yml
Full_Path:
- Path: C:\Windows\System32\verclsid.exe
- Path: C:\Windows\SysWOW64\verclsid.exe
Name: Verclsid.exe
Resources:
- Link: https://gist.github.com/NickTyrer/0598b60112eaafe6d07789f7964290d5
- Link: https://bohops.com/2018/08/18/abusing-the-com-registry-structure-part-2-loading-techniques-for-evasion-and-persistence/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Verclsid.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_verclsid_runs_com.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/a1afa0fa605639cbef7d528dec46ce7c8112194a/detections/endpoint/verclsid_clsid_execution.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_verclsid_runs_com.yml
- Splunk: https://github.com/splunk/security_content/blob/a1afa0fa605639cbef7d528dec46ce7c8112194a/detections/endpoint/verclsid_clsid_execution.yml
```
