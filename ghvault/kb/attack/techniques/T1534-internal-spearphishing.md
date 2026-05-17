---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1534 - Internal Spearphishing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1534` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

After they already have access to accounts or systems within the environment, adversaries may use internal spearphishing to gain access to additional information or compromise other users within the same organization. Internal spearphishing is multi-staged campaign where a legitimate account is initially compromised either by controlling the user's device or by compromising the account credentials of the user. Adversaries may then attempt to take advantage of the trusted internal account to increase the likelihood of tricking more victims into falling for phish attempts, often incorporating Impersonation.

For example, adversaries may leverage Spearphishing Attachment or Spearphishing Link as part of internal spearphishing to deliver a payload or redirect to an external site to capture credentials through Input Capture on sites that mimic login interfaces.

Adversaries may also leverage internal chat apps, such as Microsoft Teams, to spread malicious content or engage users in attempts to capture sensitive information and/or credentials.

## Source Verification

[source record](../../sources/mitre/internal-spearphishing.md)

## Evidence Excerpt

```text
created: '2019-09-04T19:26:12.441Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'After they already have access to accounts or systems within the environment, adversaries may use internal spearphishing
to gain access to additional information or compromise other users within the same organization. Internal spearphishing
is multi-staged campaign where a legitimate account is initially compromised either by controlling the user''s device or
by compromising the account credentials of the user. Adversaries may then attempt to take advantage of the trusted internal
account to increase the likelihood of tricking more victims into falling for phish attempts, often incorporating [Impersonation](https://attack.mitre.org/techniques/T1684/001).(Citation:
Trend Micro - Int SP)
```
