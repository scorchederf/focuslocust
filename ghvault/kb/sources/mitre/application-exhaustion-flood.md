---
parsed_by: focuslocust
source: mitre
type: generated
---
# Application Exhaustion Flood

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1499.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Application Exhaustion Flood](../../attack/techniques/T1499.003-application-exhaustion-flood.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1499.003 |
| name | Application Exhaustion Flood |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1499/003 |

## Preserved Source Material

```yaml
created: '2020-02-20T15:35:00.025Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may target resource intensive features of applications to cause a denial of service (DoS), denying
  availability to those applications. For example, specific features in web applications may be highly resource intensive.
  Repeated requests to those features may be able to exhaust system resources and deny access to the application or the server
  itself.(Citation: Arbor AnnualDoSreport Jan 2018)'
external_references:
- external_id: T1499.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1499/003
- description: Cisco. (n.d.). Detecting and Analyzing Network Threats With NetFlow. Retrieved April 25, 2019.
  source_name: Cisco DoSdetectNetflow
  url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/netflow/configuration/15-mt/nf-15-mt-book/nf-detct-analy-thrts.pdf
- description: Philippe Alcoy, Steinthor Bjarnason, Paul Bowen, C.F. Chui, Kirill Kasavchnko, and Gary Sockrider of Netscout
    Arbor. (2018, January). Insight into the Global Threat Landscape - Netscout Arbor's 13th Annual Worldwide Infrastructure
    Security Report. Retrieved April 22, 2019.
  source_name: Arbor AnnualDoSreport Jan 2018
  url: https://pages.arbornetworks.com/rs/082-KNA-087/images/13th_Worldwide_Infrastructure_Security_Report.pdf
id: attack-pattern--18cffc21-3260-437e-80e4-4ab8bf2ba5e9
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: impact
modified: '2025-10-24T17:48:27.259Z'
name: Application Exhaustion Flood
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_impact_type:
- Availability
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
- IaaS
- Linux
- macOS
x_mitre_version: '1.3'
```
