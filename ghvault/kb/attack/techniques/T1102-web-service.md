---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1102 - Web Service

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1102` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may use an existing, legitimate external Web service as a means for relaying data to/from a compromised system. Popular websites, cloud services, and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google, Microsoft, or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.

Use of Web services may also protect back-end C2 infrastructure from discovery through malware binary analysis while also enabling operational resiliency (since this infrastructure may be dynamically changed).

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Brute Ratel C4](../../tools/unknown/brute-ratel-c4.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use legitimate websites for external C2 channels including Slack, Discord, and MS Teams.(Citation: Palo Alto Brute Ratel July 2022) |
| [ngrok](../../tools/unknown/ngrok.md) | explicit | source | [ngrok](https://attack.mitre.org/software/S0508) has been used by threat actors to proxy C2 connections to ngrok service subdomains.(Citation: Zdnet Ngrok September 2018) |

## Source Verification

[source record](../../sources/mitre/web-service.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:13.915Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use an existing, legitimate external Web service as a means for relaying data to/from a compromised
system. Popular websites, cloud services, and social media acting as a mechanism for C2 may give a significant amount of
cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using
common services, such as those offered by Google, Microsoft, or Twitter, makes it easier for adversaries to hide in expected
noise.(Citation: Broadcom BirdyClient Microsoft Graph API 2024) Web service providers commonly use SSL/TLS encryption, giving
adversaries an added level of protection.
```
