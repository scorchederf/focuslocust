---
parsed_by: focuslocust
source: mitre
type: generated
---
# Clear Linux or Mac System Logs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1685.006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Clear Linux or Mac System Logs](../../attack/techniques/T1685.006-clear-linux-or-mac-system-logs.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1685.006 |
| name | Clear Linux or Mac System Logs |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1685/006 |

## Preserved Source Material

```yaml
created: '2026-04-14T22:54:04.240Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may clear system logs to hide evidence of an intrusion. macOS and Linux both keep track of system
  or user-initiated actions via system logs. The majority of native system logging is stored under the `/var/log/` directory.
  Subfolders in this directory categorize logs by their related functions, such as:(Citation: Linux Logs)


  * `/var/log/messages:`: General and system-related messages

  * `/var/log/secure or /var/log/auth.log`: Authentication logs

  * `/var/log/utmp or /var/log/wtmp`: Login records

  * `/var/log/kern.log`: Kernel logs

  * `/var/log/cron.log`: Crond logs

  * `/var/log/maillog`: Mail server logs

  * `/var/log/httpd/`: Web server access and error logs'
external_references:
- external_id: T1685.006
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1685/006
- description: Marcel. (2018, April 19). 12 Critical Linux Log Files You Must be Monitoring. Retrieved March 29, 2020.
  source_name: Linux Logs
  url: https://www.eurovps.com/blog/important-linux-log-files-you-must-be-monitoring/
id: attack-pattern--5e29d64d-2b14-4f92-875e-4c9c498e213c
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-22T15:41:39.190Z'
name: Clear Linux or Mac System Logs
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
x_mitre_version: '1.0'
```
