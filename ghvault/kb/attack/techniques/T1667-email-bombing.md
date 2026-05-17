---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1667 - Email Bombing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1667` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may flood targeted email addresses with an overwhelming volume of messages. This may bury legitimate emails in a flood of spam and disrupt business operations.

An adversary may accomplish email bombing by leveraging an automated bot to register a targeted address for e-mail lists that do not validate new signups, such as online newsletters. The result can be a wave of thousands of e-mails that effectively overloads the victim’s inbox.

By sending hundreds or thousands of e-mails in quick succession, adversaries may successfully divert attention away from and bury legitimate messages including security alerts, daily business processes like help desk tickets and client correspondence, or ongoing scams. This behavior can also be used as a tool of harassment.

This behavior may be a precursor for Spearphishing Voice. For example, an adversary may email bomb a target and then follow up with a phone call to fraudulently offer assistance. This social engineering may lead to the use of Remote Access Software to steal credentials, deploy ransomware, conduct Financial Theft, or engage in other malicious activity.

## Source Verification

[source record](../../sources/mitre/email-bombing.md)

## Evidence Excerpt

```text
created: '2025-01-31T14:39:58.478Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may flood targeted email addresses with an overwhelming volume of messages. This may bury legitimate
emails in a flood of spam and disrupt business operations.(Citation: sophos-bombing)(Citation: krebs-email-bombing)
An adversary may accomplish email bombing by leveraging an automated bot to register a targeted address for e-mail lists
that do not validate new signups, such as online newsletters. The result can be a wave of thousands of e-mails that effectively
overloads the victim’s inbox.(Citation: krebs-email-bombing)(Citation: hhs-email-bombing)
By sending hundreds or thousands of e-mails in quick succession, adversaries may successfully divert attention away from
```
