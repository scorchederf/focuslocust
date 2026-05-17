---
parsed_by: focuslocust
source: mitre
type: generated
---
# Trust Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1484.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Trust Modification](../../attack/techniques/T1484.002-trust-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1484.002 |
| name | Trust Modification |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1484/002 |

## Preserved Source Material

```yaml
created: '2020-12-28T21:59:02.181Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may add new domain trusts, modify the properties of existing domain trusts, or otherwise change\
  \ the configuration of trust relationships between domains and tenants to evade defenses and/or elevate privileges.Trust\
  \ details, such as whether or not user identities are federated, allow authentication and authorization properties to apply\
  \ between domains or tenants for the purpose of accessing shared resources.(Citation: Microsoft - Azure AD Federation) These\
  \ trust objects may include accounts, credentials, and other authentication material applied to servers, tokens, and domains.\n\
  \nManipulating these trusts may allow an adversary to escalate privileges and/or evade defenses by modifying settings to\
  \ add objects which they control. For example, in Microsoft Active Directory (AD) environments, this may be used to forge\
  \ [SAML Tokens](https://attack.mitre.org/techniques/T1606/002) without the need to compromise the signing certificate to\
  \ forge new credentials. Instead, an adversary can manipulate domain trusts to add their own signing certificate. An adversary\
  \ may also convert an AD domain to a federated domain using Active Directory Federation Services (AD FS), which may enable\
  \ malicious trust modifications such as altering the claim issuance rules to log in any valid set of credentials as a specified\
  \ user.(Citation: AADInternals zure AD Federated Domain) \n\nAn adversary may also add a new federated identity provider\
  \ to an identity tenant such as Okta or AWS IAM Identity Center, which may enable the adversary to authenticate as any user\
  \ of the tenant.(Citation: Okta Cross-Tenant Impersonation 2023) This may enable the threat actor to gain broad access into\
  \ a variety of cloud-based services that leverage the identity tenant. For example, in AWS environments, an adversary that\
  \ creates a new identity provider for an AWS Organization will be able to federate into all of the AWS Organization member\
  \ accounts without creating identities for each of the member accounts.(Citation: AWS re Inforce Trust Mod)"
external_references:
- external_id: T1484.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1484/002
- description: AWS re Inforce. (2024, June). Retrieved April 15, 2026.
  source_name: AWS re Inforce Trust Mod
  url: https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/events/approved/reinforce-2025/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf
- description: Dr. Nestori Syynimaa. (2017, November 16). Security vulnerability in Azure AD & Office 365 identity federation.
    Retrieved September 28, 2022.
  source_name: AADInternals zure AD Federated Domain
  url: https://o365blog.com/post/federation-vulnerability/
- description: Microsoft. (2018, November 28). What is federation with Azure AD?. Retrieved December 30, 2020.
  source_name: Microsoft - Azure AD Federation
  url: https://docs.microsoft.com/en-us/azure/active-directory/hybrid/whatis-fed
- description: 'Okta Defensive Cyber Operations. (2023, August 31). Cross-Tenant Impersonation: Prevention and Detection.
    Retrieved February 15, 2024.'
  source_name: Okta Cross-Tenant Impersonation 2023
  url: https://sec.okta.com/articles/2023/08/cross-tenant-impersonation-prevention-and-detection
id: attack-pattern--24769ab5-14bd-4f4e-a752-cfb185da53ee
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-16T20:07:52.987Z'
name: Trust Modification
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Blake Strom, Microsoft 365 Defender
- Praetorian
- Obsidian Security
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Identity Provider
- Windows
x_mitre_version: '3.0'
```
