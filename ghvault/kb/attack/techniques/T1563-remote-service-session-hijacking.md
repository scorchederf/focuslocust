---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1563 - Remote Service Session Hijacking

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

## Summary

Adversaries may take control of preexisting sessions with remote services to move laterally in an environment. Users may use valid credentials to log into a service specifically designed to accept remote connections, such as telnet, SSH, and RDP. When a user logs into a service, a session will be established that will allow them to maintain a continuous interaction with that service.

Adversaries may commandeer these sessions to carry out actions on remote systems. Remote Service Session Hijacking differs from use of Remote Services because it hijacks an existing session rather than creating a new session using Valid Accounts.

## Source Verification

[source record](../../sources/mitre/remote-service-session-hijacking.md)

## Evidence Excerpt

```text
created: '2020-02-25T18:26:16.994Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may take control of preexisting sessions with remote services to move laterally in an environment.
Users may use valid credentials to log into a service specifically designed to accept remote connections, such as telnet,
SSH, and RDP. When a user logs into a service, a session will be established that will allow them to maintain a continuous
interaction with that service.
Adversaries may commandeer these sessions to carry out actions on remote systems. [Remote Service Session Hijacking](https://attack.mitre.org/techniques/T1563)
differs from use of [Remote Services](https://attack.mitre.org/techniques/T1021) because it hijacks an existing session
```
