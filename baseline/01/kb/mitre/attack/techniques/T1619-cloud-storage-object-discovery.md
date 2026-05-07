---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1619
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/iaas
mitre-attack: kb/mitre/attack/techniques/T1619-cloud-storage-object-discovery
tactic:
    - Discovery
platforms:
    - IaaS
permissions required:
    - none
---

## Description

Adversaries may enumerate objects in cloud storage infrastructure. Adversaries may use this information during automated discovery to shape follow-on behaviors, including requesting all or specific objects from cloud storage.  Similar to [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery|File and Directory Discovery]] on a local host, after identifying available storage services (i.e. [[kb/mitre/attack/techniques/T1580-cloud-infrastructure-discovery|Cloud Infrastructure Discovery]]) adversaries may access the contents/objects stored in cloud infrastructure.<br><br>Cloud service providers offer APIs allowing users to enumerate objects stored within cloud storage. Examples include ListObjectsV2 in AWS [^1]  and List Blobs in Azure[^2]  .

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0683-peirates\|S0683]] | Peirates | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can list AWS S3 buckets.[^1]  |
| [[kb/mitre/attack/software/S1091-pacu\|S1091]] | Pacu | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can enumerate AWS storage services, such as S3 buckets and Elastic Block Store volumes.[^1]  |
| [[kb/mitre/attack/software/S9009-trufflehog\|S9009]] | TruffleHog | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] can enumerate cloud storage environments including Amazon Web Service (AWS) S3 buckets and Google Cloud Storage buckets.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Restrict granting of permissions related to listing objects in cloud storage to necessary accounts. |

 [^1]: [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)
 [^2]: [List Blobs](https://docs.microsoft.com/en-us/rest/api/storageservices/list-blobs)
 [^3]: [Black Hills Information Security TruffleHog January 2024](https://www.blackhillsinfosec.com/rooting-for-secrets-with-trufflehog/)
 [^4]: [Github TruffleSecurity Trufflehog April 2025](https://github.com/trufflesecurity/trufflehog)
 [^5]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)
 [^6]: [Peirates GitHub](https://github.com/inguardians/peirates)
