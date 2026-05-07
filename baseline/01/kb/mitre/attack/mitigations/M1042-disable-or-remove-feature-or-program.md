---
parsed_by: focuslocust
source: mitre
type: mitigation
aliases:
    - M1042
tags:
    - attack/domain/enterprise_attack
    - attack/type/mitigation
mitre-attack: kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program
---

## Description

Disable or remove unnecessary and potentially vulnerable software, features, or services to reduce the attack surface and prevent abuse by adversaries. This involves identifying software or features that are no longer needed or that could be exploited and ensuring they are either removed or properly disabled. This mitigation can be implemented through the following measures: <br><br>Remove Legacy Software:<br><br>- Use Case: Disable or remove older versions of software that no longer receive updates or security patches (e.g., legacy Java, Adobe Flash).<br>- Implementation: A company removes Flash Player from all employee systems after it has reached its end-of-life date.<br><br>Disable Unused Features:<br><br>- Use Case: Turn off unnecessary operating system features like SMBv1, Telnet, or RDP if they are not required.<br>- Implementation: Disable SMBv1 in a Windows environment to mitigate vulnerabilities like EternalBlue.<br><br>Control Applications Installed by Users:<br><br>- Use Case: Prevent users from installing unauthorized software via group policies or other management tools.<br>- Implementation: Block user installations of unauthorized file-sharing applications (e.g., BitTorrent clients) in an enterprise environment.<br><br>Remove Unnecessary Services:<br><br>- Use Case: Identify and disable unnecessary default services running on endpoints, servers, or network devices.<br>- Implementation: Disable unused administrative shares (e.g., C$, ADMIN$) on workstations.<br><br>Restrict Add-ons and Plugins:<br><br>- Use Case: Remove or disable browser plugins and add-ons that are not needed for business purposes.<br>- Implementation: Disable Java and ActiveX plugins in web browsers to prevent drive-by attacks.<br><br>

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1011-exfiltration-over-other-network-medium\|T1011]] | Exfiltration Over Other Network Medium | Disable WiFi connection, modem, cellular data connection, Bluetooth, or another radio frequency (RF) channel in local computer security settings or by group policy if it is not needed within an environment. |
| [[kb/mitre/attack/techniques/T1011.001-exfiltration-over-bluetooth\|T1011.001]] | Exfiltration Over Bluetooth | Disable Bluetooth in local computer security settings or by group policy if it is not needed within an environment. |
| [[kb/mitre/attack/techniques/T1021-remote-services\|T1021]] | Remote Services | If remote services, such as the ability to make direct connections to cloud virtual machines, are not required, disable these connection types where feasible. On ESXi servers, consider enabling lockdown mode, which disables direct access to an ESXi host and requires that the host be managed remotely using vCenter.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1021.001-remote-desktop-protocol\|T1021.001]] | Remote Desktop Protocol | Disable the RDP service if it is unnecessary. |
| [[kb/mitre/attack/techniques/T1021.003-distributed-component-object-model\|T1021.003]] | Distributed Component Object Model | Consider disabling DCOM through Dcomcnfg.exe.[^1]  |
| [[kb/mitre/attack/techniques/T1021.004-ssh\|T1021.004]] | SSH | Disable the SSH daemon on systems that do not require it, especially ESXi servers. For macOS, ensure Remote Login is disabled under Sharing Preferences.[^1]  |
| [[kb/mitre/attack/techniques/T1021.005-vnc\|T1021.005]] | VNC | Uninstall any VNC server software where not required. |
| [[kb/mitre/attack/techniques/T1021.006-windows-remote-management\|T1021.006]] | Windows Remote Management | Disable the WinRM service. |
| [[kb/mitre/attack/techniques/T1021.008-direct-cloud-vm-connections\|T1021.008]] | Direct Cloud VM Connections | If direct virtual machine connections are not required for administrative use, disable these connection types where feasible. |
| [[kb/mitre/attack/techniques/T1046-network-service-discovery\|T1046]] | Network Service Discovery | Ensure that unnecessary ports and services are closed to prevent risk of discovery and potential exploitation. |
| [[kb/mitre/attack/techniques/T1052-exfiltration-over-physical-medium\|T1052]] | Exfiltration Over Physical Medium | Disable Autorun if it is unnecessary. [^1]  Disallow or restrict removable media at an organizational policy level if they are not required for business operations. [^2]  |
| [[kb/mitre/attack/techniques/T1052.001-exfiltration-over-usb\|T1052.001]] | Exfiltration over USB | Disable Autorun if it is unnecessary. [^1]  Disallow or restrict removable media at an organizational policy level if they are not required for business operations. [^2]  |
| [[kb/mitre/attack/techniques/T1059-command-and-scripting-interpreter\|T1059]] | Command and Scripting Interpreter | Disable or remove any unnecessary or unused shells or interpreters. |
| [[kb/mitre/attack/techniques/T1059.001-powershell\|T1059.001]] | PowerShell | It may be possible to remove PowerShell from systems when not needed, but a review should be performed to assess the impact to an environment, since it could be in use for many legitimate purposes and administrative functions.<br><br>Disable/restrict the WinRM Service to help prevent uses of PowerShell for remote execution. |
| [[kb/mitre/attack/techniques/T1059.005-visual-basic\|T1059.005]] | Visual Basic | Turn off or restrict access to unneeded VB components. |
| [[kb/mitre/attack/techniques/T1059.007-javascript\|T1059.007]] | JavaScript | Turn off or restrict access to unneeded scripting components. |
| [[kb/mitre/attack/techniques/T1091-replication-through-removable-media\|T1091]] | Replication Through Removable Media | Disable Autorun if it is unnecessary. [^1]  Disallow or restrict removable media at an organizational policy level if it is not required for business operations. [^2]  |
| [[kb/mitre/attack/techniques/T1092-communication-through-removable-media\|T1092]] | Communication Through Removable Media | Disable Autoruns if it is unnecessary.[^1]  |
| [[kb/mitre/attack/techniques/T1098-account-manipulation\|T1098]] | Account Manipulation | Remove unnecessary and potentially abusable authentication and authorization mechanisms where possible. |
| [[kb/mitre/attack/techniques/T1098.001-additional-cloud-credentials\|T1098.001]] | Additional Cloud Credentials | Remove unnecessary and potentially abusable authentication mechanisms where possible. For example, in Entra ID environments, disable the app password feature unless explicitly required.  |
| [[kb/mitre/attack/techniques/T1098.002-additional-email-delegate-permissions\|T1098.002]] | Additional Email Delegate Permissions | If email delegation is not required, disable it. In Google Workspace this can be accomplished through the Google Admin console.[^1]  |
| [[kb/mitre/attack/techniques/T1098.004-ssh-authorized-keys\|T1098.004]] | SSH Authorized Keys | Disable SSH if it is not necessary on a host or restrict SSH access for specific users/groups using `/etc/ssh/sshd_config`. Setting the `PermitRootLogin` directive to `no` will prevent the root user from logging in via SSH.[^1]  |
| [[kb/mitre/attack/techniques/T1114.003-email-forwarding-rule\|T1114.003]] | Email Forwarding Rule | Consider disabling external email forwarding.[^1]  |
| [[kb/mitre/attack/techniques/T1127-trusted-developer-utilities-proxy-execution\|T1127]] | Trusted Developer Utilities Proxy Execution | Specific developer utilities may not be necessary within a given environment and should be removed if not used. |
| [[kb/mitre/attack/techniques/T1127.001-msbuild\|T1127.001]] | MSBuild | MSBuild.exe may not be necessary within an environment and should be removed if not being used. |
| [[kb/mitre/attack/techniques/T1127.002-clickonce\|T1127.002]] | ClickOnce | Disable ClickOnce installations from the internet using the following registry key: <br>`\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\Security\TrustManager\PromptingLevel — Internet:Disabled`[^2] [^1] <br><br>ClickOnce may not be necessary within an environment and should be disabled if not being used. |
| [[kb/mitre/attack/techniques/T1127.003-jamplus\|T1127.003]] | JamPlus | JamPlus may not be necessary within a given environment and should be removed if not used. |
| [[kb/mitre/attack/techniques/T1133-external-remote-services\|T1133]] | External Remote Services | Disable or block remotely available services that may be unnecessary. |
| [[kb/mitre/attack/techniques/T1137-office-application-startup\|T1137]] | Office Application Startup | Follow Office macro security best practices suitable for your environment. Disable Office VBA macros from executing.<br><br>Disable Office add-ins. If they are required, follow best practices for securing them by requiring them to be signed and disabling user notification for allowing add-ins. For some add-ins types (WLL, VBA) additional mitigation is likely required as disabling add-ins in the Office Trust Center does not disable WLL nor does it prevent VBA code from executing. [^1]  |
| [[kb/mitre/attack/techniques/T1137.001-office-template-macros\|T1137.001]] | Office Template Macros | Follow Office macro security best practices suitable for your environment. Disable Office VBA macros from executing.<br><br>Disable Office add-ins. If they are required, follow best practices for securing them by requiring them to be signed and disabling user notification for allowing add-ins. For some add-ins types (WLL, VBA) additional mitigation is likely required as disabling add-ins in the Office Trust Center does not disable WLL nor does it prevent VBA code from executing. [^1] <br> |
| [[kb/mitre/attack/techniques/T1205-traffic-signaling\|T1205]] | Traffic Signaling | Disable Wake-on-LAN if it is not needed within an environment. |
| [[kb/mitre/attack/techniques/T1210-exploitation-of-remote-services\|T1210]] | Exploitation of Remote Services | Minimize available services to only those that are necessary. |
| [[kb/mitre/attack/techniques/T1218-system-binary-proxy-execution\|T1218]] | System Binary Proxy Execution | Many native binaries may not be necessary within a given environment. |
| [[kb/mitre/attack/techniques/T1218.003-cmstp\|T1218.003]] | CMSTP | CMSTP.exe may not be necessary within a given environment (unless using it for VPN connection installation). |
| [[kb/mitre/attack/techniques/T1218.004-installutil\|T1218.004]] | InstallUtil | InstallUtil may not be necessary within a given environment. |
| [[kb/mitre/attack/techniques/T1218.005-mshta\|T1218.005]] | Mshta | Mshta.exe may not be necessary within a given environment since its functionality is tied to older versions of Internet Explorer that have reached end of life. |
| [[kb/mitre/attack/techniques/T1218.007-msiexec\|T1218.007]] | Msiexec | Consider disabling the `AlwaysInstallElevated` policy to prevent elevated execution of Windows Installer packages.[^1]  |
| [[kb/mitre/attack/techniques/T1218.008-odbcconf\|T1218.008]] | Odbcconf | Odbcconf.exe may not be necessary within a given environment. |
| [[kb/mitre/attack/techniques/T1218.009-regsvcs-regasm\|T1218.009]] | Regsvcs/Regasm | Regsvcs and Regasm may not be necessary within a given environment. |
| [[kb/mitre/attack/techniques/T1218.012-verclsid\|T1218.012]] | Verclsid | Consider removing verclsid.exe if it is not necessary within a given environment. |
| [[kb/mitre/attack/techniques/T1218.013-mavinject\|T1218.013]] | Mavinject | Consider removing mavinject.exe if Microsoft App-V is not used within a given environment. |
| [[kb/mitre/attack/techniques/T1218.014-mmc\|T1218.014]] | MMC | MMC may not be necessary within a given environment since it is primarily used by system administrators, not regular users or clients.  |
| [[kb/mitre/attack/techniques/T1218.015-electron-applications\|T1218.015]] | Electron Applications | Remove or deny access to unnecessary and potentially vulnerable software and features to prevent abuse by adversaries. Many native binaries may not be necessary within a given environment: for example, consider disabling the Node.js integration in all renderers that display remote content to protect users by limiting adversaries’ power to plant malicious JavaScript within Electron applications.[^1]  |
| [[kb/mitre/attack/techniques/T1219-remote-access-tools\|T1219]] | Remote Access Tools | Consider disabling unnecessary remote connection functionality, including both unapproved software installations and specific features built into supported applications. |
| [[kb/mitre/attack/techniques/T1219.002-remote-desktop-software\|T1219.002]] | Remote Desktop Software | Consider disabling unnecessary remote connection functionality, including both unapproved software installations and specific features built into supported applications. |
| [[kb/mitre/attack/techniques/T1221-template-injection\|T1221]] | Template Injection | Consider disabling Microsoft Office macros/active content to prevent the execution of malicious payloads in documents [^1] , though this setting may not mitigate the [[kb/mitre/attack/techniques/T1187-forced-authentication\|Forced Authentication]] use for this technique. |
| [[kb/mitre/attack/techniques/T1505-server-software-component\|T1505]] | Server Software Component | Consider disabling software components from servers when possible to prevent abuse by adversaries.[^1]  |
| [[kb/mitre/attack/techniques/T1505.003-web-shell\|T1505.003]] | Web Shell | Consider disabling functions from web technologies such as PHP’s `evaI()` that may be abused for web shells.[^1]  |
| [[kb/mitre/attack/techniques/T1546.002-screensaver\|T1546.002]] | Screensaver | Use Group Policy to disable screensavers if they are unnecessary.[^1]  |
| [[kb/mitre/attack/techniques/T1546.014-emond\|T1546.014]] | Emond | Consider disabling emond by removing the [[kb/mitre/attack/techniques/T1543.004-launch-daemon\|Launch Daemon]] plist file. |
| [[kb/mitre/attack/techniques/T1547.007-re-opened-applications\|T1547.007]] | Re-opened Applications | This feature can be disabled entirely with the following terminal command: `defaults write -g ApplePersistence -bool no`. |
| [[kb/mitre/attack/techniques/T1552.005-cloud-instance-metadata-api\|T1552.005]] | Cloud Instance Metadata API | Disable unnecessary metadata services and restrict or disable insecure versions of metadata services that are in use to prevent adversary access.[^1]  |
| [[kb/mitre/attack/techniques/T1553.005-mark-of-the-web-bypass\|T1553.005]] | Mark-of-the-Web Bypass | Consider disabling auto-mounting of disk image files (i.e., .iso, .img, .vhd, and .vhdx). This can be achieved by modifying the Registry values related to the Windows Explorer file associations in order to disable the automatic Explorer "Mount and Burn" dialog for these file extensions. Note: this will not deactivate the mount functionality itself.[^1]  |
| [[kb/mitre/attack/techniques/T1555.004-windows-credential-manager\|T1555.004]] | Windows Credential Manager | Consider enabling the “Network access: Do not allow storage of passwords and credentials for network authentication” setting that will prevent network credentials from being stored by the Credential Manager.[^1]  |
| [[kb/mitre/attack/techniques/T1557-adversary-in-the-middle\|T1557]] | Adversary-in-the-Middle | Disable legacy network protocols that may be used   to intercept network traffic if applicable, especially those that are not needed within an environment. |
| [[kb/mitre/attack/techniques/T1557.001-name-resolution-poisoning-and-smb-relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | Disable LLMNR, mDNS, and NetBIOS in local computer security settings or by group policy if they are not needed within an environment. [^1]  |
| [[kb/mitre/attack/techniques/T1557.002-arp-cache-poisoning\|T1557.002]] | ARP Cache Poisoning | Consider disabling updating the ARP cache on gratuitous ARP replies. |
| [[kb/mitre/attack/techniques/T1559-inter-process-communication\|T1559]] | Inter-Process Communication | Registry keys specific to Microsoft Office feature control security can be set to disable automatic DDE/OLE execution. [^1] [^2] [^3]  Microsoft also created, and enabled by default, Registry keys to completely disable DDE execution in Word and Excel.[^4]  |
| [[kb/mitre/attack/techniques/T1559.002-dynamic-data-exchange\|T1559.002]] | Dynamic Data Exchange | Registry keys specific to Microsoft Office feature control security can be set to disable automatic DDE/OLE execution. [^1] [^2] [^3]  Microsoft also created, and enabled by default, Registry keys to completely disable DDE execution in Word and Excel.[^4]  |
| [[kb/mitre/attack/techniques/T1563-remote-service-session-hijacking\|T1563]] | Remote Service Session Hijacking | Disable the remote service (ex: SSH, RDP, etc.) if it is unnecessary. |
| [[kb/mitre/attack/techniques/T1563.001-ssh-hijacking\|T1563.001]] | SSH Hijacking | Ensure that agent forwarding is disabled on systems that do not explicitly require this feature to prevent misuse. [^1]  |
| [[kb/mitre/attack/techniques/T1563.002-rdp-hijacking\|T1563.002]] | RDP Hijacking | Disable the RDP service if it is unnecessary. |
| [[kb/mitre/attack/techniques/T1564.006-run-virtual-instance\|T1564.006]] | Run Virtual Instance | Disable native virtualization technologies such as Hyper-V if not necessary within a given environment. Consider also disabling Windows Sandbox if it is not needed to test or debug applications. |
| [[kb/mitre/attack/techniques/T1564.007-vba-stomping\|T1564.007]] | VBA Stomping | Turn off or restrict access to unneeded VB components.[^1]  |
| [[kb/mitre/attack/techniques/T1595.003-wordlist-scanning\|T1595.003]] | Wordlist Scanning | Remove or disable access to any systems, resources, and infrastructure that are not explicitly required to be available externally. |
| [[kb/mitre/attack/techniques/T1609-container-administration-command\|T1609]] | Container Administration Command | Remove unnecessary tools and software from containers. |
| [[kb/mitre/attack/techniques/T1611-escape-to-host\|T1611]] | Escape to Host | Remove unnecessary tools and software from containers. |
| [[kb/mitre/attack/techniques/T1649-steal-or-forge-authentication-certificates\|T1649]] | Steal or Forge Authentication Certificates | Consider disabling old/dangerous authentication protocols (e.g. NTLM), as well as unnecessary certificate features, such as potentially vulnerable AD CS web and other enrollment server roles.[^1]  |
| [[kb/mitre/attack/techniques/T1671-cloud-application-integration\|T1671]] | Cloud Application Integration | Do not allow users to add new application integrations into a SaaS environment. In Entra ID environments, consider enforcing the “Do not allow user consent” option.[^1]  |
| [[kb/mitre/attack/techniques/T1685-disable-or-modify-tools\|T1685]] | Disable or Modify Tools | Consider removing previous versions of tools that are unnecessary to the environment when possible. |
| [[kb/mitre/attack/techniques/T1689-downgrade-attack\|T1689]] | Downgrade Attack | Consider removing previous versions of tools that are unnecessary to the environment when possible. |

 [^1]: [Apple Unified Log Analysis Remote Login and Screen Sharing](https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins)
 [^2]: [Microsoft Entra Configure OAuth Consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)
 [^3]: [Microsoft DDE Advisory Nov 2017](https://technet.microsoft.com/library/security/4053440)
 [^4]: [BleepingComputer DDE Disabled in Word Dec 2017](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)
 [^5]: [GitHub Disable DDEAUTO Oct 2017](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)
 [^6]: [Microsoft ADV170021 Dec 2017](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)
 [^7]: [ADSecurity Windows Secure Baseline](https://adsecurity.org/?p=3299)
 [^8]: [Electron Security 2](https://stackoverflow.com/questions/48854265/why-do-i-see-an-electron-security-warning-after-updating-my-electron-project-t)
 [^9]: [Microsoft Learn ClickOnce Config](https://learn.microsoft.com/en-us/visualstudio/deployment/how-to-configure-the-clickonce-trust-prompt-behavior?view=vs-2022&tabs=csharp)
 [^10]: [NetSPI ClickOnce](https://www.netspi.com/blog/technical-blog/adversary-simulation/all-you-need-is-one-a-clickonce-love-story/)
 [^11]: [SpecterOps Certified Pre Owned](https://web.archive.org/web/20220818094600/https://specterops.io/assets/resources/Certified_Pre-Owned.pdf)
 [^12]: [Microsoft BEC Campaign](https://www.microsoft.com/security/blog/2021/06/14/behind-the-scenes-of-business-email-compromise-using-cross-domain-threat-data-to-disrupt-a-large-bec-infrastructure/)
 [^13]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)
 [^14]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)
 [^15]: [GitHub MOTW](https://gist.github.com/wdormann/fca29e0dcda8b5c0472e73e10c78c3e7)
 [^16]: [ITSyndicate Disabling PHP functions](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)
 [^17]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)
 [^18]: [TechNet Screensaver GP](https://technet.microsoft.com/library/cc938799.aspx)
 [^19]: [Microsoft Disable DCOM](https://technet.microsoft.com/library/cc771387.aspx)
 [^20]: [Microsoft Network access Credential Manager](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj852185(v=ws.11)?redirectedfrom=MSDN)
 [^21]: [Broadcom ESXi SSH](https://knowledge.broadcom.com/external/article/313767/allowing-ssh-access-to-vmware-vsphere-es.html)
 [^22]: [Symantec SSH and ssh-agent](https://www.symantec.com/connect/articles/ssh-and-ssh-agent)
 [^23]: [Microsoft AlwaysInstallElevated 2018](https://docs.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated)
 [^24]: [Microsoft Disable VBA Jan 2020](https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/turn-off-visual-basic-for-application)
 [^25]: [Amazon AWS IMDS V2](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)
 [^26]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)
 [^27]: [Broadcom ESXi Lockdown Mode](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)
 [^28]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)
 [^29]: [Gmail Delegation](https://support.google.com/a/answer/7223765?hl=en)
