---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1651
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/execution
    - attack/type/technique
    - platform/iaas
mitre-attack: kb/mitre/attack/techniques/T1651-cloud-administration-command
tactic:
    - Execution
platforms:
    - IaaS
permissions required:
    - none
---

## Description

Adversaries may abuse cloud management services to execute commands within virtual machines. Resources such as AWS Systems Manager, Azure RunCommand, and Runbooks allow users to remotely run scripts in virtual machines by leveraging installed virtual machine agents. [^1] [^3] <br><br>If an adversary gains administrative access to a cloud environment, they may be able to abuse cloud management services to execute commands in the environment’s virtual machines. Additionally, an adversary that compromises a service provider or delegated administrator account may similarly be able to leverage a [[kb/mitre/attack/techniques/T1199-trusted-relationship|Trusted Relationship]] to execute commands in connected virtual machines.[^2] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0677-aadinternals\|S0677]] | AADInternals | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can execute commands on Azure virtual machines using the VM agent.[^1]  |
| [[kb/mitre/attack/software/S1091-pacu\|S1091]] | Pacu | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can run commands on EC2 instances using AWS Systems Manager Run Command.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Limit the number of cloud accounts with permissions to remotely execute commands on virtual machines, and ensure that these are not used for day-to-day operations. In Azure, limit the number of accounts with the roles Azure Virtual Machine Contributer and above, and consider using temporary Just-in-Time (JIT) roles to avoid permanently assigning privileged access to virtual machines.[^1]   |

 [^1]: [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html)
 [^2]: [MSTIC Nobelium Oct 2021](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks/)
 [^3]: [Microsoft Run Command](https://learn.microsoft.com/en-us/azure/virtual-machines/run-command-overview)
 [^4]: [AADInternals Root Access to Azure VMs](https://aadinternals.com/post/azurevms/)
 [^5]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)
 [^6]: [Mandiant Azure Run Command 2021](https://www.mandiant.com/resources/blog/azure-run-command-dummies)
