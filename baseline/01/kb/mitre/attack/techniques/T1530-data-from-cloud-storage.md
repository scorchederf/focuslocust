---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1530
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/iaas
    - platform/office_suite
    - platform/saas
mitre-attack: kb/mitre/attack/techniques/T1530-data-from-cloud-storage
tactic:
    - Collection
platforms:
    - IaaS
    - Office Suite
    - SaaS
permissions required:
    - none
---

## Description

Adversaries may access data from cloud storage.<br><br>Many IaaS providers offer solutions for online data object storage such as Amazon S3, Azure Storage, and Google Cloud Storage. Similarly, SaaS enterprise platforms such as Office 365 and Google Workspace provide cloud-based document storage to users through services such as OneDrive and Google Drive, while SaaS application providers such as Slack, Confluence, Salesforce, and Dropbox may provide cloud storage solutions as a peripheral or primary use case of their platform. <br><br>In some cases, as with IaaS-based cloud storage, there exists no overarching application (such as SQL or Elasticsearch) with which to interact with the stored objects: instead, data from these solutions is retrieved directly though the [[kb/mitre/attack/techniques/T1059.009-cloud-api|Cloud API]]. In SaaS applications, adversaries may be able to collect this data directly from APIs or backend cloud storage objects, rather than through their front-end application or interface (i.e., [[kb/mitre/attack/techniques/T1213-data-from-information-repositories|Data from Information Repositories]]). <br><br>Adversaries may collect sensitive data from these cloud storage solutions. Providers typically offer security guides to help end users configure systems, though misconfigurations are a common problem.[^1] [^2] [^4]  There have been numerous incidents where cloud storage has been improperly secured, typically by unintentionally allowing public access to unauthenticated users, overly-broad access by all users, or even access for any anonymous person outside the control of the Identity Access Management system without even needing basic user permissions.<br><br>This open access may expose various types of sensitive data, such as credit cards, personally identifiable information, or medical records.[^7] [^3] [^5] [^6] <br><br>Adversaries may also obtain then abuse leaked credentials from source repositories, logs, or other means as a way to gain access to cloud storage objects.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0677-aadinternals\|S0677]] | AADInternals | AADInternals can collect files from a user’s OneDrive.[^1]  |
| [[kb/mitre/attack/software/S0683-peirates\|S0683]] | Peirates | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can dump the contents of AWS S3 buckets. It can also retrieve service account tokens from kOps buckets in Google Cloud Storage or S3.[^1]  |
| [[kb/mitre/attack/software/S1091-pacu\|S1091]] | Pacu | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can enumerate and download files stored in AWS storage services, such as S3 buckets.[^1]  |
| [[kb/mitre/attack/software/S9009-trufflehog\|S9009]] | TruffleHog | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] has the ability to scan cloud storage services for credentials to include Amazon (AWS) S3 and Google Cloud Storage.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Configure user permissions groups and roles for access to cloud storage.[^1]  Implement strict Identity and Access Management (IAM) controls to prevent access to storage solutions except for the applications, users, and services that require access.[^2]  Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary.[^3]  |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | Use access control lists on storage systems and objects. |
| [[kb/mitre/attack/mitigations/M1032-multi-factor-authentication\|M1032]] | Multi-factor Authentication | Consider using multi-factor authentication to restrict access to resources and cloud storage APIs.[^1]  |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | Cloud service providers support IP-based restrictions when accessing cloud resources. Consider using IP allowlisting along with user account management to ensure that data access is restricted not only to valid users but only from expected IP ranges to mitigate the use of stolen credentials to access data. |
| [[kb/mitre/attack/mitigations/M1041-encrypt-sensitive-information\|M1041]] | Encrypt Sensitive Information | Encrypt data stored at rest in cloud storage.[^1] [^2]  Managed encryption keys can be rotated by most providers. At a minimum, ensure an incident response plan to storage breach includes rotating the keys and test for impact on client applications.[^3]  |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources.[^1]  |

 [^1]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)
 [^2]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)
 [^3]: [Wired Magecart S3 Buckets, 2019](https://www.wired.com/story/magecart-amazon-cloud-hacks/)
 [^4]: [Google Cloud Storage Best Practices, 2019](https://cloud.google.com/storage/docs/best-practices)
 [^5]: [HIPAA Journal S3 Breach, 2017](https://www.hipaajournal.com/47gb-medical-records-unsecured-amazon-s3-bucket/)
 [^6]: [Rclone-mega-extortion_05_2021](https://redcanary.com/blog/rclone-mega-extortion/)
 [^7]: [Trend Micro S3 Exposed PII, 2017](https://www.trendmicro.com/vinfo/us/security/news/virtualization-and-cloud/a-misconfigured-amazon-s3-exposed-almost-50-thousand-pii-in-australia)
 [^8]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)
 [^9]: [Peirates GitHub](https://github.com/inguardians/peirates)
 [^10]: [Google Cloud Encryption Key Rotation](https://cloud.google.com/kms/docs/key-rotation)
 [^11]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)
 [^12]: [AADInternals](https://o365blog.com/aadinternals/)
 [^13]: [Black Hills Information Security TruffleHog January 2024](https://www.blackhillsinfosec.com/rooting-for-secrets-with-trufflehog/)
 [^14]: [Github TruffleSecurity Trufflehog April 2025](https://github.com/trufflesecurity/trufflehog)
