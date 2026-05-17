---
parsed_by: focuslocust
source: mitre
type: generated
---
# pwdump

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

pwdump is a credential dumper.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/pwdump.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.002 - Security Account Manager](../../attack/techniques/T1003.002-security-account-manager.md) | explicit | source | [pwdump](https://attack.mitre.org/software/S0006) can be used to dump credentials from the SAM.(Citation: Wikipedia pwdump) |

## Source Verification

[source record](../../sources/mitre/pwdump.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:32:13.051Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[pwdump](https://attack.mitre.org/software/S0006) is a credential dumper. (Citation: Wikipedia pwdump)'
external_references:
- external_id: S0006
source_name: mitre-attack
url: https://attack.mitre.org/software/S0006
- description: Wikipedia. (2007, August 9). pwdump. Retrieved June 22, 2016.
```
