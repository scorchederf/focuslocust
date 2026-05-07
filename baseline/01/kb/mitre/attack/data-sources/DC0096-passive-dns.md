---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0096
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0096-passive-dns
---

## Description

"Domain Name: Passive DNS" captures logged historical and real-time domain name system (DNS) data. This includes records of domain-to-IP address resolutions over time, enabling analysts to track the evolution of domain infrastructure, uncover historical patterns of use, and detect malicious activities tied to domains and their associated IP addresses. Examples: <br><br>- Historical Resolutions<br>- Shared IP Usage<br>- Temporal Patterns<br>- Malicious Domain Clustering<br>- Historical Lookback<br><br>This data component can be collected through the following measures:<br><br>- Passive DNS Platforms: Use platforms that specialize in passive DNS collection and analysis:<br>   - Tools: Farsight DNSDB, RiskIQ PassiveTotal, PassiveDNS.<br>- Threat Intelligence Feeds: Integrate passive DNS data from commercial or open-source threat intelligence providers.<br>- Custom DNS Collectors: Deploy custom tools to capture DNS traffic at the network level for analysis.<br>- Cloud DNS Services: Leverage cloud DNS services (e.g., AWS Route 53, Azure DNS) that maintain DNS query logs.
