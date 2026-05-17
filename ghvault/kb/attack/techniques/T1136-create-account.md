---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1136 - Create Account

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1136` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may create an account to maintain access to victim systems. With a sufficient level of access, creating such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

Accounts may be created on the local system or within a domain or cloud tenant. In cloud environments, adversaries may create accounts that only have access to specific services, which can reduce the chance of detection.

## Source Verification

[source record](../../sources/mitre/create-account.md)

## Evidence Excerpt

```text
created: '2017-12-14T16:46:06.044Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may create an account to maintain access to victim systems.(Citation: Symantec WastedLocker June
2020) With a sufficient level of access, creating such accounts may be used to establish secondary credentialed access that
do not require persistent remote access tools to be deployed on the system.
Accounts may be created on the local system or within a domain or cloud tenant. In cloud environments, adversaries may create
accounts that only have access to specific services, which can reduce the chance of detection.'
external_references:
```
