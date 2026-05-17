---
parsed_by: focuslocust
source: mitre
type: generated
---
# Cloud Service Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0069` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cloud Service Modification](../../attack/data-sources/DC0069-cloud-service-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0069 |
| name | Cloud Service Modification |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0069 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Cloud service modification refers to changes made to the configuration, settings, or data of a cloud service.\
  \ These modifications can include administrative changes such as enabling or disabling features, altering permissions, or\
  \ deleting critical components. Monitoring these changes is critical to detect potential misconfigurations or malicious\
  \ activity. Examples: \n\n- AWS Cloud Service Modifications: A user disables AWS CloudTrail logging (StopLogging) or deletes\
  \ a CloudWatch configuration rule (DeleteConfigRule).\n- Azure Cloud Service Modifications: Changes to Azure Role-Based\
  \ Access Control (RBAC) roles, such as adding a new Contributor role to a sensitive resource.\n- Google Cloud Service Modifications:\
  \ Deletion of a Google Cloud Storage bucket or disabling a Google Cloud Function.\n- Office 365 Cloud Service Modifications:\
  \ Altering mailbox permissions or disabling auditing in Microsoft 365."
external_references:
- external_id: DC0069
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0069
id: x-mitre-data-component--e52d89f9-1710-4708-88a5-cbef77c4cd5e
modified: '2025-11-12T22:03:39.105Z'
name: Cloud Service Modification
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: CreateFunction
  name: AWS:CloudTrail
- channel: Creation of Power Automate flow triggered by OneDrive or Exchange event
  name: m365:unified
- channel: PutUserPolicy, PutGroupPolicy, PutRolePolicy, CreatePolicyVersion
  name: AWS:CloudTrail
- channel: Condition block updated in IAM policy (e.g., aws:SourceIp, aws:RequestedRegion)
  name: AWS:CloudTrail
- channel: 'operationName: Write, Access Review, RoleAssignment'
  name: azure:activity
- channel: UpdatePolicy
  name: azure:policy
- channel: UpdateAccountPasswordPolicy
  name: AWS:CloudTrail
- channel: PutIdentityPolicy
  name: AWS:CloudTrail
- channel: 'LeaveOrganization: API calls severing accounts from AWS Organizations'
  name: AWS:CloudTrail
- channel: 'CreateAccount: API calls creating new accounts in AWS Organizations'
  name: AWS:CloudTrail
- channel: Tenant subscription transfers or new management group creation
  name: azure:audit
- channel: UpdateIdentityPolicy or DisableMFA
  name: AWS:CloudTrail
- channel: SendMessage
  name: m365:unified
- channel: UpdateSink request modifying log export destinations
  name: gcp:config
- channel: DisableAuditLogs or ConditionalAccess logging changes
  name: azure:policy
- channel: UpdateFederationSettings or RegisterHybridConnector
  name: AWS:CloudTrail
- channel: CreateTrafficMirrorSession / ModifyTrafficMirrorTarget
  name: AWS:CloudTrail
- channel: Microsoft.Network/networkWatchers/flowLogSettings/write
  name: azure:activity
- channel: compute.packetMirroring.insert
  name: gcp:audit
- channel: 'CreateFunction / UpdateFunctionConfiguration: Function creation, role assignment, or configuration change events'
  name: AWS:CloudTrail
- channel: 'AddFlow / UpdateFlow: New automation or workflow creation events'
  name: m365:unified
- channel: 'Create / Update: Deployment of scripts with event-driven triggers'
  name: saas:appsscript
- channel: Exported file or accessed admin API
  name: saas:slack
- channel: RequestServiceQuotaIncrease
  name: AWS:CloudTrail
- channel: MICROSOFT.AUTHORIZATION/POLICIES/WRITE
  name: azure:activity
- channel: projects.updateQuota or orgPolicies.updatePolicy
  name: gcp:audit
- channel: 'Delete* / Stop*: DeleteAlarms, StopLogging, or DisableMonitoring API calls'
  name: AWS:CloudTrail
- channel: Use of temporary credentials issued from IMDS access
  name: AWS:CloudTrail
- channel: Workflow triggered via pull_request_target from forked repo
  name: saas:github
- channel: 'Consent to application: OAuth application consent granted to service principal'
  name: azure:audit
- channel: New or modified third-party application integrations with elevated permissions
  name: saas:integration
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
