---
parsed_by: focuslocust
source: lolbas
type: generated
---
# VisualUiaVerifyNative.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `visualuiaverifynative.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VisualUiaVerifyNative.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [VisualUiaVerifyNative.exe](../../tools/windows/visualuiaverifynative.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | visualuiaverifynative.exe |
| name | VisualUiaVerifyNative.exe |
| type | tool |
| source | lolbas |
| url | https://bohops.com/2020/10/15/exploring-the-wdac-microsoft-recommended-block-rules-visualuiaverifynative/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@tifkin'
  Person: Lee Christensen
- Handle: '@bohops'
  Person: Jimmy
Author: Jimmy (@bohops)
Commands:
- Category: AWL Bypass
  Command: VisualUiaVerifyNative.exe
  Description: Generate Serialized gadget and save to - `C:\Users\%USERNAME%\AppData\Roaminguiverify.config` before executing.
  MitreID: T1218
  OperatingSystem: Windows 10 2004 (likely previous and newer versions as well)
  Privileges: User
  Tags:
  - Execute: .NetObjects
  Usecase: Execute proxied payload with Microsoft signed binary to bypass WDAC policies
Created: 2021-09-26
Description: A Windows SDK binary for manual and automated testing of Microsoft UI Automation implementation and controls.
Detection:
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_visualuiaverifynative.yml
- IOC: As a Windows SDK binary, execution on a system may be suspicious
Full_Path:
- Path: c:\Program Files (x86)\Windows Kits\10\bin\<version>\arm64\UIAVerify\VisualUiaVerifyNative.exe
- Path: c:\Program Files (x86)\Windows Kits\10\bin\<version>\x64\UIAVerify\VisualUiaVerifyNative.exe
- Path: c:\Program Files (x86)\Windows Kits\10\bin\<version>\UIAVerify\VisualUiaVerifyNative.exe
Name: VisualUiaVerifyNative.exe
Resources:
- Link: https://bohops.com/2020/10/15/exploring-the-wdac-microsoft-recommended-block-rules-visualuiaverifynative/
- Link: https://github.com/MicrosoftDocs/windows-itpro-docs/commit/937db704b9148e9cee7c7010cad4d00ce9c4fdad
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VisualUiaVerifyNative.yml
```

## Detection / Analysis Notes

```text
BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
```

```text
IOC: As a Windows SDK binary, execution on a system may be suspicious
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_visualuiaverifynative.yml
```

```text
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_visualuiaverifynative.yml
- IOC: As a Windows SDK binary, execution on a system may be suspicious
```
