---
parsed_by: focuslocust
source: mitre
type: generated
---
# Firewall Rule Modification

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

## Generated Concept Page

- [Firewall Rule Modification](../../attack/data-sources/DC0051-firewall-rule-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0051 |
| name | Firewall Rule Modification |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0051 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The creation, deletion, or alteration of firewall rules to allow or block specific network traffic. Monitoring\
  \ changes to these rules is critical for detecting misconfigurations, unauthorized access, or malicious attempts to bypass\
  \ network protections. Examples: \n\n- Rule Creation: Adding a new rule to allow inbound traffic on port 3389 (RDP).\n-\
  \ Rule Deletion: Deleting a rule that blocks inbound traffic from untrusted IP ranges.\n- Rule Modification: Changing a\
  \ rule to allow traffic from \"any\" source IP instead of a specific trusted range.\n- Audit Log Metadata: Logs indicating\
  \ \"Firewall rule modified by admin@domain.com.\"\n- Platform-Specific Scenarios\n    - Azure: Altering rules in an Azure\
  \ Network Security Group (NSG).\n    - AWS: Modifying Security Group rules to allow traffic.\n    - Windows: Changes tracked\
  \ in Security Event Logs (EID 4950 or 4951).\n\nThis data component can be collected through the following measures:\n\n\
  Cloud Control Plane\n\n- Azure: Collect rule modification logs from Azure Firewall Activity Logs.\n    - Example Command:\
  \ `az network firewall policy rule-collection-group rule-collection list --policy-name <policy-name>`\n- AWS: Use CloudTrail\
  \ to track `AuthorizeSecurityGroupIngress` or `RevokeSecurityGroupIngress` actions.\n    Example: `aws ec2 describe-security-groups`\n\
  - Google Cloud: Use gcloud commands to extract firewall rules: `gcloud compute firewall-rules list --format=json`\n\nHost-Based\
  \ Firewalls\n\n- Windows: \n    - Collect events from the Windows Security Event Log (EID 4950: A rule has been modified).\n\
  \    - Use PowerShell to track rule changes: `Get-NetFirewallRule -PolicyStore PersistentStore`\n- Linux:\n    - Monitor\
  \ iptables or nftables rule modifications: `iptables -L -v`\n    - Use auditd for real-time monitoring: `auditctl -w /etc/iptables.rules\
  \ -p wa`\n- macOS: Use pfctl to monitor rule changes: `sudo pfctl -sr`\n\nSIEM Integration\n\n- Collect logs from cloud\
  \ platforms, host systems, and network appliances for centralized monitoring.\n\nAPI Monitoring\n\n- Monitor API calls for\
  \ firewall rule modifications."
external_references:
- external_id: DC0051
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0051
id: x-mitre-data-component--d2ff4b56-8351-4ed8-b0fb-d8605366005f
modified: '2025-10-21T15:14:37.073Z'
name: Firewall Rule Modification
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: Firewall Rule Modification
  name: WinEventLog:Security
- channel: Config Change
  name: Firewall Audit Logs
- channel: vSphere API calls modifying firewall settings
  name: esxi:hostd
- channel: firewall disable commands or suspicious ACL modifications
  name: networkdevice:cli
- channel: AuthorizeSecurityGroupIngress
  name: AWS:CloudTrail
- channel: new rule allowing inbound or outbound connections for remote desktop software
  name: WinEventLog:Microsoft-Windows-Windows Firewall With Advanced Security/Firewall
- channel: 'update_rule: Access control or NAT rule modified or disabled outside maintenance window'
  name: networkdevice:Firewall
- channel: iptables or nftables rule changes
  name: linux:syslog
- channel: Outbound NAT Rule Changes
  name: Firewall Audit Logs
- channel: Create egress rule allowing UDP to port 53, 123, 11211
  name: AWS:CloudTrail
- channel: Ingress rule creation or modification for security group
  name: AWS:CloudTrail
- channel: New security group created with permissive rules
  name: AWS:CloudTrail
- channel: Policy Change / Rule Update
  name: NSM:Firewall
- channel: 'rule_modification: New or modified firewall rules related to wireless interfaces'
  name: NSM:Firewall
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
