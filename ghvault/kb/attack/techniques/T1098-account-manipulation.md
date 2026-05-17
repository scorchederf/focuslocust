---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1098 - Account Manipulation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1098` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may manipulate accounts to maintain and/or elevate access to victim systems. Account manipulation may consist of any action that preserves or modifies adversary access to a compromised account, such as modifying credentials or permission groups. These actions could also include account activity designed to subvert security policies, such as performing iterative password updates to bypass password duration policies and preserve the life of compromised credentials. 

In order to create or manipulate accounts, the adversary must already have sufficient permissions on systems or the domain. However, account manipulation may also lead to privilege escalation where modifications grant access to additional roles, permissions, or higher-privileged Valid Accounts.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Mimikatz](../../tools/unknown/mimikatz.md) | explicit | source | The [Mimikatz](https://attack.mitre.org/software/S0002) credential dumper has been extended to include Skeleton Key domain controller authentication bypass functionality. The <code>LSADUMP::ChangeNTLM</code> and <code>LSADUMP::SetNTLM</code> modules can also manipulate the password hash of an account without knowing the clear text value.(Citation: Adsecurity Mimikatz Guide)(Citation: Metcalf 2015) |

## Source Verification

[source record](../../sources/mitre/account-manipulation.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:12.196Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may manipulate accounts to maintain and/or elevate access to victim systems. Account manipulation\
\ may consist of any action that preserves or modifies adversary access to a compromised account, such as modifying credentials\
\ or permission groups.(Citation: FireEye SMOKEDHAM June 2021) These actions could also include account activity designed\
\ to subvert security policies, such as performing iterative password updates to bypass password duration policies and preserve\
\ the life of compromised credentials. \n\nIn order to create or manipulate accounts, the adversary must already have sufficient\
\ permissions on systems or the domain. However, account manipulation may also lead to privilege escalation where modifications\
```
