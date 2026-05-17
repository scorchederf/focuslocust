---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Service Dashboard

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1538` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cloud Service Dashboard](../../attack/techniques/T1538-cloud-service-dashboard.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1538 |
| name | Cloud Service Dashboard |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1538 |

## Preserved Source Material

```yaml
created: '2019-08-30T18:11:24.582Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may use a cloud service dashboard GUI with stolen credentials to gain useful information from an
  operational cloud environment, such as specific services, resources, and features. For example, the GCP Command Center can
  be used to view all assets, review findings of potential security risks, and run additional queries, such as finding public
  IP addresses and open ports.(Citation: Google Command Center Dashboard)


  Depending on the configuration of the environment, an adversary may be able to enumerate more information via the graphical
  dashboard than an API. This also allows the adversary to gain information without manually making any API requests.'
external_references:
- external_id: T1538
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1538
- description: Amazon. (n.d.). AWS Console Sign-in Events. Retrieved October 23, 2019.
  source_name: AWS Console Sign-in Events
  url: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.html
- description: 'Google. (2019, October 3). Quickstart: Using the dashboard. Retrieved October 8, 2019.'
  source_name: Google Command Center Dashboard
  url: https://cloud.google.com/security-command-center/docs/quickstart-scc-dashboard
id: attack-pattern--e49920b0-6c54-40c1-9571-73723653205f
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:49:32.022Z'
name: Cloud Service Dashboard
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Praetorian
- Obsidian Security
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
- SaaS
- Office Suite
- Identity Provider
x_mitre_version: '1.5'
```
