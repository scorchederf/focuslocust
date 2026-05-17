---
parsed_by: focuslocust
source: mitre
type: generated
---
# Active Directory Object Deletion

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

## Generated Concept Page

- [Active Directory Object Deletion](../../attack/data-sources/DC0068-active-directory-object-deletion.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0068 |
| name | Active Directory Object Deletion |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0068 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Object deletion in AD (e.g., user accounts, groups, OUs) is logged as Event ID 5141. Examples:\n\n- User Account:\
  \ Deleted user.\n- Group: Deleted security/distribution group.\n- Organizational Unit (OU): Loss of configurations or policies.\n\
  - Service Account: Disrupted operations or cover tracks.\n- Trust Object: Removed domain trust, disrupting connectivity.\n\
  \n*Data Collection Measures:*\n\n- Audit Policy:\n    - Enable \"Audit Directory Service Changes\" (Success and Failure).\n\
  \    - Path: `Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration\
  \ > Audit Policies > Directory Service Changes`.\n    - Key Event: Event ID 5141.\n- Log Forwarding: Use WEF to centralize\
  \ logs for SIEM tools (e.g., Splunk).\n- Enable EDR Monitoring:\n    - Detect processes or users that initiate unauthorized\
  \ object deletions.\n    - Monitor tools and scripts that may delete key directory objects."
external_references:
- external_id: DC0068
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0068
id: x-mitre-data-component--9085a576-636a-455b-91d2-c2921bbe6d1d
modified: '2025-11-12T22:03:39.105Z'
name: Active Directory Object Deletion
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
- channel: EventCode=4929
  name: WinEventLog:Security
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
