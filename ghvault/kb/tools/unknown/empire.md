---
parsed_by: focuslocust
source: mitre
type: generated
---
# Empire

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0363` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Empire is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure PowerShell for Windows and Python for Linux/macOS. Empire was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/empire.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) contains an implementation of [Mimikatz](https://attack.mitre.org/software/S0002) to gather credentials from memory.(Citation: Github PowerShell Empire) |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can acquire network configuration information like DNS servers, public IP, and network proxies used by a host.(Citation: Github PowerShell Empire)(Citation: Talos Frankenstein June 2019) |
| [T1020 - Automated Exfiltration](../../attack/techniques/T1020-automated-exfiltration.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) has the ability to automatically send collected data back to the threat actors' C2.(Citation: Talos Frankenstein June 2019) |
| [T1021.003 - Distributed Component Object Model](../../attack/techniques/T1021.003-distributed-component-object-model.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can utilize <code>Invoke-DCOM</code> to leverage remote COM execution for lateral movement.(Citation: Github PowerShell Empire) |
| [T1021.004 - SSH](../../attack/techniques/T1021.004-ssh.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) contains modules for executing commands over SSH as well as in-memory VNC agent injection.(Citation: Github PowerShell Empire) |
| [T1027.010 - Command Obfuscation](../../attack/techniques/T1027.010-command-obfuscation.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) has the ability to obfuscate commands using <code>Invoke-Obfuscation</code>.(Citation: Github PowerShell Empire) |
| [T1033 - System Owner／User Discovery](../../attack/techniques/T1033-system-owner-user-discovery.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can enumerate the username on targeted hosts.(Citation: Talos Frankenstein June 2019) |
| [T1040 - Network Sniffing](../../attack/techniques/T1040-network-sniffing.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can be used to conduct packet captures on target hosts.(Citation: Github PowerShell Empire) |
| [T1041 - Exfiltration Over C2 Channel](../../attack/techniques/T1041-exfiltration-over-c2-channel.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can send data gathered from a target through the command and control channel.(Citation: Github PowerShell Empire)(Citation: Talos Frankenstein June 2019) |
| [T1046 - Network Service Discovery](../../attack/techniques/T1046-network-service-discovery.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can perform port scans from an infected host.(Citation: Github PowerShell Empire) |
| [T1047 - Windows Management Instrumentation](../../attack/techniques/T1047-windows-management-instrumentation.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use WMI to deliver a payload to a remote host.(Citation: Github PowerShell Empire)  |
| [T1049 - System Network Connections Discovery](../../attack/techniques/T1049-system-network-connections-discovery.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can enumerate the current network connections of a host.(Citation: Github PowerShell Empire) |
| [T1053.005 - Scheduled Task](../../attack/techniques/T1053.005-scheduled-task.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) has modules to interact with the Windows task scheduler.(Citation: Github PowerShell Empire) |
| [T1055 - Process Injection](../../attack/techniques/T1055-process-injection.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) contains multiple modules for injecting into processes, such as <code>Invoke-PSInject</code>.(Citation: Github PowerShell Empire) |
| [T1056.001 - Keylogging](../../attack/techniques/T1056.001-keylogging.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) includes keylogging capabilities for Windows, Linux, and macOS systems.(Citation: Github PowerShell Empire) |
| [T1056.004 - Credential API Hooking](../../attack/techniques/T1056.004-credential-api-hooking.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) contains some modules that leverage API hooking to carry out tasks, such as netripper.(Citation: Github PowerShell Empire) |
| [T1057 - Process Discovery](../../attack/techniques/T1057-process-discovery.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can find information about processes running on local and remote systems.(Citation: Github PowerShell Empire)(Citation: Talos Frankenstein June 2019) |
| [T1059 - Command and Scripting Interpreter](../../attack/techniques/T1059-command-and-scripting-interpreter.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) uses a command-line interface to interact with systems.(Citation: Github PowerShell Empire) |
| [T1059.001 - PowerShell](../../attack/techniques/T1059.001-powershell.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) leverages PowerShell for the majority of its client-side agent tasks. [Empire](https://attack.mitre.org/software/S0363) also contains the ability to conduct PowerShell remoting with the <code>Invoke-PSRemoting</code> module.(Citation: Github PowerShell Empire)(Citation: NCSC Joint Report Public Tools) |
| [T1059.003 - Windows Command Shell](../../attack/techniques/T1059.003-windows-command-shell.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) has modules for executing scripts.(Citation: Github PowerShell Empire) |
| [T1068 - Exploitation for Privilege Escalation](../../attack/techniques/T1068-exploitation-for-privilege-escalation.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can exploit vulnerabilities such as MS16-032 and MS16-135.(Citation: Github PowerShell Empire) |
| [T1070.006 - Timestomp](../../attack/techniques/T1070.006-timestomp.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can timestomp any files or payloads placed on a target machine to help them blend in.(Citation: Github PowerShell Empire) |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can conduct command and control over protocols like HTTP and HTTPS.(Citation: Github PowerShell Empire) |
| [T1082 - System Information Discovery](../../attack/techniques/T1082-system-information-discovery.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can enumerate host system information like OS, architecture, domain name, applied patches, and more.(Citation: Github PowerShell Empire)(Citation: Talos Frankenstein June 2019) |
| [T1083 - File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) includes various modules for finding files of interest on hosts and network shares.(Citation: Github PowerShell Empire) |
| [T1087.001 - Local Account](../../attack/techniques/T1087.001-local-account.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can acquire local and domain user account information.(Citation: Github PowerShell Empire) |
| [T1087.002 - Domain Account](../../attack/techniques/T1087.002-domain-account.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can acquire local and domain user account information.(Citation: Github PowerShell Empire)(Citation: SecureWorks August 2019) |
| [T1102.002 - Bidirectional Communication](../../attack/techniques/T1102.002-bidirectional-communication.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use Dropbox and GitHub for C2.(Citation: Github PowerShell Empire) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can upload and download to and from a victim machine.(Citation: Github PowerShell Empire) |
| [T1106 - Native API](../../attack/techniques/T1106-native-api.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) contains a variety of enumeration modules that have an option to use API calls to carry out tasks.(Citation: Github PowerShell Empire) |
| [T1113 - Screen Capture](../../attack/techniques/T1113-screen-capture.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) is capable of capturing screenshots on Windows and macOS systems.(Citation: Github PowerShell Empire) |
| [T1114.001 - Local Email Collection](../../attack/techniques/T1114.001-local-email-collection.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) has the ability to collect emails on a target system.(Citation: Github PowerShell Empire) |
| [T1115 - Clipboard Data](../../attack/techniques/T1115-clipboard-data.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can harvest clipboard data on both Windows and macOS systems.(Citation: Github PowerShell Empire) |
| [T1119 - Automated Collection](../../attack/techniques/T1119-automated-collection.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can automatically gather the username, domain name, machine name, and other information from a compromised system.(Citation: Talos Frankenstein June 2019) |
| [T1125 - Video Capture](../../attack/techniques/T1125-video-capture.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can capture webcam data on Windows and macOS systems.(Citation: Github PowerShell Empire) |
| [T1127.001 - MSBuild](../../attack/techniques/T1127.001-msbuild.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use built-in modules to abuse trusted utilities like MSBuild.exe.(Citation: Github PowerShell Empire)<br> |
| [T1134 - Access Token Manipulation](../../attack/techniques/T1134-access-token-manipulation.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Invoke-TokenManipulation</code> to manipulate access tokens.(Citation: Github PowerShell Empire) |
| [T1134.002 - Create Process with Token](../../attack/techniques/T1134.002-create-process-with-token.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use <code>Invoke-RunAs</code> to make tokens.(Citation: Github PowerShell Empire) |
| [T1134.005 - SID-History Injection](../../attack/techniques/T1134.005-sid-history-injection.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can add a SID-History to a user if on a domain controller.(Citation: Github PowerShell Empire) |
| [T1135 - Network Share Discovery](../../attack/techniques/T1135-network-share-discovery.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can find shared drives on the local system.(Citation: Github PowerShell Empire) |
| [T1136.001 - Local Account](../../attack/techniques/T1136.001-local-account.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) has a module for creating a local user if permissions allow.(Citation: Github PowerShell Empire) |
| [T1136.002 - Domain Account](../../attack/techniques/T1136.002-domain-account.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) has a module for creating a new domain user if permissions allow.(Citation: Github PowerShell Empire) |
| [T1210 - Exploitation of Remote Services](../../attack/techniques/T1210-exploitation-of-remote-services.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) has a limited number of built-in modules for exploiting remote SMB, JBoss, and Jenkins servers.(Citation: Github PowerShell Empire) |
| [T1217 - Browser Information Discovery](../../attack/techniques/T1217-browser-information-discovery.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) has the ability to gather browser data such as bookmarks and visited sites.(Citation: Github PowerShell Empire) |
| [T1482 - Domain Trust Discovery](../../attack/techniques/T1482-domain-trust-discovery.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) has modules for enumerating domain trusts.(Citation: Github PowerShell Empire) |
| [T1484.001 - Group Policy Modification](../../attack/techniques/T1484.001-group-policy-modification.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use <code>New-GPOImmediateTask</code> to modify a GPO that will install and execute a malicious [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053).(Citation: Github PowerShell Empire) |
| [T1518.001 - Security Software Discovery](../../attack/techniques/T1518.001-security-software-discovery.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can enumerate antivirus software on the target.(Citation: Github PowerShell Empire) |
| [T1543.003 - Windows Service](../../attack/techniques/T1543.003-windows-service.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can utilize built-in modules to modify service binaries and restore them to their original state.(Citation: Github PowerShell Empire) |
| [T1546.008 - Accessibility Features](../../attack/techniques/T1546.008-accessibility-features.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can leverage WMI debugging to remotely replace binaries like sethc.exe, Utilman.exe, and Magnify.exe with cmd.exe.(Citation: Github PowerShell Empire) |
| [T1547.001 - Registry Run Keys ／ Startup Folder](../../attack/techniques/T1547.001-registry-run-keys-startup-folder.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can modify the registry run keys <code>HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run</code> and <code>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run</code> for persistence.(Citation: Github PowerShell Empire) |
| [T1547.005 - Security Support Provider](../../attack/techniques/T1547.005-security-support-provider.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can enumerate Security Support Providers (SSPs) as well as utilize [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Install-SSP</code> and <code>Invoke-Mimikatz</code> to install malicious SSPs and log authentication events.(Citation: Github PowerShell Empire) |
| [T1547.009 - Shortcut Modification](../../attack/techniques/T1547.009-shortcut-modification.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can persist by modifying a .LNK file to include a backdoor.(Citation: Github PowerShell Empire) |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) includes various modules to attempt to bypass UAC for escalation of privileges.(Citation: Github PowerShell Empire) |
| [T1550.002 - Pass the Hash](../../attack/techniques/T1550.002-pass-the-hash.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can perform pass the hash attacks.(Citation: Github PowerShell Empire) |
| [T1552.001 - Credentials In Files](../../attack/techniques/T1552.001-credentials-in-files.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use various modules to search for files containing passwords.(Citation: Github PowerShell Empire) |
| [T1552.004 - Private Keys](../../attack/techniques/T1552.004-private-keys.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use modules like <code>Invoke-SessionGopher</code> to extract private key and session information.(Citation: Github PowerShell Empire) |
| [T1555.001 - Keychain](../../attack/techniques/T1555.001-keychain.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) uses the command `/usr/bin/security dump-keychain -d` to read the keychain credential.(Citation: Empire Keychain Decrypt) |
| [T1555.003 - Credentials from Web Browsers](../../attack/techniques/T1555.003-credentials-from-web-browsers.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use modules that extract passwords from common web browsers such as Firefox and Chrome.(Citation: Github PowerShell Empire) |
| [T1557.001 - Name Resolution Poisoning and SMB Relay](../../attack/techniques/T1557.001-name-resolution-poisoning-and-smb-relay.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use Inveigh to conduct name service poisoning for credential theft and associated relay attacks.(Citation: Github PowerShell Empire)(Citation: GitHub Inveigh) |
| [T1558.001 - Golden Ticket](../../attack/techniques/T1558.001-golden-ticket.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can leverage its implementation of [Mimikatz](https://attack.mitre.org/software/S0002) to obtain and use golden tickets.(Citation: Github PowerShell Empire) |
| [T1558.002 - Silver Ticket](../../attack/techniques/T1558.002-silver-ticket.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can leverage its implementation of [Mimikatz](https://attack.mitre.org/software/S0002) to obtain and use silver tickets.(Citation: Github PowerShell Empire) |
| [T1558.003 - Kerberoasting](../../attack/techniques/T1558.003-kerberoasting.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) uses [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Invoke-Kerberoast</code> to request service tickets and return crackable ticket hashes.(Citation: Github PowerShell Empire) |
| [T1560 - Archive Collected Data](../../attack/techniques/T1560-archive-collected-data.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can ZIP directories on the target system.(Citation: Github PowerShell Empire) |
| [T1567.001 - Exfiltration to Code Repository](../../attack/techniques/T1567.001-exfiltration-to-code-repository.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use GitHub for data exfiltration.(Citation: Github PowerShell Empire) |
| [T1567.002 - Exfiltration to Cloud Storage](../../attack/techniques/T1567.002-exfiltration-to-cloud-storage.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use Dropbox for data exfiltration.(Citation: Github PowerShell Empire) |
| [T1569.002 - Service Execution](../../attack/techniques/T1569.002-service-execution.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use [PsExec](https://attack.mitre.org/software/S0029) to execute a payload on a remote host.(Citation: Github PowerShell Empire) |
| [T1573.002 - Asymmetric Cryptography](../../attack/techniques/T1573.002-asymmetric-cryptography.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use TLS to encrypt its C2 channel.(Citation: Github PowerShell Empire) |
| [T1574.001 - DLL](../../attack/techniques/T1574.001-dll.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) contains modules that can discover and exploit various DLL hijacking opportunities.(Citation: Github PowerShell Empire) |
| [T1574.004 - Dylib Hijacking](../../attack/techniques/T1574.004-dylib-hijacking.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) has a dylib hijacker module that generates a malicious dylib given the path to a legitimate dylib of a vulnerable application.(Citation: Github PowerShell Empire) |
| [T1574.007 - Path Interception by PATH Environment Variable](../../attack/techniques/T1574.007-path-interception-by-path-environment-variable.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) contains modules that can discover and exploit path interception opportunities in the PATH environment variable.(Citation: Github PowerShell Empire) |
| [T1574.008 - Path Interception by Search Order Hijacking](../../attack/techniques/T1574.008-path-interception-by-search-order-hijacking.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) contains modules that can discover and exploit search order hijacking vulnerabilities.(Citation: Github PowerShell Empire) |
| [T1574.009 - Path Interception by Unquoted Path](../../attack/techniques/T1574.009-path-interception-by-unquoted-path.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) contains modules that can discover and exploit unquoted path vulnerabilities.(Citation: Github PowerShell Empire) |
| [T1615 - Group Policy Discovery](../../attack/techniques/T1615-group-policy-discovery.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) includes various modules for enumerating Group Policy.(Citation: Github PowerShell Empire) |

## Source Verification

[source record](../../sources/mitre/empire.md)

## Evidence Excerpt

```text
created: '2019-03-11T14:13:40.648Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and
post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python,
the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows
and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint
report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github
PowerShell Empire)(Citation: GitHub ATTACK Empire)'
```
