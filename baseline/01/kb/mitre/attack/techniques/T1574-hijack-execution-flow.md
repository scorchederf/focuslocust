---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1574
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/execution
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1574-hijack-execution-flow
tactic:
    - Execution
    - Stealth
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may execute their own malicious payloads by hijacking the way operating systems run programs. Hijacking execution flow can be for the purposes of persistence, since this hijacked execution may reoccur over time. Adversaries may also use these mechanisms to elevate privileges or evade defenses, such as application control or other restrictions on execution.<br><br>There are many ways an adversary may hijack the flow of execution, including by manipulating how the operating system locates programs to be executed. How the operating system locates libraries to be used by a program can also be intercepted. Locations where the operating system looks for programs/resources, such as file directories and in the case of Windows the Registry, could also be poisoned to include malicious payloads.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0354](https://attack.mitre.org/software/S0354) | Denis | Denis replaces the nonexistent Windows DLL "msfte.dll" with its own malicious version, which is loaded by the SearchIndexer.exe and SearchProtocolHost.exe.[^1]  |
| [S0444](https://attack.mitre.org/software/S0444) | ShimRat | ShimRat can hijack the cryptbase.dll within migwiz.exe to escalate privileges and bypass UAC controls.[^1]  |
| [S0567](https://attack.mitre.org/software/S0567) | Dtrack | One of Dtrack can replace the normal flow of a program execution with malicious code.[^1]  |
| [S1018](https://attack.mitre.org/software/S1018) | Saint Bot | Saint Bot will use the malicious file `slideshow.mp4` if present to load the core API provided by `ntdll.dll` to avoid any hooks placed on calls to the original `ntdll.dll` file by endpoint detection and response or antimalware software.[^1]  |
| [S1105](https://attack.mitre.org/software/S1105) | COATHANGER | COATHANGER will remove and write malicious shared objects associated with legitimate system functions such as `read(2)`.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate edits the Registry key `HKCU\Software\Classes\mscfile\shell\open\command` to execute a malicious AutoIt script.[^1]  When eventvwr.exe is executed, this will call the Microsoft Management Console (mmc.exe), which in turn references the modified Registry key. |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin will drop a copy of itself to a subfolder in `%Program Data%` or `%Program Data%\\Microsoft\\` to attempt privilege elevation and defense evasion if not running in Session 0.[^1]  |
| [S1147](https://attack.mitre.org/software/S1147) | Nightdoor | Nightdoor uses a legitimate executable to load a malicious DLL file for installation.[^1]  |
| [S9024](https://attack.mitre.org/software/S9024) | SPAWNCHIMERA | SPAWNCHIMERA can persist across system upgrades by hijacking the execution flow of dspkginstall, a binary used during the system upgrade process.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1013-application-developer-guidance\|M1013]] | Application Developer Guidance | When possible, include hash values in manifest files to help prevent side-loading of malicious libraries.[^1]  |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Limit privileges of user accounts and groups so that only authorized administrators can interact with service changes and service binary target path locations. Deny execution from user directories such as file download directories and temp directories where able.<br><br>Ensure that proper permissions and directory access control are set to deny users the ability to write files to the top-level directory `C:` and system directories, such as `C:\Windows\`, to reduce places where malicious files could be placed for execution. |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | Install software in write-protected locations. Set directory access controls to prevent file writes to the search paths for applications, both in the folders where applications are run from and the standard library folders. |
| [[kb/mitre/attack/mitigations/M1024-restrict-registry-permissions\|M1024]] | Restrict Registry Permissions | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation. |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Adversaries may use new payloads to execute this technique. Identify and block potentially malicious software executed through hijacking by using application control solutions also capable of blocking libraries loaded by legitimate software. |
| [[kb/mitre/attack/mitigations/M1040-behavior-prevention-on-endpoint\|M1040]] | Behavior Prevention on Endpoint | Some endpoint security solutions can be configured to block some types of behaviors related to process injection/memory tampering based on common sequences of indicators (ex: execution of specific API functions). |
| [[kb/mitre/attack/mitigations/M1044-restrict-library-loading\|M1044]] | Restrict Library Loading | Disallow loading of remote DLLs. This is included by default in Windows Server 2012+ and is available by patch for XP+ and Server 2003+.<br><br>Enable Safe DLL Search Mode to force search for system DLLs in directories with greater restrictions (e.g. `%SYSTEMROOT%`)to be used before local directory DLLs (e.g. a user's home directory)<br><br>The Safe DLL Search Mode can be enabled via Group Policy at Computer Configuration > [Policies] > Administrative Templates > MSS (Legacy): MSS: (SafeDllSearchMode) Enable Safe DLL search mode. The associated Windows Registry key for this is located at `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\SafeDLLSearchMode`[^1] [^2]  |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Use auditing tools capable of detecting hijacking opportunities on systems within an enterprise and correct them. Toolkits like the PowerSploit framework contain PowerUp modules that can be used to explore systems for hijacking weaknesses.[^4] <br><br>Use the program sxstrace.exe that is included with Windows along with manual inspection to check manifest files for side-loading vulnerabilities in software.<br><br>Find and eliminate path interception weaknesses in program configuration files, scripts, the PATH environment variable, services, and in shortcuts by surrounding PATH variables with quotation marks when functions allow for them. Be aware of the search order Windows uses for executing or loading binaries and use fully qualified paths wherever appropriate.<br><br>Clean up old Windows Registry keys when software is uninstalled to avoid keys with no associated legitimate binaries. Periodically search for and correct or report path interception weaknesses on systems that may have been introduced using custom or available tools that report software using insecure path configurations.[^2] [^3] [^1]  |
| [[kb/mitre/attack/mitigations/M1051-update-software\|M1051]] | Update Software | Update software regularly to include patches that fix DLL side-loading vulnerabilities. |
| [[kb/mitre/attack/mitigations/M1052-user-account-control\|M1052]] | User Account Control | Turn off UAC's privilege elevation for standard users `[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]` to automatically deny elevation requests, add: `"ConsentPromptBehaviorUser"=dword:00000000`. Consider enabling installer detection for all users by adding: `"EnableInstallerDetection"=dword:00000001`. This will prompt for a password for installation and also log the attempt. To disable installer detection, instead add: `"EnableInstallerDetection"=dword:00000000`. This may prevent potential elevation of privileges through exploitation during the process of UAC detecting the installer, but will allow the installation process to continue without being logged.  [^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1574.007-path-interception-by-path-environment-variable\|T1574.007]] | Path Interception by PATH Environment Variable |
| [[kb/mitre/attack/techniques/T1574.011-services-registry-permissions-weakness\|T1574.011]] | Services Registry Permissions Weakness |
| [[kb/mitre/attack/techniques/T1574.001-dll\|T1574.001]] | DLL |
| [[kb/mitre/attack/techniques/T1574.014-appdomainmanager\|T1574.014]] | AppDomainManager |
| [[kb/mitre/attack/techniques/T1574.008-path-interception-by-search-order-hijacking\|T1574.008]] | Path Interception by Search Order Hijacking |
| [[kb/mitre/attack/techniques/T1574.006-dynamic-linker-hijacking\|T1574.006]] | Dynamic Linker Hijacking |
| [[kb/mitre/attack/techniques/T1574.005-executable-installer-file-permissions-weakness\|T1574.005]] | Executable Installer File Permissions Weakness |
| [[kb/mitre/attack/techniques/T1574.010-services-file-permissions-weakness\|T1574.010]] | Services File Permissions Weakness |
| [[kb/mitre/attack/techniques/T1574.013-kernelcallbacktable\|T1574.013]] | KernelCallbackTable |
| [[kb/mitre/attack/techniques/T1574.009-path-interception-by-unquoted-path\|T1574.009]] | Path Interception by Unquoted Path |
| [[kb/mitre/attack/techniques/T1574.004-dylib-hijacking\|T1574.004]] | Dylib Hijacking |
| [[kb/mitre/attack/techniques/T1574.012-cor-profiler\|T1574.012]] | COR_PROFILER |

 [^1]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^2]: [Executable Installers are Vulnerable](https://seclists.org/fulldisclosure/2015/Dec/34)
 [^3]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
 [^4]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
 [^5]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
 [^6]: [Microsoft More information about DLL](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)
 [^7]: [Microsoft Dynamic Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)
 [^8]: [Vulnerability and Exploit Detector](https://skanthak.homepage.t-online.de/sentinel.html)
 [^9]: [Microsoft CreateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)
 [^10]: [Microsoft Dynamic-Link Library Security](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)
 [^11]: [Powersploit](https://github.com/mattifestation/PowerSploit)
 [^12]: [FireEye DLL Side-Loading](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)
 [^13]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^14]: [TrendMicro RaspberryRobin 2022](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
 [^15]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
 [^16]: [Symantec Daggerfly 2024](https://symantec-enterprise-blogs.security.com/threat-intelligence/daggerfly-espionage-updated-toolset)
 [^17]: [NCSC-NL COATHANGER Feb 2024](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)
 [^18]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
