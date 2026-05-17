---
parsed_by: focuslocust
source: mitre
type: generated
---
# Reg

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0075` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Reg is a Windows utility used to interact with the Windows Registry. It can be used at the command-line interface to query, add, modify, and remove information. 

Utilities such as Reg are known to be used by persistent threats.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/reg.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1012 - Query Registry](../../attack/techniques/T1012-query-registry.md) | explicit | source | [Reg](https://attack.mitre.org/software/S0075) may be used to gather details from the Windows Registry of a local or remote system at the command-line interface.(Citation: Microsoft Reg) |
| [T1112 - Modify Registry](../../attack/techniques/T1112-modify-registry.md) | explicit | source | [Reg](https://attack.mitre.org/software/S0075) may be used to interact with and modify the Windows Registry of a local or remote system at the command-line interface.(Citation: Microsoft Reg) |
| [T1552.002 - Credentials in Registry](../../attack/techniques/T1552.002-credentials-in-registry.md) | explicit | source | [Reg](https://attack.mitre.org/software/S0075) may be used to find credentials in the Windows Registry.(Citation: Pentestlab Stored Credentials) |

## Source Verification

[source record](../../sources/mitre/reg.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:32:49.000Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Reg](https://attack.mitre.org/software/S0075) is a Windows utility used to interact with the Windows Registry.
It can be used at the command-line interface to query, add, modify, and remove information. (Citation: Microsoft Reg)
Utilities such as [Reg](https://attack.mitre.org/software/S0075) are known to be used by persistent threats. (Citation:
Windows Commands JPCERT)'
external_references:
- external_id: S0075
```
