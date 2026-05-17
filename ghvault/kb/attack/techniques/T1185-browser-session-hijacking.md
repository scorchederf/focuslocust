---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1185 - Browser Session Hijacking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1185` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may take advantage of security vulnerabilities and inherent functionality in browser software to change content, modify user-behaviors, and intercept information as part of various browser session hijacking techniques.

A specific example is when an adversary injects software into a browser that allows them to inherit cookies, HTTP sessions, and SSL client certificates of a user then use the browser as a way to pivot into an authenticated intranet. Executing browser-based behaviors such as pivoting may require specific process permissions, such as <code>SeDebugPrivilege</code> and/or high-integrity/administrator rights.

Another example involves pivoting browser traffic from the adversary's browser through the user's browser by setting up a proxy which will redirect web traffic. This does not alter the user's traffic in any way, and the proxy connection can be severed as soon as the browser is closed. The adversary assumes the security context of whichever browser process the proxy is injected into. Browsers typically create a new process for each tab that is opened and permissions and certificates are separated accordingly. With these permissions, an adversary could potentially browse to any resource on an intranet, such as Sharepoint or webmail, that is accessible through the browser and which the browser has sufficient permissions. Browser pivoting may also bypass security provided by 2-factor authentication.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [evilginx2](../../tools/unknown/evilginx2.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can inject custom POST arguments into requests to silently enable "Remember Me" options during authentication to stay logged in across browser sessions.(Citation: Breakdev Evilginx 2.2 NOV 2018) |

## Source Verification

[source record](../../sources/mitre/browser-session-hijacking.md)

## Evidence Excerpt

```text
created: '2018-01-16T16:13:52.465Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may take advantage of security vulnerabilities and inherent functionality in browser software to
change content, modify user-behaviors, and intercept information as part of various browser session hijacking techniques.(Citation:
Wikipedia Man in the Browser)
A specific example is when an adversary injects software into a browser that allows them to inherit cookies, HTTP sessions,
and SSL client certificates of a user then use the browser as a way to pivot into an authenticated intranet.(Citation: Cobalt
Strike Browser Pivot)(Citation: ICEBRG Chrome Extensions) Executing browser-based behaviors such as pivoting may require
```
