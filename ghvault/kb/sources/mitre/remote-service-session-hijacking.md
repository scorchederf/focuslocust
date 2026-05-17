---
parsed_by: focuslocust
source: mitre
type: generated
---
# Remote Service Session Hijacking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1563` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Remote Service Session Hijacking](../../attack/techniques/T1563-remote-service-session-hijacking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1563 |
| name | Remote Service Session Hijacking |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1563 |

## Preserved Source Material

```yaml
created: '2020-02-25T18:26:16.994Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may take control of preexisting sessions with remote services to move laterally in an environment.
  Users may use valid credentials to log into a service specifically designed to accept remote connections, such as telnet,
  SSH, and RDP. When a user logs into a service, a session will be established that will allow them to maintain a continuous
  interaction with that service.


  Adversaries may commandeer these sessions to carry out actions on remote systems. [Remote Service Session Hijacking](https://attack.mitre.org/techniques/T1563)
  differs from use of [Remote Services](https://attack.mitre.org/techniques/T1021) because it hijacks an existing session
  rather than creating a new session using [Valid Accounts](https://attack.mitre.org/techniques/T1078).(Citation: RDP Hijacking
  Medium)(Citation: Breach Post-mortem SSH Hijack)'
external_references:
- external_id: T1563
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1563
- description: Beaumont, K. (2017, March 19). RDP hijacking — how to hijack RDS and RemoteApp sessions transparently to move
    through an organisation. Retrieved December 11, 2017.
  source_name: RDP Hijacking Medium
  url: https://medium.com/@networksecurity/rdp-hijacking-how-to-hijack-rds-and-remoteapp-sessions-transparently-to-move-through-an-da2a1e73a5f6
- description: Hodgson, M. (2019, May 8). Post-mortem and remediations for Apr 11 security incident. Retrieved November 17,
    2024.
  source_name: Breach Post-mortem SSH Hijack
  url: https://matrix.org/blog/2019/05/08/post-mortem-and-remediations-for-apr-11-security-incident/
id: attack-pattern--5b0ad6f8-6a16-4966-a4ef-d09ea6e2a9f5
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: lateral-movement
modified: '2025-10-24T17:48:50.118Z'
name: Remote Service Session Hijacking
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.1'
```
