---
parsed_by: focuslocust
source: mitre
type: generated
---
# Network Segmentation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1030` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Segmentation](../../attack/mitigations/M1030-network-segmentation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1030 |
| name | Network Segmentation |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1030 |

## Preserved Source Material

```yaml
created: '2019-06-10T20:41:03.271Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Network segmentation involves dividing a network into smaller, isolated segments to control and limit the flow
  of traffic between devices, systems, and applications. By segmenting networks, organizations can reduce the attack surface,
  restrict lateral movement by adversaries, and protect critical assets from compromise.


  Effective network segmentation leverages a combination of physical boundaries, logical separation through VLANs, and access
  control policies enforced by network appliances like firewalls, routers, and cloud-based configurations. This mitigation
  can be implemented through the following measures:


  Segment Critical Systems:


  - Identify and group systems based on their function, sensitivity, and risk. Examples include payment systems, HR databases,
  production systems, and internet-facing servers.

  - Use VLANs, firewalls, or routers to enforce logical separation.


  Implement DMZ for Public-Facing Services:


  - Host web servers, DNS servers, and email servers in a DMZ to limit their access to internal systems.

  - Apply strict firewall rules to filter traffic between the DMZ and internal networks.


  Use Cloud-Based Segmentation:


  - In cloud environments, use VPCs, subnets, and security groups to isolate applications and enforce traffic rules.

  - Apply AWS Transit Gateway or Azure VNet peering for controlled connectivity between cloud segments.


  Apply Microsegmentation for Workloads:


  - Use software-defined networking (SDN) tools to implement workload-level segmentation and prevent lateral movement.


  Restrict Traffic with ACLs and Firewalls:


  - Apply Access Control Lists (ACLs) to network devices to enforce "deny by default" policies.

  - Use firewalls to restrict both north-south (external-internal) and east-west (internal-internal) traffic.


  Monitor and Audit Segmented Networks:


  - Regularly review firewall rules, ACLs, and segmentation policies.

  - Monitor network flows for anomalies to ensure segmentation is effective.


  Test Segmentation Effectiveness:


  - Perform periodic penetration tests to verify that unauthorized access is blocked between network segments.'
external_references:
- external_id: M1030
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1030
id: course-of-action--86598de0-b347-4928-9eb0-0acbfc21908c
modified: '2026-04-24T19:41:50.467Z'
name: Network Segmentation
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: course-of-action
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '1.2'
```
