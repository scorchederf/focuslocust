---
parsed_by: focuslocust
source: mitre
type: generated
---
# Network Service Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1046` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Service Discovery](../../attack/techniques/T1046-network-service-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1046 |
| name | Network Service Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1046 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:43.915Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure\
  \ devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information\
  \ include port, vulnerability, and/or wordlist scans using tools that are brought onto a system.(Citation: CISA AR21-126A\
  \ FIVEHANDS May 2021)   \n\nWithin cloud environments, adversaries may attempt to discover services running on other cloud\
  \ hosts. Additionally, if the cloud environment is connected to a on-premises environment, adversaries may be able to identify\
  \ services running on non-cloud systems as well.\n\nWithin macOS environments, adversaries may use the native Bonjour application\
  \ to discover services running on other macOS hosts within a network. The Bonjour mDNSResponder daemon automatically registers\
  \ and advertises a host’s registered services on the network. For example, adversaries can use a mDNS query (such as <code>dns-sd\
  \ -B _ssh._tcp .</code>) to find other systems broadcasting the ssh service.(Citation: apple doco bonjour description)(Citation:\
  \ macOS APT Activity Bradley)"
external_references:
- external_id: T1046
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1046
- description: Apple Inc. (2013, April 23). Bonjour Overview. Retrieved October 11, 2021.
  source_name: apple doco bonjour description
  url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Introduction.html
- description: CISA. (2021, May 6). Analysis Report (AR21-126A) FiveHands Ransomware. Retrieved June 7, 2021.
  source_name: CISA AR21-126A FIVEHANDS May 2021
  url: https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a
- description: Jaron Bradley. (2021, November 14). What does APT Activity Look Like on macOS?. Retrieved January 19, 2022.
  source_name: macOS APT Activity Bradley
  url: https://themittenmac.com/what-does-apt-activity-look-like-on-macos/
id: attack-pattern--e3a12395-188d-4051-9a16-ea8e14d07b88
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:49:31.494Z'
name: Network Service Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Praetorian
- Aaron Sullivan aka ZerkerEOD
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Containers
- IaaS
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '3.2'
```
