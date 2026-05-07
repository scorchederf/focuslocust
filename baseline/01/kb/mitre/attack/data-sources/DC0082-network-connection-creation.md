---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0082
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0082-network-connection-creation
---

## Description

The initial establishment of a network session, where a system or process initiates a connection to a local or remote endpoint. This typically involves capturing socket information (source/destination IP, ports, protocol) and tracking session metadata. Monitoring these events helps detect lateral movement, exfiltration, and command-and-control (C2) activities.<br><br>*Data Collection Measures:*<br><br>- Windows:<br>    - Event ID 5156 – Filtering Platform Connection - Logs network connections permitted by Windows Filtering Platform (WFP).<br>    - Sysmon Event ID 3 – Network Connection Initiated - Captures process, source/destination IP, ports, and parent process.<br>- Linux/macOS:<br>    - Netfilter (iptables), nftables logs - Tracks incoming and outgoing network connections.<br>    - AuditD (`connect` syscall) - Logs TCP, UDP, and ICMP connections.<br>    - Zeek (`conn.log`) - Captures protocol, duration, and bytes transferred.<br>- Cloud & Network Infrastructure:<br>    - AWS VPC Flow Logs / Azure NSG Flow Logs - Logs IP traffic at the network level in cloud environments.<br>    - Zeek (conn.log) or Suricata (network events) - Captures packet metadata for detection and correlation.<br>- Endpoint Detection & Response (EDR):<br>    - Detect anomalous network activity such as new C2 connections or data exfiltration attempts.
