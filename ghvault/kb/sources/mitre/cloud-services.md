---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Services

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1021.007` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cloud Services](../../attack/techniques/T1021.007-cloud-services.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1021.007 |
| name | Cloud Services |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1021/007 |

## Preserved Source Material

```yaml
created: '2023-02-21T19:38:13.371Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may log into accessible cloud services within a compromised environment using [Valid Accounts](https://attack.mitre.org/techniques/T1078)\
  \ that are synchronized with or federated to on-premises user identities. The adversary may then perform management actions\
  \ or access cloud-hosted resources as the logged-on user. \n\nMany enterprises federate centrally managed user identities\
  \ to cloud services, allowing users to login with their domain credentials in order to access the cloud control plane. Similarly,\
  \ adversaries may connect to available cloud services through the web console or through the cloud command line interface\
  \ (CLI) (e.g., [Cloud API](https://attack.mitre.org/techniques/T1059/009)), using commands such as <code>Connect-AZAccount</code>\
  \ for Azure PowerShell, <code>Connect-MgGraph</code> for Microsoft Graph PowerShell, and <code>gcloud auth login</code>\
  \ for the Google Cloud CLI.\n\nIn some cases, adversaries may be able to authenticate to these services via [Application\
  \ Access Token](https://attack.mitre.org/techniques/T1550/001) instead of a username and password. "
external_references:
- external_id: T1021.007
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1021/007
id: attack-pattern--8861073d-d1b8-4941-82ce-dce621d398f0
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: lateral-movement
modified: '2025-04-15T22:03:56.494Z'
name: Cloud Services
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
- IaaS
- Identity Provider
- Office Suite
- SaaS
x_mitre_version: '1.1'
```
