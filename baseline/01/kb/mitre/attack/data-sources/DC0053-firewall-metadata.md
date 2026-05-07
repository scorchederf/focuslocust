---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0053
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0053-firewall-metadata
---

## Description

Contextual information about firewalls, including their configurations, policies, status, and other details such as names and associated rules. This metadata provides valuable insights into the operational state and configurations of firewalls, both in cloud control planes and host systems. Examples: <br><br>- Firewall Name and Configuration: The name, type, and purpose of a firewall such as "Azure Firewall - Production Environment."<br>- Policy Details: Capturing firewall policy details, such as "Allow inbound TCP 443 to web servers."<br>- Firewall Status: Status indicators like "Active," "Disabled," or "Pending Updates."<br>- Audit Log Metadata: Log entries showing administrative changes, such as "Policy modified by admin@domain.com."<br>- Rules Associated with Firewalls: Rules specifying source/destination IP ranges, protocols, and ports.<br>- Tagging Information: Tags like "Environment: Production" or "Owner: NetworkOps."<br><br>This data component can be collected through the following measures:<br><br>Cloud Control Plane<br><br>- Azure: Use Azure Activity Logs and Network Watcher to collect metadata for Azure Firewall.<br>    - Example: `az network firewall show --name <firewall-name>`<br>- AWS: Use AWS CloudTrail and describe commands: `aws ec2 describe-security-groups`<br>- Google Cloud: Use gcloud commands to extract metadata: `gcloud compute firewall-rules list --format=json`<br><br>Host-Based Firewalls<br><br>- Windows: Use PowerShell to gather metadata: `Get-NetFirewallRule -PolicyStore PersistentStore`<br>- Linux: Query iptables or nftables rulesets: `iptables -S`<br>- macOS: Use pfctl to extract metadata: `sudo pfctl -sr`<br><br>SIEM Integration<br><br>- Collect logs from cloud platforms, host systems, and network appliances.<br><br>API Monitoring<br><br>- Monitor API calls for metadata requests. Example (AWS): `Capture DescribeSecurityGroups or DescribeNetworkAcls` calls via CloudTrail.<br><br>Endpoint Detection and Response (EDR)<br><br>- Use EDR solutions to monitor firewall management tools for configuration changes or queries.
