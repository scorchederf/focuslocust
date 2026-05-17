---
parsed_by: focuslocust
source: mitre
type: generated
---
# Lslsass

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0121` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Lslsass is a publicly-available tool that can dump active logon session password hashes from the lsass process.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/lslsass.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | [Lslsass](https://attack.mitre.org/software/S0121) can dump active logon session password hashes from the lsass process.(Citation: Mandiant APT1) |

## Source Verification

[source record](../../sources/mitre/lslsass.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:10.962Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Lslsass](https://attack.mitre.org/software/S0121) is a publicly-available tool that can dump active logon session
password hashes from the lsass process. (Citation: Mandiant APT1)'
external_references:
- external_id: S0121
source_name: mitre-attack
url: https://attack.mitre.org/software/S0121
```
