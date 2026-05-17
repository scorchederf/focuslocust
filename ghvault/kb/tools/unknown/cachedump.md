---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cachedump

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0119` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Cachedump is a publicly-available tool that program extracts cached password hashes from a system’s registry.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/cachedump.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.005 - Cached Domain Credentials](../../attack/techniques/T1003.005-cached-domain-credentials.md) | explicit | source | [Cachedump](https://attack.mitre.org/software/S0119) can extract cached password hashes from cache entry information.(Citation: Mandiant APT1) |

## Source Verification

[source record](../../sources/mitre/cachedump.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:10.197Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Cachedump](https://attack.mitre.org/software/S0119) is a publicly-available tool that program extracts cached
password hashes from a system’s registry. (Citation: Mandiant APT1)'
external_references:
- external_id: S0119
source_name: mitre-attack
url: https://attack.mitre.org/software/S0119
```
