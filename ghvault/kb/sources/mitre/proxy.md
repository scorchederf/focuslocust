---
parsed_by: focuslocust
source: mitre
type: generated
---
# Proxy

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1090` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Proxy](../../attack/techniques/T1090-proxy.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1090 |
| name | Proxy |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1090 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:08.479Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use a connection proxy to direct network traffic between systems or act as an intermediary for
  network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist
  that enable traffic redirection through proxies or port redirection, including [HTRAN](https://attack.mitre.org/software/S0040),
  ZXProxy, and ZXPortMap. (Citation: Trend Micro APT Attack Tools) Adversaries use these types of proxies to manage command
  and control communications, reduce the number of simultaneous outbound network connections, provide resiliency in the face
  of connection loss, or to ride over existing trusted communications paths between victims to avoid suspicion. Adversaries
  may chain together multiple proxies to further disguise the source of malicious traffic.


  Adversaries can also take advantage of routing schemes in Content Delivery Networks (CDNs) to proxy command and control
  traffic.'
external_references:
- external_id: T1090
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1090
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
- description: 'Wilhoit, K. (2013, March 4). In-Depth Look: APT Attack Tools of the Trade. Retrieved December 2, 2015.'
  source_name: Trend Micro APT Attack Tools
  url: http://blog.trendmicro.com/trendlabs-security-intelligence/in-depth-look-apt-attack-tools-of-the-trade/
id: attack-pattern--731f4f55-b6d0-41d1-a7a9-072a66389aea
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:48:57.330Z'
name: Proxy
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Jon Sheedy
- Heather Linn
- Walker Johnson
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '3.2'
```
