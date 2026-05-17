---
parsed_by: focuslocust
source: mitre
type: generated
---
# Fgdump

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0120` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Fgdump is a Windows password hash dumper.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/fgdump.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.002 - Security Account Manager](../../attack/techniques/T1003.002-security-account-manager.md) | explicit | source | [Fgdump](https://attack.mitre.org/software/S0120) can dump Windows password hashes.(Citation: Mandiant APT1) |

## Source Verification

[source record](../../sources/mitre/fgdump.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:10.569Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Fgdump](https://attack.mitre.org/software/S0120) is a Windows password hash dumper. (Citation: Mandiant APT1)'
external_references:
- external_id: S0120
source_name: mitre-attack
url: https://attack.mitre.org/software/S0120
- description: Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.
```
