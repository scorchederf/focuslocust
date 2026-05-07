---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0085
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0085-network-traffic-content
---

## Description

The full packet capture (PCAP) or session data that logs both protocol headers and payload content. This allows analysts to inspect command and control (C2) traffic, exfiltration, and other suspicious activity within network communications. Unlike metadata-based logs, full content analysis enables deeper protocol inspection, payload decoding, and forensic investigations.<br><br>*Data Collection Measures:*<br><br>- Network Packet Capture (Full Content Logging)<br>    - Wireshark / tcpdump / tshark<br>        - Full packet captures (PCAP files) for manual analysis or IDS correlation. `tcpdump -i eth0 -w capture.pcap`<br>    - Zeek (formerly Bro)<br>        - Extracts protocol headers and payload details into structured logs. `echo "redef Log::default_store = Log::ASCII;" > local.zeek | zeek -Cr capture.pcap local.zeek`<br>    - Suricata / Snort (IDS/IPS with PCAP Logging)<br>        - Deep packet inspection (DPI) with signature-based and behavioral analysis. `suricata -c /etc/suricata/suricata.yaml -i eth0 -l /var/log/suricata`<br>- Host-Based Collection<br>    - Sysmon Event ID 22 – DNS Query Logging, Captures DNS requests made by processes, useful for detecting C2 domains.<br>    - Sysmon Event ID 3 – Network Connection Initiated, Logs process-to-network connection relationships.<br>    - AuditD (Linux) – syscall=connect, Monitors outbound network requests from processes. `auditctl -a always,exit -F arch=b64 -S connect -k network_activity`<br>- Cloud & SaaS Traffic Collection<br>    - AWS VPC Flow Logs / Azure NSG Flow Logs / Google VPC Flow Logs, Captures metadata about inbound/outbound network traffic.<br>    - Cloud IDS (AWS GuardDuty, Azure Sentinel, Google Chronicle), Detects malicious activity in cloud environments by analyzing network traffic patterns.
