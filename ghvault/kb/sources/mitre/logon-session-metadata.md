---
parsed_by: focuslocust
source: mitre
type: generated
---
# Logon Session Metadata

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0088` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Logon Session Metadata](../../attack/data-sources/DC0088-logon-session-metadata.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0088 |
| name | Logon Session Metadata |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0088 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Contextual data about a logon session, such as username, logon type, access tokens (security context, user SIDs,
  logon identifiers, and logon SID), and any activity associated within it
external_references:
- external_id: DC0088
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0088
id: x-mitre-data-component--39b9db72-8b48-4595-a18d-db5bbba3091b
modified: '2025-11-12T22:03:39.105Z'
name: Logon Session Metadata
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- ics-attack
- enterprise-attack
x_mitre_log_sources:
- channel: None
  name: Logon Session
- channel: EventCode=4672
  name: WinEventLog:Security
- channel: LoginWindow context with associated PID linked to reopened plist paths
  name: macos:unifiedlog
- channel: EventCode=4672, 4634
  name: WinEventLog:Security
- channel: SAML-based login with anomalous issuer or NotOnOrAfter lifetime
  name: azure:signinlogs
- channel: Abnormal user claims or unexpected elevated role assignment in SAML assertion
  name: m365:unified
- channel: authd generating multiple MFA token requests
  name: macos:unifiedlog
- channel: None
  name: linux:syslog
- channel: EventCode=4624, 4625, 4768, 4769
  name: WinEventLog:Security
- channel: sssd / sudo logs
  name: linux:syslog
- channel: /var/log/hostd.log
  name: esxi:hostd
- channel: EventCode=4778, EventCode=4779
  name: WinEventLog:Security
- channel: ssh logins or execve of remote commands
  name: auditd:SYSCALL
- channel: Remote login (ssh) or screen sharing authentication attempts
  name: macos:unifiedlog
- channel: Unauthorized container creation or kubelet exec logs
  name: kubernetes:audit
- channel: USER_LOGIN
  name: auditd:USER_LOGIN
- channel: loginwindow or sshd
  name: macos:unifiedlog
- channel: EventCode=4800, 4801
  name: WinEventLog:Security
- channel: EventCode=4776, 4771, 4770
  name: WinEventLog:Security
- channel: execve,socket,connect,openat
  name: auditd:SYSCALL
- channel: Group membership change for admin or wheel
  name: macos:unifiedlog
- channel: Add delegated admin / Assign admin roles / Update application consent
  name: azure:audit
- channel: user.session.start, app.oauth2.as.authorize, policy.mfa.bypass
  name: saas:okta
- channel: google.iam.credentials.generateAccessToken / serviceAccountTokenCreator
  name: gcp:audit
- channel: ConnectedApp OAuth policy change / Login as user
  name: saas:salesforce
- channel: Unusual Kerberos TGS-REQ without TGT or anomalous ticket lifetime
  name: macos:unifiedlog
- channel: user.authentication.sso
  name: saas:okta
- channel: FileAccessed, SharingSet
  name: m365:unified
- channel: UserLogin
  name: m365:signinlogs
- channel: loginwindow, sshd
  name: macos:unifiedlog
- channel: Successful sudo or ssh from unknown IPs
  name: NSM:Connections
- channel: loginwindow or sshd events with external IP
  name: macos:unifiedlog
- channel: process = 'sshd'
  name: macos:unifiedlog
- channel: None
  name: esxi:auth
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
