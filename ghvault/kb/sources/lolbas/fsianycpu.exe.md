---
parsed_by: focuslocust
source: lolbas
type: generated
---
# FsiAnyCpu.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `fsianycpu.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/FsiAnyCpu.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [FsiAnyCpu.exe](../../tools/windows/fsianycpu.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | fsianycpu.exe |
| name | FsiAnyCpu.exe |
| type | tool |
| source | lolbas |
| url | https://bohops.com/2020/11/02/exploring-the-wdac-microsoft-recommended-block-rules-part-ii-wfc-fsi/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@NickTyrer'
  Person: Nick Tyrer
- Handle: '@bohops'
  Person: Jimmy
Author: Jimmy (@bohops)
Code_Sample:
- Code: https://gist.github.com/NickTyrer/51eb8c774a909634fa69b4d06fc79ae1
Commands:
- Category: AWL Bypass
  Command: fsianycpu.exe {PATH:.fsscript}
  Description: Execute F# code via script file
  MitreID: T1059
  OperatingSystem: Windows 10 2004 (likely previous and newer versions as well)
  Privileges: User
  Tags:
  - Execute: FSharp
  Usecase: Execute payload with Microsoft signed binary to bypass WDAC policies
- Category: AWL Bypass
  Command: fsianycpu.exe
  Description: Execute F# code via interactive command line
  MitreID: T1059
  OperatingSystem: Windows 10 2004 (likely previous and newer versions as well)
  Privileges: User
  Tags:
  - Execute: FSharp
  Usecase: Execute payload with Microsoft signed binary to bypass WDAC policies
Created: 2021-09-26
Description: 32/64-bit FSharp (F#) Interpreter included with Visual Studio.
Detection:
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: FsiAnyCpu.exe execution may be suspicious on non-developer machines
- Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_fsharp_interpreters.yml
Full_Path:
- Path: c:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\CommonExtensions\Microsoft\FSharp\fsianycpu.exe
Name: FsiAnyCpu.exe
Resources:
- Link: https://bohops.com/2020/11/02/exploring-the-wdac-microsoft-recommended-block-rules-part-ii-wfc-fsi/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/FsiAnyCpu.yml
```

## Detection / Analysis Notes

```text
BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
```

```text
IOC: FsiAnyCpu.exe execution may be suspicious on non-developer machines
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_fsharp_interpreters.yml
```

```text
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: FsiAnyCpu.exe execution may be suspicious on non-developer machines
- Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_fsharp_interpreters.yml
```
