---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1091 - Replication Through Removable Media

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1091` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may move onto systems, possibly those on disconnected or air-gapped networks, by copying malware to removable media and taking advantage of Autorun features when the media is inserted into a system and executes. In the case of Lateral Movement, this may occur through modification of executable files stored on removable media or by copying malware and renaming it to look like a legitimate file to trick users into executing it on a separate system. In the case of Initial Access, this may occur through manual manipulation of the media, modification of systems used to initially format the media, or modification to the media's firmware itself.

Mobile devices may also be used to infect PCs with malware if connected via USB. This infection may be achieved using devices (Android, iOS, etc.) and, in some instances, USB charging cables. For example, when a smartphone is connected to a system, it may appear to be mounted similar to a USB-connected disk drive. If malware that is compatible with the connected system is on the mobile device, the malware could infect the machine (especially if Autorun features are enabled).

## Source Verification

[source record](../../sources/mitre/replication-through-removable-media.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:08.977Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may move onto systems, possibly those on disconnected or air-gapped networks, by copying malware
to removable media and taking advantage of Autorun features when the media is inserted into a system and executes. In the
case of Lateral Movement, this may occur through modification of executable files stored on removable media or by copying
malware and renaming it to look like a legitimate file to trick users into executing it on a separate system. In the case
of Initial Access, this may occur through manual manipulation of the media, modification of systems used to initially format
the media, or modification to the media''s firmware itself.
```
