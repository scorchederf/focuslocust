---
parsed_by: focuslocust
source: mitre
type: generated
---
# Disable or Modify Linux Audit System Log

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1685.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Disable or Modify Linux Audit System Log](../../attack/techniques/T1685.004-disable-or-modify-linux-audit-system-log.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1685.004 |
| name | Disable or Modify Linux Audit System Log |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1685/004 |

## Preserved Source Material

```yaml
created: '2026-04-14T22:54:03.325Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may disable or modify the Linux Audit system to hide malicious activity and avoid detection. Linux\
  \ admins use the Linux Audit system to track security-relevant information on a system. The Linux Audit system operates\
  \ at the kernel-level and maintains event logs on application and system activity such as process, network, file, and login\
  \ events based on pre-configured rules. \n\nOften referred to as `auditd`, this is the name of the daemon used to write\
  \ events to disk and is governed by the parameters set in the `audit.conf` configuration file. Two primary ways to configure\
  \ the log generation rules are through the command line `auditctl` utility and the file `/etc/audit/audit.rules`, containing\
  \ a sequence of `auditctl` commands loaded at boot time.(Citation: IzyKnows auditd threat detection 2022)(Citation: Red\
  \ Hat Linux Disable or Mod)\n\nWith root privileges, adversaries may be able to ensure their activity is not logged through\
  \ disabling the Audit system service, editing the configuration/rule files, or by hooking the Audit system library functions.\
  \ Using the command line, adversaries can disable the Audit system service through killing processes associated with `auditd`\
  \ daemon or use `systemctl` to stop the Audit service. Adversaries can also hook Audit system functions to disable logging\
  \ or modify the rules contained in the `/etc/audit/audit.rules` or `audit.conf` files to ignore malicious activity.(Citation:\
  \ ESET Ebury Feb 2014)"
external_references:
- external_id: T1685.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1685/004
- description: IzySec. (2022, January 26). Linux auditd for Threat Detection. Retrieved September 29, 2023.
  source_name: IzyKnows auditd threat detection 2022
  url: https://izyknows.medium.com/linux-auditd-for-threat-detection-d06c8b941505
- description: M.Léveillé, M.. (2014, February 21). An In-depth Analysis of Linux/Ebury. Retrieved April 19, 2019.
  source_name: ESET Ebury Feb 2014
  url: https://www.welivesecurity.com/2014/02/21/an-in-depth-analysis-of-linuxebury/
- description: Red Hat. (n.d.). Retrieved April 15, 2026.
  source_name: Red Hat Linux Disable or Mod
  url: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/security_guide/chap-system_auditing
id: attack-pattern--23d69d00-80c4-42ff-9dac-dbd0459dad75
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-22T15:42:49.357Z'
name: Disable or Modify Linux Audit System Log
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Tim (Wadhwa-)Brown
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
x_mitre_version: '1.0'
```
