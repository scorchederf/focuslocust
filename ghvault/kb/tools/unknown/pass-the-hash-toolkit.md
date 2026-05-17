---
parsed_by: focuslocust
source: mitre
type: generated
---
# Pass-The-Hash Toolkit

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0122` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Pass-The-Hash Toolkit is a toolkit that allows an adversary to "pass" a password hash (without knowing the original password) to log in to systems.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/pass-the-hash-toolkit.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1550.002 - Pass the Hash](../../attack/techniques/T1550.002-pass-the-hash.md) | explicit | source | [Pass-The-Hash Toolkit](https://attack.mitre.org/software/S0122) can perform pass the hash.(Citation: Mandiant APT1) |

## Source Verification

[source record](../../sources/mitre/pass-the-hash-toolkit.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:11.426Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Pass-The-Hash Toolkit](https://attack.mitre.org/software/S0122) is a toolkit that allows an adversary to "pass"
a password hash (without knowing the original password) to log in to systems. (Citation: Mandiant APT1)'
external_references:
- external_id: S0122
source_name: mitre-attack
url: https://attack.mitre.org/software/S0122
```
