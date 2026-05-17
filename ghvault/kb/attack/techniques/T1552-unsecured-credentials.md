---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1552 - Unsecured Credentials

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1552` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may search compromised systems to find and obtain insecurely stored credentials. These credentials can be stored and/or misplaced in many locations on a system, including plaintext files (e.g. Shell History), operating system or application-specific repositories (e.g. Credentials in Registry),  or other specialized files/artifacts (e.g. Private Keys).

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [NPPSPY](../../tools/unknown/nppspy.md) | explicit | source | [NPPSPY](https://attack.mitre.org/software/S1131) captures credentials by recording them through an alternative network listener registered to the <code>mpnotify.exe</code> process, allowing for cleartext recording of logon information.(Citation: Huntress NPPSPY 2022) |
| [Pacu](../../tools/unknown/pacu.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can search for sensitive data: for example, in Code Build environment variables, EC2 user data, and Cloud Formation templates.(Citation: GitHub Pacu) |

## Source Verification

[source record](../../sources/mitre/unsecured-credentials.md)

## Evidence Excerpt

```text
created: '2020-02-04T12:47:23.631Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may search compromised systems to find and obtain insecurely stored credentials. These credentials
can be stored and/or misplaced in many locations on a system, including plaintext files (e.g. [Shell History](https://attack.mitre.org/techniques/T1552/003)),
operating system or application-specific repositories (e.g. [Credentials in Registry](https://attack.mitre.org/techniques/T1552/002)),  or
other specialized files/artifacts (e.g. [Private Keys](https://attack.mitre.org/techniques/T1552/004)).(Citation: Brining
MimiKatz to Unix)'
external_references:
```
