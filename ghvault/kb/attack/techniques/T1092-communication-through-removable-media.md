---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1092 - Communication Through Removable Media

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1092` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries can perform command and control between compromised hosts on potentially disconnected networks using removable media to transfer commands from system to system. Both systems would need to be compromised, with the likelihood that an Internet-connected system was compromised first and the second through lateral movement by Replication Through Removable Media. Commands and files would be relayed from the disconnected system to the Internet-connected system to which the adversary has direct access.

## Source Verification

[source record](../../sources/mitre/communication-through-removable-media.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:09.379Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries can perform command and control between compromised hosts on potentially disconnected networks using
removable media to transfer commands from system to system.(Citation: ESET Sednit USBStealer 2014) Both systems would need
to be compromised, with the likelihood that an Internet-connected system was compromised first and the second through lateral
movement by [Replication Through Removable Media](https://attack.mitre.org/techniques/T1091). Commands and files would be
relayed from the disconnected system to the Internet-connected system to which the adversary has direct access.'
external_references:
```
