---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1609
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/containers
mitre-attack: kb/mitre/attack/techniques/T1609-container-administration-command
tactic:
    - Execution
platforms:
    - Containers
permissions required:
    - none
---

## Description

Adversaries may abuse a container administration service to execute commands within a container. A container administration service such as the Docker daemon, the Kubernetes API server, or the kubelet may allow remote management of containers within an environment.[^3] [^6] [^5] <br><br>In Docker, adversaries may specify an entrypoint during container deployment that executes a script or command, or they may use a command such as `docker exec` to execute a command within a running container.[^2] [^1]  In Kubernetes, if an adversary has sufficient permissions, they may gain remote execution in a container in the cluster via interaction with the Kubernetes API server, the kubelet, or by running a command such as `kubectl exec`.[^4] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0599](https://attack.mitre.org/software/S0599) | Kinsing | Kinsing was executed with an Ubuntu container entry point that runs shell scripts.[^1]  |
| [S0601](https://attack.mitre.org/software/S0601) | Hildegard | Hildegard was executed through the kubelet API run command and by executing commands on running containers.[^1]  |
| [S0623](https://attack.mitre.org/software/S0623) | Siloscape | Siloscape can send kubectl commands to victim clusters through an IRC channel and can run kubectl locally to spread once within a victim cluster.[^1]  |
| [[kb/mitre/attack/software/S0683-peirates\|S0683]] | Peirates | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can use `kubectl` or the Kubernetes API to run commands.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Enforce authentication and role-based access control on the container service to restrict users to the least privileges required.[^2]  When using Kubernetes, avoid giving users wildcard permissions or adding users to the `system:masters` group, and use `RoleBindings` rather than `ClusterRoleBindings` to limit user privileges to specific namespaces.[^1]  |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Ensure containers are not running as root by default. In Kubernetes environments, consider defining Pod Security Standards that prevent pods from running privileged containers and using the `NodeRestriction` admission controller to deny the kublet access to nodes and pods outside of the node it belongs to.[^2]  [^1]  |
| [[kb/mitre/attack/mitigations/M1035-limit-access-to-resource-over-network\|M1035]] | Limit Access to Resource Over Network | Limit communications with the container service to managed and secured channels, such as local Unix sockets or remote access via SSH. Require secure port access to communicate with the APIs over TLS by disabling unauthenticated access to the Docker API and Kubernetes API Server.[^1] [^4]  In Kubernetes clusters deployed in cloud environments, use native cloud platform features to restrict the IP ranges that are permitted to access to API server.[^2]  Where possible, consider enabling just-in-time (JIT) access to the Kubernetes API to place additional restrictions on access.[^3]  |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Use read-only containers, read-only file systems, and minimal images when possible to prevent the execution of commands.[^2]  Where possible, also consider using application control and software restriction tools (such as those provided by SELinux) to restrict access to files, processes, and system calls in containers.[^1]  |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Remove unnecessary tools and software from containers. |

 [^1]: [Docker Exec](https://docs.docker.com/engine/reference/commandline/exec/)
 [^2]: [Docker Entrypoint](https://docs.docker.com/engine/reference/run/#entrypoint-default-command-to-execute-at-runtime)
 [^3]: [Docker Daemon CLI](https://docs.docker.com/engine/reference/commandline/dockerd/)
 [^4]: [Kubectl Exec Get Shell](https://kubernetes.io/docs/tasks/debug-application-cluster/get-shell-running-container/)
 [^5]: [Kubernetes Kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)
 [^6]: [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)
 [^7]: [Peirates GitHub](https://github.com/inguardians/peirates)
 [^8]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
 [^9]: [Kubernetes RBAC](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)
 [^10]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)
 [^11]: [Kubernetes Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers)
 [^12]: [Unit 42 Siloscape Jun 2021](https://unit42.paloaltonetworks.com/siloscape/)
 [^13]: [Aqua Kinsing April 2020](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)
 [^14]: [Docker Daemon Socket Protect](https://docs.docker.com/engine/security/protect-access/)
 [^15]: [Kubernetes Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/)
 [^16]: [Microsoft AKS Azure AD 2023](https://learn.microsoft.com/en-us/azure/aks/managed-aad)
 [^17]: [Kubernetes API Control Access](https://kubernetes.io/docs/concepts/security/controlling-access/)
 [^18]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
