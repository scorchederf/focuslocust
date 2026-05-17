---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1217 - Browser Information Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1217` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may enumerate information about browsers to learn more about compromised environments. Data saved by browsers (such as bookmarks, accounts, and browsing history) may reveal a variety of personal information about users (e.g., banking sites, relationships/interests, social media, etc.) as well as details about internal network resources such as servers, tools/dashboards, or other related infrastructure.

Browser information may also highlight additional targets after an adversary has access to valid credentials, especially Credentials In Files associated with logins cached by a browser.

Specific storage locations vary based on platform and/or application, but browser information is typically stored in local files and databases (e.g., `%APPDATA%/Google/Chrome`).

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) has the ability to gather browser data such as bookmarks and visited sites.(Citation: Github PowerShell Empire) |

## Source Verification

[source record](../../sources/mitre/browser-information-discovery.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may enumerate information about browsers to learn more about compromised environments. Data saved
by browsers (such as bookmarks, accounts, and browsing history) may reveal a variety of personal information about users
(e.g., banking sites, relationships/interests, social media, etc.) as well as details about internal network resources such
as servers, tools/dashboards, or other related infrastructure.(Citation: Kaspersky Autofill)
Browser information may also highlight additional targets after an adversary has access to valid credentials, especially
[Credentials In Files](https://attack.mitre.org/techniques/T1552/001) associated with logins cached by a browser.
```
