---
parsed_by: focuslocust
source: mitre
type: generated
---
# dsquery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0105` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

dsquery is a command-line utility that can be used to query Active Directory for information from a system within a domain.  It is typically installed only on Windows Server versions but can be installed on non-server variants through the Microsoft-provided Remote Server Administration Tools bundle.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/dsquery.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1069.002 - Domain Groups](../../attack/techniques/T1069.002-domain-groups.md) | explicit | source | [dsquery](https://attack.mitre.org/software/S0105) can be used to gather information on permission groups within a domain.(Citation: TechNet Dsquery)(Citation: Mandiant APT41) |
| [T1082 - System Information Discovery](../../attack/techniques/T1082-system-information-discovery.md) | explicit | source | [dsquery](https://attack.mitre.org/software/S0105) has the ability to enumerate various information, such as the operating system and host name, for systems within a domain.(Citation: Mandiant APT41) |
| [T1087.002 - Domain Account](../../attack/techniques/T1087.002-domain-account.md) | explicit | source | [dsquery](https://attack.mitre.org/software/S0105) can be used to gather information on user accounts within a domain.(Citation: TechNet Dsquery)(Citation: Mandiant APT41) |
| [T1482 - Domain Trust Discovery](../../attack/techniques/T1482-domain-trust-discovery.md) | explicit | source | [dsquery](https://attack.mitre.org/software/S0105) can be used to gather information on domain trusts with <code>dsquery * -filter "(objectClass=trustedDomain)" -attr *</code>.(Citation: Harmj0y Domain Trusts) |

## Source Verification

[source record](../../sources/mitre/dsquery.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:04.937Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[dsquery](https://attack.mitre.org/software/S0105) is a command-line utility that can be used to query Active
Directory for information from a system within a domain. (Citation: TechNet Dsquery) It is typically installed only on Windows
Server versions but can be installed on non-server variants through the Microsoft-provided Remote Server Administration
Tools bundle.'
external_references:
- external_id: S0105
```
