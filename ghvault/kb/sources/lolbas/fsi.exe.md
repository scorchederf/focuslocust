---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Fsi.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `fsi.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Fsi.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Fsi.exe](../../tools/windows/fsi.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | fsi.exe |
| name | Fsi.exe |
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
  Command: fsi.exe {PATH:.fsscript}
  Description: Execute F# code via script file
  MitreID: T1059
  OperatingSystem: Windows 10 2004 (likely previous and newer versions as well)
  Privileges: User
  Tags:
  - Execute: FSharp
  Usecase: Execute payload with Microsoft signed binary to bypass WDAC policies
- Category: AWL Bypass
  Command: fsi.exe
  Description: Execute F# code via interactive command line
  MitreID: T1059
  OperatingSystem: Windows 10 2004 (likely previous and newer versions as well)
  Privileges: User
  Tags:
  - Execute: FSharp
  Usecase: Execute payload with Microsoft signed binary to bypass WDAC policies
Created: 2021-09-26
Description: 64-bit FSharp (F#) Interpreter included with Visual Studio and DotNet Core SDK.
Detection:
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: Fsi.exe execution may be suspicious on non-developer machines
- Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_fsharp_interpreters.yml
Full_Path:
- Path: C:\Program Files\dotnet\sdk\<version>\FSharp\fsi.exe
- Path: C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\CommonExtensions\Microsoft\FSharp\fsi.exe
Name: Fsi.exe
Resources:
- Link: https://twitter.com/NickTyrer/status/904273264385589248
- Link: https://bohops.com/2020/11/02/exploring-the-wdac-microsoft-recommended-block-rules-part-ii-wfc-fsi/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Fsi.yml
```

## Detection / Analysis Notes

```text
BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
```

```text
IOC: Fsi.exe execution may be suspicious on non-developer machines
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_fsharp_interpreters.yml
```

```text
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: Fsi.exe execution may be suspicious on non-developer machines
- Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_fsharp_interpreters.yml
```
