---
parsed_by: focuslocust
source: mitre
type: generated
---
# Active Directory Object Access

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

## Generated Concept Page

- [Active Directory Object Access](../../attack/data-sources/DC0071-active-directory-object-access.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0071 |
| name | Active Directory Object Access |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0071 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Object access refers to activities where AD objects (e.g., user accounts, groups, policies) are accessed or\
  \ queried. Example: Windows Event ID 4661 logs object access attempts. Examples:\n\n- Attribute Access: e.g., `userPassword`,\
  \ `memberOf`, `securityDescriptor`.\n- Group Enumeration: Enumerating critical group members (e.g., Domain Admins).\n- User\
  \ Attributes: Commonly accessed attributes like `samAccountName`, `lastLogonTimestamp`.\n- Policy Access: Accessing GPOs\
  \ to understand security settings.\n\n*Data Collection Measures:*\n\n- Audit Policies:\n    - Enable \"Audit Directory Service\
  \ Access\" under Advanced Audit Policies (Success and Failure).\n    - Path: `Computer Configuration > Policies > Windows\
  \ Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies > Object AccessEnable: Audit Directory\
  \ Service Access` (Success and Failure).\n    - Captured Events: IDs 4661, 4662.\n- Event Forwarding: Use WEF to centralize\
  \ logs for SIEM analysis.\n- SIEM Integration: Collect and parse logs (e.g., 4661, 4662) using tools like Splunk or Azure\
  \ Sentinel.\n- Log Filtering:\n- Focus on sensitive objects/attributes like:\n    - `Domain Admins` group.\n    - `userPassword`,\
  \ `ntSecurityDescriptor`.\n- Enable EDR Monitoring:\n    - Detect processes accessing sensitive AD objects (e.g., samAccountName,\
  \ securityDescriptor).\n    - Log all attempts to enumerate critical groups (e.g., \"Domain Admins\")."
external_references:
- external_id: DC0071
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0071
id: x-mitre-data-component--5c6de881-bc70-4070-855a-7a9631a407f7
modified: '2025-10-21T15:14:35.607Z'
name: Active Directory Object Access
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
- channel: EventCode=4662
  name: WinEventLog:Security
- channel: EventCode=4661
  name: WinEventLog:Security
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
