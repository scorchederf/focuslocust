---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1200 - Hardware Additions

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1200` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may physically introduce computer accessories, networking hardware, or other computing devices into a system or network that can be used as a vector to gain access. Rather than just connecting and distributing payloads via removable storage (i.e. Replication Through Removable Media), more robust hardware additions can be used to introduce new functionalities and/or features into a system that can then be abused.

While public references of usage by threat actors are scarce, many red teams/penetration testers leverage hardware additions for initial access. Commercial and open source products can be leveraged with capabilities such as passive network tapping, network traffic modification (i.e. Adversary-in-the-Middle), keystroke injection, kernel memory reading via DMA, addition of new wireless access points to an existing network, and others.

## Source Verification

[source record](../../sources/mitre/hardware-additions.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may physically introduce computer accessories, networking hardware, or other computing devices into
a system or network that can be used as a vector to gain access. Rather than just connecting and distributing payloads via
removable storage (i.e. [Replication Through Removable Media](https://attack.mitre.org/techniques/T1091)), more robust hardware
additions can be used to introduce new functionalities and/or features into a system that can then be abused.
While public references of usage by threat actors are scarce, many red teams/penetration testers leverage hardware additions
for initial access. Commercial and open source products can be leveraged with capabilities such as passive network tapping,
```
