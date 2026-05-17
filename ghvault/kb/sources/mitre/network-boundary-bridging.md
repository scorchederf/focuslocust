---
parsed_by: focuslocust
source: mitre
type: generated
---
# Network Boundary Bridging

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1599` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Boundary Bridging](../../attack/techniques/T1599-network-boundary-bridging.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1599 |
| name | Network Boundary Bridging |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1599 |

## Preserved Source Material

```yaml
created: '2020-10-19T16:08:29.817Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may bridge network boundaries by compromising perimeter network devices or internal devices responsible
  for network segmentation. Breaching these devices may enable an adversary to bypass restrictions on traffic routing that
  otherwise separate trusted and untrusted networks.


  Devices such as routers and firewalls can be used to create boundaries between trusted and untrusted networks.  They achieve
  this by restricting traffic types to enforce organizational policy in an attempt to reduce the risk inherent in such connections.  Restriction
  of traffic can be achieved by prohibiting IP addresses, layer 4 protocol ports, or through deep packet inspection to identify
  applications.  To participate with the rest of the network, these devices can be directly addressable or transparent, but
  their mode of operation has no bearing on how the adversary can bypass them when compromised.


  When an adversary takes control of such a boundary device, they can bypass its policy enforcement to pass normally prohibited
  traffic across the trust boundary between the two separated networks without hinderance.  By achieving sufficient rights
  on the device, an adversary can reconfigure the device to allow the traffic they want, allowing them to then further achieve
  goals such as command and control via [Multi-hop Proxy](https://attack.mitre.org/techniques/T1090/003) or exfiltration of
  data via [Traffic Duplication](https://attack.mitre.org/techniques/T1020/001). Adversaries may also target internal devices
  responsible for network segmentation and abuse these in conjunction with [Internal Proxy](https://attack.mitre.org/techniques/T1090/001)
  to achieve the same goals.(Citation: Kaspersky ThreatNeedle Feb 2021)  In the cases where a border device separates two
  separate organizations, the adversary can also facilitate lateral movement into new victim environments.'
external_references:
- external_id: T1599
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1599
- description: Vyacheslav Kopeytsev and Seongsu Park. (2021, February 25). Lazarus targets defense industry with ThreatNeedle.
    Retrieved October 27, 2021.
  source_name: Kaspersky ThreatNeedle Feb 2021
  url: https://securelist.com/lazarus-threatneedle/100803/
id: attack-pattern--b8017880-4b1e-42de-ad10-ae7ac6705166
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-16T20:07:53.048Z'
name: Network Boundary Bridging
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Network Devices
x_mitre_version: '2.0'
```
