---
parsed_by: focuslocust
source: mitre
type: generated
---
# Web Portal Capture

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1056.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Web Portal Capture](../../attack/techniques/T1056.003-web-portal-capture.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1056.003 |
| name | Web Portal Capture |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1056/003 |

## Preserved Source Material

```yaml
created: '2020-02-11T18:59:50.058Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may install code on externally facing portals, such as a VPN login page, to capture and transmit
  credentials of users who attempt to log into the service. For example, a compromised login page may log provided user credentials
  before logging the user in to the service.


  This variation on input capture may be conducted post-compromise using legitimate administrative access as a backup measure
  to maintain network access through [External Remote Services](https://attack.mitre.org/techniques/T1133) and [Valid Accounts](https://attack.mitre.org/techniques/T1078)
  or as part of the initial compromise by exploitation of the externally facing web service.(Citation: Volexity Virtual Private
  Keylogging)'
external_references:
- external_id: T1056.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1056/003
- description: 'Adair, S. (2015, October 7). Virtual Private Keylogging: Cisco Web VPNs Leveraged for Access and Persistence.
    Retrieved March 20, 2017.'
  source_name: Volexity Virtual Private Keylogging
  url: https://www.volexity.com/blog/2015/10/07/virtual-private-keylogging-cisco-web-vpns-leveraged-for-access-and-persistence/
id: attack-pattern--69e5226d-05dc-4f15-95d7-44f5ed78d06e
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:54.254Z'
name: Web Portal Capture
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.1'
```
