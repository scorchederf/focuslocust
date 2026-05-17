---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1204 - User Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1204` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

An adversary may rely upon specific actions by a user in order to gain execution. Users may be subjected to social engineering to get them to execute malicious code by, for example, opening a malicious document file or link. These user actions will typically be observed as follow-on behavior from forms of Phishing.

While User Execution frequently occurs shortly after Initial Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after Internal Spearphishing.

Adversaries may also deceive users into performing actions such as:

* Enabling Remote Access Tools, allowing direct control of the system to the adversary
* Running malicious JavaScript in their browser, allowing adversaries to Steal Web Session Cookies
* Downloading and executing malware for User Execution
* Coerceing users to copy, paste, and execute malicious code manually

For example, tech support scams can be facilitated through Phishing, vishing, or various forms of user interaction. Adversaries can use a combination of these methods, such as spoofing and promoting toll-free numbers or call centers that are used to direct victims to malicious websites, to deliver and execute payloads containing malware or Remote Access Tools.

## Source Verification

[source record](../../sources/mitre/user-execution.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may rely upon specific actions by a user in order to gain execution. Users may be subjected to
social engineering to get them to execute malicious code by, for example, opening a malicious document file or link. These
user actions will typically be observed as follow-on behavior from forms of [Phishing](https://attack.mitre.org/techniques/T1566).
While [User Execution](https://attack.mitre.org/techniques/T1204) frequently occurs shortly after Initial Access it may
occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user''s desktop
hoping that a user will click on it. This activity may also be seen shortly after [Internal Spearphishing](https://attack.mitre.org/techniques/T1534).
```
