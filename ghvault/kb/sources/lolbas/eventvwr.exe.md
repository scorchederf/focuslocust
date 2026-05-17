---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Eventvwr.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `eventvwr.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Eventvwr.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Eventvwr.exe](../../tools/windows/eventvwr.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | eventvwr.exe |
| name | Eventvwr.exe |
| type | tool |
| source | lolbas |
| url | https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@enigma0x3'
  Person: Matt Nelson
- Handle: '@mattifestation'
  Person: Matt Graeber
- Handle: '@orange_8361'
  Person: Orange Tsai
Author: Jacob Gajek
Code_Sample:
- Code: https://github.com/enigma0x3/Misc-PowerShell-Stuff/blob/master/Invoke-EventVwrBypass.ps1
Commands:
- Category: UAC Bypass
  Command: eventvwr.exe
  Description: During startup, eventvwr.exe checks the registry value `HKCU\Software\Classes\mscfile\shell\open\command` for
    the location of mmc.exe, which is used to open the eventvwr.msc saved console file. If the location of another binary
    or script is added to this registry value, it will be executed as a high-integrity process without a UAC prompt being
    displayed to the user.
  MitreID: T1548.002
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
  Privileges: User
  Tags:
  - Application: GUI
  - Execute: EXE
  Usecase: Execute a binary or script as a high-integrity process without a UAC prompt.
- Category: UAC Bypass
  Command: ysoserial.exe -o raw -f BinaryFormatter - g DataSet -c "{CMD}" > RecentViews & copy RecentViews %LOCALAPPDATA%\Microsoft\EventV~1\RecentViews
    & eventvwr.exe
  Description: During startup, eventvwr.exe uses .NET deserialization with `%LOCALAPPDATA%\Microsoft\EventV~1\RecentViews`
    file. This file can be created using https://github.com/pwntester/ysoserial.net
  MitreID: T1548.002
  OperatingSystem: Windows 7, Windows 8, Windows 8.1, Windows 10
  Privileges: Administrator
  Tags:
  - Application: GUI
  - Execute: .NetObjects
  Usecase: Execute a command to bypass security restrictions that limit the use of command-line interpreters.
Created: 2018-11-01
Description: Displays Windows Event Logs in a GUI window.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_uac_bypass_eventvwr.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/registry/registry_set/registry_set_uac_bypass_eventvwr.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/file/file_event/file_event_win_uac_bypass_eventvwr.yml
- Elastic: https://github.com/elastic/detection-rules/blob/d31ea6253ea40789b1fc49ade79b7ec92154d12a/rules/windows/privilege_escalation_uac_bypass_event_viewer.toml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/eventvwr_uac_bypass.yml
- IOC: eventvwr.exe launching child process other than mmc.exe
- IOC: Creation or modification of the registry value HKCU\Software\Classes\mscfile\shell\open\command
Full_Path:
- Path: C:\Windows\System32\eventvwr.exe
- Path: C:\Windows\SysWOW64\eventvwr.exe
Name: Eventvwr.exe
Resources:
- Link: https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/
- Link: https://github.com/enigma0x3/Misc-PowerShell-Stuff/blob/master/Invoke-EventVwrBypass.ps1
- Link: https://twitter.com/orange_8361/status/1518970259868626944
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Eventvwr.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/d31ea6253ea40789b1fc49ade79b7ec92154d12a/rules/windows/privilege_escalation_uac_bypass_event_viewer.toml
```

```text
IOC: Creation or modification of the registry value HKCU\Software\Classes\mscfile\shell\open\command
```

```text
IOC: eventvwr.exe launching child process other than mmc.exe
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/file/file_event/file_event_win_uac_bypass_eventvwr.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_uac_bypass_eventvwr.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/registry/registry_set/registry_set_uac_bypass_eventvwr.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/eventvwr_uac_bypass.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_uac_bypass_eventvwr.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/registry/registry_set/registry_set_uac_bypass_eventvwr.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/file/file_event/file_event_win_uac_bypass_eventvwr.yml
- Elastic: https://github.com/elastic/detection-rules/blob/d31ea6253ea40789b1fc49ade79b7ec92154d12a/rules/windows/privilege_escalation_uac_bypass_event_viewer.toml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/eventvwr_uac_bypass.yml
- IOC: eventvwr.exe launching child process other than mmc.exe
- IOC: Creation or modification of the registry value HKCU\Software\Classes\mscfile\shell\open\command
```
