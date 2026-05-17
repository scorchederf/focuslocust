---
parsed_by: focuslocust
source: mitre
type: generated
---
# M1032 - Multi-factor Authentication

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1032` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Multi-Factor Authentication (MFA) enhances security by requiring users to provide at least two forms of verification to prove their identity before granting access. These factors typically include:

- *Something you know*: Passwords, PINs.
- *Something you have*: Physical tokens, smartphone authenticator apps.
- *Something you are*: Biometric data such as fingerprints, facial recognition, or retinal scans.

Implementing MFA across all critical systems and services ensures robust protection against account takeover and unauthorized access. This mitigation can be implemented through the following measures:

Identity and Access Management (IAM):

- Use IAM solutions like Azure Active Directory, Okta, or AWS IAM to enforce MFA policies for all user logins, especially for privileged roles.
- Enable conditional access policies to enforce MFA for risky sign-ins (e.g., unfamiliar devices, geolocations).
- Enable Conditional Access policies to only allow logins from trusted devices, such as those enrolled in Intune or joined via Hybrid/Entra.

Authentication Tools and Methods:

- Use authenticator applications such as Google Authenticator, Microsoft Authenticator, or Authy for time-based one-time passwords (TOTP).
- Deploy hardware-based tokens like YubiKey, RSA SecurID, or smart cards for additional security.
- Enforce biometric authentication for compatible devices and applications.

Secure Legacy Systems:

- Integrate MFA solutions with older systems using third-party tools like Duo Security or Thales SafeNet.
- Enable RADIUS/NPS servers to facilitate MFA for VPNs, RDP, and other network logins.

Monitoring and Alerting:

- Use SIEM tools to monitor failed MFA attempts, login anomalies, or brute-force attempts against MFA systems.
- Implement alerts for suspicious MFA activities, such as repeated failed codes or new device registrations.

Training and Policy Enforcement:

- Educate employees on the importance of MFA and secure authenticator usage.
- Enforce policies that require MFA on all critical systems, especially for remote access, privileged accounts, and cloud applications.

## Source Verification

[source record](../../sources/mitre/multi-factor-authentication.md)

## Evidence Excerpt

```text
created: '2019-06-10T20:53:36.319Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Multi-Factor Authentication (MFA) enhances security by requiring users to provide at least two forms of verification
to prove their identity before granting access. These factors typically include:
- *Something you know*: Passwords, PINs.
- *Something you have*: Physical tokens, smartphone authenticator apps.
- *Something you are*: Biometric data such as fingerprints, facial recognition, or retinal scans.
Implementing MFA across all critical systems and services ensures robust protection against account takeover and unauthorized
```
