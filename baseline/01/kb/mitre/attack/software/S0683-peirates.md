---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0683
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0683-peirates
---

## Description

[[kb/mitre/attack/software/S0683-peirates|Peirates]] is a post-exploitation Kubernetes exploitation framework with a focus on gathering service account tokens for lateral movement and privilege escalation. The tool is written in GoLang and publicly available on GitHub.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1046-network-service-discovery\|T1046]] | Network Service Discovery | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can initiate a port scan against a given IP address.[^1]  |
| [[kb/mitre/attack/techniques/T1078.004-cloud-accounts\|T1078.004]] | Cloud Accounts | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can use stolen service account tokens to perform its operations.[^1]  |
| [[kb/mitre/attack/techniques/T1528-steal-application-access-token\|T1528]] | Steal Application Access Token | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] gathers Kubernetes service account tokens using a variety of techniques.[^1]  |
| [[kb/mitre/attack/techniques/T1530-data-from-cloud-storage\|T1530]] | Data from Cloud Storage | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can dump the contents of AWS S3 buckets. It can also retrieve service account tokens from kOps buckets in Google Cloud Storage or S3.[^1]  |
| [[kb/mitre/attack/techniques/T1550.001-application-access-token\|T1550.001]] | Application Access Token | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can use stolen service account tokens to perform its operations. It also enables adversaries to switch between valid service accounts.[^1]  |
| [[kb/mitre/attack/techniques/T1552.005-cloud-instance-metadata-api\|T1552.005]] | Cloud Instance Metadata API | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can query the query AWS and GCP metadata APIs for secrets.[^1]  |
| [[kb/mitre/attack/techniques/T1552.007-container-api\|T1552.007]] | Container API | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can query the Kubernetes API for secrets.[^1]  |
| [[kb/mitre/attack/techniques/T1609-container-administration-command\|T1609]] | Container Administration Command | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can use `kubectl` or the Kubernetes API to run commands.[^1]  |
| [[kb/mitre/attack/techniques/T1610-deploy-container\|T1610]] | Deploy Container | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can deploy a pod that mounts its node’s root file system, then execute a command to create a reverse shell on the node.[^1]  |
| [[kb/mitre/attack/techniques/T1611-escape-to-host\|T1611]] | Escape to Host | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can gain a reverse shell on a host node by mounting the Kubernetes hostPath.[^1]  |
| [[kb/mitre/attack/techniques/T1613-container-and-resource-discovery\|T1613]] | Container and Resource Discovery | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can enumerate Kubernetes pods in a given namespace.[^1]  |
| [[kb/mitre/attack/techniques/T1619-cloud-storage-object-discovery\|T1619]] | Cloud Storage Object Discovery | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can list AWS S3 buckets.[^1]  |

 [^1]: [Peirates GitHub](https://github.com/inguardians/peirates)
