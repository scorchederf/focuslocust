---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0084 - Active Directory Credential Request

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

## Summary

Requests for authentication credentials via Kerberos or other methods like NTLM and LDAP queries. Examples:

- Kerberos TGT and Service Tickets (Event IDs 4768, 4769)
- NTLM Authentication Events
- LDAP Bind Requests.

## Source Verification

[source record](../../sources/mitre/active-directory-credential-request.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Requests for authentication credentials via Kerberos or other methods like NTLM and LDAP queries. Examples:
- Kerberos TGT and Service Tickets (Event IDs 4768, 4769)
- NTLM Authentication Events
- LDAP Bind Requests.'
external_references:
- external_id: DC0084
```
