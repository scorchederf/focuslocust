---
parsed_by: focuslocust
source: lolbas
type: generated
---
# rcsi.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `rcsi.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Rcsi.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [rcsi.exe](../../tools/windows/rcsi.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rcsi.exe |
| name | rcsi.exe |
| type | tool |
| source | lolbas |
| url | https://enigma0x3.net/2016/11/21/bypassing-application-whitelisting-by-using-rcsi-exe/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@enigma0x3'
  Person: Matt Nelson
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: rcsi.exe {PATH:.csx}
  Description: Use embedded C# within the csx script to execute the code.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: CSharp
  Usecase: Local execution of arbitrary C# code stored in local CSX file.
- Category: AWL Bypass
  Command: rcsi.exe {PATH:.csx}
  Description: Use embedded C# within the csx script to execute the code.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: CSharp
  Usecase: Local execution of arbitrary C# code stored in local CSX file.
Created: 2018-05-25
Description: Non-Interactive command line inerface included with Visual Studio.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_csi_execution.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- BlockRule: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_csi_execution.yml
Full_Path:
- Path: no default
Name: rcsi.exe
Resources:
- Link: https://enigma0x3.net/2016/11/21/bypassing-application-whitelisting-by-using-rcsi-exe/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Rcsi.yml
```

## Detection / Analysis Notes

```text
BlockRule: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_csi_execution.yml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_csi_execution.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_csi_execution.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- BlockRule: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_csi_execution.yml
```
