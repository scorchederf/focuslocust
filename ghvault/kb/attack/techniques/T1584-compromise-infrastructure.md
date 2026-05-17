---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1584 - Compromise Infrastructure

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1584` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may compromise third-party infrastructure that can be used during targeting. Infrastructure solutions include physical or cloud servers, domains, network devices, and third-party web and DNS services. Instead of buying, leasing, or renting infrastructure an adversary may compromise infrastructure and use it during other phases of the adversary lifecycle. Additionally, adversaries may compromise numerous machines to form a botnet they can leverage.

Use of compromised infrastructure allows adversaries to stage, launch, and execute operations. Compromised infrastructure can help adversary operations blend in with traffic that is seen as normal, such as contact with high reputation or trusted sites. For example, adversaries may leverage compromised infrastructure (potentially also in conjunction with Digital Certificates) to further blend in and support staged information gathering and/or Phishing campaigns. Adversaries may also compromise numerous machines to support Proxy and/or proxyware services or to form a botnet. Additionally, adversaries may compromise infrastructure residing in close proximity to a target in order to gain Initial Access via Wi-Fi Networks.

By using compromised infrastructure, adversaries may enable follow-on malicious operations. Prior to targeting, adversaries may also compromise the infrastructure of other adversaries.

## Source Verification

[source record](../../sources/mitre/compromise-infrastructure.md)

## Evidence Excerpt

```text
created: '2020-10-01T00:36:30.759Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may compromise third-party infrastructure that can be used during targeting. Infrastructure solutions
include physical or cloud servers, domains, network devices, and third-party web and DNS services. Instead of buying, leasing,
or renting infrastructure an adversary may compromise infrastructure and use it during other phases of the adversary lifecycle.(Citation:
Mandiant APT1)(Citation: ICANNDomainNameHijacking)(Citation: Talos DNSpionage Nov 2018)(Citation: FireEye EPS Awakens Part
2) Additionally, adversaries may compromise numerous machines to form a botnet they can leverage.
Use of compromised infrastructure allows adversaries to stage, launch, and execute operations. Compromised infrastructure
```
