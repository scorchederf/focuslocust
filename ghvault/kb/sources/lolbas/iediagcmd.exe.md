---
parsed_by: focuslocust
source: lolbas
type: generated
---
# iediagcmd.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `iediagcmd.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Iediagcmd.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [iediagcmd.exe](../../tools/windows/iediagcmd.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iediagcmd.exe |
| name | iediagcmd.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/Hexacorn/status/1507516393859731456 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@hexacorn'
  Person: Adam
Author: manasmbellani
Commands:
- Category: Execute
  Command: set windir=c:\test& cd "C:\Program Files\Internet Explorer\" & iediagcmd.exe /out:{PATH_ABSOLUTE:.cab}
  Description: Executes binary that is pre-planted at C:\test\system32\netsh.exe.
  MitreID: T1218
  OperatingSystem: Windows 10 1803, Windows 10 1703, Windows 10 22H1, Windows 10 22H2, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Spawn a pre-planted executable from iediagcmd.exe.
Created: 2022-03-29
Description: Diagnostics Utility for Internet Explorer
Detection:
- Sigma: https://github.com/manasmbellani/mycode_public/blob/master/sigma/rules/win_proc_creation_lolbin_iediagcmd.yml
- IOC: Sysmon Event ID 1
- IOC: Execution of process iediagcmd.exe with /out could be suspicious
Full_Path:
- Path: C:\Program Files\Internet Explorer\iediagcmd.exe
Name: iediagcmd.exe
Resources:
- Link: https://twitter.com/Hexacorn/status/1507516393859731456
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Iediagcmd.yml
```

## Detection / Analysis Notes

```text
IOC: Execution of process iediagcmd.exe with /out could be suspicious
```

```text
IOC: Sysmon Event ID 1
```

```text
Sigma: https://github.com/manasmbellani/mycode_public/blob/master/sigma/rules/win_proc_creation_lolbin_iediagcmd.yml
```

```text
- Sigma: https://github.com/manasmbellani/mycode_public/blob/master/sigma/rules/win_proc_creation_lolbin_iediagcmd.yml
- IOC: Sysmon Event ID 1
- IOC: Execution of process iediagcmd.exe with /out could be suspicious
```
