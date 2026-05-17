---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0053 - Firewall Metadata

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0053` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Contextual information about firewalls, including their configurations, policies, status, and other details such as names and associated rules. This metadata provides valuable insights into the operational state and configurations of firewalls, both in cloud control planes and host systems. Examples: 

- Firewall Name and Configuration: The name, type, and purpose of a firewall such as "Azure Firewall - Production Environment."
- Policy Details: Capturing firewall policy details, such as "Allow inbound TCP 443 to web servers."
- Firewall Status: Status indicators like "Active," "Disabled," or "Pending Updates."
- Audit Log Metadata: Log entries showing administrative changes, such as "Policy modified by admin@domain.com."
- Rules Associated with Firewalls: Rules specifying source/destination IP ranges, protocols, and ports.
- Tagging Information: Tags like "Environment: Production" or "Owner: NetworkOps."

This data component can be collected through the following measures:

Cloud Control Plane

- Azure: Use Azure Activity Logs and Network Watcher to collect metadata for Azure Firewall.
    - Example: `az network firewall show --name <firewall-name>`
- AWS: Use AWS CloudTrail and describe commands: `aws ec2 describe-security-groups`
- Google Cloud: Use gcloud commands to extract metadata: `gcloud compute firewall-rules list --format=json`

Host-Based Firewalls

- Windows: Use PowerShell to gather metadata: `Get-NetFirewallRule -PolicyStore PersistentStore`
- Linux: Query iptables or nftables rulesets: `iptables -S`
- macOS: Use pfctl to extract metadata: `sudo pfctl -sr`

SIEM Integration

- Collect logs from cloud platforms, host systems, and network appliances.

API Monitoring

- Monitor API calls for metadata requests. Example (AWS): `Capture DescribeSecurityGroups or DescribeNetworkAcls` calls via CloudTrail.

Endpoint Detection and Response (EDR)

- Use EDR solutions to monitor firewall management tools for configuration changes or queries.

## Source Verification

[source record](../../sources/mitre/firewall-metadata.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Contextual information about firewalls, including their configurations, policies, status, and other details\
\ such as names and associated rules. This metadata provides valuable insights into the operational state and configurations\
\ of firewalls, both in cloud control planes and host systems. Examples: \n\n- Firewall Name and Configuration: The name,\
\ type, and purpose of a firewall such as \"Azure Firewall - Production Environment.\"\n- Policy Details: Capturing firewall\
\ policy details, such as \"Allow inbound TCP 443 to web servers.\"\n- Firewall Status: Status indicators like \"Active,\"\
\ \"Disabled,\" or \"Pending Updates.\"\n- Audit Log Metadata: Log entries showing administrative changes, such as \"Policy\
```
