---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0096 - Passive DNS

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0096` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

"Domain Name: Passive DNS" captures logged historical and real-time domain name system (DNS) data. This includes records of domain-to-IP address resolutions over time, enabling analysts to track the evolution of domain infrastructure, uncover historical patterns of use, and detect malicious activities tied to domains and their associated IP addresses. Examples: 

- Historical Resolutions
- Shared IP Usage
- Temporal Patterns
- Malicious Domain Clustering
- Historical Lookback

This data component can be collected through the following measures:

- Passive DNS Platforms: Use platforms that specialize in passive DNS collection and analysis:
   - Tools: Farsight DNSDB, RiskIQ PassiveTotal, PassiveDNS.
- Threat Intelligence Feeds: Integrate passive DNS data from commercial or open-source threat intelligence providers.
- Custom DNS Collectors: Deploy custom tools to capture DNS traffic at the network level for analysis.
- Cloud DNS Services: Leverage cloud DNS services (e.g., AWS Route 53, Azure DNS) that maintain DNS query logs.

## Source Verification

[source record](../../sources/mitre/passive-dns.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.275Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "\"Domain Name: Passive DNS\" captures logged historical and real-time domain name system (DNS) data. This includes\
\ records of domain-to-IP address resolutions over time, enabling analysts to track the evolution of domain infrastructure,\
\ uncover historical patterns of use, and detect malicious activities tied to domains and their associated IP addresses.\
\ Examples: \n\n- Historical Resolutions\n- Shared IP Usage\n- Temporal Patterns\n- Malicious Domain Clustering\n- Historical\
\ Lookback\n\nThis data component can be collected through the following measures:\n\n- Passive DNS Platforms: Use platforms\
\ that specialize in passive DNS collection and analysis:\n   - Tools: Farsight DNSDB, RiskIQ PassiveTotal, PassiveDNS.\n\
```
