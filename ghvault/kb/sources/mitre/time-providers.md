---
parsed_by: focuslocust
source: mitre
type: generated
---
# Time Providers

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1547.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Time Providers](../../attack/techniques/T1547.003-time-providers.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1547.003 |
| name | Time Providers |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1547/003 |

## Preserved Source Material

```yaml
created: '2020-01-24T15:51:52.317Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse time providers to execute DLLs when the system boots. The Windows Time service (W32Time)
  enables time synchronization across and within domains.(Citation: Microsoft W32Time Feb 2018) W32Time time providers are
  responsible for retrieving time stamps from hardware/network resources and outputting these values to other network clients.(Citation:
  Microsoft TimeProvider)


  Time providers are implemented as dynamic-link libraries (DLLs) that are registered in the subkeys of `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\W32Time\TimeProviders\`.(Citation:
  Microsoft TimeProvider) The time provider manager, directed by the service control manager, loads and starts time providers
  listed and enabled under this key at system startup and/or whenever parameters are changed.(Citation: Microsoft TimeProvider)


  Adversaries may abuse this architecture to establish persistence, specifically by creating a new arbitrarily named subkey  pointing
  to a malicious DLL in the `DllName` value. Administrator privileges are required for time provider registration, though
  execution will run in context of the Local Service account.(Citation: Github W32Time Oct 2017)'
external_references:
- external_id: T1547.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1547/003
- description: Lundgren, S. (2017, October 28). w32time. Retrieved March 26, 2018.
  source_name: Github W32Time Oct 2017
  url: https://github.com/scottlundgren/w32time
- description: Mathers, B. (2017, May 31). Windows Time Service Tools and Settings. Retrieved March 26, 2018.
  source_name: Microsoft W32Time May 2017
  url: https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings
- description: Microsoft. (2018, February 1). Windows Time Service (W32Time). Retrieved March 26, 2018.
  source_name: Microsoft W32Time Feb 2018
  url: https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-top
- description: Microsoft. (n.d.). Time Provider. Retrieved March 26, 2018.
  source_name: Microsoft TimeProvider
  url: https://msdn.microsoft.com/library/windows/desktop/ms725475.aspx
- description: Russinovich, M. (2016, January 4). Autoruns for Windows v13.51. Retrieved June 6, 2016.
  source_name: TechNet Autoruns
  url: https://technet.microsoft.com/en-us/sysinternals/bb963902
id: attack-pattern--61afc315-860c-4364-825d-0d62b2e91edc
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-24T17:48:51.278Z'
name: Time Providers
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Scott Lundgren, @5twenty9, Carbon Black
- Harun Küßner
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.2'
```
