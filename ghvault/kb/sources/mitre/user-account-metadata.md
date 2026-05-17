---
parsed_by: focuslocust
source: mitre
type: generated
---
# User Account Metadata

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0013` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [User Account Metadata](../../attack/data-sources/DC0013-user-account-metadata.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0013 |
| name | User Account Metadata |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/data-components/DC0013 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.271Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Contextual data about an account, which may include a username, user ID, environmental data, etc.
external_references:
- external_id: DC0013
  source_name: mitre-attack
  url: https://attack.mitre.org/data-components/DC0013
id: x-mitre-data-component--b5d0492b-cda4-421c-8e51-ed2b8d85c5d0
modified: '2026-03-13T22:24:06.660Z'
name: User Account Metadata
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
- channel: EventCode=4720, 4738
  name: WinEventLog:Security
- channel: EventCode=4673
  name: WinEventLog:Security
- channel: AssumeRole
  name: AWS:CloudTrail
- channel: open,openat,read
  name: auditd:SYSCALL
- channel: profiles -P|getaccountpolicies
  name: macos:MDM
- channel: GetAccountPasswordPolicy
  name: AWS:CloudTrail
- channel: operation contains 'Get*Password*Policy' OR 'List*Authentication*Policy' OR 'Get-ADDefaultDomainPasswordPolicy'
  name: azure:audit
- channel: Workload=AzureActiveDirectory OR Exchange AND (Operation=Cmdlet AND Parameters contains 'Password' AND (CmdletName='Get-*'
    OR CmdletName='Get-OrganizationConfig'))
  name: m365:unified
- channel: Refresh token issuance or refresh token usage from new IPs or user agents
  name: saas:auth
- channel: 'Directory API Access: users.list or groups.list'
  name: gcp:audit
- channel: GetCallerIdentity
  name: CloudTrail:GetCallerIdentity
- channel: vCenter Management
  name: vpxd.log
- channel: Creation of user account with UID <500
  name: macos:unifiedlog
- channel: EventCode=4674
  name: WinEventLog:Security
- channel: User enumeration with creation/last modified timestamps
  name: windows:osquery
- channel: Listing of /etc/passwd and /etc/shadow metadata
  name: linux:osquery
- channel: User lifecycle events
  name: saas:okta
- channel: RoleManagement.Read.Directory or Directory.Read.All
  name: Microsoft Entra ID Audit Logs
- channel: 'Azure CLI Operation: Microsoft.Graph/users/read'
  name: azure:activity
- channel: 'IAM API call: serviceAccounts.list or projects.getIamPolicy'
  name: gcp:audit
- channel: users.list, directoryObjects.getByIds
  name: Microsoft Graph API Logs
- channel: Suspicious Enumeration of Cloud Directory
  name: Defender for Identity
- channel: users.list, groups.list
  name: Google Admin Audit
- channel: PassRole
  name: AWS:CloudTrail
- channel: PrincipalEmail with serviceAccountTokenCreator impersonating new identity
  name: gcp:iam
- channel: 'AssumeRole: Discovery actions tied to assumed identities outside of normal context'
  name: AWS:CloudTrail
- channel: User Enumeration Events
  name: saas:okta
- channel: Directory API Access
  name: gcp:audit
- channel: DirectoryService queries retrieving account information
  name: macos:unifiedlog
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.1'
```
