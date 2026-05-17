---
parsed_by: focuslocust
source: mitre
type: generated
---
# M1027 - Password Policies

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1027` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Set and enforce secure password policies for accounts to reduce the likelihood of unauthorized access. Strong password policies include enforcing password complexity, requiring regular password changes, and preventing password reuse. This mitigation can be implemented through the following measures:

Windows Systems:

- Use Group Policy Management Console (GPMC) to configure:
    - Minimum password length (e.g., 12+ characters).
    - Password complexity requirements.
    - Password history (e.g., disallow last 24 passwords).
    - Account lockout duration and thresholds.

Linux Systems:

- Configure Pluggable Authentication Modules (PAM):
- Use `pam_pwquality` to enforce complexity and length requirements.
- Implement `pam_tally2` or `pam_faillock` for account lockouts.
- Use `pwunconv` to disable password reuse.

Password Managers:

- Enforce usage of enterprise password managers (e.g., Bitwarden, 1Password, LastPass) to generate and store strong passwords.

Password Blacklisting:

- Use tools like Have I Been Pwned password checks or NIST-based blacklist solutions to prevent users from setting compromised passwords.

Regular Auditing:

- Periodically audit password policies and account configurations to ensure compliance using tools like LAPS (Local Admin Password Solution) and vulnerability scanners.

*Tools for Implementation*

Windows:

- Group Policy Management Console (GPMC): Enforce password policies.
- Microsoft Local Administrator Password Solution (LAPS): Enforce random, unique admin passwords.

Linux/macOS:

- PAM Modules (pam_pwquality, pam_tally2, pam_faillock): Enforce password rules.
- Lynis: Audit password policies and system configurations.

Cross-Platform:

- Password Managers (Bitwarden, 1Password, KeePass): Manage and enforce strong passwords.
- Have I Been Pwned API: Prevent the use of breached passwords.
- NIST SP 800-63B compliant tools: Enforce password guidelines and blacklisting.

## Source Verification

[source record](../../sources/mitre/password-policies.md)

## Evidence Excerpt

```text
created: '2019-06-06T21:10:35.792Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Set and enforce secure password policies for accounts to reduce the likelihood of unauthorized access. Strong\
\ password policies include enforcing password complexity, requiring regular password changes, and preventing password reuse.\
\ This mitigation can be implemented through the following measures:\n\nWindows Systems:\n\n- Use Group Policy Management\
\ Console (GPMC) to configure:\n    - Minimum password length (e.g., 12+ characters).\n    - Password complexity requirements.\n\
\    - Password history (e.g., disallow last 24 passwords).\n    - Account lockout duration and thresholds.\n\nLinux Systems:\n\
\n- Configure Pluggable Authentication Modules (PAM):\n- Use `pam_pwquality` to enforce complexity and length requirements.\n\
```
