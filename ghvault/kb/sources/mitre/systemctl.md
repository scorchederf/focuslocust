---
parsed_by: focuslocust
source: mitre
type: generated
---
# Systemctl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1569.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Systemctl](../../attack/techniques/T1569.003-systemctl.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1569.003 |
| name | Systemctl |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1569/003 |

## Preserved Source Material

```yaml
created: '2025-03-18T13:44:12.618Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may abuse systemctl to execute commands or programs. Systemctl is the primary interface for systemd,\
  \ the Linux init system and service manager. Typically invoked from a shell, Systemctl can also be integrated into scripts\
  \ or applications.   \n\nAdversaries may use systemctl to execute commands or programs as [Systemd Service](https://attack.mitre.org/techniques/T1543/002)s.\
  \ Common subcommands include: `systemctl start`, `systemctl stop`, `systemctl enable`, `systemctl disable`, and `systemctl\
  \ status`.(Citation: Red Hat Systemctl 2022)"
external_references:
- external_id: T1569.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1569/003
- description: Damon Garn. (2022, May 17). How to use systemctl to manage Linux services. Retrieved March 18, 2025.
  source_name: Red Hat Systemctl 2022
  url: https://www.redhat.com/en/blog/linux-systemctl-manage-services
id: attack-pattern--4b46767d-4a61-4f30-995e-c19a75c2e536
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-04-15T19:58:28.694Z'
name: Systemctl
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
x_mitre_remote_support: false
x_mitre_version: '1.0'
```
