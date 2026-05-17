---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1573 - Encrypted Channel

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1573` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may employ an encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Despite the use of a secure algorithm, these implementations may be vulnerable to reverse engineering if secret keys are encoded and/or generated within malware samples/configuration files.

## Source Verification

[source record](../../sources/mitre/encrypted-channel.md)

## Evidence Excerpt

```text
created: '2020-03-16T15:33:01.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Adversaries may employ an encryption algorithm to conceal command and control traffic rather than relying on
any inherent protections provided by a communication protocol. Despite the use of a secure algorithm, these implementations
may be vulnerable to reverse engineering if secret keys are encoded and/or generated within malware samples/configuration
files.
external_references:
- external_id: T1573
```
