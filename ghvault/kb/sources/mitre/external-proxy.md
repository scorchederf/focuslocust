---
parsed_by: focuslocust
source: mitre
type: generated
---
# External Proxy

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1090.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [External Proxy](../../attack/techniques/T1090.002-external-proxy.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1090.002 |
| name | External Proxy |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1090/002 |

## Preserved Source Material

```yaml
created: '2020-03-14T23:12:18.466Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use an external proxy to act as an intermediary for network communications to a command and
  control server to avoid direct connections to their infrastructure. Many tools exist that enable traffic redirection through
  proxies or port redirection, including [HTRAN](https://attack.mitre.org/software/S0040), ZXProxy, and ZXPortMap. (Citation:
  Trend Micro APT Attack Tools) Adversaries use these types of proxies to manage command and control communications, to provide
  resiliency in the face of connection loss, or to ride over existing trusted communications paths to avoid suspicion.


  External connection proxies are used to mask the destination of C2 traffic and are typically implemented with port redirectors.
  Compromised systems outside of the victim environment may be used for these purposes, as well as purchased infrastructure
  such as cloud-based resources or virtual private servers. Proxies may be chosen based on the low likelihood that a connection
  to them from a compromised system would be investigated. Victim systems would communicate directly with the external proxy
  on the Internet and then the proxy would forward communications to the C2 server.'
external_references:
- external_id: T1090.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1090/002
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
- description: 'Wilhoit, K. (2013, March 4). In-Depth Look: APT Attack Tools of the Trade. Retrieved December 2, 2015.'
  source_name: Trend Micro APT Attack Tools
  url: http://blog.trendmicro.com/trendlabs-security-intelligence/in-depth-look-apt-attack-tools-of-the-trade/
id: attack-pattern--69b8fd78-40e8-4600-ae4d-662c9d7afdb3
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:48:54.165Z'
name: External Proxy
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
- ESXi
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.3'
```
