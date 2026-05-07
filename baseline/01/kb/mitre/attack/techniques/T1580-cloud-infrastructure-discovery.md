---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1580
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/iaas
mitre-attack: kb/mitre/attack/techniques/T1580-cloud-infrastructure-discovery
tactic:
    - Discovery
platforms:
    - IaaS
permissions required:
    - none
---

## Description

An adversary may attempt to discover infrastructure and resources that are available within an infrastructure-as-a-service (IaaS) environment. This includes compute service resources such as instances, virtual machines, and snapshots as well as resources of other services including the storage and database services.<br><br>Cloud providers offer methods such as APIs and commands issued through CLIs to serve information about infrastructure. For example, AWS provides a `DescribeInstances` API within the Amazon EC2 API that can return information about one or more instances within an account, the `ListBuckets` API that returns a list of all buckets owned by the authenticated sender of the request, the `HeadBucket` API to determine a bucket’s existence along with access permissions of the request sender, or the `GetPublicAccessBlock` API to retrieve access block configuration for a bucket.[^5] [^6] [^3] [^2]  Similarly, GCP's Cloud SDK CLI provides the `gcloud compute instances list` command to list all Google Compute Engine instances in a project [^7] , and Azure's CLI command `az vm list` lists details of virtual machines.[^9]  In addition to API commands, adversaries can utilize open source tools to discover cloud storage infrastructure through [[kb/mitre/attack/techniques/T1595.003-wordlist-scanning|Wordlist Scanning]].[^10] <br><br>An adversary may enumerate resources using a compromised user's access keys to determine which are available to that user.[^1]  The discovery of these available resources may help adversaries determine their next steps in the Cloud environment, such as establishing Persistence.[^8] An adversary may also use this information to change the configuration to make the bucket publicly accessible, allowing data to be accessed without authentication. Adversaries have also may use infrastructure discovery APIs such as `DescribeDBInstances` to determine size, owner, permissions, and network ACLs of database resources. [^4]  Adversaries can use this information to determine the potential value of databases and discover the requirements to access them. Unlike in [[kb/mitre/attack/techniques/T1526-cloud-service-discovery|Cloud Service Discovery]], this technique focuses on the discovery of components of the provided services rather than the services themselves.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S1091-pacu\|S1091]] | Pacu | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can enumerate AWS infrastructure, such as EC2 instances.[^1]  |
| [[kb/mitre/attack/software/S9009-trufflehog\|S9009]] | TruffleHog | [[kb/mitre/attack/software/S9009-trufflehog\|TruffleHog]] can enumerate AWS Infrastructure to include EC2 instances.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Limit permissions to discover cloud infrastructure in accordance with least privilege. Organizations should limit the number of users within the organization with an IAM role that has administrative privileges, strive to reduce all permanent privileged role assignments, and conduct periodic entitlement reviews on IAM users, roles and policies. |

 [^1]: [Expel IO Evil in AWS](https://expel.io/blog/finding-evil-in-aws/)
 [^2]: [AWS Head Bucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html)
 [^3]: [AWS Get Public Access Block](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html)
 [^4]: [AWS Describe DB Instances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html)
 [^5]: [Amazon Describe Instance](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-instance-information.html)
 [^6]: [Amazon Describe Instances API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html)
 [^7]: [Google Compute Instances](https://cloud.google.com/sdk/gcloud/reference/compute/instances/list)
 [^8]: [Mandiant M-Trends 2020](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)
 [^9]: [Microsoft AZ CLI](https://docs.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest)
 [^10]: [Malwarebytes OSINT Leaky Buckets - Hioureas](https://blog.malwarebytes.com/researchers-corner/2019/09/hacking-with-aws-incorporating-leaky-buckets-osint-workflow/)
 [^11]: [Github TruffleSecurity Trufflehog April 2025](https://github.com/trufflesecurity/trufflehog)
 [^12]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)
