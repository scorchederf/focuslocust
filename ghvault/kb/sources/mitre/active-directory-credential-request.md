---
parsed_by: focuslocust
source: mitre
type: generated
---
# Active Directory Credential Request

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0084` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory Credential Request](../../attack/data-sources/DC0084-active-directory-credential-request.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0084 |
| name | Active Directory Credential Request |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0084 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Requests for authentication credentials via Kerberos or other methods like NTLM and LDAP queries. Examples:


  - Kerberos TGT and Service Tickets (Event IDs 4768, 4769)

  - NTLM Authentication Events

  - LDAP Bind Requests.'
external_references:
- external_id: DC0084
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0084
id: x-mitre-data-component--02d090b6-8157-48da-98a2-517f7edd49fc
modified: '2025-11-12T22:03:39.105Z'
name: Active Directory Credential Request
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
- channel: EventCode=4768
  name: WinEventLog:Security
- channel: EventCode=4769
  name: WinEventLog:Security
- channel: Kerberos TGS-REQ anomalies without KDC validation (Silver Ticket behavior)
  name: WinEventLog:Kerberos
- channel: EventCode=4929
  name: WinEventLog:Security
- channel: Unusual kinit or klist activity
  name: linux:syslog
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
