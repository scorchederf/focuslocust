---
parsed_by: focuslocust
source: mitre
type: generated
---
# User Account Deletion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0009` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [User Account Deletion](../../attack/data-sources/DC0009-user-account-deletion.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0009 |
| name | User Account Deletion |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0009 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.271Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: The removal of a user, service, or machine account from an operating system, cloud identity management system,
  or directory service.
external_references:
- external_id: DC0009
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0009
id: x-mitre-data-component--d6257b8e-869c-41c0-8731-fdca40858a91
modified: '2025-11-12T22:03:39.105Z'
name: User Account Deletion
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
- channel: EventCode=4726, 4657
  name: WinEventLog:Security
- channel: method=RemoveUser or esxcli system account remove invocation
  name: esxi:hostd
- channel: Remove-Mailbox, Set-Mailbox
  name: m365:unified
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
