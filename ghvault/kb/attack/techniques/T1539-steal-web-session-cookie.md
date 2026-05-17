---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1539 - Steal Web Session Cookie

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1539` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

An adversary may steal web application or service session cookies and use them to gain access to web applications or Internet services as an authenticated user without needing credentials. Web applications and services often use session cookies as an authentication token after a user has authenticated to a website.

Cookies are often valid for an extended period of time, even if the web application is not actively used. Cookies can be found on disk, in the process memory of the browser, and in network traffic to remote systems. Additionally, other applications on the targets machine might store sensitive authentication cookies in memory (e.g. apps which authenticate to cloud services). Session cookies can be used to bypasses some multi-factor authentication protocols.

There are several examples of malware targeting cookies from web browsers on the local system. Adversaries may also steal cookies by injecting malicious JavaScript content into websites or relying on User Execution by tricking victims into running malicious JavaScript in their browser.

There are also open source frameworks such as `Evilginx2` and `Muraena` that can gather session cookies through a malicious proxy (e.g., Adversary-in-the-Middle) that can be set up by an adversary and used in phishing campaigns.

After an adversary acquires a valid cookie, they can then perform a Web Session Cookie technique to login to the corresponding web application.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [evilginx2](../../tools/unknown/evilginx2.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can collect information on each session with a victim including the session cookie.(Citation: Evilginx 2 July 2018)(Citation: Sophos Evilginx MAR 2025)<br> |

## Source Verification

[source record](../../sources/mitre/steal-web-session-cookie.md)

## Evidence Excerpt

```text
created: '2019-10-08T20:04:35.508Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may steal web application or service session cookies and use them to gain access to web applications
or Internet services as an authenticated user without needing credentials. Web applications and services often use session
cookies as an authentication token after a user has authenticated to a website.
Cookies are often valid for an extended period of time, even if the web application is not actively used. Cookies can be
found on disk, in the process memory of the browser, and in network traffic to remote systems. Additionally, other applications
on the targets machine might store sensitive authentication cookies in memory (e.g. apps which authenticate to cloud services).
```
