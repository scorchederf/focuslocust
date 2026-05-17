---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1056 - Input Capture

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1056` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may use methods of capturing user input to obtain credentials or collect information. During normal system usage, users often provide credentials to various different locations, such as login pages/portals or system dialog boxes. Input capture mechanisms may be transparent to the user (e.g. Credential API Hooking) or rely on deceiving the user into providing input into what they believe to be a genuine service (e.g. Web Portal Capture).

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [NPPSPY](../../tools/unknown/nppspy.md) | explicit | source | [NPPSPY](https://attack.mitre.org/software/S1131) captures user input into the Winlogon process by redirecting RPC traffic from legitimate listening DLLs within the operating system to a newly registered malicious item that allows for recording logon information in cleartext.(Citation: Huntress NPPSPY 2022) |

## Source Verification

[source record](../../sources/mitre/input-capture.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:48.323Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Adversaries may use methods of capturing user input to obtain credentials or collect information. During normal
system usage, users often provide credentials to various different locations, such as login pages/portals or system dialog
boxes. Input capture mechanisms may be transparent to the user (e.g. [Credential API Hooking](https://attack.mitre.org/techniques/T1056/004))
or rely on deceiving the user into providing input into what they believe to be a genuine service (e.g. [Web Portal Capture](https://attack.mitre.org/techniques/T1056/003)).
external_references:
- external_id: T1056
```
