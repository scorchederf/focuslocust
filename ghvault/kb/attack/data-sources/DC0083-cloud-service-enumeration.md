---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0083 - Cloud Service Enumeration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0083` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Cloud service enumeration involves listing or querying available cloud services in a cloud control plane. This activity is often performed to identify resources such as virtual machines, storage buckets, compute clusters, or other services within a cloud environment. Examples include API calls like `AWS ECS ListServices`, `Azure ListAllResources`, or `Google Cloud ListInstances`. Examples: 

AWS Cloud Service Enumeration: The adversary gathers details about existing ECS services to identify opportunities for privilege escalation or exfiltration.
- Azure Resource Enumeration: The adversary collects information about virtual machines, resource groups, and other Azure assets for reconnaissance purposes.
- Google Cloud Resource Enumeration: The attacker seeks to map the environment and find misconfigured or underutilized resources for exploitation.
- Office 365 Service Enumeration: The attacker may look for data repositories or collaboration tools to exfiltrate sensitive information.

## Source Verification

[source record](../../sources/mitre/cloud-service-enumeration.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Cloud service enumeration involves listing or querying available cloud services in a cloud control plane. This\
\ activity is often performed to identify resources such as virtual machines, storage buckets, compute clusters, or other\
\ services within a cloud environment. Examples include API calls like `AWS ECS ListServices`, `Azure ListAllResources`,\
\ or `Google Cloud ListInstances`. Examples: \n\nAWS Cloud Service Enumeration: The adversary gathers details about existing\
\ ECS services to identify opportunities for privilege escalation or exfiltration.\n- Azure Resource Enumeration: The adversary\
\ collects information about virtual machines, resource groups, and other Azure assets for reconnaissance purposes.\n- Google\
```
