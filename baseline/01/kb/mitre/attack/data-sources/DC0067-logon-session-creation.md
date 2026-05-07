---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0067
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0067-logon-session-creation
---

## Description

The successful establishment of a new user session following a successful authentication attempt. This typically signifies that a user has provided valid credentials or authentication tokens, and the system has initiated a session associated with that user account. This data is crucial for tracking authentication events and identifying potential unauthorized access. Examples: <br><br>- Windows Systems<br>    - Event ID: 4624<br>        - Logon Type: 2 (Interactive) or 10 (Remote Interactive via RDP).<br>        - Account Name: JohnDoe<br>        - Source Network Address: 192.168.1.100<br>        - Authentication Package: NTLM<br>- Linux Systems<br>    - /var/log/utmp or /var/log/wtmp:<br>        - Log format: login user [tty] from [source_ip]<br>        - User: jane<br>        - IP: 10.0.0.5<br>        - Timestamp: 2024-12-28 08:30:00<br>- macOS Systems<br>    - /var/log/asl.log or unified logging framework:<br>        - Log: com.apple.securityd: Authentication succeeded for user 'admin'<br>- Cloud Environments<br>    - Azure Sign-In Logs:<br>        - Activity: Sign-in successful<br>        - Client App: Browser<br>        - Location: Unknown (Country: X)<br>- Google Workspace<br>    - Activity: Login<br>        - Event Type: successful_login<br>        - Source IP: 203.0.113.55
