---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0044 - Firewall Enumeration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0044` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Querying and extracting a list of available firewalls or their associated configurations and rules. This activity can occur across host systems and cloud control planes, providing insight into the state and configuration of firewalls that protect the environment. Examples: 

- Querying Host-Based Firewalls: Using Windows PowerShell commands like `Get-NetFirewallRule` or Linux commands such as `iptables -L` or `firewalld --list-all`.
- Cloud Firewall Rule Listing: Running commands like `az network firewall list` for Azure or `aws ec2 describe-security-groups` for AWS.
- Using Management APIs: Leveraging APIs like Google Cloud Firewall's `list` API method or AWS's DescribeSecurityGroups API.
Identifying Misconfigurations: Extracting firewall rules to identify “allow all” policies or rules that lack logging.
- Enumerating with CLI Tools: Using CLI commands like `gcloud compute firewall-rules list` to extract firewall settings in Google Cloud.

## Source Verification

[source record](../../sources/mitre/firewall-enumeration.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Querying and extracting a list of available firewalls or their associated configurations and rules. This activity\
\ can occur across host systems and cloud control planes, providing insight into the state and configuration of firewalls\
\ that protect the environment. Examples: \n\n- Querying Host-Based Firewalls: Using Windows PowerShell commands like `Get-NetFirewallRule`\
\ or Linux commands such as `iptables -L` or `firewalld --list-all`.\n- Cloud Firewall Rule Listing: Running commands like\
\ `az network firewall list` for Azure or `aws ec2 describe-security-groups` for AWS.\n- Using Management APIs: Leveraging\
\ APIs like Google Cloud Firewall's `list` API method or AWS's DescribeSecurityGroups API.\nIdentifying Misconfigurations:\
```
