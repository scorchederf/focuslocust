---
parsed_by: focuslocust
source: mitre
type: generated
---
# Protocol or Service Impersonation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1001.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Protocol or Service Impersonation](../../attack/techniques/T1001.003-protocol-or-service-impersonation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1001.003 |
| name | Protocol or Service Impersonation |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1001/003 |

## Preserved Source Material

```yaml
created: '2020-03-15T00:40:27.503Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may impersonate legitimate protocols or web service traffic to disguise command and control activity\
  \ and thwart analysis efforts. By impersonating legitimate protocols or web services, adversaries can make their command\
  \ and control traffic blend in with legitimate network traffic.  \n\nAdversaries may impersonate a fake SSL/TLS handshake\
  \ to make it look like subsequent traffic is SSL/TLS encrypted, potentially interfering with some security tooling, or to\
  \ make the traffic look like it is related with a trusted entity. \n\nAdversaries may also leverage legitimate protocols\
  \ to impersonate expected web traffic or trusted services. For example, adversaries may manipulate HTTP headers, URI endpoints,\
  \ SSL certificates, and transmitted data to disguise C2 communications or mimic legitimate services such as Gmail, Google\
  \ Drive, and Yahoo Messenger.(Citation: ESET Okrum July 2019)(Citation: Malleable-C2-U42)"
external_references:
- external_id: T1001.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1001/003
- description: 'Chris Navarrete Durgesh Sangvikar Andrew Guan Yu Fu Yanhui Jia Siddhart Shibiraj. (2022, March 16). Cobalt
    Strike Analysis and Tutorial: How Malleable C2 Profiles Make Cobalt Strike Difficult to Detect. Retrieved September 24,
    2024.'
  source_name: Malleable-C2-U42
  url: https://unit42.paloaltonetworks.com/cobalt-strike-malleable-c2-profile/
- description: Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting.
    Retrieved April 20, 2016.
  source_name: University of Birmingham C2
  url: https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf
- description: 'Hromcova, Z. (2019, July). OKRUM AND KETRICAN: AN OVERVIEW OF RECENT KE3CHANG GROUP ACTIVITY. Retrieved May
    6, 2020.'
  source_name: ESET Okrum July 2019
  url: https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf
id: attack-pattern--c325b232-d5bc-4dde-a3ec-71f3db9e8adc
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-24T17:49:20.574Z'
name: Protocol or Service Impersonation
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- James Emery-Callcott, Emerging Threats Team, Proofpoint
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Windows
x_mitre_version: '2.1'
```
