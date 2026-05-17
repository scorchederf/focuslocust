---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1548 - Abuse Elevation Control Mechanism

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1548` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may circumvent mechanisms designed to control privilege elevation to gain higher-level permissions. Most modern systems contain native elevation control mechanisms that are intended to limit privileges that a user can perform on a machine. Authorization has to be granted to specific users in order to perform tasks that can be considered of higher risk. An adversary can perform several methods to take advantage of built-in control mechanisms in order to escalate privileges on a system.

## Source Verification

[source record](../../sources/mitre/abuse-elevation-control-mechanism.md)

## Evidence Excerpt

```text
created: '2020-01-30T13:58:14.373Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may circumvent mechanisms designed to control privilege elevation to gain higher-level permissions.
Most modern systems contain native elevation control mechanisms that are intended to limit privileges that a user can perform
on a machine. Authorization has to be granted to specific users in order to perform tasks that can be considered of higher
risk.(Citation: TechNet How UAC Works)(Citation: sudo man page 2018) An adversary can perform several methods to take advantage
of built-in control mechanisms in order to escalate privileges on a system.(Citation: OSX Keydnap malware)(Citation: Fortinet
Fareit)'
```
