---
parsed_by: focuslocust
source: mitre
type: generated
---
# Password Policy Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1201` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Password Policy Discovery](../../attack/techniques/T1201-password-policy-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1201 |
| name | Password Policy Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1201 |

## Preserved Source Material

```yaml
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to access detailed information about the password policy used within an enterprise network
  or cloud environment. Password policies are a way to enforce complex passwords that are difficult to guess or crack through
  [Brute Force](https://attack.mitre.org/techniques/T1110). This information may help the adversary to create a list of common
  passwords and launch dictionary and/or brute force attacks which adheres to the policy (e.g. if the minimum password length
  should be 8, then not trying passwords such as ''pass123''; not checking for more than 3-4 passwords per account if the
  lockout is set to 6 as to not lock out accounts).


  Password policies can be set and discovered on Windows, Linux, and macOS systems via various command shell utilities such
  as <code>net accounts (/domain)</code>, <code>Get-ADDefaultDomainPasswordPolicy</code>, <code>chage -l <username></code>,
  <code>cat /etc/pam.d/common-password</code>, and <code>pwpolicy getaccountpolicies</code> (Citation: Superuser Linux Password
  Policies) (Citation: Jamf User Password Policies). Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008)
  on network devices to discover password policy information (e.g. <code>show aaa</code>, <code>show aaa common-criteria policy
  all</code>).(Citation: US-CERT-TA18-106A)


  Password policies can be discovered in cloud environments using available APIs such as <code>GetAccountPasswordPolicy</code>
  in AWS (Citation: AWS GetPasswordPolicy).'
external_references:
- external_id: T1201
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1201
- description: Amazon Web Services. (n.d.). AWS API GetAccountPasswordPolicy. Retrieved June 8, 2021.
  source_name: AWS GetPasswordPolicy
  url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountPasswordPolicy.html
- description: Holland, J. (2016, January 25). User password policies on non AD machines. Retrieved April 5, 2018.
  source_name: Jamf User Password Policies
  url: https://www.jamf.com/jamf-nation/discussions/18574/user-password-policies-on-non-ad-machines
- description: Matutiae, M. (2014, August 6). How to display password policy information for a user (Ubuntu)?. Retrieved April
    5, 2018.
  source_name: Superuser Linux Password Policies
  url: https://superuser.com/questions/150675/how-to-display-password-policy-information-for-a-user-ubuntu
- description: US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure
    Devices. Retrieved October 19, 2020.
  source_name: US-CERT-TA18-106A
  url: https://www.us-cert.gov/ncas/alerts/TA18-106A
id: attack-pattern--b6075259-dba3-44e9-87c7-e954f37ec0d5
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:49:15.781Z'
name: Password Policy Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Regina Elwell
- Sudhanshu Chauhan, @Sudhanshu_C
- Isif Ibrahima, Mandiant
- Austin Clark, @c2defense
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
- Linux
- macOS
- IaaS
- Network Devices
- Identity Provider
- SaaS
- Office Suite
x_mitre_version: '1.7'
```
