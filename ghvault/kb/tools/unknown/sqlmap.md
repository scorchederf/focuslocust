---
parsed_by: focuslocust
source: mitre
type: generated
---
# sqlmap

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0225` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

sqlmap is an open source penetration testing tool that can be used to automate the process of detecting and exploiting SQL injection flaws.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/sqlmap.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1190 - Exploit Public-Facing Application](../../attack/techniques/T1190-exploit-public-facing-application.md) | explicit | source | [sqlmap](https://attack.mitre.org/software/S0225) can be used to automate exploitation of SQL injection vulnerabilities.(Citation: sqlmap Introduction) |

## Source Verification

[source record](../../sources/mitre/sqlmap.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[sqlmap](https://attack.mitre.org/software/S0225) is an open source penetration testing tool that can be used
to automate the process of detecting and exploiting SQL injection flaws. (Citation: sqlmap Introduction)'
external_references:
- external_id: S0225
source_name: mitre-attack
url: https://attack.mitre.org/software/S0225
```
