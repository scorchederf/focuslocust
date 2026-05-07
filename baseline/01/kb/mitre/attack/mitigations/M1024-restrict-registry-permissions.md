---
parsed_by: focuslocust
source: mitre
type: mitigation
aliases:
    - M1024
tags:
    - attack/domain/enterprise_attack
    - attack/type/mitigation
mitre-attack: kb/mitre/attack/mitigations/M1024-restrict-registry-permissions
---

## Description

Restricting registry permissions involves configuring access control settings for sensitive registry keys and hives to ensure that only authorized users or processes can make modifications. By limiting access, organizations can prevent unauthorized changes that adversaries might use for persistence, privilege escalation, or defense evasion. This mitigation can be implemented through the following measures:<br><br>Review and Adjust Permissions on Critical Keys<br><br>- Regularly review permissions on keys such as `Run`, `RunOnce`, and `Services` to ensure only authorized users have write access.<br>- Use tools like `icacls` or `PowerShell` to automate permission adjustments.<br><br>Enable Registry Auditing<br><br>- Enable auditing on sensitive keys to log access attempts.<br>- Use Event Viewer or SIEM solutions to analyze logs and detect suspicious activity.<br>- Example Audit Policy: `auditpol /set /subcategory:"Registry" /success:enable /failure:enable`<br><br>Protect Credential-Related Hives<br><br>- Limit access to hives like `SAM`,`SECURITY`, and `SYSTEM` to prevent credential dumping or other unauthorized access.<br>- Use LSA Protection to add an additional security layer for credential storage.<br><br>Restrict Registry Editor Usage<br><br>- Use Group Policy to restrict access to regedit.exe for non-administrative users.<br>- Block execution of registry editing tools on endpoints where they are unnecessary.<br><br>Deploy Baseline Configuration Tools<br><br>- Use tools like Microsoft Security Compliance Toolkit or CIS Benchmarks to apply and maintain secure registry configurations.<br><br>*Tools for Implementation* <br><br>Registry Permission Tools:<br><br>- Registry Editor (regedit): Built-in tool to manage registry permissions.<br>- PowerShell: Automate permissions and manage keys. `Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "KeyName" -Value "Value"`<br>- icacls: Command-line tool to modify ACLs.<br><br>Monitoring Tools:<br><br>- Sysmon: Monitor and log registry events.<br>- Event Viewer: View registry access logs.<br><br>Policy Management Tools:<br><br>- Group Policy Management Console (GPMC): Enforce registry permissions via GPOs.<br>- Microsoft Endpoint Manager: Deploy configuration baselines for registry permissions.

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1037-boot-or-logon-initialization-scripts\|T1037]] | Boot or Logon Initialization Scripts | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for logon scripts that may lead to persistence. |
| [[kb/mitre/attack/techniques/T1037.001-logon-script-windows\|T1037.001]] | Logon Script (Windows) | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for logon scripts that may lead to persistence. |
| [[kb/mitre/attack/techniques/T1070.007-clear-network-connection-history-and-configurations\|T1070.007]] | Clear Network Connection History and Configurations | Protect generated event files and logs that are stored locally with proper permissions and authentication and limit opportunities for adversaries to increase privileges by preventing Privilege Escalation opportunities. |
| [[kb/mitre/attack/techniques/T1112-modify-registry\|T1112]] | Modify Registry | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation. |
| [[kb/mitre/attack/techniques/T1489-service-stop\|T1489]] | Service Stop | Ensure proper registry permissions are in place to inhibit adversaries from disabling or interfering with critical services. |
| [[kb/mitre/attack/techniques/T1505-server-software-component\|T1505]] | Server Software Component | Consider using Group Policy to configure and block modifications to service and other critical server parameters in the Registry.[^1]  |
| [[kb/mitre/attack/techniques/T1505.005-terminal-services-dll\|T1505.005]] | Terminal Services DLL | Consider using Group Policy to configure and block modifications to Terminal Services parameters in the Registry.(Citation: Microsoft System Services Fundamentals) |
| [[kb/mitre/attack/techniques/T1547.003-time-providers\|T1547.003]] | Time Providers | Consider using Group Policy to configure and block modifications to W32Time parameters in the Registry. [^1]  |
| [[kb/mitre/attack/techniques/T1553-subvert-trust-controls\|T1553]] | Subvert Trust Controls | Ensure proper permissions are set for Registry hives to prevent users from modifying keys related to SIP and trust provider components. Components may still be able to be hijacked to suitable functions already present on disk if malicious modifications to Registry keys are not prevented. |
| [[kb/mitre/attack/techniques/T1553.003-sip-and-trust-provider-hijacking\|T1553.003]] | SIP and Trust Provider Hijacking | Ensure proper permissions are set for Registry hives to prevent users from modifying keys related to SIP and trust provider components. Components may still be able to be hijacked to suitable functions already present on disk if malicious modifications to Registry keys are not prevented.  |
| [[kb/mitre/attack/techniques/T1553.006-code-signing-policy-modification\|T1553.006]] | Code Signing Policy Modification | Ensure proper permissions are set for the Registry to prevent users from modifying keys related to code signing policies. |
| [[kb/mitre/attack/techniques/T1556-modify-authentication-process\|T1556]] | Modify Authentication Process | Restrict Registry permissions to disallow the modification of sensitive Registry keys such as `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order`. |
| [[kb/mitre/attack/techniques/T1556.008-network-provider-dll\|T1556.008]] | Network Provider DLL | Restrict Registry permissions to disallow the modification of sensitive Registry keys such as `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order`. |
| [[kb/mitre/attack/techniques/T1574-hijack-execution-flow\|T1574]] | Hijack Execution Flow | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation. |
| [[kb/mitre/attack/techniques/T1574.011-services-registry-permissions-weakness\|T1574.011]] | Services Registry Permissions Weakness | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation.  |
| [[kb/mitre/attack/techniques/T1574.012-cor-profiler\|T1574.012]] | COR_PROFILER | Ensure proper permissions are set for Registry hives to prevent users from modifying keys associated with COR_PROFILER. |
| [[kb/mitre/attack/techniques/T1685-disable-or-modify-tools\|T1685]] | Disable or Modify Tools | Ensure proper Registry permissions are in place to prevent adversaries from disabling or interfering with security services. |
| [[kb/mitre/attack/techniques/T1685.001-disable-or-modify-windows-event-log\|T1685.001]] | Disable or Modify Windows Event Log | Ensure proper Registry permissions are in place to prevent adversaries from disabling or interfering logging. The addition of the MiniNT registry key disables Event Viewer.[^1]  |
| [[kb/mitre/attack/techniques/T1686-disable-or-modify-system-firewall\|T1686]] | Disable or Modify System Firewall | Ensure proper Registry permissions are in place to prevent adversaries from disabling or modifying firewall settings. |
| [[kb/mitre/attack/techniques/T1686.003-windows-host-firewall\|T1686.003]] | Windows Host Firewall | Ensure proper Registry permissions are in place to prevent adversaries from disabling or modifying firewall settings. |

 [^1]: [Microsoft W32Time May 2017](https://docs.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)
 [^2]: [Microsoft System Services Fundamentals](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)
 [^3]: [def_ev_win_event_logging](https://www.hackingarticles.in/defense-evasion-windows-event-logging-t1562-002/)
