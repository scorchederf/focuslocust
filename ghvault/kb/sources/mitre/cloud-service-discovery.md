---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Service Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1526` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cloud Service Discovery](../../attack/techniques/T1526-cloud-service-discovery.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1526 |
| name | Cloud Service Discovery |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1526 |

## Preserved Source Material

```yaml
created: '2019-08-30T13:01:10.120Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may attempt to enumerate the cloud services running on a system after gaining access. These methods
  can differ from platform-as-a-service (PaaS), to infrastructure-as-a-service (IaaS), or software-as-a-service (SaaS). Many
  services exist throughout the various cloud providers and can include Continuous Integration and Continuous Delivery (CI/CD),
  Lambda Functions, Entra ID, etc. They may also include security services, such as AWS GuardDuty and Microsoft Defender for
  Cloud, and logging services, such as AWS CloudTrail and Google Cloud Audit Logs.


  Adversaries may attempt to discover information about the services enabled throughout the environment. Azure tools and APIs,
  such as the Microsoft Graph API and Azure Resource Manager API, can enumerate resources and services, including applications,
  management groups, resources and policy definitions, and their relationships that are accessible by an identity.(Citation:
  Azure - Resource Manager API)(Citation: Azure AD Graph API)


  For example, Stormspotter is an open source tool for enumerating and constructing a graph for Azure resources and services,
  and Pacu is an open source AWS exploitation framework that supports several methods for discovering cloud services.(Citation:
  Azure - Stormspotter)(Citation: GitHub Pacu)


  Adversaries may use the information gained to shape follow-on behaviors, such as targeting data or credentials from enumerated
  services or evading identified defenses through [Disable or Modify Tools](https://attack.mitre.org/techniques/T1685) or
  [Disable or Modify Cloud Log](https://attack.mitre.org/techniques/T1685/002).'
external_references:
- external_id: T1526
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1526
- description: Microsoft. (2016, March 26). Operations overview | Graph API concepts. Retrieved June 18, 2020.
  source_name: Azure AD Graph API
  url: https://docs.microsoft.com/en-us/previous-versions/azure/ad/graph/howto/azure-ad-graph-api-operations-overview
- description: Microsoft. (2019, May 20). Azure Resource Manager. Retrieved June 17, 2020.
  source_name: Azure - Resource Manager API
  url: https://docs.microsoft.com/en-us/rest/api/resources/
- description: Microsoft. (2020). Azure Stormspotter GitHub. Retrieved June 17, 2020.
  source_name: Azure - Stormspotter
  url: https://github.com/Azure/Stormspotter
- description: Rhino Security Labs. (2019, August 22). Pacu. Retrieved October 17, 2019.
  source_name: GitHub Pacu
  url: https://github.com/RhinoSecurityLabs/pacu
id: attack-pattern--e24fcba8-2557-4442-a139-1ee2f2e784db
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2026-04-17T14:17:35.798Z'
name: Cloud Service Discovery
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Suzy Schapperle - Microsoft Azure Red Team
- Praetorian
- Thanabodi Phrakhun, I-SECURE
- Arun Seelagan, CISA
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
- Identity Provider
- Office Suite
- SaaS
x_mitre_version: '1.4'
```
