---
parsed_by: focuslocust
source: mitre
type: generated
---
# Device Driver Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1652` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Device Driver Discovery](../../attack/techniques/T1652-device-driver-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1652 |
| name | Device Driver Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1652 |

## Preserved Source Material

```yaml
created: '2023-03-28T20:14:49.087Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to enumerate local device drivers on a victim host. Information about device drivers
  may highlight various insights that shape follow-on behaviors, such as the function/purpose of the host, present security
  tools (i.e. [Security Software Discovery](https://attack.mitre.org/techniques/T1518/001)) or other defenses (e.g., [Virtualization/Sandbox
  Evasion](https://attack.mitre.org/techniques/T1497)), as well as potential exploitable vulnerabilities (e.g., [Exploitation
  for Privilege Escalation](https://attack.mitre.org/techniques/T1068)).


  Many OS utilities may provide information about local device drivers, such as `driverquery.exe` and the `EnumDeviceDrivers()`
  API function on Windows.(Citation: Microsoft Driverquery)(Citation: Microsoft EnumDeviceDrivers) Information about device
  drivers (as well as associated services, i.e., [System Service Discovery](https://attack.mitre.org/techniques/T1007)) may
  also be available in the Registry.(Citation: Microsoft Registry Drivers)


  On Linux/macOS, device drivers (in the form of kernel modules) may be visible within `/dev` or using utilities such as `lsmod`
  and `modinfo`.(Citation: Linux Kernel Programming)(Citation: lsmod man)(Citation: modinfo man)'
external_references:
- external_id: T1652
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1652
- description: Kerrisk, M. (2022, December 18). lsmod(8) — Linux manual page. Retrieved March 28, 2023.
  source_name: lsmod man
  url: https://man7.org/linux/man-pages/man8/lsmod.8.html
- description: Microsoft. (2021, December 14). Registry Trees for Devices and Drivers. Retrieved March 28, 2023.
  source_name: Microsoft Registry Drivers
  url: https://learn.microsoft.com/windows-hardware/drivers/install/overview-of-registry-trees-and-keys
- description: Microsoft. (2021, October 12). EnumDeviceDrivers function (psapi.h). Retrieved March 28, 2023.
  source_name: Microsoft EnumDeviceDrivers
  url: https://learn.microsoft.com/windows/win32/api/psapi/nf-psapi-enumdevicedrivers
- description: Microsoft. (n.d.). driverquery. Retrieved March 28, 2023.
  source_name: Microsoft Driverquery
  url: https://learn.microsoft.com/windows-server/administration/windows-commands/driverquery
- description: Pomerantz, O., Salzman, P.. (2003, April 4). The Linux Kernel Module Programming Guide. Retrieved April 6,
    2018.
  source_name: Linux Kernel Programming
  url: https://www.tldp.org/LDP/lkmpg/2.4/lkmpg.pdf
- description: Russell, R. (n.d.). modinfo(8) - Linux man page. Retrieved March 28, 2023.
  source_name: modinfo man
  url: https://linux.die.net/man/8/modinfo
id: attack-pattern--215d9700-5881-48b8-8265-6449dbb7195d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-04-15T22:17:22.391Z'
name: Device Driver Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- ESET
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.0'
```
