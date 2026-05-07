---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1612
tags:
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/containers
mitre-attack: kb/mitre/attack/techniques/T1612-build-image-on-host
tactic:
    - Stealth
platforms:
    - Containers
permissions required:
    - none
---

## Description

Adversaries may build a container image directly on a host to bypass defenses that monitor for the retrieval of malicious images from a public registry. A remote `build` request may be sent to the Docker API that includes a Dockerfile that pulls a vanilla base image, such as alpine, from a public or local registry and then builds a custom image upon it.[^2] <br><br>An adversary may take advantage of that `build` API to build a custom image on the host that includes malware downloaded from their C2 server, and then they may utilize [[kb/mitre/attack/techniques/T1610-deploy-container|Deploy Container]] using that custom image.[^1] [^3]  If the base image is pulled from a public registry, defenses will likely not detect the image as malicious since it’s a vanilla image. If the base image already resides in a local registry, the pull may be considered even less suspicious since the image is already in the environment. 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Ensure containers are not running as root by default. In Kubernetes environments, consider defining Pod Security Standards that prevent pods from running privileged containers.[^1]  |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Deny direct remote access to internal systems through the use of network proxies, gateways, and firewalls. |
| [[kb/mitre/attack/mitigations/M1035-limit-access-to-resource-over-network\|M1035]] | Limit Access to Resource Over Network | Limit communications with the container service to local Unix sockets or remote access via SSH. Require secure port access to communicate with the APIs over TLS by disabling unauthenticated access to the Docker API on port 2375. Instead, communicate with the Docker API over TLS on port 2376.[^1]  |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Audit images deployed within the environment to ensure they do not contain any malicious components. |

 [^1]: [Aqua Build Images on Hosts](https://blog.aquasec.com/malicious-container-image-docker-container-host)
 [^2]: [Docker Build Image](https://docs.docker.com/engine/api/v1.41/#operation/ImageBuild)
 [^3]: [Aqua Security Cloud Native Threat Report June 2021](https://info.aquasec.com/hubfs/Threat%20reports/AquaSecurity_Cloud_Native_Threat_Report_2021.pdf?utm_campaign=WP%20-%20Jun2021%20Nautilus%202021%20Threat%20Research%20Report&utm_medium=email&_hsmi=132931006&_hsenc=p2ANqtz-_8oopT5Uhqab8B7kE0l3iFo1koirxtyfTehxF7N-EdGYrwk30gfiwp5SiNlW3G0TNKZxUcDkYOtwQ9S6nNVNyEO-Dgrw&utm_content=132931006&utm_source=hs_automation)
 [^4]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)
 [^5]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)
