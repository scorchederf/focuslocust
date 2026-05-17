---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0067 - Logon Session Creation

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

## Summary

The successful establishment of a new user session following a successful authentication attempt. This typically signifies that a user has provided valid credentials or authentication tokens, and the system has initiated a session associated with that user account. This data is crucial for tracking authentication events and identifying potential unauthorized access. Examples: 

- Windows Systems
    - Event ID: 4624
        - Logon Type: 2 (Interactive) or 10 (Remote Interactive via RDP).
        - Account Name: JohnDoe
        - Source Network Address: 192.168.1.100
        - Authentication Package: NTLM
- Linux Systems
    - /var/log/utmp or /var/log/wtmp:
        - Log format: login user (tty) from (source_ip)
        - User: jane
        - IP: 10.0.0.5
        - Timestamp: 2024-12-28 08:30:00
- macOS Systems
    - /var/log/asl.log or unified logging framework:
        - Log: com.apple.securityd: Authentication succeeded for user 'admin'
- Cloud Environments
    - Azure Sign-In Logs:
        - Activity: Sign-in successful
        - Client App: Browser
        - Location: Unknown (Country: X)
- Google Workspace
    - Activity: Login
        - Event Type: successful_login
        - Source IP: 203.0.113.55

## Source Verification

[source record](../../sources/mitre/logon-session-creation.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The successful establishment of a new user session following a successful authentication attempt. This typically\
\ signifies that a user has provided valid credentials or authentication tokens, and the system has initiated a session\
\ associated with that user account. This data is crucial for tracking authentication events and identifying potential unauthorized\
\ access. Examples: \n\n- Windows Systems\n    - Event ID: 4624\n        - Logon Type: 2 (Interactive) or 10 (Remote Interactive\
\ via RDP).\n        - Account Name: JohnDoe\n        - Source Network Address: 192.168.1.100\n        - Authentication\
\ Package: NTLM\n- Linux Systems\n    - /var/log/utmp or /var/log/wtmp:\n        - Log format: login user [tty] from [source_ip]\n\
```
