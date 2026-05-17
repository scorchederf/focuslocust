---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0082 - Network Connection Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0082` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The initial establishment of a network session, where a system or process initiates a connection to a local or remote endpoint. This typically involves capturing socket information (source/destination IP, ports, protocol) and tracking session metadata. Monitoring these events helps detect lateral movement, exfiltration, and command-and-control (C2) activities.

*Data Collection Measures:*

- Windows:
    - Event ID 5156 – Filtering Platform Connection - Logs network connections permitted by Windows Filtering Platform (WFP).
    - Sysmon Event ID 3 – Network Connection Initiated - Captures process, source/destination IP, ports, and parent process.
- Linux/macOS:
    - Netfilter (iptables), nftables logs - Tracks incoming and outgoing network connections.
    - AuditD (`connect` syscall) - Logs TCP, UDP, and ICMP connections.
    - Zeek (`conn.log`) - Captures protocol, duration, and bytes transferred.
- Cloud & Network Infrastructure:
    - AWS VPC Flow Logs / Azure NSG Flow Logs - Logs IP traffic at the network level in cloud environments.
    - Zeek (conn.log) or Suricata (network events) - Captures packet metadata for detection and correlation.
- Endpoint Detection & Response (EDR):
    - Detect anomalous network activity such as new C2 connections or data exfiltration attempts.

## Source Verification

[source record](../../sources/mitre/network-connection-creation.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The initial establishment of a network session, where a system or process initiates a connection to a local\
\ or remote endpoint. This typically involves capturing socket information (source/destination IP, ports, protocol) and\
\ tracking session metadata. Monitoring these events helps detect lateral movement, exfiltration, and command-and-control\
\ (C2) activities.\n\n*Data Collection Measures:*\n\n- Windows:\n    - Event ID 5156 – Filtering Platform Connection - Logs\
\ network connections permitted by Windows Filtering Platform (WFP).\n    - Sysmon Event ID 3 – Network Connection Initiated\
\ - Captures process, source/destination IP, ports, and parent process.\n- Linux/macOS:\n    - Netfilter (iptables), nftables\
```
