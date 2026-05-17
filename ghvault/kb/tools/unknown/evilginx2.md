---
parsed_by: focuslocust
source: mitre
type: generated
---
# evilginx2

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S9003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

evilginx2 is an open-source adversary-in-the-middle (AiTM) attack framework based on the open-source nginx web server. evilginx2 can be used as a reverse proxy between victims and legitimate web services to intercept and capture credentials, authentication tokens, and session cookies.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/evilginx2.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1001 - Data Obfuscation](../../attack/techniques/T1001-data-obfuscation.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can modify the Origin and Referrer fields in HTTPS headers it relays between intended victims and legitimate websites to comply with cross-origin resource sharing (CORS) restrictions.(Citation: Evilginx 2 July 2018) |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can capture information from each session with a victim including the public IP used to access the server and the user agent.(Citation: Sophos Evilginx MAR 2025) |
| [T1059.007 - JavaScript](../../attack/techniques/T1059.007-javascript.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can inject JavaScript code into HTML content to customize phishing attacks.(Citation: Breakdev Evilginx 2.3 JAN 2019) |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can proxy HTTPS connections between victims and destination websites.(Citation: Evilginx 2 July 2018)(Citation: Breakdev Evilginx 2.4 SEP 2020)(Citation: Breakdev Evilginx 3.3 APR 2024) |
| [T1090.002 - External Proxy](../../attack/techniques/T1090.002-external-proxy.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can route traffic via SOCKS5 and HTTP(S) proxies between an intended phishing victim's machine and legitimate websites.(Citation: Evilginx 2 July 2018)(Citation: Breakdev Evilginx 2.4 SEP 2020)(Citation: Sophos Evilginx MAR 2025)<br> |
| [T1111 - Multi-Factor Authentication Interception](../../attack/techniques/T1111-multi-factor-authentication-interception.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can intercept authentication tokens to enable bypass of non-phishing resistant forms of MFA.(Citation: Evilginx 2 July 2018) |
| [T1132 - Data Encoding](../../attack/techniques/T1132-data-encoding.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can randomly generate and Base64 encode parameters in phishing links to defeat static detection.(Citation: Breakdev Evilginx 2.4 SEP 2020) |
| [T1185 - Browser Session Hijacking](../../attack/techniques/T1185-browser-session-hijacking.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can inject custom POST arguments into requests to silently enable "Remember Me" options during authentication to stay logged in across browser sessions.(Citation: Breakdev Evilginx 2.2 NOV 2018) |
| [T1480 - Execution Guardrails](../../attack/techniques/T1480-execution-guardrails.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can reject requests to phishing URLs if the User-Agent of the visitor doesn't match the allowlist REGEX filter for a specific lure.(Citation: Breakdev Evilginx 2.4 SEP 2020) |
| [T1497.003 - Time Based Checks](../../attack/techniques/T1497.003-time-based-checks.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) has the ability to hide phishing lures for a set time to avoid scanning by sandboxes.(Citation: Breakdev Evilginx 3.2 AUG 2023) |
| [T1539 - Steal Web Session Cookie](../../attack/techniques/T1539-steal-web-session-cookie.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can collect information on each session with a victim including the session cookie.(Citation: Evilginx 2 July 2018)(Citation: Sophos Evilginx MAR 2025)<br> |
| [T1553.004 - Install Root Certificate](../../attack/techniques/T1553.004-install-root-certificate.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) has obtained a valid SSL/TLS certificate from LetsEncrypt to provide responses to Automatic Certificate Management Environment (ACME) challenges.(Citation: Evilginx 2 July 2018) |
| [T1557 - Adversary-in-the-Middle](../../attack/techniques/T1557-adversary-in-the-middle.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) has the ability to act as an adversary-in-the-middle (AiTM) relay between a legitimate website and a phished user to capture all transmitted data including usernames, passwords, authentication tokens, and session cookies and tokens.(Citation: Evilginx 2 July 2018)(Citation: Breakdev Evilginx 3.0 May 2023)(Citation: Breakdev Evilginx 3.2 AUG 2023)(Citation: Sophos Evilginx MAR 2025) |
| [T1598.003 - Spearphishing Link](../../attack/techniques/T1598.003-spearphishing-link.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can generate and display phishing URLs including hidden tracking pixels and can also embed URLs within iframes for browser-in-the-browser phishing.(Citation: Breakdev Evilginx 2.3 JAN 2019)(Citation: Breakdev Evilginx 3.3 APR 2024)(Citation: Sophos Evilginx MAR 2025)<br> |

## Source Verification

[source record](../../sources/mitre/evilginx2.md)

## Evidence Excerpt

```text
created: '2026-01-30T20:15:05.674Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "[evilginx2](https://attack.mitre.org/software/S9003) is an open-source adversary-in-the-middle (AiTM) attack\
\ framework based on the open-source nginx web server. [evilginx2](https://attack.mitre.org/software/S9003) can be used\
\ as a reverse proxy between victims and legitimate web services to intercept and capture credentials, authentication tokens,\
\ and session cookies.(Citation: Evilginx 2 July 2018)(Citation: Breakdev Evilginx 2.1 SEP 2018)(Citation: Sophos Evilginx\
\ MAR 2025)\n "
external_references:
```
