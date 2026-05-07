---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1525
tags:
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/persistence
    - attack/type/technique
    - platform/containers
    - platform/iaas
mitre-attack: kb/mitre/attack/techniques/T1525-implant-internal-image
tactic:
    - Persistence
platforms:
    - IaaS
    - Containers
permissions required:
    - none
---

## Description

Adversaries may implant cloud or container images with malicious code to establish persistence after gaining access to an environment. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and Azure Images as well as popular container runtimes such as Docker can be implanted or backdoored. Unlike [[kb/mitre/attack/techniques/T1608.001-upload-malware|Upload Malware]], this technique focuses on adversaries implanting an image in a registry within a victim’s environment. Depending on how the infrastructure is provisioned, this could provide persistent access if the infrastructure provisioning tool is instructed to always use the latest image.[^1] <br><br>A tool has been developed to facilitate planting backdoors in cloud container images.[^2]  If an adversary has access to a compromised AWS instance, and permissions to list the available container images, they may implant a backdoor such as a [[kb/mitre/attack/techniques/T1505.003-web-shell|Web Shell]].[^1] 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Limit permissions associated with creating and modifying platform images or containers based on the principle of least privilege. |
| [[kb/mitre/attack/mitigations/M1045-code-signing\|M1045]] | Code Signing | Several cloud service providers support content trust models that require container images be signed by trusted sources.[^1] [^2]  |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Periodically check the integrity of images and containers used in cloud deployments to ensure they have not been modified to include malicious software. |

 [^1]: [Rhino Labs Cloud Image Backdoor Technique Sept 2019](https://rhinosecuritylabs.com/aws/cloud-container-attack-tool/)
 [^2]: [Rhino Labs Cloud Backdoor September 2019](https://github.com/RhinoSecurityLabs/ccat)
 [^3]: [Content trust in Azure Container Registry](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-content-trust)
 [^4]: [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)
