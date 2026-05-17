---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1621 - Multi-Factor Authentication Request Generation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1621` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to bypass multi-factor authentication (MFA) mechanisms and gain access to accounts by generating MFA requests sent to users.

Adversaries in possession of credentials to Valid Accounts may be unable to complete the login process if they lack access to the 2FA or MFA mechanisms required as an additional credential and security control. To circumvent this, adversaries may abuse the automatic generation of push notifications to MFA services such as Duo Push, Microsoft Authenticator, Okta, or similar services to have the user grant access to their account. If adversaries lack credentials to victim accounts, they may also abuse automatic push notification generation when this option is configured for self-service password reset (SSPR).

In some cases, adversaries may continuously repeat login attempts in order to bombard users with MFA push notifications, SMS messages, and phone calls, potentially resulting in the user finally accepting the authentication request in response to “MFA fatigue.”

## Source Verification

[source record](../../sources/mitre/multi-factor-authentication-request-generation.md)

## Evidence Excerpt

```text
created: '2022-04-01T02:15:49.754Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to bypass multi-factor authentication (MFA) mechanisms and gain access to accounts by
generating MFA requests sent to users.
Adversaries in possession of credentials to [Valid Accounts](https://attack.mitre.org/techniques/T1078) may be unable to
complete the login process if they lack access to the 2FA or MFA mechanisms required as an additional credential and security
control. To circumvent this, adversaries may abuse the automatic generation of push notifications to MFA services such as
Duo Push, Microsoft Authenticator, Okta, or similar services to have the user grant access to their account. If adversaries
```
