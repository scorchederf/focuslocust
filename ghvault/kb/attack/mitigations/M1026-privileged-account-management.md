---
parsed_by: focuslocust
source: mitre
type: generated
---
# M1026 - Privileged Account Management

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1026` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Privileged Account Management focuses on implementing policies, controls, and tools to securely manage privileged accounts (e.g., SYSTEM, root, or administrative accounts). This includes restricting access, limiting the scope of permissions, monitoring privileged account usage, and ensuring accountability through logging and auditing.This mitigation can be implemented through the following measures:

Account Permissions and Roles:

- Implement RBAC and least privilege principles to allocate permissions securely.
- Use tools like Active Directory Group Policies to enforce access restrictions.

Credential Security:

- Deploy password vaulting tools like CyberArk, HashiCorp Vault, or KeePass for secure storage and rotation of credentials.
- Enforce password policies for complexity, uniqueness, and expiration using tools like Microsoft Group Policy Objects (GPO).

Multi-Factor Authentication (MFA):

- Enforce MFA for all privileged accounts using Duo Security, Okta, or Microsoft Azure AD MFA.

Privileged Access Management (PAM):

- Use PAM solutions like CyberArk, BeyondTrust, or Thycotic to manage, monitor, and audit privileged access.

Auditing and Monitoring:

- Integrate activity monitoring into your SIEM (e.g., Splunk or QRadar) to detect and alert on anomalous privileged account usage.

Just-In-Time Access:

- Deploy JIT solutions like Azure Privileged Identity Management (PIM) or configure ephemeral roles in AWS and GCP to grant time-limited elevated permissions.

*Tools for Implementation*

Privileged Access Management (PAM):

- CyberArk, BeyondTrust, Thycotic, HashiCorp Vault.

Credential Management:

- Microsoft LAPS (Local Admin Password Solution), Password Safe, HashiCorp Vault, KeePass.

Multi-Factor Authentication:

- Duo Security, Okta, Microsoft Azure MFA, Google Authenticator.

Linux Privilege Management:

- sudo configuration, SELinux, AppArmor.

Just-In-Time Access:

- Azure Privileged Identity Management (PIM), AWS IAM Roles with session constraints, GCP Identity-Aware Proxy.

## Source Verification

[source record](../../sources/mitre/privileged-account-management.md)

## Evidence Excerpt

```text
created: '2019-06-06T21:09:47.115Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Privileged Account Management focuses on implementing policies, controls, and tools to securely manage privileged
accounts (e.g., SYSTEM, root, or administrative accounts). This includes restricting access, limiting the scope of permissions,
monitoring privileged account usage, and ensuring accountability through logging and auditing.This mitigation can be implemented
through the following measures:
Account Permissions and Roles:
- Implement RBAC and least privilege principles to allocate permissions securely.
```
