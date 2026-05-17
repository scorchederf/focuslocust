---
parsed_by: focuslocust
source: lolbas
type: generated
---
# ntdsutil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ntdsutil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Ntdsutil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ntdsutil.exe](../../tools/windows/ntdsutil.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ntdsutil.exe |
| name | ntdsutil.exe |
| type | tool |
| source | lolbas |
| url | https://adsecurity.org/?p=2398#CreateIFM |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@PyroTek3'
  Person: Sean Metcalf
Author: Tony Lambert
Commands:
- Category: Dump
  Command: ntdsutil.exe "ac i ntds" "ifm" "create full c:\" q q
  Description: Dump NTDS.dit into folder
  MitreID: T1003.003
  OperatingSystem: Windows
  Privileges: Administrator
  Usecase: Dumping of Active Directory NTDS.dit database
Created: 2020-01-10
Description: Command line utility used to export Active Directory.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_ntdsutil_usage.yml
- Splunk: https://github.com/splunk/security_content/blob/2b87b26bdc2a84b65b1355ffbd5174bdbdb1879c/detections/endpoint/ntdsutil_export_ntds.yml
- Elastic: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
- IOC: ntdsutil.exe with command line including "ifm"
Full_Path:
- Path: C:\Windows\System32\ntdsutil.exe
Name: ntdsutil.exe
Resources:
- Link: https://adsecurity.org/?p=2398#CreateIFM
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Ntdsutil.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
```

```text
IOC: ntdsutil.exe with command line including "ifm"
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_ntdsutil_usage.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/2b87b26bdc2a84b65b1355ffbd5174bdbdb1879c/detections/endpoint/ntdsutil_export_ntds.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_ntdsutil_usage.yml
- Splunk: https://github.com/splunk/security_content/blob/2b87b26bdc2a84b65b1355ffbd5174bdbdb1879c/detections/endpoint/ntdsutil_export_ntds.yml
- Elastic: https://github.com/elastic/detection-rules/blob/5bdf70e72c6cd4547624c521108189af994af449/rules/windows/credential_access_cmdline_dump_tool.toml
- IOC: ntdsutil.exe with command line including "ifm"
```
