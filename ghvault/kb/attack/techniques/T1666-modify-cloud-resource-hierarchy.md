---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1666 - Modify Cloud Resource Hierarchy

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1666` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to modify hierarchical structures in infrastructure-as-a-service (IaaS) environments in order to evade defenses.  

IaaS environments often group resources into a hierarchy, enabling improved resource management and application of policies to relevant groups. Hierarchical structures differ among cloud providers. For example, in AWS environments, multiple accounts can be grouped under a single organization, while in Azure environments, multiple subscriptions can be grouped under a single management group.

Adversaries may add, delete, or otherwise modify resource groups within an IaaS hierarchy. For example, in Azure environments, an adversary who has gained access to a Global Administrator account may create new subscriptions in which to deploy resources. They may also engage in subscription hijacking by transferring an existing pay-as-you-go subscription from a victim tenant to an adversary-controlled tenant. This will allow the adversary to use the victim’s compute resources without generating logs on the victim tenant.

In AWS environments, adversaries with appropriate permissions in a given account may call the `LeaveOrganization` API, causing the account to be severed from the AWS Organization to which it was tied and removing any Service Control Policies, guardrails, or restrictions imposed upon it by its former Organization. Alternatively, adversaries may call the `CreateAccount` API in order to create a new account within an AWS Organization. This account will use the same payment methods registered to the payment account but may not be subject to existing detections or Service Control Policies.

## Source Verification

[source record](../../sources/mitre/modify-cloud-resource-hierarchy.md)

## Evidence Excerpt

```text
created: '2024-09-25T14:16:19.234Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may attempt to modify hierarchical structures in infrastructure-as-a-service (IaaS) environments\
\ in order to evade defenses.  \n\nIaaS environments often group resources into a hierarchy, enabling improved resource\
\ management and application of policies to relevant groups. Hierarchical structures differ among cloud providers. For example,\
\ in AWS environments, multiple accounts can be grouped under a single organization, while in Azure environments, multiple\
\ subscriptions can be grouped under a single management group.(Citation: AWS Organizations)(Citation: Microsoft Azure Resources)\n\
\nAdversaries may add, delete, or otherwise modify resource groups within an IaaS hierarchy. For example, in Azure environments,\
```
