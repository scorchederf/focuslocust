---
parsed_by: focuslocust
source: mitre
type: generated
---
# ngrok

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0508` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

ngrok is a legitimate reverse proxy tool that can create a secure tunnel to servers located behind firewalls or on local machines that do not have a public IP. ngrok has been leveraged by threat actors in several campaigns including use for lateral movement and data exfiltration.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/ngrok.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1090 - Proxy](../../attack/techniques/T1090-proxy.md) | explicit | source | [ngrok](https://attack.mitre.org/software/S0508) can be used to proxy connections to machines located behind NAT or firewalls.(Citation: MalwareBytes Ngrok February 2020)(Citation: Zdnet Ngrok September 2018) |
| [T1102 - Web Service](../../attack/techniques/T1102-web-service.md) | explicit | source | [ngrok](https://attack.mitre.org/software/S0508) has been used by threat actors to proxy C2 connections to ngrok service subdomains.(Citation: Zdnet Ngrok September 2018) |
| [T1567 - Exfiltration Over Web Service](../../attack/techniques/T1567-exfiltration-over-web-service.md) | explicit | source | [ngrok](https://attack.mitre.org/software/S0508) has been used by threat actors to configure servers for data exfiltration.(Citation: MalwareBytes Ngrok February 2020) |
| [T1568.002 - Domain Generation Algorithms](../../attack/techniques/T1568.002-domain-generation-algorithms.md) | explicit | source | [ngrok](https://attack.mitre.org/software/S0508) can provide DGA for C2 servers through the use of random URL strings that change every 12 hours.(Citation: Zdnet Ngrok September 2018) |
| [T1572 - Protocol Tunneling](../../attack/techniques/T1572-protocol-tunneling.md) | explicit | source | [ngrok](https://attack.mitre.org/software/S0508) can tunnel RDP and other services securely over internet connections.(Citation: FireEye Maze May 2020)(Citation: Cyware Ngrok May 2019)(Citation: MalwareBytes Ngrok February 2020)(Citation: Trend Micro Ngrok September 2020) |

## Source Verification

[source record](../../sources/mitre/ngrok.md)

## Evidence Excerpt

```text
created: '2023-09-14T18:56:34.771Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[ngrok](https://attack.mitre.org/software/S0508) is a legitimate reverse proxy tool that can create a secure
tunnel to servers located behind firewalls or on local machines that do not have a public IP. [ngrok](https://attack.mitre.org/software/S0508)
has been leveraged by threat actors in several campaigns including use for lateral movement and data exfiltration.(Citation:
Zdnet Ngrok September 2018)(Citation: FireEye Maze May 2020)(Citation: Cyware Ngrok May 2019)(Citation: MalwareBytes LazyScripter
Feb 2021)'
external_references:
```
