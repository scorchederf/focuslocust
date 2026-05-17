---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1599 - Network Boundary Bridging

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

## Summary

Adversaries may bridge network boundaries by compromising perimeter network devices or internal devices responsible for network segmentation. Breaching these devices may enable an adversary to bypass restrictions on traffic routing that otherwise separate trusted and untrusted networks.

Devices such as routers and firewalls can be used to create boundaries between trusted and untrusted networks.  They achieve this by restricting traffic types to enforce organizational policy in an attempt to reduce the risk inherent in such connections.  Restriction of traffic can be achieved by prohibiting IP addresses, layer 4 protocol ports, or through deep packet inspection to identify applications.  To participate with the rest of the network, these devices can be directly addressable or transparent, but their mode of operation has no bearing on how the adversary can bypass them when compromised.

When an adversary takes control of such a boundary device, they can bypass its policy enforcement to pass normally prohibited traffic across the trust boundary between the two separated networks without hinderance.  By achieving sufficient rights on the device, an adversary can reconfigure the device to allow the traffic they want, allowing them to then further achieve goals such as command and control via Multi-hop Proxy or exfiltration of data via Traffic Duplication. Adversaries may also target internal devices responsible for network segmentation and abuse these in conjunction with Internal Proxy to achieve the same goals.  In the cases where a border device separates two separate organizations, the adversary can also facilitate lateral movement into new victim environments.

## Source Verification

[source record](../../sources/mitre/network-boundary-bridging.md)

## Evidence Excerpt

```text
created: '2020-10-19T16:08:29.817Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may bridge network boundaries by compromising perimeter network devices or internal devices responsible
for network segmentation. Breaching these devices may enable an adversary to bypass restrictions on traffic routing that
otherwise separate trusted and untrusted networks.
Devices such as routers and firewalls can be used to create boundaries between trusted and untrusted networks.  They achieve
this by restricting traffic types to enforce organizational policy in an attempt to reduce the risk inherent in such connections.  Restriction
of traffic can be achieved by prohibiting IP addresses, layer 4 protocol ports, or through deep packet inspection to identify
```
