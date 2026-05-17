---
parsed_by: focuslocust
source: mitre
type: generated
---
# Web Credential Usage

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0007` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Web Credential Usage](../../attack/data-sources/DC0007-web-credential-usage.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0007 |
| name | Web Credential Usage |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0007 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.271Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An attempt by a user to gain access to a network or computing resource by providing web credentials (ex: Windows
  EID 1202)'
external_references:
- external_id: DC0007
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0007
id: x-mitre-data-component--ff93f688-d7a4-49cf-9c79-a14454da8428
modified: '2025-11-12T22:03:39.105Z'
name: Web Credential Usage
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: SessionToken used without preceding MFA or login event
  name: AWS:CloudTrail
- channel: SessionId reused from different device/browser fingerprint
  name: m365:unified
- channel: AssumeRoleWithSAML
  name: AWS:CloudTrail
- channel: SAML token accepted without preceding login challenge
  name: saas:access
- channel: Mailbox access using SAML token without corresponding MFA event
  name: m365:exchange
- channel: GetSessionToken, AssumeRoleWithWebIdentity
  name: AWS:CloudTrail
- channel: New session initiated using cookies without normal MFA or password validation
  name: macos:unifiedlog
- channel: Session activity without correlated login event
  name: m365:unified
- channel: AssumeRole, GetFederationToken, GetSessionToken
  name: AWS:CloudTrail
- channel: TokenIssued, RefreshTokenUsed
  name: azure:signinlogs
- channel: OAuthTokenGranted, APIRequest
  name: saas:googleworkspace
- channel: OAuthTokenIssued, FileAccessed, MailItemsAccessed
  name: m365:unified
- channel: serviceAccount token used in API requests not tied to workload identity
  name: kubernetes:apiserver
- channel: Pre-authentication keys generated or token signing anomalies
  name: NSM:Connections
- channel: Web sessions initiated with newly forged tokens
  name: macos:unifiedlog
- channel: API requests made with tokens not associated with expected user logins
  name: saas:auth
- channel: TokenIssuanceStart, TokenIssuanceSuccess
  name: azure:signinlogs
- channel: access_token issued
  name: saas:googleworkspace
- channel: TokenIssued, FileAccessed
  name: m365:unified
- channel: GetCallerIdentity
  name: AWS:CloudTrail
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
