---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1659 - Content Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1659` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may gain access and continuously communicate with victims by injecting malicious content into systems through online network traffic. Rather than luring victims to malicious payloads hosted on a compromised website (i.e., Drive-by Target followed by Drive-by Compromise), adversaries may initially access victims through compromised data-transfer channels where they can manipulate traffic and/or inject their own content. These compromised online network channels may also be used to deliver additional payloads (i.e., Ingress Tool Transfer) and other data to already compromised systems.

Adversaries may inject content to victim systems in various ways, including:

* From the middle, where the adversary is in-between legitimate online client-server communications (**Note:** this is similar but distinct from Adversary-in-the-Middle, which describes AiTM activity solely within an enterprise environment) 
* From the side, where malicious content is injected and races to the client as a fake response to requests of a legitimate online server 

Content injection is often the result of compromised upstream communication channels, for example at the level of an internet service provider (ISP) as is the case with "lawful interception."

## Source Verification

[source record](../../sources/mitre/content-injection.md)

## Evidence Excerpt

```text
created: '2023-09-01T21:03:13.406Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may gain access and continuously communicate with victims by injecting malicious content into systems
through online network traffic. Rather than luring victims to malicious payloads hosted on a compromised website (i.e.,
[Drive-by Target](https://attack.mitre.org/techniques/T1608/004) followed by [Drive-by Compromise](https://attack.mitre.org/techniques/T1189)),
adversaries may initially access victims through compromised data-transfer channels where they can manipulate traffic and/or
inject their own content. These compromised online network channels may also be used to deliver additional payloads (i.e.,
[Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) and other data to already compromised systems.(Citation:
```
