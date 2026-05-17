---
parsed_by: focuslocust
source: mitre
type: generated
---
# gsecdump

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0008` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

gsecdump is a publicly-available credential dumper used to obtain password hashes and LSA secrets from Windows operating systems.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/gsecdump.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.002 - Security Account Manager](../../attack/techniques/T1003.002-security-account-manager.md) | explicit | source | [gsecdump](https://attack.mitre.org/software/S0008) can dump Windows password hashes from the SAM.(Citation: Microsoft Gsecdump) |
| [T1003.004 - LSA Secrets](../../attack/techniques/T1003.004-lsa-secrets.md) | explicit | source | [gsecdump](https://attack.mitre.org/software/S0008) can dump LSA secrets.(Citation: TrueSec Gsecdump) |

## Source Verification

[source record](../../sources/mitre/gsecdump.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:32:13.755Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[gsecdump](https://attack.mitre.org/software/S0008) is a publicly-available credential dumper used to obtain
password hashes and LSA secrets from Windows operating systems. (Citation: TrueSec Gsecdump)'
external_references:
- external_id: S0008
source_name: mitre-attack
url: https://attack.mitre.org/software/S0008
```
