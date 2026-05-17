---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0066 - Active Directory Object Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0066` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Changes to AD objects (e.g., users, groups, OUs) are logged as Event ID 5136 (Object Modification) or 5163 (Attribute Changes). Examples:

- User Account: Modifying attributes (e.g., group membership, enabling/disabling accounts).
- Group Membership: Adding/removing members.
- OU: Changing properties/permissions (e.g., delegation).
- Service Account: Modifying SPNs or other attributes.
- Object Attributes: Changes to passwords, logon hours, or control flags.

## Source Verification

[source record](../../sources/mitre/active-directory-object-modification.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Changes to AD objects (e.g., users, groups, OUs) are logged as Event ID 5136 (Object Modification) or 5163 (Attribute
Changes). Examples:
- User Account: Modifying attributes (e.g., group membership, enabling/disabling accounts).
- Group Membership: Adding/removing members.
- OU: Changing properties/permissions (e.g., delegation).
- Service Account: Modifying SPNs or other attributes.
```
