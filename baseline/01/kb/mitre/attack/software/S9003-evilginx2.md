---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S9003
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S9003-evilginx2
---

## Description

[[kb/mitre/attack/software/S9003-evilginx2|evilginx2]] is an open-source adversary-in-the-middle (AiTM) attack framework based on the open-source nginx web server. [[kb/mitre/attack/software/S9003-evilginx2|evilginx2]] can be used as a reverse proxy between victims and legitimate web services to intercept and capture credentials, authentication tokens, and session cookies.[^3] [^2] [^1] <br> 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1001-data-obfuscation\|T1001]] | Data Obfuscation | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can modify the Origin and Referrer fields in HTTPS headers it relays between intended victims and legitimate websites to comply with cross-origin resource sharing (CORS) restrictions.[^1]  |
| [[kb/mitre/attack/techniques/T1016-system-network-configuration-discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can capture information from each session with a victim including the public IP used to access the server and the user agent.[^1]  |
| [[kb/mitre/attack/techniques/T1059.007-javascript\|T1059.007]] | JavaScript | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can inject JavaScript code into HTML content to customize phishing attacks.[^1]  |
| [[kb/mitre/attack/techniques/T1071.001-web-protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can proxy HTTPS connections between victims and destination websites.[^3] [^1] [^2]  |
| [[kb/mitre/attack/techniques/T1090.002-external-proxy\|T1090.002]] | External Proxy | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can route traffic via SOCKS5 and HTTP(S) proxies between an intended phishing victim's machine and legitimate websites.[^3] [^2] [^1] <br> |
| [[kb/mitre/attack/techniques/T1111-multi-factor-authentication-interception\|T1111]] | Multi-Factor Authentication Interception | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can intercept authentication tokens to enable bypass of non-phishing resistant forms of MFA.[^1]  |
| [[kb/mitre/attack/techniques/T1132-data-encoding\|T1132]] | Data Encoding | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can randomly generate and Base64 encode parameters in phishing links to defeat static detection.[^1]  |
| [[kb/mitre/attack/techniques/T1185-browser-session-hijacking\|T1185]] | Browser Session Hijacking | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can inject custom POST arguments into requests to silently enable "Remember Me" options during authentication to stay logged in across browser sessions.[^1]  |
| [[kb/mitre/attack/techniques/T1480-execution-guardrails\|T1480]] | Execution Guardrails | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can reject requests to phishing URLs if the User-Agent of the visitor doesn't match the allowlist REGEX filter for a specific lure.[^1]  |
| [[kb/mitre/attack/techniques/T1497.003-time-based-checks\|T1497.003]] | Time Based Checks | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] has the ability to hide phishing lures for a set time to avoid scanning by sandboxes.[^1]  |
| [[kb/mitre/attack/techniques/T1539-steal-web-session-cookie\|T1539]] | Steal Web Session Cookie | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can collect information on each session with a victim including the session cookie.[^2] [^1] <br> |
| [[kb/mitre/attack/techniques/T1553.004-install-root-certificate\|T1553.004]] | Install Root Certificate | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] has obtained a valid SSL/TLS certificate from LetsEncrypt to provide responses to Automatic Certificate Management Environment (ACME) challenges.[^1]  |
| [[kb/mitre/attack/techniques/T1557-adversary-in-the-middle\|T1557]] | Adversary-in-the-Middle | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] has the ability to act as an adversary-in-the-middle (AiTM) relay between a legitimate website and a phished user to capture all transmitted data including usernames, passwords, authentication tokens, and session cookies and tokens.[^4] [^3] [^2] [^1]  |
| [[kb/mitre/attack/techniques/T1598.003-spearphishing-link\|T1598.003]] | Spearphishing Link | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] can generate and display phishing URLs including hidden tracking pixels and can also embed URLs within iframes for browser-in-the-browser phishing.[^2] [^3] [^1] <br> |

 [^1]: [Sophos Evilginx MAR 2025](https://www.sophos.com/en-us/blog/stealing-user-credentials-with-evilginx)
 [^2]: [Breakdev Evilginx 2.1 SEP 2018](https://breakdev.org/evilginx-2-1-the-first-post-release-update/)
 [^3]: [Evilginx 2 July 2018](https://breakdev.org/evilginx-2-next-generation-of-phishing-2fa-tokens/)
 [^4]: [Breakdev Evilginx 2.3 JAN 2019](https://breakdev.org/evilginx-2-3-phishermans-dream/)
 [^5]: [Breakdev Evilginx 3.2 AUG 2023](https://breakdev.org/evilginx-3-2/)
 [^6]: [Breakdev Evilginx 2.4 SEP 2020](https://breakdev.org/evilginx-2-4-gone-phishing/)
 [^7]: [Breakdev Evilginx 3.3 APR 2024](https://breakdev.org/evilginx-3-3-go-phish/)
 [^8]: [Breakdev Evilginx 3.0 May 2023](https://breakdev.org/evilginx-3-0-evilginx-mastery/)
 [^9]: [Breakdev Evilginx 2.2 NOV 2018](https://breakdev.org/evilginx-2-2-jolly-winter-update)
