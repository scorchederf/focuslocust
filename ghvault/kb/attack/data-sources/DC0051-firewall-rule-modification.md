---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0051 - Firewall Rule Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0051` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The creation, deletion, or alteration of firewall rules to allow or block specific network traffic. Monitoring changes to these rules is critical for detecting misconfigurations, unauthorized access, or malicious attempts to bypass network protections. Examples: 

- Rule Creation: Adding a new rule to allow inbound traffic on port 3389 (RDP).
- Rule Deletion: Deleting a rule that blocks inbound traffic from untrusted IP ranges.
- Rule Modification: Changing a rule to allow traffic from "any" source IP instead of a specific trusted range.
- Audit Log Metadata: Logs indicating "Firewall rule modified by admin@domain.com."
- Platform-Specific Scenarios
    - Azure: Altering rules in an Azure Network Security Group (NSG).
    - AWS: Modifying Security Group rules to allow traffic.
    - Windows: Changes tracked in Security Event Logs (EID 4950 or 4951).

This data component can be collected through the following measures:

Cloud Control Plane

- Azure: Collect rule modification logs from Azure Firewall Activity Logs.
    - Example Command: `az network firewall policy rule-collection-group rule-collection list --policy-name <policy-name>`
- AWS: Use CloudTrail to track `AuthorizeSecurityGroupIngress` or `RevokeSecurityGroupIngress` actions.
    Example: `aws ec2 describe-security-groups`
- Google Cloud: Use gcloud commands to extract firewall rules: `gcloud compute firewall-rules list --format=json`

Host-Based Firewalls

- Windows: 
    - Collect events from the Windows Security Event Log (EID 4950: A rule has been modified).
    - Use PowerShell to track rule changes: `Get-NetFirewallRule -PolicyStore PersistentStore`
- Linux:
    - Monitor iptables or nftables rule modifications: `iptables -L -v`
    - Use auditd for real-time monitoring: `auditctl -w /etc/iptables.rules -p wa`
- macOS: Use pfctl to monitor rule changes: `sudo pfctl -sr`

SIEM Integration

- Collect logs from cloud platforms, host systems, and network appliances for centralized monitoring.

API Monitoring

- Monitor API calls for firewall rule modifications.

## Source Verification

[source record](../../sources/mitre/firewall-rule-modification.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The creation, deletion, or alteration of firewall rules to allow or block specific network traffic. Monitoring\
\ changes to these rules is critical for detecting misconfigurations, unauthorized access, or malicious attempts to bypass\
\ network protections. Examples: \n\n- Rule Creation: Adding a new rule to allow inbound traffic on port 3389 (RDP).\n-\
\ Rule Deletion: Deleting a rule that blocks inbound traffic from untrusted IP ranges.\n- Rule Modification: Changing a\
\ rule to allow traffic from \"any\" source IP instead of a specific trusted range.\n- Audit Log Metadata: Logs indicating\
\ \"Firewall rule modified by admin@domain.com.\"\n- Platform-Specific Scenarios\n    - Azure: Altering rules in an Azure\
```
