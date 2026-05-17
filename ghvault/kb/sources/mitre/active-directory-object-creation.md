---
parsed_by: focuslocust
source: mitre
type: generated
---
# Active Directory Object Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0087` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory Object Creation](../../attack/data-sources/DC0087-active-directory-object-creation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0087 |
| name | Active Directory Object Creation |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0087 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Creating new objects in AD, such as user accounts, groups, organizational units (OUs), or trust relationships.
  Logged as Event ID 5137. Examples:


  - User Account Creation: New user account.

  - Group Creation: New security/distribution group.

  - OU Creation: New organizational unit.

  - Service Account Creation: New service account for automation or malicious tasks.

  - Trust Object Creation: Trust relationship with another domain.'
external_references:
- external_id: DC0087
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0087
id: x-mitre-data-component--18b236d8-7224-488f-9d2f-50076a0f653a
modified: '2025-11-12T22:03:39.105Z'
name: Active Directory Object Creation
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: New device object creation
  name: azure:audit
- channel: Device Object Creation
  name: WinEventLog:Security
- channel: EventCode=4928
  name: WinEventLog:Security
- channel: CreateAccessKey, ImportKeyPair, CreateLoginProfile, CreateKeyPair
  name: AWS:CloudTrail
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
