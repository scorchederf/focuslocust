---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S1091
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S1091-pacu
---

## Description

Pacu is an open-source AWS exploitation framework. The tool is written in Python and publicly available on GitHub.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1049-system-network-connections-discovery\|T1049]] | System Network Connections Discovery | Once inside a Virtual Private Cloud, [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can attempt to identify DirectConnect, VPN, or VPC Peering.[^1]  |
| [[kb/mitre/attack/techniques/T1059.009-cloud-api\|T1059.009]] | Cloud API | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] leverages the AWS CLI for its operations.[^1]  |
| [[kb/mitre/attack/techniques/T1069.003-cloud-groups\|T1069.003]] | Cloud Groups | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can enumerate IAM permissions.[^1]  |
| [[kb/mitre/attack/techniques/T1078.004-cloud-accounts\|T1078.004]] | Cloud Accounts | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] leverages valid cloud accounts to perform most of its operations.[^1]  |
| [[kb/mitre/attack/techniques/T1087.004-cloud-account\|T1087.004]] | Cloud Account | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can enumerate IAM users, roles, and groups. [^1]  |
| [[kb/mitre/attack/techniques/T1098.001-additional-cloud-credentials\|T1098.001]] | Additional Cloud Credentials | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can generate SSH and API keys for AWS infrastructure and additional API keys for other IAM users.[^1]  |
| [[kb/mitre/attack/techniques/T1119-automated-collection\|T1119]] | Automated Collection | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can automatically collect data, such as CloudFormation templates, EC2 user data, AWS Inspector reports, and IAM credential reports.[^1]  |
| [[kb/mitre/attack/techniques/T1518.001-security-software-discovery\|T1518.001]] | Security Software Discovery | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can enumerate AWS security services, including WAF rules and GuardDuty detectors.[^1]  |
| [[kb/mitre/attack/techniques/T1526-cloud-service-discovery\|T1526]] | Cloud Service Discovery | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can enumerate AWS services, such as CloudTrail and CloudWatch.[^1]  |
| [[kb/mitre/attack/techniques/T1530-data-from-cloud-storage\|T1530]] | Data from Cloud Storage | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can enumerate and download files stored in AWS storage services, such as S3 buckets.[^1]  |
| [[kb/mitre/attack/techniques/T1546-event-triggered-execution\|T1546]] | Event Triggered Execution | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can set up S3 bucket notifications to trigger a malicious Lambda function when a CloudFormation template is uploaded to the bucket. It can also create Lambda functions that trigger upon the creation of users, roles, and groups.[^1]  |
| [[kb/mitre/attack/techniques/T1552-unsecured-credentials\|T1552]] | Unsecured Credentials | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can search for sensitive data: for example, in Code Build environment variables, EC2 user data, and Cloud Formation templates.[^1]  |
| [[kb/mitre/attack/techniques/T1555.006-cloud-secrets-management-stores\|T1555.006]] | Cloud Secrets Management Stores | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can retrieve secrets from the AWS Secrets Manager via the enum_secrets module.[^1]  |
| [[kb/mitre/attack/techniques/T1578.001-create-snapshot\|T1578.001]] | Create Snapshot | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can create snapshots of EBS volumes and RDS instances.[^1]  |
| [[kb/mitre/attack/techniques/T1580-cloud-infrastructure-discovery\|T1580]] | Cloud Infrastructure Discovery | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can enumerate AWS infrastructure, such as EC2 instances.[^1]  |
| [[kb/mitre/attack/techniques/T1619-cloud-storage-object-discovery\|T1619]] | Cloud Storage Object Discovery | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can enumerate AWS storage services, such as S3 buckets and Elastic Block Store volumes.[^1]  |
| [[kb/mitre/attack/techniques/T1648-serverless-execution\|T1648]] | Serverless Execution | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can create malicious Lambda functions.[^1]  |
| [[kb/mitre/attack/techniques/T1651-cloud-administration-command\|T1651]] | Cloud Administration Command | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can run commands on EC2 instances using AWS Systems Manager Run Command.[^1]  |
| [[kb/mitre/attack/techniques/T1654-log-enumeration\|T1654]] | Log Enumeration | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can collect CloudTrail event histories and CloudWatch logs.[^1]  |
| [[kb/mitre/attack/techniques/T1685.002-disable-or-modify-cloud-log\|T1685.002]] | Disable or Modify Cloud Log | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can disable or otherwise restrict various AWS logging services, such as AWS CloudTrail and VPC flow logs.[^1]  |
| [[kb/mitre/attack/techniques/T1686.001-cloud-firewall\|T1686.001]] | Cloud Firewall | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can allowlist IP addresses in AWS GuardDuty.[^1]  |

 [^1]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)
