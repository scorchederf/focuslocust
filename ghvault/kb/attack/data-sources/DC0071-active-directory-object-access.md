---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0071 - Active Directory Object Access

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0071` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Object access refers to activities where AD objects (e.g., user accounts, groups, policies) are accessed or queried. Example: Windows Event ID 4661 logs object access attempts. Examples:

- Attribute Access: e.g., `userPassword`, `memberOf`, `securityDescriptor`.
- Group Enumeration: Enumerating critical group members (e.g., Domain Admins).
- User Attributes: Commonly accessed attributes like `samAccountName`, `lastLogonTimestamp`.
- Policy Access: Accessing GPOs to understand security settings.

*Data Collection Measures:*

- Audit Policies:
    - Enable "Audit Directory Service Access" under Advanced Audit Policies (Success and Failure).
    - Path: `Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies > Object AccessEnable: Audit Directory Service Access` (Success and Failure).
    - Captured Events: IDs 4661, 4662.
- Event Forwarding: Use WEF to centralize logs for SIEM analysis.
- SIEM Integration: Collect and parse logs (e.g., 4661, 4662) using tools like Splunk or Azure Sentinel.
- Log Filtering:
- Focus on sensitive objects/attributes like:
    - `Domain Admins` group.
    - `userPassword`, `ntSecurityDescriptor`.
- Enable EDR Monitoring:
    - Detect processes accessing sensitive AD objects (e.g., samAccountName, securityDescriptor).
    - Log all attempts to enumerate critical groups (e.g., "Domain Admins").

## Source Verification

[source record](../../sources/mitre/active-directory-object-access.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Object access refers to activities where AD objects (e.g., user accounts, groups, policies) are accessed or\
\ queried. Example: Windows Event ID 4661 logs object access attempts. Examples:\n\n- Attribute Access: e.g., `userPassword`,\
\ `memberOf`, `securityDescriptor`.\n- Group Enumeration: Enumerating critical group members (e.g., Domain Admins).\n- User\
\ Attributes: Commonly accessed attributes like `samAccountName`, `lastLogonTimestamp`.\n- Policy Access: Accessing GPOs\
\ to understand security settings.\n\n*Data Collection Measures:*\n\n- Audit Policies:\n    - Enable \"Audit Directory Service\
\ Access\" under Advanced Audit Policies (Success and Failure).\n    - Path: `Computer Configuration > Policies > Windows\
```
