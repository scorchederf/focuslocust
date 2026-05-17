---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0087 - Active Directory Object Creation

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

## Summary

Creating new objects in AD, such as user accounts, groups, organizational units (OUs), or trust relationships. Logged as Event ID 5137. Examples:

- User Account Creation: New user account.
- Group Creation: New security/distribution group.
- OU Creation: New organizational unit.
- Service Account Creation: New service account for automation or malicious tasks.
- Trust Object Creation: Trust relationship with another domain.

## Source Verification

[source record](../../sources/mitre/active-directory-object-creation.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Creating new objects in AD, such as user accounts, groups, organizational units (OUs), or trust relationships.
Logged as Event ID 5137. Examples:
- User Account Creation: New user account.
- Group Creation: New security/distribution group.
- OU Creation: New organizational unit.
- Service Account Creation: New service account for automation or malicious tasks.
```
