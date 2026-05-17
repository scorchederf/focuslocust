---
parsed_by: focuslocust
source: mitre
type: generated
---
# Windows Registry Key Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0063` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows Registry Key Modification](../../attack/data-sources/DC0063-windows-registry-key-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0063 |
| name | Windows Registry Key Modification |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/data-components/DC0063 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Changes made to an existing registry key or its values. These modifications can include altering permissions,\
  \ modifying stored data, or updating configuration settings.\n\n*Data Collection Measures:*\n\n- Windows Event Logs\n  \
  \  - Event ID 4657 - Registry Value Modified: Logs changes to registry values, including modifications to startup entries,\
  \ security settings, or system configurations.\n- Sysmon (System Monitor) for Windows\n    - Sysmon Event ID 13 - Registry\
  \ Value Set: Captures changes to specific registry values.\n    - Sysmon Event ID 14 - Registry Key & Value Renamed: Logs\
  \ renaming of registry keys, which may indicate evasion attempts.\n- Endpoint Detection and Response (EDR) Solutions\n \
  \   - Monitor registry modifications for suspicious behavior."
external_references:
- external_id: DC0063
  source_name: mitre-attack
  url: https://attack.mitre.org/data-components/DC0063
id: x-mitre-data-component--da85d358-741a-410d-9433-20d6269a6170
modified: '2026-03-13T23:12:09.029Z'
name: Windows Registry Key Modification
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- ics-attack
- enterprise-attack
x_mitre_log_sources:
- channel: EventCode=4657
  name: WinEventLog:Security
- channel: EventCode=4663, 4670, 4656
  name: WinEventLog:Security
- channel: StubPath value written under HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components
  name: WinEventLog:Sysmon
- channel: MacroSecuritySettingsChanged or SafeModeDisabled
  name: m365:unified
- channel: EventCode=13, 14
  name: WinEventLog:Sysmon
- channel: modification to Winlogon registry keys such as Shell, Notify, or Userinit
  name: WinEventLog:Security
- channel: Registry key modification HKLM\Software\Policies\Microsoft\Windows NT\DNSClient\EnableMulticast
  name: WinEventLog:Security
- channel: g_CiOptions modification or SIP state change
  name: macos:unifiedlog
- channel: Autoruns reports DLLs in AppInit_DLLs key
  name: WinEventLog:Sysmon
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
