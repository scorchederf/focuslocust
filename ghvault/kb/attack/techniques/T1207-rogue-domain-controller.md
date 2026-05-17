---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1207 - Rogue Domain Controller

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1207` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may register a rogue Domain Controller to enable manipulation of Active Directory data. DCShadow may be used to create a rogue Domain Controller (DC). DCShadow is a method of manipulating Active Directory (AD) data, including objects and schemas, by registering (or reusing an inactive registration) and simulating the behavior of a DC.  Once registered, a rogue DC may be able to inject and replicate changes into AD infrastructure for any domain object, including credentials and keys.

Registering a rogue DC involves creating a new server and nTDSDSA objects in the Configuration partition of the AD schema, which requires Administrator privileges (either Domain or local to the DC) or the KRBTGT hash. 

This technique may bypass system logging and security monitors such as security information and event management (SIEM) products (since actions taken on a rogue DC may not be reported to these sensors).  The technique may also be used to alter and delete replication and other associated metadata to obstruct forensic analysis. Adversaries may also utilize this technique to perform SID-History Injection and/or manipulate AD objects (such as accounts, access control lists, schemas) to establish backdoors for Persistence.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Mimikatz](../../tools/unknown/mimikatz.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002)’s <code>LSADUMP::DCShadow</code> module can be used to make AD updates by temporarily setting a computer to be a DC.(Citation: Deply Mimikatz)(Citation: Adsecurity Mimikatz Guide) |

## Source Verification

[source record](../../sources/mitre/rogue-domain-controller.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may register a rogue Domain Controller to enable manipulation of Active Directory data. DCShadow
may be used to create a rogue Domain Controller (DC). DCShadow is a method of manipulating Active Directory (AD) data, including
objects and schemas, by registering (or reusing an inactive registration) and simulating the behavior of a DC. (Citation:
DCShadow Blog) Once registered, a rogue DC may be able to inject and replicate changes into AD infrastructure for any domain
object, including credentials and keys.
Registering a rogue DC involves creating a new server and nTDSDSA objects in the Configuration partition of the AD schema,
```
