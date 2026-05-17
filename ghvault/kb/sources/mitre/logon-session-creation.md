---
parsed_by: focuslocust
source: mitre
type: generated
---
# Logon Session Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0067` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Logon Session Creation](../../attack/data-sources/DC0067-logon-session-creation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0067 |
| name | Logon Session Creation |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0067 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The successful establishment of a new user session following a successful authentication attempt. This typically\
  \ signifies that a user has provided valid credentials or authentication tokens, and the system has initiated a session\
  \ associated with that user account. This data is crucial for tracking authentication events and identifying potential unauthorized\
  \ access. Examples: \n\n- Windows Systems\n    - Event ID: 4624\n        - Logon Type: 2 (Interactive) or 10 (Remote Interactive\
  \ via RDP).\n        - Account Name: JohnDoe\n        - Source Network Address: 192.168.1.100\n        - Authentication\
  \ Package: NTLM\n- Linux Systems\n    - /var/log/utmp or /var/log/wtmp:\n        - Log format: login user [tty] from [source_ip]\n\
  \        - User: jane\n        - IP: 10.0.0.5\n        - Timestamp: 2024-12-28 08:30:00\n- macOS Systems\n    - /var/log/asl.log\
  \ or unified logging framework:\n        - Log: com.apple.securityd: Authentication succeeded for user 'admin'\n- Cloud\
  \ Environments\n    - Azure Sign-In Logs:\n        - Activity: Sign-in successful\n        - Client App: Browser\n     \
  \   - Location: Unknown (Country: X)\n- Google Workspace\n    - Activity: Login\n        - Event Type: successful_login\n\
  \        - Source IP: 203.0.113.55"
external_references:
- external_id: DC0067
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0067
id: x-mitre-data-component--9ce98c86-8d30-4043-ba54-0784d478d0b5
modified: '2025-11-12T22:03:39.105Z'
name: Logon Session Creation
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
- channel: UserLoggedIn
  name: macos:unifiedlog
- channel: ConsoleLogin, AssumeRole, ListResources
  name: AWS:CloudTrail
- channel: UserLoginSuccess, TokenIssued
  name: azure:signin
- channel: user.authentication.sso, app.oauth.grant
  name: Okta:SystemLog
- channel: SignInSuccess, RoleAssignmentRead
  name: m365:signinlogs
- channel: UserLoggedIn
  name: m365:unified
- channel: LoginAudit, DriveAudit
  name: gcp:audit
- channel: LoginSuccess, APIKeyUse, AdminAction
  name: saas:auth
- channel: Abnormal sign-in from scripting tools (PowerShell, AADInternals)
  name: azure:signinlogs
- channel: Suspicious login to cloud mailbox system
  name: azure:signinlogs
- channel: Failed MFA attempts, unusual conditional access triggers, login attempts from unexpected IP ranges
  name: azure:signinlogs
- channel: ConsoleLogin
  name: AWS:CloudTrail
- channel: EventCode=4624, 4648
  name: WinEventLog:Security
- channel: Mismatch between recorded user logon and active sessions (e.g., wtmp/utmp entries without corresponding authentication
    in auth.log)
  name: NSM:Connections
- channel: Authentication inconsistencies where commands are executed without corresponding login events
  name: macos:unifiedlog
- channel: SAML login without corresponding IdP authentication log
  name: CloudTrail:Signin
- channel: File access with forged or anomalous SAML claims
  name: m365:sharepoint
- channel: Web console logins using session cookies without corresponding MFA event
  name: AWS:CloudTrail
- channel: Multiple concurrent logins using same cookie from different locations
  name: saas:access
- channel: 'ConsoleLogin: If IdP backed by cloud provider, Console login from new IP/agent after correlated endpoint compromise'
  name: AWS:CloudTrail
- channel: authentication
  name: macos:unifiedlog
- channel: SendSSHPublicKey, StartSession (SSM), EC2InstanceConnect
  name: AWS:CloudTrail
- channel: Microsoft.Compute/virtualMachines/serialConsole/connect/action
  name: azure:signin
- channel: cloud.ssh.publicKey.inserted, compute.instances.osLogin
  name: gcp:audit
- channel: Missing new login event but session activity continues
  name: NSM:Connections
- channel: Session reuse without new auth event
  name: macos:unifiedlog
- channel: Temporary security credentials used to authenticate into management console or APIs
  name: AWS:CloudTrail
- channel: Access to Keychain items or browser credential stores
  name: macos:unifiedlog
- channel: Token usage events with device/user mismatch
  name: m365:signinlogs
- channel: Login from unusual IP, device fingerprint, or location; access token creation from new client
  name: saas:github
- channel: 'sshd: Accepted password/publickey'
  name: linux:syslog
- channel: eventMessage CONTAINS 'screensharingd' or 'AuthorizationRefCreate'
  name: macos:unifiedlog
- channel: AWS ConsoleLogin, StartSession
  name: AWS:CloudTrail
- channel: vim.fault.*, DCUI login, SSH shell
  name: esxi:vmkernel
- channel: GetConsoleOutput
  name: AWS:CloudTrail
- channel: user.session.start
  name: saas:okta
- channel: ViewAdminReport
  name: m365:unified
- channel: Zoom Admin Dashboard accessed from unfamiliar IP/device
  name: saas:zoom
- channel: Anomalous logon without MFA enforcement
  name: WinEventLog:Security
- channel: Login from untrusted IP, or new admin account accessing firewall console/API
  name: networkdevice:Firewall
- channel: authentication success after file access
  name: linux:syslog
- channel: Keychain or user login post-access
  name: macos:unifiedlog
- channel: sudden role assumption after credential file access
  name: AWS:CloudTrail
- channel: Accepted publickey for user from unusual IP or without tty
  name: NSM:Connections
- channel: logon
  name: saas:confluence
- channel: auth.log / secure.log
  name: linux:syslog
- channel: Shell login or escalation
  name: esxi:auth
- channel: User login event followed by unexpected process tree
  name: linux:auth
- channel: 'InteractiveUserLogin: Discovery behavior linked to privileged logins from atypical IP ranges'
  name: azure:signinlogs
- channel: 'UserLogin: Discovery operations shortly after account logins from new geolocations'
  name: m365:signinlogs
- channel: 'Login, TokenGranted: Discovery actions tied to anomalous login sessions or tokens'
  name: saas:auth
- channel: simultaneous or anomalous logon sessions across multiple systems
  name: NSM:Connections
- channel: authentication plugin load or modification events
  name: macos:unifiedlog
- channel: SignInEvents
  name: azure:ad
- channel: Accepted publickey/password for * from * port * ssh2
  name: linux:syslog
- channel: loginwindow or sshd successful login events
  name: macos:unifiedlog
- channel: InteractiveUser, ServicePrincipalSignIn
  name: azure:signinlogs
- channel: AssumeRole,AssumeRoleWithSAML,AssumeRoleWithWebIdentity
  name: AWS:CloudTrail
- channel: InteractiveUser, NonInteractiveUser
  name: azure:signinlogs
- channel: UserLogin, ConditionalAccessPolicyEvaluated
  name: azure:signinlogs
- channel: session.token.reuse
  name: saas:okta
- channel: capset or setns
  name: auditd:SYSCALL
- channel: admin.googleapis.com
  name: gcp:audit
- channel: UserLoggedIn
  name: m365:signinlogs
- channel: EventCode=4624
  name: WinEventLog:Security
- channel: None
  name: linux:syslog
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
