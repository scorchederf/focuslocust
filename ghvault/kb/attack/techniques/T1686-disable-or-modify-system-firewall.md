---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1686 - Disable or Modify System Firewall

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1686` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may disable or modify host-based or network firewalls to impair defensive mechanisms and enable further action. Once an adversary has gathered sufficient privileges, they can tamper with firewall services, policies, or rule sets to remove restrictions on inbound or outbound traffic. For example, this may include turning off firewall profiles, altering existing rules to permit previously blocked ports or protocols, or adding new rules that create covert communication paths (e.g., adding a new firewall rule for a well-known protocol (such as RDP) using a non-traditional and potentially less securitized port.

Adversaries may disable or modify firewalls using different behaviors, depending on the platform. For example, in ESXi, firewall rules may be modified directly via the esxcli (e.g., via esxcli network firewall set) or via the vCenter user interface.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [netsh](../../tools/unknown/netsh.md) | explicit | source | [netsh](https://attack.mitre.org/software/S0108) can be used to disable local firewall settings.(Citation: TechNet Netsh)(Citation: TechNet Netsh Firewall) |

## Source Verification

[source record](../../sources/mitre/disable-or-modify-system-firewall.md)

## Evidence Excerpt

```text
created: '2026-04-14T22:53:27.275Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may disable or modify host-based or network firewalls to impair defensive mechanisms and enable
further action. Once an adversary has gathered sufficient privileges, they can tamper with firewall services, policies,
or rule sets to remove restrictions on inbound or outbound traffic. For example, this may include turning off firewall profiles,
altering existing rules to permit previously blocked ports or protocols, or adding new rules that create covert communication
paths (e.g., adding a new firewall rule for a well-known protocol (such as RDP) using a non-traditional and potentially
less securitized port.(Citation: change_rdp_port_conti)
```
