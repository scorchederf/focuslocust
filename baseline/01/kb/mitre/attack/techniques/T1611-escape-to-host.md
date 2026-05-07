---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1611
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/privilege_escalation
    - attack/type/technique
    - platform/containers
    - platform/esxi
    - platform/linux
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1611-escape-to-host
tactic:
    - Privilege Escalation
platforms:
    - Windows
    - Linux
    - Containers
    - ESXi
permissions required:
    - none
---

## Description

Adversaries may break out of a container or virtualized environment to gain access to the underlying host. This can allow an adversary access to other containerized or virtualized resources from the host level or to the host itself. In principle, containerized / virtualized resources should provide a clear separation of application functionality and be isolated from the host environment.[^4] <br><br>There are multiple ways an adversary may escape from a container to a host environment. Examples include creating a container configured to mount the host’s filesystem using the bind parameter, which allows the adversary to drop payloads and execute control utilities such as cron on the host; utilizing a privileged container to run commands or load a malicious kernel module on the underlying host; or abusing system calls such as `unshare` and `keyctl` to escalate privileges and steal secrets.[^5] [^6] [^7] [^1] [^8] [^9] <br><br>Additionally, an adversary may be able to exploit a compromised container with a mounted container management socket, such as `docker.sock`, to break out of the container via a [[kb/mitre/attack/techniques/T1609-container-administration-command|Container Administration Command]].[^1]  Adversaries may also escape via [[kb/mitre/attack/techniques/T1068-exploitation-for-privilege-escalation|Exploitation for Privilege Escalation]], such as exploiting vulnerabilities in global symbolic links in order to access the root directory of a host machine.[^3] <br><br>In ESXi environments, an adversary may exploit a vulnerability in order to escape from a virtual machine into the hypervisor.[^2] <br><br>Gaining access to the host may provide the adversary with the opportunity to achieve follow-on objectives, such as establishing persistence, moving laterally within the environment, accessing other containers or virtual machines running on the host, or setting up a command and control channel on the host.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0600](https://attack.mitre.org/software/S0600) | Doki | Doki’s container was configured to bind the host root directory.[^1]  |
| [S0601](https://attack.mitre.org/software/S0601) | Hildegard | Hildegard has used the BOtB tool that can break out of containers. [^1]   |
| [S0623](https://attack.mitre.org/software/S0623) | Siloscape | Siloscape maps the host’s C drive to the container by creating a global symbolic link to the host through the calling of `NtSetInformationSymbolicLink`.[^1]  |
| [[kb/mitre/attack/software/S0683-peirates\|S0683]] | Peirates | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can gain a reverse shell on a host node by mounting the Kubernetes hostPath.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Ensure containers are not running as root by default and do not use unnecessary privileges or mounted components. In Kubernetes environments, consider defining Pod Security Standards that prevent pods from running privileged containers.[^1]  |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Use read-only containers, read-only file systems, and minimal images when possible to prevent the running of commands.[^2]  Where possible, also consider using application control and software restriction tools (such as those provided by SELinux) to restrict access to files, processes, and system calls in containers.[^1]  |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Remove unnecessary tools and software from containers. |
| [[kb/mitre/attack/mitigations/M1048-application-isolation-and-sandboxing\|M1048]] | Application Isolation and Sandboxing | Consider utilizing seccomp, seccomp-bpf, or a similar solution that restricts certain system calls such as mount. In Kubernetes environments, consider defining Pod Security Standards that limit container access to host process namespaces, the host network, and the host file system.[^1]  |
| [[kb/mitre/attack/mitigations/M1051-update-software\|M1051]] | Update Software | Ensure that hosts are kept up-to-date with security patches.  |

 [^1]: [Container Escape](https://0xn3va.gitbook.io/cheat-sheets/container/escaping)
 [^2]: [Broadcom VMSA-2025-004](https://github.com/vmware/vcf-security-and-compliance-guidelines/tree/main/security-advisories/vmsa-2025-0004)
 [^3]: [Windows Server Containers Are Open](https://unit42.paloaltonetworks.com/windows-server-containers-vulnerabilities/)
 [^4]: [Docker Overview](https://docs.docker.com/get-started/overview/)
 [^5]: [Docker Bind Mounts](https://docs.docker.com/storage/bind-mounts/)
 [^6]: [Trend Micro Privileged Container](https://www.trendmicro.com/en_us/research/19/l/why-running-a-privileged-container-in-docker-is-a-bad-idea.html)
 [^7]: [Intezer Doki July 20](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
 [^8]: [Crowdstrike Kubernetes Container Escape](https://www.crowdstrike.com/blog/cve-2022-0185-kubernetes-container-escape-using-linux-kernel-exploit/)
 [^9]: [Keyctl-unmask](https://www.antitree.com/2020/07/keyctl-unmask-going-florida-on-the-state-of-containerizing-linux-keyrings/)
 [^10]: [Peirates GitHub](https://github.com/inguardians/peirates)
 [^11]: [Kubernetes Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
 [^12]: [Kubernetes Hardening Guide](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)
 [^13]: [Unit 42 Siloscape Jun 2021](https://unit42.paloaltonetworks.com/siloscape/)
 [^14]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
