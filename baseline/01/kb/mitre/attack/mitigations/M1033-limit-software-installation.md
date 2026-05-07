---
parsed_by: focuslocust
source: mitre
type: mitigation
aliases:
    - M1033
tags:
    - attack/domain/enterprise_attack
    - attack/type/mitigation
mitre-attack: kb/mitre/attack/mitigations/M1033-limit-software-installation
---

## Description

Prevent users or groups from installing unauthorized or unapproved software to reduce the risk of introducing malicious or vulnerable applications. This can be achieved through allowlists, software restriction policies, endpoint management tools, and least privilege access principles. This mitigation can be implemented through the following measures:<br><br>Application Whitelisting<br><br>- Implement Microsoft AppLocker or Windows Defender Application Control (WDAC) to create and enforce allowlists for approved software.<br>- Whitelist applications based on file hash, path, or digital signatures.<br><br>Restrict User Permissions<br><br>- Remove local administrator rights for all non-IT users.<br>- Use Role-Based Access Control (RBAC) to restrict installation permissions to privileged accounts only.<br><br>Software Restriction Policies (SRP)<br><br>- Use GPO to configure SRP to deny execution of binaries from directories such as `%AppData%`, `%Temp%`, and external drives.<br>- Restrict specific file types (`.exe`, `.bat`, `.msi`, `.js`, `.vbs`) to trusted directories only.<br><br>Endpoint Management Solutions<br><br>- Deploy tools like Microsoft Intune, SCCM, or Jamf for centralized software management.<br>- Maintain a list of approved software, versions, and updates across the enterprise.<br><br>Monitor Software Installation Events<br><br>- Enable logging of software installation events and monitor Windows Event ID 4688 and Event ID 11707 for software installs.<br>- Use SIEM or EDR tools to alert on attempts to install unapproved software.<br><br>Implement Software Inventory Management<br><br>- Use tools like OSQuery or Wazuh to scan for unauthorized software on endpoints and servers.<br>- Conduct regular audits to detect and remove unapproved software.<br><br>*Tools for Implementation*<br><br>Application Whitelisting:<br><br>- Microsoft AppLocker<br>- Windows Defender Application Control (WDAC)<br><br>Endpoint Management:<br><br>- Microsoft Intune<br>- SCCM (System Center Configuration Manager)<br>- Jamf Pro (macOS)<br>- Puppet or Ansible for automation<br><br>Software Restriction Policies:<br><br>- Group Policy Object (GPO)<br>- Microsoft Software Restriction Policies (SRP)<br><br>Monitoring and Logging:<br><br>- Splunk<br>- OSQuery<br>- Wazuh (open-source SIEM and XDR)<br>- EDRs<br><br>Inventory Management and Auditing:<br><br>- OSQuery<br>- Wazuh

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1021.005-vnc\|T1021.005]] | VNC | Restrict software installation to user groups that require it. A VNC server must be manually installed by the user or adversary. |
| [[kb/mitre/attack/techniques/T1059-command-and-scripting-interpreter\|T1059]] | Command and Scripting Interpreter | Prevent user installation of unrequired command and scripting interpreters. |
| [[kb/mitre/attack/techniques/T1059.006-python\|T1059.006]] | Python | Prevent users from installing Python where not required. |
| [[kb/mitre/attack/techniques/T1059.011-lua\|T1059.011]] | Lua | Prevent users from installing Lua where not required. |
| [[kb/mitre/attack/techniques/T1072-software-deployment-tools\|T1072]] | Software Deployment Tools | Restrict the use of third-party software suites installed within an enterprise network.  |
| [[kb/mitre/attack/techniques/T1176-software-extensions\|T1176]] | Software Extensions | Only install extensions from trusted sources that can be verified. |
| [[kb/mitre/attack/techniques/T1176.001-browser-extensions\|T1176.001]] | Browser Extensions | Only install browser extensions from trusted sources that can be verified. Browser extensions for some browsers can be controlled through Group Policy. Change settings to prevent the browser from installing extensions without sufficient permissions. |
| [[kb/mitre/attack/techniques/T1176.002-ide-extensions\|T1176.002]] | IDE Extensions | Only install IDE extensions from trusted sources that can be verified.   |
| [[kb/mitre/attack/techniques/T1195-supply-chain-compromise\|T1195]] | Supply Chain Compromise | Where possible, consider requiring developers to pull from internal repositories containing verified and approved packages rather than from external ones.[^1]  |
| [[kb/mitre/attack/techniques/T1195.001-compromise-software-dependencies-and-development-tools\|T1195.001]] | Compromise Software Dependencies and Development Tools | Where possible, consider requiring developers to pull from internal repositories containing verified and approved packages rather than from external ones.[^1]  |
| [[kb/mitre/attack/techniques/T1204-user-execution\|T1204]] | User Execution | Where possible, consider requiring developers to pull from internal repositories containing verified and approved packages rather than from external ones. |
| [[kb/mitre/attack/techniques/T1204.005-malicious-library\|T1204.005]] | Malicious Library | Where possible, consider requiring developers to pull from internal repositories containing verified and approved packages rather than from external ones.  |
| [[kb/mitre/attack/techniques/T1543-create-or-modify-system-process\|T1543]] | Create or Modify System Process | Restrict software installation to trusted repositories only and be cautious of orphaned software packages. |
| [[kb/mitre/attack/techniques/T1543.002-systemd-service\|T1543.002]] | Systemd Service | Restrict software installation to trusted repositories only and be cautious of orphaned software packages. |
| [[kb/mitre/attack/techniques/T1547.013-xdg-autostart-entries\|T1547.013]] | XDG Autostart Entries | Restrict software installation to trusted repositories only and be cautious of orphaned software packages. |
| [[kb/mitre/attack/techniques/T1564-hide-artifacts\|T1564]] | Hide Artifacts | Restrict the installation of software that may be abused to create hidden desktops, such as hVNC, to user groups that require it. |
| [[kb/mitre/attack/techniques/T1564.003-hidden-window\|T1564.003]] | Hidden Window | Restrict the installation of software that may be abused to create hidden desktops, such as hVNC, to user groups that require it. |

 [^1]: [Cider Security Top 10 CICD Security Risks](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)
