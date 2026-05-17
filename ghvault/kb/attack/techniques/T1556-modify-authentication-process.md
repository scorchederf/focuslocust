---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1556 - Modify Authentication Process

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1556` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may modify authentication mechanisms and processes to access user credentials or enable otherwise unwarranted access to accounts. The authentication process is handled by mechanisms, such as the Local Security Authentication Server (LSASS) process and the Security Accounts Manager (SAM) on Windows, pluggable authentication modules (PAM) on Unix-based systems, and authorization plugins on MacOS systems, responsible for gathering, storing, and validating credentials. By modifying an authentication process, an adversary may be able to authenticate to a service or system without using Valid Accounts.

Adversaries may maliciously modify a part of this process to either reveal credentials or bypass authentication mechanisms. Compromised credentials or access may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access and remote desktop.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can create a backdoor in KeePass using a malicious config file and in TortoiseSVN using a registry hook.(Citation: GitHub SILENTTRINITY Modules July 2019) |

## Source Verification

[source record](../../sources/mitre/modify-authentication-process.md)

## Evidence Excerpt

```text
created: '2020-02-11T19:01:56.887Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may modify authentication mechanisms and processes to access user credentials or enable otherwise
unwarranted access to accounts. The authentication process is handled by mechanisms, such as the Local Security Authentication
Server (LSASS) process and the Security Accounts Manager (SAM) on Windows, pluggable authentication modules (PAM) on Unix-based
systems, and authorization plugins on MacOS systems, responsible for gathering, storing, and validating credentials. By
modifying an authentication process, an adversary may be able to authenticate to a service or system without using [Valid
Accounts](https://attack.mitre.org/techniques/T1078).
```
