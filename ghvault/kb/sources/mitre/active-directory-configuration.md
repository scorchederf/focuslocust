---
parsed_by: focuslocust
source: mitre
type: generated
---
# Active Directory Configuration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1015` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Active Directory Configuration](../../attack/mitigations/M1015-active-directory-configuration.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1015 |
| name | Active Directory Configuration |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1015 |

## Preserved Source Material

```yaml
created: '2019-06-06T16:39:58.291Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Implement robust Active Directory (AD) configurations using group policies to secure user accounts, control
  access, and minimize the attack surface. AD configurations enable centralized control over account settings, logon policies,
  and permissions, reducing the risk of unauthorized access and lateral movement within the network. This mitigation can be
  implemented through the following measures:


  Account Configuration:


  - Implementation: Use domain accounts instead of local accounts to leverage AD’s centralized management, including group
  policies, auditing, and access control.

  - Use Case: For IT staff managing shared resources, provision domain accounts that allow IT teams to log in centrally, reducing
  the risk of unmanaged, rogue local accounts on individual machines.


  Interactive Logon Restrictions:


  - Implementation: Configure group policies to restrict interactive logons (e.g., direct physical or RDP logons) for service
  accounts or privileged accounts that do not require such access.

  - Use Case: Prevent service accounts, such as SQL Server accounts, from having interactive logon privileges. This reduces
  the risk of these accounts being leveraged for lateral movement if compromised.


  Remote Desktop Settings:


  - Implementation: Limit Remote Desktop Protocol (RDP) access to specific, authorized accounts. Use group policies to enforce
  this, allowing only necessary users to establish RDP sessions.

  - Use Case: On sensitive servers (e.g., domain controllers or financial databases), restrict RDP access to administrative
  accounts only, while all other users are denied access.


  Dedicated Administrative Accounts:


  - Implementation: Create domain-wide administrative accounts that are restricted from interactive logons, designed solely
  for high-level tasks (e.g., software installation, patching).

  - Use Case: Create separate administrative accounts for different purposes, such as one set of accounts for installations
  and another for managing repository access. This limits exposure and helps reduce attack vectors.


  Authentication Silos:


  - Implementation: Configure Authentication Silos in AD, using group policies to create access zones with restrictions based
  on membership, such as the Protected Users security group. This restricts access to critical accounts and minimizes exposure
  to potential threats.

  - Use Case: Place high-risk or high-value accounts, such as executive or administrative accounts, in an Authentication Silo
  with extra controls, limiting their exposure to only necessary systems. This reduces the risk of credential misuse or abuse
  if these accounts are compromised.


  **Tools for Implementation**:


  - Active Directory Group Policies: Use Group Policy Management Console (GPMC) to configure, deploy, and enforce policies
  across AD environments.

  - PowerShell: Automate account configuration, logon restrictions, and policy application using PowerShell scripts.

  - AD Administrative Center: Manage Authentication Silos and configure high-level policies for critical user groups within
  AD.'
external_references:
- external_id: M1015
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1015
id: course-of-action--e3388c78-2a8d-47c2-8422-c1398b324462
modified: '2024-12-10T15:57:59.336Z'
name: Active Directory Configuration
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
