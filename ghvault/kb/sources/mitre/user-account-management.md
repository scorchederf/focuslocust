---
parsed_by: focuslocust
source: mitre
type: generated
---
# User Account Management

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1018` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [User Account Management](../../attack/mitigations/M1018-user-account-management.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1018 |
| name | User Account Management |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1018 |

## Preserved Source Material

```yaml
created: '2019-06-06T16:50:58.767Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'User Account Management involves implementing and enforcing policies for the lifecycle of user accounts, including
  creation, modification, and deactivation. Proper account management reduces the attack surface by limiting unauthorized
  access, managing account privileges, and ensuring accounts are used according to organizational policies. This mitigation
  can be implemented through the following measures:


  Enforcing the Principle of Least Privilege


  - Implementation: Assign users only the minimum permissions required to perform their job functions. Regularly audit accounts
  to ensure no excess permissions are granted.

  - Use Case: Reduces the risk of privilege escalation by ensuring accounts cannot perform unauthorized actions.


  Implementing Strong Password Policies


  - Implementation: Enforce password complexity requirements (e.g., length, character types). Require password expiration
  every 90 days and disallow password reuse.

  - Use Case: Prevents adversaries from gaining unauthorized access through password guessing or brute force attacks.


  Managing Dormant and Orphaned Accounts


  - Implementation: Implement automated workflows to disable accounts after a set period of inactivity (e.g., 30 days). Remove
  orphaned accounts (e.g., accounts without an assigned owner) during regular account audits.

  - Use Case: Eliminates dormant accounts that could be exploited by attackers.


  Account Lockout Policies


  - Implementation: Configure account lockout thresholds (e.g., lock accounts after five failed login attempts). Set lockout
  durations to a minimum of 15 minutes.

  - Use Case: Mitigates automated attack techniques that rely on repeated login attempts.


  Multi-Factor Authentication (MFA) for High-Risk Accounts


  - Implementation: Require MFA for all administrative accounts and high-risk users. Use MFA mechanisms like hardware tokens,
  authenticator apps, or biometrics.

  - Use Case: Prevents unauthorized access, even if credentials are stolen.


  Restricting Interactive Logins


  - Implementation: Restrict interactive logins for privileged accounts to specific secure systems or management consoles.
  Use group policies to enforce logon restrictions.

  - Use Case: Protects sensitive accounts from misuse or exploitation.


  *Tools for Implementation*


  Built-in Tools:


  - Microsoft Active Directory (AD): Centralized account management and RBAC enforcement.

  - Group Policy Object (GPO): Enforce password policies, logon restrictions, and account lockout policies.


  Identity and Access Management (IAM) Tools:


  - Okta: Centralized user provisioning, MFA, and SSO integration.

  - Microsoft Azure Active Directory: Provides advanced account lifecycle management, role-based access, and conditional access
  policies.


  Privileged Account Management (PAM):

  - CyberArk, BeyondTrust, Thycotic: Manage and monitor privileged account usage, enforce session recording, and JIT access.'
external_references:
- external_id: M1018
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1018
id: course-of-action--93e7968a-9074-4eac-8ae9-9f5200ec3317
modified: '2024-12-24T14:33:36.029Z'
name: User Account Management
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: course-of-action
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '1.2'
```
