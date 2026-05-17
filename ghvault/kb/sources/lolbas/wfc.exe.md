---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Wfc.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wfc.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Wfc.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Wfc.exe](../../tools/windows/wfc.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | wfc.exe |
| name | Wfc.exe |
| type | tool |
| source | lolbas |
| url | https://bohops.com/2020/11/02/exploring-the-wdac-microsoft-recommended-block-rules-part-ii-wfc-fsi/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@mattifestation'
  Person: Matt Graeber
- Handle: '@bohops'
  Person: Jimmy
Author: Jimmy (@bohops)
Code_Sample:
- Code: https://bohops.com/2020/11/02/exploring-the-wdac-microsoft-recommended-block-rules-part-ii-wfc-fsi/
Commands:
- Category: AWL Bypass
  Command: wfc.exe {PATH_ABSOLUTE:.xoml}
  Description: Execute arbitrary C# code embedded in a XOML file.
  MitreID: T1127
  OperatingSystem: Windows 10 2004 (likely previous and newer versions as well)
  Privileges: User
  Tags:
  - Execute: XOML
  Usecase: Execute proxied payload with Microsoft signed binary to bypass WDAC policies
Created: 2021-09-26
Description: The Workflow Command-line Compiler tool is included with the Windows Software Development Kit (SDK).
Detection:
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_wfc.yml
- IOC: As a Windows SDK binary, execution on a system may be suspicious
Full_Path:
- Path: C:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.8 Tools\wfc.exe
Name: Wfc.exe
Resources:
- Link: https://bohops.com/2020/11/02/exploring-the-wdac-microsoft-recommended-block-rules-part-ii-wfc-fsi/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Wfc.yml
```

## Detection / Analysis Notes

```text
BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
```

```text
IOC: As a Windows SDK binary, execution on a system may be suspicious
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_wfc.yml
```

```text
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_wfc.yml
- IOC: As a Windows SDK binary, execution on a system may be suspicious
```
