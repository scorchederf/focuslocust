---
parsed_by: focuslocust
source: mitre
type: generated
---
# MailSniper

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0413` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

MailSniper is a penetration testing tool for searching through email in a Microsoft Exchange environment for specific terms (passwords, insider intel, network architecture information, etc.). It can be used by a non-administrative user to search their own email, or by an Exchange administrator to search the mailboxes of every user in a domain.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/mailsniper.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1087.003 - Email Account](../../attack/techniques/T1087.003-email-account.md) | explicit | source | [MailSniper](https://attack.mitre.org/software/S0413) can be used to obtain account names from Exchange and Office 365 using the <code>Get-GlobalAddressList</code> cmdlet.(Citation: Black Hills Attacking Exchange MailSniper, 2016) |
| [T1110.003 - Password Spraying](../../attack/techniques/T1110.003-password-spraying.md) | explicit | source | [MailSniper](https://attack.mitre.org/software/S0413) can be used for password spraying against Exchange and Office 365.(Citation: GitHub MailSniper) |
| [T1114.002 - Remote Email Collection](../../attack/techniques/T1114.002-remote-email-collection.md) | explicit | source | [MailSniper](https://attack.mitre.org/software/S0413) can be used for searching through email in Exchange and Office 365 environments.(Citation: GitHub MailSniper) |

## Source Verification

[source record](../../sources/mitre/mailsniper.md)

## Evidence Excerpt

```text
created: '2019-10-05T02:34:01.189Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'MailSniper is a penetration testing tool for searching through email in a Microsoft Exchange environment for
specific terms (passwords, insider intel, network architecture information, etc.). It can be used by a non-administrative
user to search their own email, or by an Exchange administrator to search the mailboxes of every user in a domain.(Citation:
GitHub MailSniper)'
external_references:
- external_id: S0413
```
