---
parsed_by: focuslocust
source: mitre
type: generated
---
# Limit Access to Resource Over Network

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1035` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Limit Access to Resource Over Network](../../attack/mitigations/M1035-limit-access-to-resource-over-network.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1035 |
| name | Limit Access to Resource Over Network |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1035 |

## Preserved Source Material

```yaml
created: '2019-06-11T16:30:16.672Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Restrict access to network resources, such as file shares, remote systems, and services, to only those users,
  accounts, or systems with a legitimate business requirement. This can include employing technologies like network concentrators,
  RDP gateways, and zero-trust network access (ZTNA) models, alongside hardening services and protocols. This mitigation can
  be implemented through the following measures:


  Audit and Restrict Access:


  - Regularly audit permissions for file shares, network services, and remote access tools.

  - Remove unnecessary access and enforce least privilege principles for users and services.

  - Use Active Directory and IAM tools to restrict access based on roles and attributes.


  Deploy Secure Remote Access Solutions:


  - Use RDP gateways, VPN concentrators, and ZTNA solutions to aggregate and secure remote access connections.

  - Configure access controls to restrict connections based on time, device, and user identity.

  - Enforce MFA for all remote access mechanisms.


  Disable Unnecessary Services:


  - Identify running services using tools like netstat (Windows/Linux) or Nmap.

  - Disable unused services, such as Telnet, FTP, and legacy SMB, to reduce the attack surface.

  - Use firewall rules to block traffic on unused ports and protocols.


  Network Segmentation and Isolation:


  - Use VLANs, firewalls, or micro-segmentation to isolate critical network resources from general access.

  - Restrict communication between subnets to prevent lateral movement.


  Monitor and Log Access:


  - Monitor access attempts to file shares, RDP, and remote network resources using SIEM tools.

  - Enable auditing and logging for successful and failed attempts to access restricted resources.


  *Tools for Implementation*


  File Share Management:


  - Microsoft Active Directory Group Policies

  - Samba (Linux/Unix file share management)

  - AccessEnum (Windows access auditing tool)


  Secure Remote Access:


  - Microsoft Remote Desktop Gateway

  - Apache Guacamole (open-source RDP/VNC gateway)

  - Zero Trust solutions: Tailscale, Cloudflare Zero Trust


  Service and Protocol Hardening:


  - Nmap or Nessus for network service discovery

  - Windows Group Policy Editor for disabling SMBv1, Telnet, and legacy protocols

  - iptables or firewalld (Linux) for blocking unnecessary traffic


  Network Segmentation:


  - pfSense for open-source network isolation'
external_references:
- external_id: M1035
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1035
id: course-of-action--1dcaeb21-9348-42ea-950a-f842aaf1ae1f
modified: '2024-12-18T15:50:51.212Z'
name: Limit Access to Resource Over Network
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: course-of-action
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '1.1'
```
