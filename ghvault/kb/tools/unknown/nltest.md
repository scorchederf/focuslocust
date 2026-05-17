---
parsed_by: focuslocust
source: mitre
type: generated
---
# Nltest

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0359` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Nltest is a Windows command-line utility used to list domain controllers and enumerate domain trusts.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/nltest.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [Nltest](https://attack.mitre.org/software/S0359) may be used to enumerate the parent domain of a local machine using <code>/parentdomain</code>.(Citation: Nltest Manual) |
| [T1018 - Remote System Discovery](../../attack/techniques/T1018-remote-system-discovery.md) | explicit | source | [Nltest](https://attack.mitre.org/software/S0359) may be used to enumerate remote domain controllers using options such as <code>/dclist</code> and <code>/dsgetdc</code>.(Citation: Nltest Manual) |
| [T1482 - Domain Trust Discovery](../../attack/techniques/T1482-domain-trust-discovery.md) | explicit | source | [Nltest](https://attack.mitre.org/software/S0359) may be used to enumerate trusted domains by using commands such as <code>nltest /domain_trusts</code>.(Citation: Nltest Manual)(Citation: Fortinet TrickBot) |

## Source Verification

[source record](../../sources/mitre/nltest.md)

## Evidence Excerpt

```text
created: '2019-02-14T17:08:55.176Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Nltest](https://attack.mitre.org/software/S0359) is a Windows command-line utility used to list domain controllers
and enumerate domain trusts.(Citation: Nltest Manual)'
external_references:
- external_id: S0359
source_name: mitre-attack
url: https://attack.mitre.org/software/S0359
```
