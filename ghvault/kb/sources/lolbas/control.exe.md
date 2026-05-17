---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Control.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `control.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Control.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Control.exe](../../tools/windows/control.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | control.exe |
| name | Control.exe |
| type | tool |
| source | lolbas |
| url | https://bohops.com/2018/01/23/loading-alternate-data-stream-ads-dll-cpl-binaries-to-bypass-applocker/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@bohops'
  Person: Jimmy
Author: Oddvar Moe
Commands:
- Category: ADS
  Command: control.exe {PATH_ABSOLUTE}:evil.dll
  Description: Execute evil.dll which is stored in an Alternate Data Stream (ADS).
  MitreID: T1218.002
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Can be used to evade defensive countermeasures or to hide as a persistence mechanism
- Category: Execute
  Command: control.exe {PATH_ABSOLUTE:.cpl}
  Description: Execute .cpl file. A CPL is a DLL file with CPlApplet export function)
  MitreID: T1218.002
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Use to execute code and bypass application whitelisting
Created: 2018-05-25
Description: Binary used to launch controlpanel items in Windows
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules-emerging-threats/2021/Exploits/CVE-2021-40444/proc_creation_win_exploit_cve_2021_40444.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_control_dll_load.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- Elastic: https://github.com/elastic/detection-rules/blob/0875c1e4c4370ab9fbf453c8160bb5abc8ad95e7/rules/windows/defense_evasion_execution_control_panel_suspicious_args.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_unusual_dir_ads.toml
- IOC: Control.exe executing files from alternate data streams
- IOC: Control.exe executing library file without cpl extension
- IOC: Suspicious network connections from control.exe
Full_Path:
- Path: C:\Windows\System32\control.exe
- Path: C:\Windows\SysWOW64\control.exe
Name: Control.exe
Resources:
- Link: https://pentestlab.blog/2017/05/24/applocker-bypass-control-panel/
- Link: https://www.contextis.com/resources/blog/applocker-bypass-registry-key-manipulation/
- Link: https://twitter.com/bohops/status/955659561008017409
- Link: https://docs.microsoft.com/en-us/windows/desktop/shell/executing-control-panel-items
- Link: https://bohops.com/2018/01/23/loading-alternate-data-stream-ads-dll-cpl-binaries-to-bypass-applocker/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Control.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/0875c1e4c4370ab9fbf453c8160bb5abc8ad95e7/rules/windows/defense_evasion_execution_control_panel_suspicious_args.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_unusual_dir_ads.toml
```

```text
IOC: Control.exe executing files from alternate data streams
```

```text
IOC: Control.exe executing library file without cpl extension
```

```text
IOC: Suspicious network connections from control.exe
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules-emerging-threats/2021/Exploits/CVE-2021-40444/proc_creation_win_exploit_cve_2021_40444.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_control_dll_load.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules-emerging-threats/2021/Exploits/CVE-2021-40444/proc_creation_win_exploit_cve_2021_40444.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_control_dll_load.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- Elastic: https://github.com/elastic/detection-rules/blob/0875c1e4c4370ab9fbf453c8160bb5abc8ad95e7/rules/windows/defense_evasion_execution_control_panel_suspicious_args.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_unusual_dir_ads.toml
- IOC: Control.exe executing files from alternate data streams
- IOC: Control.exe executing library file without cpl extension
- IOC: Suspicious network connections from control.exe
```
