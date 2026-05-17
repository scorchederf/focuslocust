---
parsed_by: focuslocust
source: mitre
type: generated
---
# User Account Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0014` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [User Account Creation](../../attack/data-sources/DC0014-user-account-creation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0014 |
| name | User Account Creation |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0014 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.271Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: The initial establishment of a new user, service, or machine account within an operating system, cloud environment,
  or identity management system.
external_references:
- external_id: DC0014
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0014
id: x-mitre-data-component--deb22295-7e37-4a3b-ac6f-c86666fbe63d
modified: '2025-11-12T22:03:39.105Z'
name: User Account Creation
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
- channel: EventCode=4720
  name: WinEventLog:Security
- channel: Add user
  name: azure:audit
- channel: CreateUser
  name: AWS:CloudTrail
- channel: New user created
  name: saas:zoom
- channel: admin.user.create
  name: saas:slack
- channel: Add user
  name: m365:unified
- channel: adduser
  name: auditd:SYSCALL
- channel: ExecCreate + usermod or useradd
  name: docker:daemon
- channel: useradd or adduser executed
  name: auditd:SYSCALL
- channel: username <user> privilege <level>
  name: networkdevice:syslog
- channel: user.lifecycle.create
  name: saas:okta
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
