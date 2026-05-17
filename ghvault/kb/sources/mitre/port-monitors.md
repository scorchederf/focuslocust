---
parsed_by: focuslocust
source: mitre
type: generated
---
# Port Monitors

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1547.010` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Port Monitors](../../attack/techniques/T1547.010-port-monitors.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1547.010 |
| name | Port Monitors |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1547/010 |

## Preserved Source Material

```yaml
created: '2020-01-24T19:46:27.750Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may use port monitors to run an adversary supplied DLL during system boot for persistence or privilege\
  \ escalation. A port monitor can be set through the <code>AddMonitor</code> API call to set a DLL to be loaded at startup.(Citation:\
  \ AddMonitor) This DLL can be located in <code>C:\\Windows\\System32</code> and will be loaded and run by the print spooler\
  \ service, `spoolsv.exe`, under SYSTEM level permissions on boot.(Citation: Bloxham) \n\nAlternatively, an arbitrary DLL\
  \ can be loaded if permissions allow writing a fully-qualified pathname for that DLL to the `Driver` value of an existing\
  \ or new arbitrarily named subkey of <code>HKLM\\SYSTEM\\CurrentControlSet\\Control\\Print\\Monitors</code>. The Registry\
  \ key contains entries for the following:\n\n* Local Port\n* Standard TCP/IP Port\n* USB Monitor\n* WSD Port\n"
external_references:
- external_id: T1547.010
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1547/010
- description: Bloxham, B. (n.d.). Getting Windows to Play with Itself &#91;PowerPoint slides&#93;. Retrieved November 12,
    2014.
  source_name: Bloxham
  url: https://www.defcon.org/images/defcon-22/dc-22-presentations/Bloxham/DEFCON-22-Brady-Bloxham-Windows-API-Abuse-UPDATED.pdf
- description: Microsoft. (n.d.). AddMonitor function. Retrieved September 12, 2024.
  source_name: AddMonitor
  url: https://learn.microsoft.com/en-us/windows/win32/printdocs/addmonitor
- description: Russinovich, M. (2016, January 4). Autoruns for Windows v13.51. Retrieved June 6, 2016.
  source_name: TechNet Autoruns
  url: https://technet.microsoft.com/en-us/sysinternals/bb963902
id: attack-pattern--43881e51-ac74-445b-b4c6-f9f9e9bf23fe
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-24T17:48:42.872Z'
name: Port Monitors
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Stefan Kanthak
- Travis Smith, Tripwire
- Harun Küßner
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.3'
```
