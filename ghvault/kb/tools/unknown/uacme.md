---
parsed_by: focuslocust
source: mitre
type: generated
---
# UACMe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0116` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

UACMe is an open source assessment tool that contains many methods for bypassing Windows User Account Control on multiple versions of the operating system.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/uacme.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | [UACMe](https://attack.mitre.org/software/S0116) contains many methods for bypassing Windows User Account Control on multiple versions of the operating system.(Citation: Github UACMe) |

## Source Verification

[source record](../../sources/mitre/uacme.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:09.047Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[UACMe](https://attack.mitre.org/software/S0116) is an open source assessment tool that contains many methods
for bypassing Windows User Account Control on multiple versions of the operating system. (Citation: Github UACMe)'
external_references:
- external_id: S0116
source_name: mitre-attack
url: https://attack.mitre.org/software/S0116
```
