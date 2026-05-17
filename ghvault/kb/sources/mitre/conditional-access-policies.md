---
parsed_by: focuslocust
source: mitre
type: generated
---
# Conditional Access Policies

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1556.009` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Conditional Access Policies](../../attack/techniques/T1556.009-conditional-access-policies.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1556.009 |
| name | Conditional Access Policies |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1556/009 |

## Preserved Source Material

```yaml
created: '2024-01-02T13:43:37.389Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may disable or modify conditional access policies to enable persistent access to compromised accounts.\
  \ Conditional access policies are additional verifications used by identity providers and identity and access management\
  \ systems to determine whether a user should be granted access to a resource.\n\nFor example, in Entra ID, Okta, and JumpCloud,\
  \ users can be denied access to applications based on their IP address, device enrollment status, and use of multi-factor\
  \ authentication.(Citation: Microsoft Conditional Access)(Citation: JumpCloud Conditional Access Policies)(Citation: Okta\
  \ Conditional Access Policies) In some cases, identity providers may also support the use of risk-based metrics to deny\
  \ sign-ins based on a variety of indicators. In AWS and GCP, IAM policies can contain `condition` attributes that verify\
  \ arbitrary constraints such as the source IP, the date the request was made, and the nature of the resources or regions\
  \ being requested.(Citation: AWS IAM Conditions)(Citation: GCP IAM Conditions) These measures help to prevent compromised\
  \ credentials from resulting in unauthorized access to data or resources, as well as limit user permissions to only those\
  \ required. \n\nBy modifying conditional access policies, such as adding additional trusted IP ranges, removing [Multi-Factor\
  \ Authentication](https://attack.mitre.org/techniques/T1556/006) requirements, or allowing additional [Unused/Unsupported\
  \ Cloud Regions](https://attack.mitre.org/techniques/T1535), adversaries may be able to ensure persistent access to accounts\
  \ and circumvent defensive measures."
external_references:
- external_id: T1556.009
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1556/009
- description: 'AWS. (n.d.). IAM JSON policy elements: Condition. Retrieved January 2, 2024.'
  source_name: AWS IAM Conditions
  url: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html
- description: Google Cloud. (n.d.). Overview of IAM Conditions. Retrieved January 2, 2024.
  source_name: GCP IAM Conditions
  url: https://cloud.google.com/iam/docs/conditions-overview
- description: 'JumpCloud. (n.d.). Get Started: Conditional Access Policies. Retrieved January 2, 2024.'
  source_name: JumpCloud Conditional Access Policies
  url: https://jumpcloud.com/support/get-started-conditional-access-policies
- description: Microsoft. (2023, November 15). What is Conditional Access?. Retrieved January 2, 2024.
  source_name: Microsoft Conditional Access
  url: https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview
- description: Okta. (2023, November 30). Conditional Access Based on Device Security Posture. Retrieved January 2, 2024.
  source_name: Okta Conditional Access Policies
  url: https://support.okta.com/help/s/article/Conditional-access-based-on-device-security-posture?language=en_US
id: attack-pattern--ceaeb6d8-95ee-4da2-9d42-dc6aa6ca43ae
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2026-04-16T20:07:53.111Z'
name: Conditional Access Policies
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Gavin Knapp
- Joshua Penny
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
- Identity Provider
x_mitre_version: '2.0'
```
