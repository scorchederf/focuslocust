---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Wsreset.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wsreset.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wsreset.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Wsreset.exe](../../tools/windows/wsreset.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | wsreset.exe |
| name | Wsreset.exe |
| type | tool |
| source | lolbas |
| url | https://github.com/hfiref0x/UACME/blob/master/README.md |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@ihack4falafel'
  Person: Hashim Jawad
Author: Oddvar Moe
Commands:
- Category: UAC Bypass
  Command: wsreset.exe
  Description: During startup, wsreset.exe checks the registry value HKCU\Software\Classes\AppX82a6gwre4fdg3bt635tn5ctqjf8msdd2\Shell\open\command
    for the command to run. Binary will be executed as a high-integrity process without a UAC prompt being displayed to the
    user.
  MitreID: T1548.002
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Usecase: Execute a binary or script as a high-integrity process without a UAC prompt.
Created: 2019-03-18
Description: Used to reset Windows Store settings according to its manifest file
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_uac_bypass_wsreset_integrity_level.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_uac_bypass_wsreset.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/registry/registry_event/registry_event_bypass_via_wsreset.yml#
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/wsreset_uac_bypass.yml
- IOC: wsreset.exe launching child process other than mmc.exe
- IOC: Creation or modification of the registry value HKCU\Software\Classes\AppX82a6gwre4fdg3bt635tn5ctqjf8msdd2\Shell\open\command
- IOC: Microsoft Defender Antivirus as Behavior:Win32/UACBypassExp.T!gen
Full_Path:
- Path: C:\Windows\System32\wsreset.exe
Name: Wsreset.exe
Resources:
- Link: https://www.activecyber.us/activelabs/windows-uac-bypass
- Link: https://twitter.com/ihack4falafel/status/1106644790114947073
- Link: https://github.com/hfiref0x/UACME/blob/master/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wsreset.yml
```

## Detection / Analysis Notes

```text
IOC: Creation or modification of the registry value HKCU\Software\Classes\AppX82a6gwre4fdg3bt635tn5ctqjf8msdd2\Shell\open\command
```

```text
IOC: Microsoft Defender Antivirus as Behavior:Win32/UACBypassExp.T!gen
```

```text
IOC: wsreset.exe launching child process other than mmc.exe
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_uac_bypass_wsreset.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_uac_bypass_wsreset_integrity_level.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/registry/registry_event/registry_event_bypass_via_wsreset.yml#
```

```text
Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/wsreset_uac_bypass.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_uac_bypass_wsreset_integrity_level.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_uac_bypass_wsreset.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/registry/registry_event/registry_event_bypass_via_wsreset.yml#
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/wsreset_uac_bypass.yml
- IOC: wsreset.exe launching child process other than mmc.exe
- IOC: Creation or modification of the registry value HKCU\Software\Classes\AppX82a6gwre4fdg3bt635tn5ctqjf8msdd2\Shell\open\command
- IOC: Microsoft Defender Antivirus as Behavior:Win32/UACBypassExp.T!gen
```
