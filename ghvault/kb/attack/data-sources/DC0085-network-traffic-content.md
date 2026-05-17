---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0085 - Network Traffic Content

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0085` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The full packet capture (PCAP) or session data that logs both protocol headers and payload content. This allows analysts to inspect command and control (C2) traffic, exfiltration, and other suspicious activity within network communications. Unlike metadata-based logs, full content analysis enables deeper protocol inspection, payload decoding, and forensic investigations.

*Data Collection Measures:*

- Network Packet Capture (Full Content Logging)
    - Wireshark / tcpdump / tshark
        - Full packet captures (PCAP files) for manual analysis or IDS correlation. `tcpdump -i eth0 -w capture.pcap`
    - Zeek (formerly Bro)
        - Extracts protocol headers and payload details into structured logs. `echo "redef Log::default_store = Log::ASCII;" > local.zeek | zeek -Cr capture.pcap local.zeek`
    - Suricata / Snort (IDS/IPS with PCAP Logging)
        - Deep packet inspection (DPI) with signature-based and behavioral analysis. `suricata -c /etc/suricata/suricata.yaml -i eth0 -l /var/log/suricata`
- Host-Based Collection
    - Sysmon Event ID 22 – DNS Query Logging, Captures DNS requests made by processes, useful for detecting C2 domains.
    - Sysmon Event ID 3 – Network Connection Initiated, Logs process-to-network connection relationships.
    - AuditD (Linux) – syscall=connect, Monitors outbound network requests from processes. `auditctl -a always,exit -F arch=b64 -S connect -k network_activity`
- Cloud & SaaS Traffic Collection
    - AWS VPC Flow Logs / Azure NSG Flow Logs / Google VPC Flow Logs, Captures metadata about inbound/outbound network traffic.
    - Cloud IDS (AWS GuardDuty, Azure Sentinel, Google Chronicle), Detects malicious activity in cloud environments by analyzing network traffic patterns.

## Source Verification

[source record](../../sources/mitre/network-traffic-content.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The full packet capture (PCAP) or session data that logs both protocol headers and payload content. This allows\
\ analysts to inspect command and control (C2) traffic, exfiltration, and other suspicious activity within network communications.\
\ Unlike metadata-based logs, full content analysis enables deeper protocol inspection, payload decoding, and forensic investigations.\n\
\n*Data Collection Measures:*\n\n- Network Packet Capture (Full Content Logging)\n    - Wireshark / tcpdump / tshark\n \
\       - Full packet captures (PCAP files) for manual analysis or IDS correlation. `tcpdump -i eth0 -w capture.pcap`\n\
\    - Zeek (formerly Bro)\n        - Extracts protocol headers and payload details into structured logs. `echo \"redef\
```
