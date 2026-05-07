---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0044
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0044-firewall-enumeration
---

## Description

Querying and extracting a list of available firewalls or their associated configurations and rules. This activity can occur across host systems and cloud control planes, providing insight into the state and configuration of firewalls that protect the environment. Examples: <br><br>- Querying Host-Based Firewalls: Using Windows PowerShell commands like `Get-NetFirewallRule` or Linux commands such as `iptables -L` or `firewalld --list-all`.<br>- Cloud Firewall Rule Listing: Running commands like `az network firewall list` for Azure or `aws ec2 describe-security-groups` for AWS.<br>- Using Management APIs: Leveraging APIs like Google Cloud Firewall's `list` API method or AWS's DescribeSecurityGroups API.<br>Identifying Misconfigurations: Extracting firewall rules to identify “allow all” policies or rules that lack logging.<br>- Enumerating with CLI Tools: Using CLI commands like `gcloud compute firewall-rules list` to extract firewall settings in Google Cloud.
