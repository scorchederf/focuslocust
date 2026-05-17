---
parsed_by: focuslocust
source: mitre
type: generated
---
# Web Credential Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Web Credential Creation](../../attack/data-sources/DC0006-web-credential-creation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0006 |
| name | Web Credential Creation |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0006 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.271Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Initial construction of new web credential material (ex: Windows EID 1200 or 4769)'
external_references:
- external_id: DC0006
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0006
id: x-mitre-data-component--5f7c9def-0ddf-423b-b1f8-fb2ddeed0ce3
modified: '2025-11-12T22:03:39.105Z'
name: Web Credential Creation
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: Token issuance events showing anomalous claims or issuers
  name: WinEventLog:ADFS
- channel: AssumeRole, GetFederationToken API calls by unusual or new entities
  name: AWS:CloudTrail
- channel: SAML/OIDC tokens issued without corresponding MFA or password validation
  name: azure:signinlogs
- channel: Session creation without MFA or login event
  name: m365:unified
- channel: OAuth grants or tokens issued without expected user consent
  name: m365:oauth
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
