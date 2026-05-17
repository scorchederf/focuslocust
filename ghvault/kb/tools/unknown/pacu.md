---
parsed_by: focuslocust
source: mitre
type: generated
---
# Pacu

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S1091` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Pacu is an open-source AWS exploitation framework. The tool is written in Python and publicly available on GitHub.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/pacu.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1049 - System Network Connections Discovery](../../attack/techniques/T1049-system-network-connections-discovery.md) | explicit | source | Once inside a Virtual Private Cloud, [Pacu](https://attack.mitre.org/software/S1091) can attempt to identify DirectConnect, VPN, or VPC Peering.(Citation: GitHub Pacu) |
| [T1059.009 - Cloud API](../../attack/techniques/T1059.009-cloud-api.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) leverages the AWS CLI for its operations.(Citation: GitHub Pacu) |
| [T1069.003 - Cloud Groups](../../attack/techniques/T1069.003-cloud-groups.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can enumerate IAM permissions.(Citation: GitHub Pacu) |
| [T1078.004 - Cloud Accounts](../../attack/techniques/T1078.004-cloud-accounts.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) leverages valid cloud accounts to perform most of its operations.(Citation: GitHub Pacu) |
| [T1087.004 - Cloud Account](../../attack/techniques/T1087.004-cloud-account.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can enumerate IAM users, roles, and groups. (Citation: GitHub Pacu) |
| [T1098.001 - Additional Cloud Credentials](../../attack/techniques/T1098.001-additional-cloud-credentials.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can generate SSH and API keys for AWS infrastructure and additional API keys for other IAM users.(Citation: GitHub Pacu) |
| [T1119 - Automated Collection](../../attack/techniques/T1119-automated-collection.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can automatically collect data, such as CloudFormation templates, EC2 user data, AWS Inspector reports, and IAM credential reports.(Citation: GitHub Pacu) |
| [T1518.001 - Security Software Discovery](../../attack/techniques/T1518.001-security-software-discovery.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can enumerate AWS security services, including WAF rules and GuardDuty detectors.(Citation: GitHub Pacu) |
| [T1526 - Cloud Service Discovery](../../attack/techniques/T1526-cloud-service-discovery.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can enumerate AWS services, such as CloudTrail and CloudWatch.(Citation: GitHub Pacu) |
| [T1530 - Data from Cloud Storage](../../attack/techniques/T1530-data-from-cloud-storage.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can enumerate and download files stored in AWS storage services, such as S3 buckets.(Citation: GitHub Pacu) |
| [T1546 - Event Triggered Execution](../../attack/techniques/T1546-event-triggered-execution.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can set up S3 bucket notifications to trigger a malicious Lambda function when a CloudFormation template is uploaded to the bucket. It can also create Lambda functions that trigger upon the creation of users, roles, and groups.(Citation: GitHub Pacu) |
| [T1552 - Unsecured Credentials](../../attack/techniques/T1552-unsecured-credentials.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can search for sensitive data: for example, in Code Build environment variables, EC2 user data, and Cloud Formation templates.(Citation: GitHub Pacu) |
| [T1555.006 - Cloud Secrets Management Stores](../../attack/techniques/T1555.006-cloud-secrets-management-stores.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can retrieve secrets from the AWS Secrets Manager via the enum_secrets module.(Citation: GitHub Pacu) |
| [T1578.001 - Create Snapshot](../../attack/techniques/T1578.001-create-snapshot.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can create snapshots of EBS volumes and RDS instances.(Citation: GitHub Pacu) |
| [T1580 - Cloud Infrastructure Discovery](../../attack/techniques/T1580-cloud-infrastructure-discovery.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can enumerate AWS infrastructure, such as EC2 instances.(Citation: GitHub Pacu) |
| [T1619 - Cloud Storage Object Discovery](../../attack/techniques/T1619-cloud-storage-object-discovery.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can enumerate AWS storage services, such as S3 buckets and Elastic Block Store volumes.(Citation: GitHub Pacu) |
| [T1648 - Serverless Execution](../../attack/techniques/T1648-serverless-execution.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can create malicious Lambda functions.(Citation: GitHub Pacu) |
| [T1651 - Cloud Administration Command](../../attack/techniques/T1651-cloud-administration-command.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can run commands on EC2 instances using AWS Systems Manager Run Command.(Citation: GitHub Pacu) |
| [T1654 - Log Enumeration](../../attack/techniques/T1654-log-enumeration.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can collect CloudTrail event histories and CloudWatch logs.(Citation: GitHub Pacu) |
| [T1685.002 - Disable or Modify Cloud Log](../../attack/techniques/T1685.002-disable-or-modify-cloud-log.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can disable or otherwise restrict various AWS logging services, such as AWS CloudTrail and VPC flow logs.(Citation: GitHub Pacu) |
| [T1686.001 - Cloud Firewall](../../attack/techniques/T1686.001-cloud-firewall.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can allowlist IP addresses in AWS GuardDuty.(Citation: GitHub Pacu) |

## Source Verification

[source record](../../sources/mitre/pacu.md)

## Evidence Excerpt

```text
created: '2023-09-28T13:21:49.652Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Pacu is an open-source AWS exploitation framework. The tool is written in Python and publicly available on GitHub.(Citation:
GitHub Pacu)'
external_references:
- external_id: S1091
source_name: mitre-attack
url: https://attack.mitre.org/software/S1091
```
