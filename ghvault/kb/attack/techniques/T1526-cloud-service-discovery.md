---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1526 - Cloud Service Discovery

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

## Summary

An adversary may attempt to enumerate the cloud services running on a system after gaining access. These methods can differ from platform-as-a-service (PaaS), to infrastructure-as-a-service (IaaS), or software-as-a-service (SaaS). Many services exist throughout the various cloud providers and can include Continuous Integration and Continuous Delivery (CI/CD), Lambda Functions, Entra ID, etc. They may also include security services, such as AWS GuardDuty and Microsoft Defender for Cloud, and logging services, such as AWS CloudTrail and Google Cloud Audit Logs.

Adversaries may attempt to discover information about the services enabled throughout the environment. Azure tools and APIs, such as the Microsoft Graph API and Azure Resource Manager API, can enumerate resources and services, including applications, management groups, resources and policy definitions, and their relationships that are accessible by an identity.

For example, Stormspotter is an open source tool for enumerating and constructing a graph for Azure resources and services, and Pacu is an open source AWS exploitation framework that supports several methods for discovering cloud services.

Adversaries may use the information gained to shape follow-on behaviors, such as targeting data or credentials from enumerated services or evading identified defenses through Disable or Modify Tools or Disable or Modify Cloud Log.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AADInternals](../../tools/unknown/aadinternals.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can enumerate information about a variety of cloud services, such as Office 365 and Sharepoint instances or OpenID Configurations.(Citation: AADInternals Documentation) |
| [Pacu](../../tools/unknown/pacu.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can enumerate AWS services, such as CloudTrail and CloudWatch.(Citation: GitHub Pacu) |
| [ROADTools](../../tools/unknown/roadtools.md) | explicit | source | [ROADTools](https://attack.mitre.org/software/S0684) can enumerate Azure AD applications and service principals.(Citation: Roadtools)	 |
| [TruffleHog](../../tools/unknown/trufflehog.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has the ability to scan code repositories and CI/CD platforms.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Github TruffleSecurity Trufflehog April 2025) |

## Source Verification

[source record](../../sources/mitre/cloud-service-discovery.md)

## Evidence Excerpt

```text
created: '2019-08-30T13:01:10.120Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may attempt to enumerate the cloud services running on a system after gaining access. These methods
can differ from platform-as-a-service (PaaS), to infrastructure-as-a-service (IaaS), or software-as-a-service (SaaS). Many
services exist throughout the various cloud providers and can include Continuous Integration and Continuous Delivery (CI/CD),
Lambda Functions, Entra ID, etc. They may also include security services, such as AWS GuardDuty and Microsoft Defender for
Cloud, and logging services, such as AWS CloudTrail and Google Cloud Audit Logs.
Adversaries may attempt to discover information about the services enabled throughout the environment. Azure tools and APIs,
```
