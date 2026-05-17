---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0106 - Response Metadata

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0106` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Contextual information about an Internet-facing resource collected during a scan, including details such as open ports, running services, protocols, and versions. This metadata is typically derived from interpreting scan results and helps build a profile of the targeted system. Examples: 

- Port and Service Details:
    - Open ports (e.g., 22, 80, 443).
    - Identified services running on those ports (e.g., SSH, HTTP, HTTPS).
- Service Versions: Detected software version information (e.g., Apache 2.4.41, OpenSSH 8.2).
- Operating System Information: OS fingerprinting data (e.g., Linux Kernel 5.4.0).
- TLS/SSL Certificate Data: Information about the TLS/SSL certificate, such as the expiration date, issuer, and cipher suites.

*Data Collection Measures:*

- Scanning Tools:
    - Nmap: Collects port, service, and version information using commands like nmap -sV <IP>.
    - Masscan: High-speed scanning tool for discovering open ports and active services.
    - Zmap: Focused on large-scale Internet scanning, collecting metadata about discovered services.
    - Shodan API: Retrieves scan metadata for publicly exposed devices and services.
- Network Logs:
    - Use logs from firewalls, intrusion detection systems (IDS), or intrusion prevention systems (IPS) to gather metadata from scan attempts. Example: Zeek or Suricata logs for incoming scan traffic.
- OSINT Platforms: Platforms like Censys, GreyNoise, or Shodan provide aggregated metadata about Internet-facing resources.
- Cloud Metadata Services: AWS Security Hub, Azure Monitor, or GCP Security Command Center can collect and centralize scan-related metadata for Internet-facing resources in cloud environments.

## Source Verification

[source record](../../sources/mitre/response-metadata.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.275Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Contextual information about an Internet-facing resource collected during a scan, including details such as\
\ open ports, running services, protocols, and versions. This metadata is typically derived from interpreting scan results\
\ and helps build a profile of the targeted system. Examples: \n\n- Port and Service Details:\n    - Open ports (e.g., 22,\
\ 80, 443).\n    - Identified services running on those ports (e.g., SSH, HTTP, HTTPS).\n- Service Versions: Detected software\
\ version information (e.g., Apache 2.4.41, OpenSSH 8.2).\n- Operating System Information: OS fingerprinting data (e.g.,\
\ Linux Kernel 5.4.0).\n- TLS/SSL Certificate Data: Information about the TLS/SSL certificate, such as the expiration date,\
```
