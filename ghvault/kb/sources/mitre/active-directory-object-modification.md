---
parsed_by: focuslocust
source: mitre
type: generated
---
# Active Directory Object Modification

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

## Generated Concept Page

- [Active Directory Object Modification](../../attack/data-sources/DC0066-active-directory-object-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0066 |
| name | Active Directory Object Modification |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0066 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Changes to AD objects (e.g., users, groups, OUs) are logged as Event ID 5136 (Object Modification) or 5163 (Attribute
  Changes). Examples:


  - User Account: Modifying attributes (e.g., group membership, enabling/disabling accounts).

  - Group Membership: Adding/removing members.

  - OU: Changing properties/permissions (e.g., delegation).

  - Service Account: Modifying SPNs or other attributes.

  - Object Attributes: Changes to passwords, logon hours, or control flags.'
external_references:
- external_id: DC0066
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0066
id: x-mitre-data-component--5b8b466b-2c81-4fe7-946f-d677a74ae3db
modified: '2025-11-12T22:03:39.105Z'
name: Active Directory Object Modification
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
- channel: Update conditionalAccessPolicy
  name: azure:activity
- channel: vim.SessionManager.login / vim.AccountManager.createUser
  name: esxi:vpxa
- channel: EventCode=5163
  name: WinEventLog:Security
- channel: EventCode=4739
  name: WinEventLog:Security
- channel: Add certificate credential, Update certificate credential
  name: azure:signinlogs
- channel: Replication cookie changes involving Configuration partition with new server/nTDSDSA objects.
  name: m365:dirsync
- channel: EventCode=5136
  name: WinEventLog:Security
- channel: EventCode=4663, 4670, 4656
  name: WinEventLog:Security
- channel: permission change operations on datastores or VMs
  name: esxi:vpxd
- channel: Set-Mailbox, Set-AppPassword, Add-MailboxPermission
  name: m365:unified
- channel: 'Add app role assignment grant to user: Consent to application by privileged or unexpected accounts'
  name: m365:unified
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
