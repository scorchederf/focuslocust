---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1557 - Adversary-in-the-Middle

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1557` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to position themselves between two or more networked devices using an adversary-in-the-middle (AiTM) technique to support follow-on behaviors such as Network Sniffing, Transmitted Data Manipulation, or replay attacks (Exploitation for Credential Access). By abusing features of common networking protocols that can determine the flow of network traffic (e.g. ARP, DNS, LLMNR, etc.), adversaries may force a device to communicate through an adversary controlled system so they can collect information or perform additional actions.

For example, adversaries may manipulate victim DNS settings to enable other malicious activities such as preventing/redirecting users from accessing legitimate sites and/or pushing additional malware. Adversaries may also manipulate DNS and leverage their position in order to intercept user credentials, including access tokens (Steal Application Access Token) and session cookies (Steal Web Session Cookie). Downgrade Attacks can also be used to establish an AiTM position, such as by negotiating a less secure, deprecated, or weaker version of communication protocol (SSL/TLS) or encryption algorithm.

Adversaries may also leverage the AiTM position to attempt to monitor and/or modify traffic, such as in Transmitted Data Manipulation. Adversaries can setup a position similar to AiTM to prevent traffic from flowing to the appropriate destination, potentially to impair defenses and/or in support of a Network Denial of Service.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [NPPSPY](../../tools/unknown/nppspy.md) | explicit | source | [NPPSPY](https://attack.mitre.org/software/S1131) opens a new network listener for the <code>mpnotify.exe</code> process that is typically contacted by the Winlogon process in Windows. A new, alternative RPC channel is set up with a malicious DLL recording plaintext credentials entered into Winlogon, effectively intercepting and redirecting the logon information.(Citation: Huntress NPPSPY 2022) |
| [evilginx2](../../tools/unknown/evilginx2.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) has the ability to act as an adversary-in-the-middle (AiTM) relay between a legitimate website and a phished user to capture all transmitted data including usernames, passwords, authentication tokens, and session cookies and tokens.(Citation: Evilginx 2 July 2018)(Citation: Breakdev Evilginx 3.0 May 2023)(Citation: Breakdev Evilginx 3.2 AUG 2023)(Citation: Sophos Evilginx MAR 2025) |

## Source Verification

[source record](../../sources/mitre/adversary-in-the-middle.md)

## Evidence Excerpt

```text
created: '2020-02-11T19:07:12.114Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to position themselves between two or more networked devices using an adversary-in-the-middle
(AiTM) technique to support follow-on behaviors such as [Network Sniffing](https://attack.mitre.org/techniques/T1040), [Transmitted
Data Manipulation](https://attack.mitre.org/techniques/T1565/002), or replay attacks ([Exploitation for Credential Access](https://attack.mitre.org/techniques/T1212)).
By abusing features of common networking protocols that can determine the flow of network traffic (e.g. ARP, DNS, LLMNR,
etc.), adversaries may force a device to communicate through an adversary controlled system so they can collect information
or perform additional actions.(Citation: Rapid7 MiTM Basics)
```
