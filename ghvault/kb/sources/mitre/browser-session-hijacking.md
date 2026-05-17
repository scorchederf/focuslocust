---
parsed_by: focuslocust
source: mitre
type: generated
---
# Browser Session Hijacking

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

## Generated Concept Page

- [Browser Session Hijacking](../../attack/techniques/T1185-browser-session-hijacking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1185 |
| name | Browser Session Hijacking |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1185 |

## Preserved Source Material

```yaml
created: '2018-01-16T16:13:52.465Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may take advantage of security vulnerabilities and inherent functionality in browser software to
  change content, modify user-behaviors, and intercept information as part of various browser session hijacking techniques.(Citation:
  Wikipedia Man in the Browser)


  A specific example is when an adversary injects software into a browser that allows them to inherit cookies, HTTP sessions,
  and SSL client certificates of a user then use the browser as a way to pivot into an authenticated intranet.(Citation: Cobalt
  Strike Browser Pivot)(Citation: ICEBRG Chrome Extensions) Executing browser-based behaviors such as pivoting may require
  specific process permissions, such as <code>SeDebugPrivilege</code> and/or high-integrity/administrator rights.


  Another example involves pivoting browser traffic from the adversary''s browser through the user''s browser by setting up
  a proxy which will redirect web traffic. This does not alter the user''s traffic in any way, and the proxy connection can
  be severed as soon as the browser is closed. The adversary assumes the security context of whichever browser process the
  proxy is injected into. Browsers typically create a new process for each tab that is opened and permissions and certificates
  are separated accordingly. With these permissions, an adversary could potentially browse to any resource on an intranet,
  such as [Sharepoint](https://attack.mitre.org/techniques/T1213/002) or webmail, that is accessible through the browser and
  which the browser has sufficient permissions. Browser pivoting may also bypass security provided by 2-factor authentication.(Citation:
  cobaltstrike manual)'
external_references:
- external_id: T1185
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1185
- description: De Tore, M., Warner, J. (2018, January 15). MALICIOUS CHROME EXTENSIONS ENABLE CRIMINALS TO IMPACT OVER HALF
    A MILLION USERS AND GLOBAL BUSINESSES. Retrieved January 17, 2018.
  source_name: ICEBRG Chrome Extensions
  url: https://www.icebrg.io/blog/malicious-chrome-extensions-enable-criminals-to-impact-over-half-a-million-users-and-global-businesses
- description: Mudge, R. (n.d.). Browser Pivoting. Retrieved January 10, 2018.
  source_name: Cobalt Strike Browser Pivot
  url: https://www.cobaltstrike.com/help-browser-pivoting
- description: Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.
  source_name: cobaltstrike manual
  url: https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf
- description: Wikipedia. (2017, October 28). Man-in-the-browser. Retrieved January 10, 2018.
  source_name: Wikipedia Man in the Browser
  url: https://en.wikipedia.org/wiki/Man-in-the-browser
id: attack-pattern--544b0346-29ad-41e1-a808-501bb4193f47
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:48:48.383Z'
name: Browser Session Hijacking
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Justin Warner, ICEBRG
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '2.1'
```
