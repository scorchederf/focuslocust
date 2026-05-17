---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1001 - Data Obfuscation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may obfuscate command and control traffic to make it more difficult to detect. Command and control (C2) communications are hidden (but not necessarily encrypted) in an attempt to make the content more difficult to discover or decipher and to make the communication less conspicuous and hide commands from being seen. This encompasses many methods, such as adding junk data to protocol traffic, using steganography, or impersonating legitimate protocols.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [evilginx2](../../tools/unknown/evilginx2.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can modify the Origin and Referrer fields in HTTPS headers it relays between intended victims and legitimate websites to comply with cross-origin resource sharing (CORS) restrictions.(Citation: Evilginx 2 July 2018) |

## Source Verification

[source record](../../sources/mitre/data-obfuscation.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:18.931Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may obfuscate command and control traffic to make it more difficult to detect.(Citation: Bitdefender
FunnyDream Campaign November 2020) Command and control (C2) communications are hidden (but not necessarily encrypted) in
an attempt to make the content more difficult to discover or decipher and to make the communication less conspicuous and
hide commands from being seen. This encompasses many methods, such as adding junk data to protocol traffic, using steganography,
or impersonating legitimate protocols. '
external_references:
```
