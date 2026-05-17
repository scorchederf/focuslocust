---
parsed_by: focuslocust
source: mitre
type: generated
---
# netsh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0108` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

netsh is a scripting utility used to interact with networking components on local or remote systems.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/netsh.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1090 - Proxy](../../attack/techniques/T1090-proxy.md) | explicit | source | [netsh](https://attack.mitre.org/software/S0108) can be used to set up a proxy tunnel to allow remote host access to an infected host.(Citation: Securelist fileless attacks Feb 2017) |
| [T1518.001 - Security Software Discovery](../../attack/techniques/T1518.001-security-software-discovery.md) | explicit | source | [netsh](https://attack.mitre.org/software/S0108) can be used to discover system firewall settings.(Citation: TechNet Netsh)(Citation: TechNet Netsh Firewall) |
| [T1546.007 - Netsh Helper DLL](../../attack/techniques/T1546.007-netsh-helper-dll.md) | explicit | source | [netsh](https://attack.mitre.org/software/S0108) can be used as a persistence proxy technique to execute a helper DLL when netsh.exe is executed.(Citation: Demaske Netsh Persistence) |
| [T1686 - Disable or Modify System Firewall](../../attack/techniques/T1686-disable-or-modify-system-firewall.md) | explicit | source | [netsh](https://attack.mitre.org/software/S0108) can be used to disable local firewall settings.(Citation: TechNet Netsh)(Citation: TechNet Netsh Firewall) |

## Source Verification

[source record](../../sources/mitre/netsh.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:06.083Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[netsh](https://attack.mitre.org/software/S0108) is a scripting utility used to interact with networking components
on local or remote systems. (Citation: TechNet Netsh)'
external_references:
- external_id: S0108
source_name: mitre-attack
url: https://attack.mitre.org/software/S0108
```
