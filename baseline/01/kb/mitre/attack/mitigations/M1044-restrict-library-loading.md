---
parsed_by: focuslocust
source: mitre
type: mitigation
aliases:
    - M1044
tags:
    - attack/domain/enterprise_attack
    - attack/type/mitigation
mitre-attack: kb/mitre/attack/mitigations/M1044-restrict-library-loading
---

## Description

Restricting library loading involves implementing security controls to ensure that only trusted and verified libraries (DLLs, shared objects, etc.) are loaded into processes. Adversaries often abuse Dynamic-Link Library (DLL) Injection, DLL Search Order Hijacking, or LD_PRELOAD mechanisms to execute malicious code by forcing the operating system to load untrusted libraries. This mitigation can be implemented through the following measures: <br><br>Enforce Safe Library Loading Practices:<br><br>- Enable `SafeDLLSearchMode` on Windows.<br>- Restrict `LD_PRELOAD` and `LD_LIBRARY_PATH` usage on Linux systems.<br><br>Code Signing Enforcement:<br><br>- Require digital signatures for all libraries loaded into processes.<br>- Use tools like Signtool, and WDAC to enforce signed DLL execution.<br><br>Environment Hardening:<br><br>- Secure library paths and directories to prevent adversaries from placing rogue libraries.<br>- Monitor user-writable directories and system configurations for unauthorized changes.<br><br>Audit and Monitor Library Loading:<br><br>- Enable `Sysmon` on Windows to monitor for suspicious library loads.<br>- Use `auditd` on Linux to monitor shared library paths and configuration file changes.<br><br>Use Application Control Solutions:<br><br>- Implement AppLocker, WDAC, or SELinux to allow only trusted libraries.<br><br>*Tools for Implementation*<br><br>Windows-Specific Tools:<br><br>- AppLocker: Application whitelisting for DLLs.<br>- Windows Defender Application Control (WDAC): Restrict unauthorized library execution.<br>- Signtool: Verify and enforce code signing.<br>- Sysmon: Monitor DLL load events (Event ID 7).<br><br>Linux-Specific Tools:<br><br>- auditd: Monitor changes to library paths and critical files.<br>- SELinux/AppArmor: Define policies to restrict library loading.<br>- ldconfig and chattr: Secure LD configuration files and prevent unauthorized modifications.<br><br>Cross-Platform Solutions:<br><br>- Wazuh or OSSEC: File integrity monitoring for library changes.<br>- Tripwire: Detect and alert on unauthorized library modifications.

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1547.008-lsass-driver\|T1547.008]] | LSASS Driver | Ensure safe DLL search mode is enabled `HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\SafeDllSearchMode` to mitigate risk that lsass.exe loads a malicious code library. [^1]  |
| [[kb/mitre/attack/techniques/T1574-hijack-execution-flow\|T1574]] | Hijack Execution Flow | Disallow loading of remote DLLs. This is included by default in Windows Server 2012+ and is available by patch for XP+ and Server 2003+.<br><br>Enable Safe DLL Search Mode to force search for system DLLs in directories with greater restrictions (e.g. `%SYSTEMROOT%`)to be used before local directory DLLs (e.g. a user's home directory)<br><br>The Safe DLL Search Mode can be enabled via Group Policy at Computer Configuration > [Policies] > Administrative Templates > MSS (Legacy): MSS: (SafeDllSearchMode) Enable Safe DLL search mode. The associated Windows Registry key for this is located at `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\SafeDLLSearchMode`[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1574.001-dll\|T1574.001]] | DLL | Disallow loading of remote DLLs. This is included by default in Windows Server 2012+ and is available by patch for XP+ and Server 2003+.[^1] <br><br>Enable Safe DLL Search Mode to move the user's current folder later in the search order. This is included by default in modern versions of Windows; the associated Windows Registry key is located at `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\SafeDLLSearchMode`.[^2]  |

 [^1]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)
 [^2]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)
 [^3]: [Microsoft DLL Security](https://msdn.microsoft.com/library/windows/desktop/ff919712.aspx)
