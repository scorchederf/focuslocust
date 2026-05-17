---
parsed_by: focuslocust
source: mitre
type: generated
---
# CDNs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1596.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CDNs](../../attack/techniques/T1596.004-cdns.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1596.004 |
| name | CDNs |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1596/004 |

## Preserved Source Material

```yaml
created: '2020-10-02T16:59:56.648Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may search content delivery network (CDN) data about victims that can be used during targeting.
  CDNs allow an organization to host content from a distributed, load balanced array of servers. CDNs may also allow organizations
  to customize content delivery based on the requestor’s geographical region.


  Adversaries may search CDN data to gather actionable information. Threat actors can use online resources and lookup tools
  to harvest information about content servers within a CDN. Adversaries may also seek and target CDN misconfigurations that
  leak sensitive information not intended to be hosted and/or do not have the same protection mechanisms (ex: login portals)
  as the content hosted on the organization’s website.(Citation: DigitalShadows CDN) Information from these sources may reveal
  opportunities for other forms of reconnaissance (ex: [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Search
  Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583)
  or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [Drive-by Compromise](https://attack.mitre.org/techniques/T1189)).'
external_references:
- external_id: T1596.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1596/004
- description: Swisscom & Digital Shadows. (2017, September 6). Content Delivery Networks (CDNs) Can Leave You Exposed – How
    You Might Be Affected And What You Can Do About It. Retrieved October 20, 2020.
  source_name: DigitalShadows CDN
  url: https://www.digitalshadows.com/blog-and-research/content-delivery-networks-cdns-can-leave-you-exposed-how-you-might-be-affected-and-what-you-can-do-about-it/
id: attack-pattern--91177e6d-b616-4a03-ba4b-f3b32f7dda75
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:49:06.210Z'
name: CDNs
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
- PRE
x_mitre_version: '1.0'
```
