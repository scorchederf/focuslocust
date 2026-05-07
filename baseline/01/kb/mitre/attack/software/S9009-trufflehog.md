---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S9009
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S9009-trufflehog
---

## Description

[[kb/mitre/attack/software/S9009-trufflehog|TruffleHog]] is an open-source secrets-discovery tool that is used to search for credentials, API keys, and encryption keys across a variety of data sources and environments.[^1] [^3]  [[kb/mitre/attack/software/S9009-trufflehog|TruffleHog]] has the ability to discover credentials and secrets stored in code repositories, git history, CI/CD pipelines, among other common storage locations to include filesystems and cloud storage buckets.[^1] [^2] [^3]  [[kb/mitre/attack/software/S9009-trufflehog|TruffleHog]] was first released by its author in 2016.[^3] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1005-data-from-local-system\|T1005]] | Data from Local System | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has gathered data from home directories of the victim environment.[^1]  |
| [[kb/mitre/attack/techniques/T1059.009-cloud-api\|T1059.009]] | Cloud API | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has leveraged Cloud CLI in order to enumerate and gather credentials.[^1]  |
| [[kb/mitre/attack/techniques/T1078.004-cloud-accounts\|T1078.004]] | Cloud Accounts | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has used stolen credentials to log into cloud services to access cloud hosted repositories and other cloud storage solutions to discover sensitive data to include API Keys, tokens and credentials.[^1]  |
| [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has can browse and scan individual files and directories.[^1] [^2] [^3]  |
| [[kb/mitre/attack/techniques/T1213.001-confluence\|T1213.001]] | Confluence | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has collected credentials and data associated with Confluence.[^1]  |
| [[kb/mitre/attack/techniques/T1213.002-sharepoint\|T1213.002]] | Sharepoint | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has searched SharePoint for data and credentials.[^1]  |
| [[kb/mitre/attack/techniques/T1213.003-code-repositories\|T1213.003]] | Code Repositories | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has gathered data and credentials from code repositories.[^1]  |
| [[kb/mitre/attack/techniques/T1213.005-messaging-applications\|T1213.005]] | Messaging Applications | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has obtained data and credentials associated with messaging applications to include Slack.[^1]  |
| [[kb/mitre/attack/techniques/T1526-cloud-service-discovery\|T1526]] | Cloud Service Discovery | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has the ability to scan code repositories and CI/CD platforms.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1528-steal-application-access-token\|T1528]] | Steal Application Access Token | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has gathered access tokens and API tokens from CI/CD pipeline solutions and repositories.[^1]  |
| [[kb/mitre/attack/techniques/T1530-data-from-cloud-storage\|T1530]] | Data from Cloud Storage | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has the ability to scan cloud storage services for credentials to include Amazon (AWS) S3 and Google Cloud Storage.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1552.001-credentials-in-files\|T1552.001]] | Credentials In Files | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has obtained credentials stored in config files and credential files in victim environments.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1552.005-cloud-instance-metadata-api\|T1552.005]] | Cloud Instance Metadata API | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] can query the AWS and GCP metadata endpoints for instances and service credentials.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1555.006-cloud-secrets-management-stores\|T1555.006]] | Cloud Secrets Management Stores | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] can obtain secrets from AWS Secrets and GCP Secret Manager.[^1] [^3]  [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has also gathered passwords, secrets and API keys from source repositories, .env files, and git history.[^2]  |
| [[kb/mitre/attack/techniques/T1580-cloud-infrastructure-discovery\|T1580]] | Cloud Infrastructure Discovery | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] can enumerate AWS Infrastructure to include EC2 instances.[^1]  |
| [[kb/mitre/attack/techniques/T1619-cloud-storage-object-discovery\|T1619]] | Cloud Storage Object Discovery | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] can enumerate cloud storage environments including Amazon Web Service (AWS) S3 buckets and Google Cloud Storage buckets.[^1] [^2]  |

 [^1]: [Black Hills Information Security TruffleHog January 2024](https://www.blackhillsinfosec.com/rooting-for-secrets-with-trufflehog/)
 [^2]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
 [^3]: [Github TruffleSecurity Trufflehog April 2025](https://github.com/trufflesecurity/trufflehog)
