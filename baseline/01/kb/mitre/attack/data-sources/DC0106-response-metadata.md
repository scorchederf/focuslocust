---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0106
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0106-response-metadata
---

## Description

Contextual information about an Internet-facing resource collected during a scan, including details such as open ports, running services, protocols, and versions. This metadata is typically derived from interpreting scan results and helps build a profile of the targeted system. Examples: <br><br>- Port and Service Details:<br>    - Open ports (e.g., 22, 80, 443).<br>    - Identified services running on those ports (e.g., SSH, HTTP, HTTPS).<br>- Service Versions: Detected software version information (e.g., Apache 2.4.41, OpenSSH 8.2).<br>- Operating System Information: OS fingerprinting data (e.g., Linux Kernel 5.4.0).<br>- TLS/SSL Certificate Data: Information about the TLS/SSL certificate, such as the expiration date, issuer, and cipher suites.<br><br>*Data Collection Measures:*<br><br>- Scanning Tools:<br>    - Nmap: Collects port, service, and version information using commands like nmap -sV <IP>.<br>    - Masscan: High-speed scanning tool for discovering open ports and active services.<br>    - Zmap: Focused on large-scale Internet scanning, collecting metadata about discovered services.<br>    - Shodan API: Retrieves scan metadata for publicly exposed devices and services.<br>- Network Logs:<br>    - Use logs from firewalls, intrusion detection systems (IDS), or intrusion prevention systems (IPS) to gather metadata from scan attempts. Example: Zeek or Suricata logs for incoming scan traffic.<br>- OSINT Platforms: Platforms like Censys, GreyNoise, or Shodan provide aggregated metadata about Internet-facing resources.<br>- Cloud Metadata Services: AWS Security Hub, Azure Monitor, or GCP Security Command Center can collect and centralize scan-related metadata for Internet-facing resources in cloud environments.
