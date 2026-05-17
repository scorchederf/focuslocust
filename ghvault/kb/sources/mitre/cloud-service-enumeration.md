---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Service Enumeration

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

## Generated Concept Page

- [Cloud Service Enumeration](../../attack/data-sources/DC0083-cloud-service-enumeration.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0083 |
| name | Cloud Service Enumeration |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/data-components/DC0083 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Cloud service enumeration involves listing or querying available cloud services in a cloud control plane. This\
  \ activity is often performed to identify resources such as virtual machines, storage buckets, compute clusters, or other\
  \ services within a cloud environment. Examples include API calls like `AWS ECS ListServices`, `Azure ListAllResources`,\
  \ or `Google Cloud ListInstances`. Examples: \n\nAWS Cloud Service Enumeration: The adversary gathers details about existing\
  \ ECS services to identify opportunities for privilege escalation or exfiltration.\n- Azure Resource Enumeration: The adversary\
  \ collects information about virtual machines, resource groups, and other Azure assets for reconnaissance purposes.\n- Google\
  \ Cloud Resource Enumeration: The attacker seeks to map the environment and find misconfigured or underutilized resources\
  \ for exploitation.\n- Office 365 Service Enumeration: The attacker may look for data repositories or collaboration tools\
  \ to exfiltrate sensitive information."
external_references:
- external_id: DC0083
  source_name: mitre-attack
  url: https://attack.mitre.org/data-components/DC0083
id: x-mitre-data-component--8c826308-2760-492f-9e36-4f0f7e23bcac
modified: '2026-02-23T19:38:20.657Z'
name: Cloud Service Enumeration
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
- mobile-attack
x_mitre_log_sources:
- channel: GetSecretValue
  name: AWS:CloudTrail
- channel: accessSecretVersion
  name: gcp:secrets
- channel: SecretGet
  name: azure:ad
- channel: ssm:ListInventoryEntries
  name: AWS:CloudTrail
- channel: 'DescribeInstances, DescribeServices, ListFunctions: High frequency enumeration calls or unusual user agents performing
    discovery'
  name: AWS:CloudTrail
- channel: 'ListApplications, ListServicePrincipals: Large-scale queries against identity or application objects'
  name: azure:audit
- channel: 'Get-MsolServicePrincipal, ListAppRoles: Service discovery operations executed by accounts not normally performing
    administrative tasks'
  name: m365:unified
- channel: 'ListIntegrations, ListServices: Repeated service discovery requests from accounts without administrative responsibilities'
  name: saas:adminapi
- channel: GetInstanceIdentityDocument or IMDSv2 token requests
  name: AWS:CloudTrail
- channel: DescribeUsers / ListUsers / GetUser
  name: AWS:CloudTrail
- channel: Graph API Query
  name: azure:signinlogs
- channel: Device lookup, location query, or remote management operation
  name: saas:MDM
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '3.0'
```
