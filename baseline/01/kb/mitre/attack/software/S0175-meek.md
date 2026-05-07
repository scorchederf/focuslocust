---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0175
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0175-meek
---

## Description

[[kb/mitre/attack/software/S0175-meek|meek]] is an open-source Tor plugin that tunnels Tor traffic through HTTPS connections.

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1090.004-domain-fronting\|T1090.004]] | Domain Fronting | [[kb/mitre/attack/software/S0175-meek\|meek]] uses Domain Fronting to disguise the destination of network traffic as another server that is hosted in the same Content Delivery Network (CDN) as the intended destination. |
