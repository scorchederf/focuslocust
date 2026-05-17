---
parsed_by: focuslocust
source: lolbas
type: generated
---
# csi.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `csi.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Csi.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [csi.exe](../../tools/windows/csi.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | csi.exe |
| name | csi.exe |
| type | tool |
| source | lolbas |
| url | https://enigma0x3.net/2016/11/17/bypassing-application-whitelisting-by-using-dnx-exe/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@subtee'
  Person: Casey Smith
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: csi.exe {PATH:.cs}
  Description: Use csi.exe to run unsigned C# code.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: CSharp
  Usecase: Local execution of unsigned C# code.
Created: 2018-05-25
Description: Command line interface included with Visual Studio.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_csi_execution.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_csi_use_of_csharp_console.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
Full_Path:
- Path: c:\Program Files (x86)\Microsoft Visual Studio\2017\Community\MSBuild\15.0\Bin\Roslyn\csi.exe
- Path: c:\Program Files (x86)\Microsoft Web Tools\Packages\Microsoft.Net.Compilers.X.Y.Z\tools\csi.exe
Name: csi.exe
Resources:
- Link: https://twitter.com/subTee/status/781208810723549188
- Link: https://enigma0x3.net/2016/11/17/bypassing-application-whitelisting-by-using-dnx-exe/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Csi.yml
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
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_csi_use_of_csharp_console.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_csi_execution.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_csi_execution.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_csi_use_of_csharp_console.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
```
