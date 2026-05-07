---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0051
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0051-firewall-rule-modification
---

## Description

The creation, deletion, or alteration of firewall rules to allow or block specific network traffic. Monitoring changes to these rules is critical for detecting misconfigurations, unauthorized access, or malicious attempts to bypass network protections. Examples: <br><br>- Rule Creation: Adding a new rule to allow inbound traffic on port 3389 (RDP).<br>- Rule Deletion: Deleting a rule that blocks inbound traffic from untrusted IP ranges.<br>- Rule Modification: Changing a rule to allow traffic from "any" source IP instead of a specific trusted range.<br>- Audit Log Metadata: Logs indicating "Firewall rule modified by admin@domain.com."<br>- Platform-Specific Scenarios<br>    - Azure: Altering rules in an Azure Network Security Group (NSG).<br>    - AWS: Modifying Security Group rules to allow traffic.<br>    - Windows: Changes tracked in Security Event Logs (EID 4950 or 4951).<br><br>This data component can be collected through the following measures:<br><br>Cloud Control Plane<br><br>- Azure: Collect rule modification logs from Azure Firewall Activity Logs.<br>    - Example Command: `az network firewall policy rule-collection-group rule-collection list --policy-name <policy-name>`<br>- AWS: Use CloudTrail to track `AuthorizeSecurityGroupIngress` or `RevokeSecurityGroupIngress` actions.<br>    Example: `aws ec2 describe-security-groups`<br>- Google Cloud: Use gcloud commands to extract firewall rules: `gcloud compute firewall-rules list --format=json`<br><br>Host-Based Firewalls<br><br>- Windows: <br>    - Collect events from the Windows Security Event Log (EID 4950: A rule has been modified).<br>    - Use PowerShell to track rule changes: `Get-NetFirewallRule -PolicyStore PersistentStore`<br>- Linux:<br>    - Monitor iptables or nftables rule modifications: `iptables -L -v`<br>    - Use auditd for real-time monitoring: `auditctl -w /etc/iptables.rules -p wa`<br>- macOS: Use pfctl to monitor rule changes: `sudo pfctl -sr`<br><br>SIEM Integration<br><br>- Collect logs from cloud platforms, host systems, and network appliances for centralized monitoring.<br><br>API Monitoring<br><br>- Monitor API calls for firewall rule modifications.
