---
parsed_by: focuslocust
source: mitre
type: generated
---
# Rubeus

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S1071` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Rubeus is a C# toolset designed for raw Kerberos interaction that has been used since at least 2020, including in ransomware operations.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/rubeus.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1482 - Domain Trust Discovery](../../attack/techniques/T1482-domain-trust-discovery.md) | explicit | source | [Rubeus](https://attack.mitre.org/software/S1071) can gather information about domain trusts.(Citation: DFIR Ryuk's Return October 2020)(Citation: DFIR Ryuk 2 Hour Speed Run November 2020) |
| [T1558.001 - Golden Ticket](../../attack/techniques/T1558.001-golden-ticket.md) | explicit | source | [Rubeus](https://attack.mitre.org/software/S1071) can forge a ticket-granting ticket.(Citation: GitHub Rubeus March 2023) |
| [T1558.002 - Silver Ticket](../../attack/techniques/T1558.002-silver-ticket.md) | explicit | source | [Rubeus](https://attack.mitre.org/software/S1071) can create silver tickets.(Citation: GitHub Rubeus March 2023) |
| [T1558.003 - Kerberoasting](../../attack/techniques/T1558.003-kerberoasting.md) | explicit | source | [Rubeus](https://attack.mitre.org/software/S1071) can use the `KerberosRequestorSecurityToken.GetRequest` method to request kerberoastable service tickets.(Citation: GitHub Rubeus March 2023) |
| [T1558.004 - AS-REP Roasting](../../attack/techniques/T1558.004-as-rep-roasting.md) | explicit | source | [Rubeus](https://attack.mitre.org/software/S1071) can reveal the credentials of accounts that have Kerberos pre-authentication disabled through AS-REP roasting.(Citation: GitHub Rubeus March 2023)(Citation: DFIR Ryuk's Return October 2020)(Citation: DFIR Ryuk 2 Hour Speed Run November 2020)  |

## Source Verification

[source record](../../sources/mitre/rubeus.md)

## Evidence Excerpt

```text
created: '2023-03-29T20:19:26.940Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Rubeus](https://attack.mitre.org/software/S1071) is a C# toolset designed for raw Kerberos interaction that
has been used since at least 2020, including in ransomware operations.(Citation: GitHub Rubeus March 2023)(Citation: FireEye
KEGTAP SINGLEMALT October 2020)(Citation: DFIR Ryuk''s Return October 2020)(Citation: DFIR Ryuk 2 Hour Speed Run November
2020)'
external_references:
- external_id: S1071
```
