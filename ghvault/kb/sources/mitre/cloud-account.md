---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Account

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1136.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cloud Account](../../attack/techniques/T1136.003-cloud-account.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1136.003 |
| name | Cloud Account |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1136/003 |

## Preserved Source Material

```yaml
created: '2020-01-29T17:32:30.711Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may create a cloud account to maintain access to victim systems. With a sufficient level of access,
  such accounts may be used to establish secondary credentialed access that does not require persistent remote access tools
  to be deployed on the system.(Citation: Microsoft O365 Admin Roles)(Citation: Microsoft Support O365 Add Another Admin,
  October 2019)(Citation: AWS Create IAM User)(Citation: GCP Create Cloud Identity Users)(Citation: Microsoft Azure AD Users)


  In addition to user accounts, cloud accounts may be associated with services. Cloud providers handle the concept of service
  accounts in different ways. In Azure, service accounts include service principals and managed identities, which can be linked
  to various resources such as OAuth applications, serverless functions, and virtual machines in order to grant those resources
  permissions to perform various activities in the environment.(Citation: Microsoft Entra ID Service Principals) In GCP, service
  accounts can also be linked to specific resources, as well as be impersonated by other accounts for [Temporary Elevated
  Cloud Access](https://attack.mitre.org/techniques/T1548/005).(Citation: GCP Service Accounts) While AWS has no specific
  concept of service accounts, resources can be directly granted permission to assume roles.(Citation: AWS Instance Profiles)(Citation:
  AWS Lambda Execution Role)


  Adversaries may create accounts that only have access to specific cloud services, which can reduce the chance of detection.


  Once an adversary has created a cloud account, they can then manipulate that account to ensure persistence and allow access
  to additional resources - for example, by adding [Additional Cloud Credentials](https://attack.mitre.org/techniques/T1098/001)
  or assigning [Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003).'
external_references:
- external_id: T1136.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1136/003
- description: Ako-Adjei, K., Dickhaus, M., Baumgartner, P., Faigel, D., et. al.. (2019, October 8). About admin roles. Retrieved
    October 18, 2019.
  source_name: Microsoft O365 Admin Roles
  url: https://docs.microsoft.com/en-us/office365/admin/add-users/about-admin-roles?view=o365-worldwide
- description: AWS. (n.d.). Creating an IAM User in Your AWS Account. Retrieved January 29, 2020.
  source_name: AWS Create IAM User
  url: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html
- description: AWS. (n.d.). Lambda execution role. Retrieved February 28, 2024.
  source_name: AWS Lambda Execution Role
  url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html
- description: AWS. (n.d.). Using instance profiles. Retrieved February 28, 2024.
  source_name: AWS Instance Profiles
  url: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html
- description: Google. (n.d.). Create Cloud Identity user accounts. Retrieved January 29, 2020.
  source_name: GCP Create Cloud Identity Users
  url: https://support.google.com/cloudidentity/answer/7332836?hl=en&ref_topic=7558554
- description: Google. (n.d.). Service Accounts Overview. Retrieved February 28, 2024.
  source_name: GCP Service Accounts
  url: https://cloud.google.com/iam/docs/service-account-overview
- description: Microsoft. (2019, November 11). Add or delete users using Azure Active Directory. Retrieved January 30, 2020.
  source_name: Microsoft Azure AD Users
  url: https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/add-users-azure-active-directory
- description: Microsoft. (2023, December 15). Application and service principal objects in Microsoft Entra ID. Retrieved
    February 28, 2024.
  source_name: Microsoft Entra ID Service Principals
  url: https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals?tabs=browser
- description: Microsoft. (n.d.). Add Another Admin. Retrieved October 18, 2019.
  source_name: Microsoft Support O365 Add Another Admin, October 2019
  url: https://support.office.com/en-us/article/add-another-admin-f693489f-9f55-4bd0-a637-a81ce93de22d
id: attack-pattern--a009cb25-4801-4116-9105-80a91cf15c1b
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-10-24T17:49:09.917Z'
name: Cloud Account
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Praetorian
- Microsoft Threat Intelligence Center (MSTIC)
- Arun Seelagan, CISA
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
- SaaS
- Office Suite
- Identity Provider
x_mitre_version: '1.6'
```
