---
parsed_by: focuslocust
source: mitre
type: generated
---
# M1037 - Filter Network Traffic

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1037` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Employ network appliances and endpoint software to filter ingress, egress, and lateral network traffic. This includes protocol-based filtering, enforcing firewall rules, and blocking or restricting traffic based on predefined conditions to limit adversary movement and data exfiltration. This mitigation can be implemented through the following measures:

Ingress Traffic Filtering:

- Use Case: Configure network firewalls to allow traffic only from authorized IP addresses to public-facing servers.
- Implementation: Limit SSH (port 22) and RDP (port 3389) traffic to specific IP ranges.

Egress Traffic Filtering:

- Use Case: Use firewalls or endpoint security software to block unauthorized outbound traffic to prevent data exfiltration and command-and-control (C2) communications.
- Implementation: Block outbound traffic to known malicious IPs or regions where communication is unexpected.

Protocol-Based Filtering:

- Use Case: Restrict the use of specific protocols that are commonly abused by adversaries, such as SMB, RPC, or Telnet, based on business needs.
- Implementation: Disable SMBv1 on endpoints to prevent exploits like EternalBlue.

Network Segmentation:

- Use Case: Create network segments for critical systems and restrict communication between segments unless explicitly authorized.
- Implementation: Implement VLANs to isolate IoT devices or guest networks from core business systems.

Application Layer Filtering:

- Use Case: Use proxy servers or Web Application Firewalls (WAFs) to inspect and block malicious HTTP/S traffic.
- Implementation: Configure a WAF to block SQL injection attempts or other web application exploitation techniques.

## Source Verification

[source record](../../sources/mitre/filter-network-traffic.md)

## Evidence Excerpt

```text
created: '2019-06-11T16:33:55.337Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Employ network appliances and endpoint software to filter ingress, egress, and lateral network traffic. This
includes protocol-based filtering, enforcing firewall rules, and blocking or restricting traffic based on predefined conditions
to limit adversary movement and data exfiltration. This mitigation can be implemented through the following measures:
Ingress Traffic Filtering:
- Use Case: Configure network firewalls to allow traffic only from authorized IP addresses to public-facing servers.
- Implementation: Limit SSH (port 22) and RDP (port 3389) traffic to specific IP ranges.
```
