---
generated_by: focuslocust
source: mitre
type: mitigation
aliases:
    - M1039
tags:
    - attack/domain/enterprise_attack
    - attack/type/mitigation
mitre-attack: kb/mitre/attack/mitigations/M1039-environment-variable-permissions
---

## Description

Restrict the modification of environment variables to authorized users and processes by enforcing strict permissions and policies. This ensures the integrity of environment variables, preventing adversaries from abusing or altering them for malicious purposes. This mitigation can be implemented through the following measures:<br><br>Restrict Write Access:<br><br>- Use Case: Set file system-level permissions to restrict access to environment variable configuration files (e.g., `.bashrc`, `.bash_profile`, `.zshrc`, `systemd` service files).<br>- Implementation: Configure `/etc/environment` or `/etc/profile` on Linux systems to only allow root or administrators to modify the file.<br><br>Secure Access Controls:<br><br>- Use Case: Limit access to environment variable settings in application deployment tools or CI/CD pipelines to authorized personnel.<br>- Implementation: Use role-based access control (RBAC) in tools like Jenkins or GitLab to ensure only specific users can modify environment variables.<br><br>Restrict Process Scope:<br><br>- Use Case: Configure policies to ensure environment variables are only accessible to the processes they are explicitly intended for.<br>- Implementation: Use containerized environments like Docker to isolate environment variables to specific containers and ensure they are not inherited by other processes.<br><br>Audit Environment Variable Changes:<br><br>- Use Case: Enable logging for changes to critical environment variables.<br>- Implementation: Use `auditd` on Linux to monitor changes to files like `/etc/environment` or application-specific environment files.

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1070.003-clear-command-history\|T1070.003]] | Clear Command History | Making the environment variables associated with command history read only may ensure that the history is preserved.[^1]  |
| [[kb/mitre/attack/techniques/T1690-prevent-command-history-logging\|T1690]] | Prevent Command History Logging | Prevent users from changing the `HISTCONTROL`, `HISTFILE`, and `HISTFILESIZE` environment variables. [^1]  |

 [^1]: [Securing bash history](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)
