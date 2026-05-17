---
parsed_by: focuslocust
source: mitre
type: generated
---
# Web Services

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1584.006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Web Services](../../attack/techniques/T1584.006-web-services.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1584.006 |
| name | Web Services |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1584/006 |

## Preserved Source Material

```yaml
created: '2020-10-01T01:01:00.176Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may compromise access to third-party web services that can be used during targeting. A variety of
  popular websites exist for legitimate users to register for web-based services, such as GitHub, Twitter, Dropbox, Google,
  SendGrid, etc. Adversaries may try to take ownership of a legitimate user''s access to a web service and use that web service
  as infrastructure in support of cyber operations. Such web services can be abused during later stages of the adversary lifecycle,
  such as during Command and Control ([Web Service](https://attack.mitre.org/techniques/T1102)), [Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567),
  or [Phishing](https://attack.mitre.org/techniques/T1566).(Citation: Recorded Future Turla Infra 2020) Using common services,
  such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. By utilizing a web
  service, particularly when access is stolen from legitimate users, adversaries can make it difficult to physically tie back
  operations to them. Additionally, leveraging compromised web-based email services may allow adversaries to leverage the
  trust associated with legitimate domains.'
external_references:
- external_id: T1584.006
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1584/006
- description: 'Insikt Group. (2020, March 12). Swallowing the Snake’s Tail: Tracking Turla Infrastructure. Retrieved September
    16, 2024.'
  source_name: Recorded Future Turla Infra 2020
  url: https://www.recordedfuture.com/research/turla-apt-infrastructure
- description: 'ThreatConnect. (2020, December 15). Infrastructure Research and Hunting: Boiling the Domain Ocean. Retrieved
    October 12, 2021.'
  source_name: ThreatConnect Infrastructure Dec 2020
  url: https://threatconnect.com/blog/infrastructure-research-hunting/
id: attack-pattern--ae797531-3219-49a4-bccf-324ad7a4c7b2
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: resource-development
modified: '2025-10-24T17:49:13.641Z'
name: Web Services
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Dor Edry, Microsoft
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.2'
```
