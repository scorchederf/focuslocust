---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0068 - Active Directory Object Deletion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0068` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Object deletion in AD (e.g., user accounts, groups, OUs) is logged as Event ID 5141. Examples:

- User Account: Deleted user.
- Group: Deleted security/distribution group.
- Organizational Unit (OU): Loss of configurations or policies.
- Service Account: Disrupted operations or cover tracks.
- Trust Object: Removed domain trust, disrupting connectivity.

*Data Collection Measures:*

- Audit Policy:
    - Enable "Audit Directory Service Changes" (Success and Failure).
    - Path: `Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies > Directory Service Changes`.
    - Key Event: Event ID 5141.
- Log Forwarding: Use WEF to centralize logs for SIEM tools (e.g., Splunk).
- Enable EDR Monitoring:
    - Detect processes or users that initiate unauthorized object deletions.
    - Monitor tools and scripts that may delete key directory objects.

## Source Verification

[source record](../../sources/mitre/active-directory-object-deletion.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Object deletion in AD (e.g., user accounts, groups, OUs) is logged as Event ID 5141. Examples:\n\n- User Account:\
\ Deleted user.\n- Group: Deleted security/distribution group.\n- Organizational Unit (OU): Loss of configurations or policies.\n\
- Service Account: Disrupted operations or cover tracks.\n- Trust Object: Removed domain trust, disrupting connectivity.\n\
\n*Data Collection Measures:*\n\n- Audit Policy:\n    - Enable \"Audit Directory Service Changes\" (Success and Failure).\n\
\    - Path: `Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration\
\ > Audit Policies > Directory Service Changes`.\n    - Key Event: Event ID 5141.\n- Log Forwarding: Use WEF to centralize\
```
