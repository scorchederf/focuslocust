---
generated_by: focuslocust
source: mitre
type: mitigation
aliases:
    - M1025
tags:
    - attack/domain/enterprise_attack
    - attack/type/mitigation
mitre-attack: kb/mitre/attack/mitigations/M1025-privileged-process-integrity
---

## Description

Privileged Process Integrity focuses on defending highly privileged processes (e.g., system services, antivirus, or authentication processes) from tampering, injection, or compromise by adversaries. These processes often interact with critical components, making them prime targets for techniques like code injection, privilege escalation, and process manipulation. This mitigation can be implemented through the following measures:<br><br>Protected Process Mechanisms:<br><br>- Enable RunAsPPL on Windows systems to protect LSASS and other critical processes.<br>- Use registry modifications to enforce protected process settings: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL`<br><br>Anti-Injection and Memory Protection:<br><br>- Enable Control Flow Guard (CFG), DEP, and ASLR to protect against process memory tampering.<br>- Deploy endpoint protection tools that actively block process injection attempts.<br><br>Code Signing Validation:<br><br>- Implement policies for Windows Defender Application Control (WDAC) or AppLocker to enforce execution of signed binaries.<br>- Ensure critical processes are signed with valid certificates.<br><br>Access Controls:<br><br>- Use DACLs and MIC to limit which users and processes can interact with privileged processes.<br>- Disable unnecessary debugging capabilities for high-privileged processes.<br><br>Kernel-Level Protections:<br><br>- Ensure Kernel Patch Protection (PatchGuard) is enabled on Windows systems.<br>- Leverage SELinux or AppArmor on Linux to enforce kernel-level security policies.<br><br>*Tools for Implementation*<br><br>Protected Process Light (PPL):<br><br>- RunAsPPL (Windows)<br>- Windows Defender Credential Guard<br><br>Code Integrity and Signing:<br><br>- Windows Defender Application Control (WDAC)<br>- AppLocker<br>- SELinux/AppArmor (Linux)<br><br>Memory Protection:<br><br>- Control Flow Guard (CFG), Data Execution Prevention (DEP), ASLR<br><br>Process Isolation/Sandboxing:<br><br>- Firejail (Linux Sandbox)<br>- Windows Sandbox<br>- QEMU/KVM-based isolation<br><br>Kernel Protection:<br><br>- PatchGuard (Windows Kernel Patch Protection)<br>- SELinux (Mandatory Access Control for Linux)<br>- AppArmor

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003-os-credential-dumping\|T1003]] | OS Credential Dumping | <br>On Windows 8.1 and Windows Server 2012 R2, enable Protected Process Light for LSA.[^1]  |
| [[kb/mitre/attack/techniques/T1003.001-lsass-memory\|T1003.001]] | LSASS Memory | On Windows 8.1 and Windows Server 2012 R2, enable Protected Process Light for LSA.[^1]  |
| [[kb/mitre/attack/techniques/T1547.002-authentication-package\|T1547.002]] | Authentication Package | Windows 8.1, Windows Server 2012 R2, and later versions, may make LSA run as a Protected Process Light (PPL) by setting the Registry key `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL`, which requires all DLLs loaded by LSA to be signed by Microsoft. [^1]  [^2]  |
| [[kb/mitre/attack/techniques/T1547.005-security-support-provider\|T1547.005]] | Security Support Provider | Windows 8.1, Windows Server 2012 R2, and later versions may make LSA run as a Protected Process Light (PPL) by setting the Registry key `HKLM\\SYSTEM\\CurrentControlSet\\Control\\Lsa\\RunAsPPL`, which requires all SSP DLLs to be signed by Microsoft. [^1]  [^2]  |
| [[kb/mitre/attack/techniques/T1547.008-lsass-driver\|T1547.008]] | LSASS Driver | On Windows 8.1 and Server 2012 R2, enable LSA Protection by setting the Registry key `HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Lsa\\RunAsPPL` to `dword:00000001`. [^1]  LSA Protection ensures that LSA plug-ins and drivers are only loaded if they are digitally signed with a Microsoft signature and adhere to the Microsoft Security Development Lifecycle (SDL) process guidance.  |
| [[kb/mitre/attack/techniques/T1556-modify-authentication-process\|T1556]] | Modify Authentication Process | Enabled features, such as Protected Process Light (PPL), for LSA.[^1]  |
| [[kb/mitre/attack/techniques/T1556.001-domain-controller-authentication\|T1556.001]] | Domain Controller Authentication | Enabled features, such as Protected Process Light (PPL), for LSA.[^1]  |

 [^1]: [Microsoft LSA Protection Mar 2014](https://technet.microsoft.com/library/dn408187.aspx)
 [^2]: [Graeber 2014](http://docplayer.net/20839173-Analysis-of-malicious-security-support-provider-dlls.html)
 [^3]: [Microsoft Configure LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)
 [^4]: [Microsoft LSA](https://technet.microsoft.com/en-us/library/dn408187.aspx)
