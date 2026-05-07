---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1685
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/containers
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1685-disable-or-modify-tools
tactic:
    - Defense Impairment
platforms:
    - Containers
    - ESXi
    - IaaS
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may disable, degrade, or tamper with security tools or applications (e.g., endpoint detection and response (EDR) tools, intrusion detection systems (IDS), antivirus, logging agents, sensors, etc.) to impair or reduce visibility of defensive capabilities. This may include stopping specific services, killing processes, modifying or deleting tool configuration files and Registry keys, or preventing tools from updating. This may also include impairing defenses more broadly by disrupting preventative, detection, and response mechanisms across host, network, and cloud environments.[^4]  <br><br>In addition to directly targeting tools, adversaries may block or manipulate indicators and telemetry used for detection. This includes maliciously disabling or redirecting sensors such as Event Tracing for Windows (ETW), modifying event log configurations (e.g., redirecting Security logs), or interfering with logging pipelines and forwarding mechanisms (e.g., SIEM ingestion).[^2] [^3] <br><br>More advanced techniques include leveraging legitimate drivers or debugging mechanisms to render tools non-functional, bypassing anti-tampering protections, and targeting specific defenses such as Sysmon or cloud monitoring agents. Adversaries may also disrupt broader defensive operations, including update mechanisms, logging infrastructure (e.g., syslog), or event aggregation, further degrading an organization’s ability to detect and respond to malicious activity.[^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0004](https://attack.mitre.org/software/S0004) | TinyZBot | TinyZBot can disable Avira anti-virus.[^1]  |
| [S0058](https://attack.mitre.org/software/S0058) | SslMM | SslMM identifies and kills anti-malware processes.[^1]  |
| [S0061](https://attack.mitre.org/software/S0061) | HDoor | HDoor kills anti-virus found on the victim.[^1]  |
| [S0130](https://attack.mitre.org/software/S0130) | Unknown Logger | Unknown Logger has functionality to disable security tools, including Kaspersky, BitDefender, and MalwareBytes.[^1]  |
| [S0132](https://attack.mitre.org/software/S0132) | H1N1 | H1N1 kills and disables services for Windows Security Center, and Windows Defender.[^1]  |
| [S0144](https://attack.mitre.org/software/S0144) | ChChes | ChChes can alter the victim's proxy configuration.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike has the ability to use Smart Applet attacks to disable the Java SecurityManager sandbox.[^1] [^2]  |
| [S0201](https://attack.mitre.org/software/S0201) | JPIN | JPIN can lower security settings by changing Registry keys.[^1]  |
| [S0223](https://attack.mitre.org/software/S0223) | POWERSTATS | POWERSTATS can disable Microsoft Office Protected View by changing Registry keys.[^1]  |
| [S0228](https://attack.mitre.org/software/S0228) | NanHaiShu | NanHaiShu can change Internet Explorer settings to reduce warnings about malware activity.[^1]  |
| [S0249](https://attack.mitre.org/software/S0249) | Gold Dragon | Gold Dragon terminates anti-malware processes if they’re found running on the system.[^1]  |
| [S0252](https://attack.mitre.org/software/S0252) | Brave Prince | Brave Prince terminates antimalware processes.[^1]  |
| [S0253](https://attack.mitre.org/software/S0253) | RunningRAT | RunningRAT kills antimalware running process.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot can disable Windows Defender.[^1]  |
| [S0279](https://attack.mitre.org/software/S0279) | Proton | Proton kills security tools like Wireshark that are running.[^1]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla has the capability to kill any running analysis processes and AV software.[^1]  |
| [S0334](https://attack.mitre.org/software/S0334) | DarkComet | DarkComet can disable Security Center functions like anti-virus.[^1] [^2]  |
| [S0336](https://attack.mitre.org/software/S0336) | NanoCore | NanoCore can modify the victim's anti-virus.[^1] [^2]  |
| [S0372](https://attack.mitre.org/software/S0372) | LockerGoga | LockerGoga installation has been immediately preceded by a "task kill" command in order to disable anti-virus.[^1]  |
| [S0377](https://attack.mitre.org/software/S0377) | Ebury | Ebury can disable SELinux Role-Based Access Control and deactivate PAM modules.[^1]  |
| [S0400](https://attack.mitre.org/software/S0400) | RobbinHood | RobbinHood will search for Windows services that are associated with antivirus software on the system and kill the process.[^1]   |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell can kill AV products' processes.[^1]   |
| [[kb/mitre/attack/software/S0434-imminent-monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a feature to disable Windows Task Manager.[^1] 	 |
| [S0446](https://attack.mitre.org/software/S0446) | Ryuk | Ryuk has stopped services related to anti-virus.[^1]  |
| [S0449](https://attack.mitre.org/software/S0449) | Maze | Maze has disabled dynamic analysis and other security tools including IDA debugger, x32dbg, and OllyDbg.[^1]  It has also disabled Windows Defender's Real-Time Monitoring feature and attempted to disable endpoint protection services.[^2]  |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo has a function to kill processes associated with defenses and can prevent certain processes from launching.[^1] [^2]   |
| [S0457](https://attack.mitre.org/software/S0457) | Netwalker | Netwalker can detect and terminate active security software-related processes on infected systems.[^1] [^2]  |
| [S0468](https://attack.mitre.org/software/S0468) | Skidmap | Skidmap has the ability to set SELinux to permissive mode.[^1]  |
| [S0477](https://attack.mitre.org/software/S0477) | Goopy | Goopy has the ability to disable Microsoft Outlook's security policies to disable macro warnings.[^1] 	 |
| [S0481](https://attack.mitre.org/software/S0481) | Ragnar Locker | Ragnar Locker has attempted to terminate/stop processes and services associated with endpoint security products.[^1]  |
| [S0482](https://attack.mitre.org/software/S0482) | Bundlore | Bundlore can change browser security settings to enable extensions to be installed. Bundlore uses the `pkill cfprefsd` command to prevent users from inspecting processes.[^1] [^2]  |
| [S0484](https://attack.mitre.org/software/S0484) | Carberp | Carberp has attempted to disable security software by creating a suspended process for the security software and injecting code to delete antivirus core files when the process is resumed.[^1]  |
| [S0491](https://attack.mitre.org/software/S0491) | StrongPity | StrongPity can add directories used by the malware to the Windows Defender exclusions list to prevent detection.[^1]  |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil can connect to and disable the Symantec server on the victim's network.[^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can hook APIs, kill processes, break file system paths, and change ACLs to prevent security tools from running.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar has manually loaded ntdll from disk in order to identity and remove API hooks set by security products.[^1] 	 |
| [S0554](https://attack.mitre.org/software/S0554) | Egregor | Egregor has disabled Windows Defender to evade protections.[^1]  |
| [S0559](https://attack.mitre.org/software/S0559) | SUNBURST | SUNBURST attempted to disable software security services following checks against a FNV-1a + XOR hashed hardcoded blocklist.[^1]  |
| [S0576](https://attack.mitre.org/software/S0576) | MegaCortex | MegaCortex was used to kill endpoint security processes.[^1]  |
| [S0579](https://attack.mitre.org/software/S0579) | Waterbear | Waterbear can hook the `ZwOpenProcess` and `GetExtendedTcpTable` APIs called by the process of a security product to hide PIDs and TCP records from detection.[^1]  |
| [S0583](https://attack.mitre.org/software/S0583) | Pysa | Pysa has the capability to stop antivirus services and disable Windows Defender.[^1]   |
| [S0595](https://attack.mitre.org/software/S0595) | ThiefQuest | ThiefQuest uses the function `kill_unwanted` to obtain a list of running processes and kills each process matching a list of security related processes.[^1]  |
| [S0601](https://attack.mitre.org/software/S0601) | Hildegard | Hildegard has modified DNS resolvers to evade DNS monitoring tools.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet reduces the integrity level of objects to allow write actions.[^1]  |
| [S0605](https://attack.mitre.org/software/S0605) | EKANS | EKANS stops processes related to security and management software.[^1] [^2]  |
| [S0608](https://attack.mitre.org/software/S0608) | Conficker | Conficker terminates various services related to system security and Windows.[^1]  |
| [S0611](https://attack.mitre.org/software/S0611) | Clop | Clop can uninstall or disable security products.[^1]  |
| [S0638](https://attack.mitre.org/software/S0638) | Babuk | Babuk can stop anti-virus services on a compromised host.[^1]  |
| [S0640](https://attack.mitre.org/software/S0640) | Avaddon | Avaddon looks for and attempts to stop anti-malware solutions.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot has the ability to modify the Registry to add its binaries to the Windows Defender exclusion list.[^1]  |
| [S0659](https://attack.mitre.org/software/S0659) | Diavol | Diavol can attempt to stop security software.[^1]  |
| [S0669](https://attack.mitre.org/software/S0669) | KOCTOPUS | KOCTOPUS will attempt to delete or disable all Registry keys and scheduled tasks related to Microsoft Security Defender and Security Essentials.[^1]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT can disarm Windows Defender during the UAC process to evade detection.[^1]  |
| [S0688](https://attack.mitre.org/software/S0688) | Meteor | Meteor can attempt to uninstall Kaspersky Antivirus or remove the Kaspersky license; it can also add all files and folders related to the attack to the Windows Defender exclusion list.[^1]  |
| [S0689](https://attack.mitre.org/software/S0689) | WhisperGate | WhisperGate can download and execute AdvancedRun.exe to disable the Windows Defender Theat Protection service and set an exclusion path for the C:\ drive.[^2] [^1] [^3]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]]'s `amsiPatch.py` module can disable Antimalware Scan Interface (AMSI) functions.[^1]  |
| [[kb/mitre/attack/software/S0695-donut\|S0695]] | Donut | [[kb/mitre/attack/software/S0695-donut\|Donut]] can patch Antimalware Scan Interface (AMSI), Windows Lockdown Policy (WLDP), as well as exit-related [[kb/mitre/attack/techniques/T1106-native-api\|Native API]] functions to avoid process termination.[^1] 	 |
| [S0697](https://attack.mitre.org/software/S0697) | HermeticWiper | HermeticWiper has the ability to set the `HKLM:\SYSTEM\\CurrentControlSet\\Control\\CrashControl\CrashDumpEnabled` Registry key to `0` in order to disable crash dumps.[^1] [^2] [^3]  |
| [S1048](https://attack.mitre.org/software/S1048) | macOS.OSAMiner | macOS.OSAMiner has searched for the Activity Monitor process in the System Events process list and kills the process if running. macOS.OSAMiner also searches the operating system's `install.log` for apps matching its hardcoded list, killing all matching process names.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has the ability to hide memory artifacts and to patch Event Tracing for Windows (ETW) and the Anti Malware Scan Interface (AMSI).[^2] [^1]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT has suppressed all error reporting by calling `SetErrorMode` with 0x8007 as a parameter.[^1]  |
| [S1097](https://attack.mitre.org/software/S1097) | HUI Loader | HUI Loader has the ability to disable Windows Event Tracing for Windows (ETW) and Antimalware Scan Interface (AMSI) functions.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate will terminate processes associated with several security software products if identified during execution.[^1]  |
| [S1114](https://attack.mitre.org/software/S1114) | ZIPLINE |  ZIPLINE can add itself to the exclusion list for the Ivanti Connect Secure Integrity Checker Tool if the `--exclude` parameter is passed by the `tar` process.[^1]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin can add an exception to Microsoft Defender that excludes the entire main drive from anti-malware scanning to evade detection.[^1]  |
| [S1135](https://attack.mitre.org/software/S1135) | MultiLayer Wiper | MultiLayer Wiper removes the Volume Shadow Copy (VSS) service from infected devices along with all present shadow copies.[^1]  |
| [S1169](https://attack.mitre.org/software/S1169) | Mango | Mango contains an unused capability to block endpoint security solutions from loading user-mode code hooks via a DLL in a specified process by using the `UpdateProcThreadAttribute API` to set the `PROC_THREAD_ATTRIBUTE_MITIGATION_POLICY` to `PROCESS_CREATION_MITIGATION_POLICY_BLOCK_NON_MICROSOFT_BINARIES_ALWAYS_ON` for an identified process. [^1]  |
| [S1178](https://attack.mitre.org/software/S1178) | ShrinkLocker | ShrinkLocker disables protectors used to secure the BitLocker encryption key on victim systems.[^1] [^2]  |
| [S1180](https://attack.mitre.org/software/S1180) | BlackByte Ransomware | BlackByte Ransomware adds .JS and .EXE extensions to the Microsoft Defender exclusion list. BlackByte Ransomware terminates and removes the Raccine anti-ransomware utility.[^1]  |
| [S1184](https://attack.mitre.org/software/S1184) | BOLDMOVE | BOLDMOVE can disable the Fortinet daemons `moglogd` and `syslogd` to evade detection and logging.[^1]  |
| [S1199](https://attack.mitre.org/software/S1199) | LockBit 2.0 | LockBit 2.0 can disable firewall rules and anti-malware and monitoring software including Windows Defender.[^2] [^1]  |
| [S1200](https://attack.mitre.org/software/S1200) | StealBit | StealBit can configure processes to not display certain Windows error messages by through use of the `NtSetInformationProcess`.[^1]  |
| [S1202](https://attack.mitre.org/software/S1202) | LockBit 3.0 | LockBit 3.0 can disable security tools to evade detection including Windows Defender.[^1] [^2] [^3]  |
| [S1206](https://attack.mitre.org/software/S1206) | JumbledPath | JumbledPath can impair logging on all devices used along its connection path to compromised hosts.[^1]  |
| [S1207](https://attack.mitre.org/software/S1207) | XLoader | XLoader loads a copy of NTDLL to evade hooks from security monitoring tools on this library.[^2]  XLoader can add the path of its executable to the Microsoft Defender exclusion list.[^1]  |
| [S1213](https://attack.mitre.org/software/S1213) | Lumma Stealer | Lumma Stealer has attempted to bypass Windows Antimalware Scan Interface (AMSI) by removing the string “AmsiScanBuffer” from the “clr.dll” module in memory to prevent it from being called.[^1]  |
| [S1234](https://attack.mitre.org/software/S1234) | SplatCloak | SplatCloak has identified and disabled API callback features of Windows Defender and Kaspersky.[^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer can disable security software and update services.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can terminate antivirus-related processes and services.[^3] [^4] [^2] [^1] <br><br> |
| [S1244](https://attack.mitre.org/software/S1244) | Medusa Ransomware | Medusa Ransomware has terminated antivirus services utilizing the gaze.exe executable.[^1]  Medusa Ransomware has also terminated antivirus services utilizing PowerShell scripts.[^1] [^2]  |
| [S9008](https://attack.mitre.org/software/S9008) | Shai-Hulud | Shai-Hulud has replaced DNS configuration from `/tmp/resolved.conf` in order to gain control of network-level control within CI environments and has flushed iptables rules using `sudo iptables -F OUTPUT` and `sudo iptables -F DOCKER-USER`.[^1]  |
| [S9013](https://attack.mitre.org/software/S9013) | DRYHOOK | DRYHOOK has killed all instances of the `cgi-server` process in order for the modified Perl module to be activated.[^1]  |
| [S9014](https://attack.mitre.org/software/S9014) | PHASEJAM | PHASEJAM has modified Ivanti Connect Secure appliances and blocks the system upgrades by altering the DSUpgrade.pm file.[^1]  |
| [[kb/mitre/attack/software/S9017-dcrat\|S9017]] | DCRAT | [[kb/mitre/attack/software/S9017-dcrat\|DCRAT]] can patch Microsoft’s Antimalware Scan Interface (AMSI) to evade detection.[^1]  |
| [S9019](https://attack.mitre.org/software/S9019) | PureCrypter | PureCrypter has executed `Set-MpPreference -ExclusionPath` to exclude files or folders from Windows Defender scans.[^1]  |
| [S9024](https://attack.mitre.org/software/S9024) | SPAWNCHIMERA | SPAWNCHIMERA has modified the Ivanti Integrity Checker Tool to evade detection.[^1] [^2]  |
| [S9039](https://attack.mitre.org/software/S9039) | LazyWiper | LazyWiper can disable Microsoft Windows Defender Real-Time Monitoring with the `Set-MpPreference` cmdlet.[^1]    |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Ensure proper user permissions are in place to prevent adversaries from disabling or interfering with security services. |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | Ensure proper process and file permissions are in place to prevent adversaries from disabling or interfering with security services. |
| [[kb/mitre/attack/mitigations/M1024-restrict-registry-permissions\|M1024]] | Restrict Registry Permissions | Ensure proper Registry permissions are in place to prevent adversaries from disabling or interfering with security services. |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | Use application control where appropriate, especially regarding the execution of tools outside of the organization's security policies (such as rootkit removal tools) that have been abused to impair system defenses. Ensure that only approved security applications are used and running on enterprise systems. |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Consider removing previous versions of tools that are unnecessary to the environment when possible. |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Periodically verify that tools are functioning appropriately – for example, that all expected hosts with EDRs or monitoring agents are checking in to the central console. Check EDRs to ensure that no unexpected exclusion paths have been added. In Microsoft Defender for Endpoint, exclusions can be reviewed with the `Get-MpPreference` cmdlet.[^1]  |
| [[kb/mitre/attack/mitigations/M1054-software-configuration\|M1054]] | Software Configuration | Consider automatically relaunching forwarding mechanisms at recurring intervals (ex: temporal, on-logon, etc.) as well as applying appropriate change management to firewall rules and other related system configurations. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1685.003-modify-or-spoof-tool-ui\|T1685.003]] | Modify or Spoof Tool UI |
| [[kb/mitre/attack/techniques/T1685.001-disable-or-modify-windows-event-log\|T1685.001]] | Disable or Modify Windows Event Log |
| [[kb/mitre/attack/techniques/T1685.004-disable-or-modify-linux-audit-system-log\|T1685.004]] | Disable or Modify Linux Audit System Log |
| [[kb/mitre/attack/techniques/T1685.002-disable-or-modify-cloud-log\|T1685.002]] | Disable or Modify Cloud Log |
| [[kb/mitre/attack/techniques/T1685.006-clear-linux-or-mac-system-logs\|T1685.006]] | Clear Linux or Mac System Logs |
| [[kb/mitre/attack/techniques/T1685.005-clear-windows-event-logs\|T1685.005]] | Clear Windows Event Logs |

 [^1]: [Cocomazzi FIN7 Reboot](https://www.sentinelone.com/labs/fin7-reboot-cybercrime-gang-enhances-ops-with-new-edr-bypasses-and-automated-attacks/)
 [^2]: [Microsoft Lamin Sept 2017](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?name=Backdoor:Win32/Lamin.A)
 [^3]: [ETW Palantir](https://blog.palantir.com/tampering-with-windows-event-tracing-background-offense-and-defense-4be7ac62ac63)
 [^4]: [SCADAfence_ransomware](https://cdn.logic-control.com/docs/scadafence/Anatomy-Of-A-Targeted-Ransomware-Attack-WP.pdf)
 [^5]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
 [^6]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
 [^7]: [SentinelLabs reversing run-only applescripts 2021](https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/)
 [^8]: [IBM MegaCortex](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
 [^9]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
 [^10]: [Sogeti CERT ESEC Babuk March 2021](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
 [^11]: [HP RaspberryRobin 2024](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
 [^12]: [SentinelOne Hermetic Wiper February 2022](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)
 [^13]: [Crowdstrike DriveSlayer February 2022](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
 [^14]: [Qualys Hermetic Wiper March 2022](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
 [^15]: [Sophos Ragnar May 2020](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)
 [^16]: [Cisco Ukraine Wipers January 2022](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
 [^17]: [Unit 42 WhisperGate January 2022](https://unit42.paloaltonetworks.com/ukraine-cyber-conflict-cve-2021-32648-whispergate/#whispergate-malware-family)
 [^18]: [Medium S2W WhisperGate January 2022](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)
 [^19]: [TrendMicro Netwalker May 2020](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
 [^20]: [Sophos Netwalker May 2020](https://news.sophos.com/en-us/2020/05/27/netwalker-ransomware-tools-give-insight-into-threat-actor/)
 [^21]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
 [^22]: [Netskope XLoader 2022](https://www.netskope.com/blog/new-formbook-campaign-delivered-through-phishing-emails)
 [^23]: [Zscaler XLoader 2025](https://www.zscaler.com/blogs/security-research/technical-analysis-xloader-versions-6-and-7-part-1)
 [^24]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
 [^25]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
 [^26]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^27]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
 [^28]: [CERT Polska](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
 [^29]: [Cylance Cleaver](https://web.archive.org/web/20200302085133/https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance_Operation_Cleaver_Report.pdf)
 [^30]: [Palo Alto Lockbit 2.0 JUN 2022](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)
 [^31]: [FBI Lockbit 2.0 FEB 2022](https://www.ic3.gov/CSA/2022/220204.pdf)
 [^32]: [Proofpoint Leviathan Oct 2017](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
 [^33]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
 [^34]: [Trend Micro Skidmap](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)
 [^35]: [Cisco Salt Typhoon FEB 2025](https://blog.talosintelligence.com/salt-typhoon-analysis/)
 [^36]: [Socket Shai-Hulud November 2025](https://socket.dev/blog/shai-hulud-strikes-again-v2)
 [^37]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^38]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
 [^39]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
 [^40]: [CodeX Microsoft Defender 2021](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)
 [^41]: [Arxiv Avaddon Feb 2021](https://arxiv.org/pdf/2102.04796.pdf)
 [^42]: [Joint Cybersecurity Advisory LockBit JUN 2023](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)
 [^43]: [Joint Cybersecurity Advisory LockBit 3.0 MAR 2023](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
 [^44]: [INCIBE-CERT LockBit MAR 2024](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)
 [^45]: [DigiTrust NanoCore Jan 2017](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)
 [^46]: [PaloAlto NanoCore Feb 2016](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)
 [^47]: [CERT-FR PYSA April 2020](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)
 [^48]: [wardle evilquest parti](https://objective-see.com/blog/blog_0x59.html)
 [^49]: [FireEye SUNBURST Additional Details Dec 2020](https://www.fireeye.com/blog/threat-research/2020/12/sunburst-additional-technical-details.html)
 [^50]: [Check Point Meteor Aug 2021](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
 [^51]: [Imminent Unit42 Dec2019](https://unit42.paloaltonetworks.com/imminent-monitor-a-rat-down-under/)
 [^52]: [Cylance Sodinokibi July 2019](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
 [^53]: [Cybereason Cobalt Kitty 2017](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
 [^54]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)
 [^55]: [MacKeeper Bundlore Apr 2019](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)
 [^56]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
 [^57]: [Netskope LummaStealer 2025](https://www.netskope.com/blog/lumma-stealer-fake-captchas-new-techniques-to-evade-detection)
 [^58]: [Wired Lockergoga 2019](https://www.wired.com/story/lockergoga-ransomware-crippling-industrial-firms/)
 [^59]: [ESET OilRig Campaigns Sep 2023](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
 [^60]: [MDSec Brute Ratel August 2022](https://www.mdsec.co.uk/2022/08/part-3-how-i-met-your-beacon-brute-ratel/)
 [^61]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^62]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
 [^63]: [Intrinsec Egregor Nov 2020](https://www.intrinsec.com/egregor-prolock/?cn-reloaded=1)
 [^64]: [CarbonBlack RobbinHood May 2019](https://www.carbonblack.com/2019/05/17/cb-tau-threat-intelligence-notification-robbinhood-ransomware-stops-181-windows-services-before-encryption/)
 [^65]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
 [^66]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
 [^67]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^68]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
 [^69]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)
 [^70]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
 [^71]: [FireEye Ryuk and Trickbot January 2019](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)
 [^72]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^73]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
 [^74]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
 [^75]: [Trend Micro Trickbot Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-shows-off-new-trick-password-grabber-module/)
 [^76]: [Talos Promethium June 2020](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)
 [^77]: [Donut Github](https://github.com/TheWover/donut)
 [^78]: [McAfee Maze March 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
 [^79]: [Sophos Maze VM September 2020](https://news.sophos.com/en-us/2020/09/17/maze-attackers-adopt-ragnar-locker-virtual-machine-technique/)
 [^80]: [Fortinet Agent Tesla June 2017](https://www.fortinet.com/blog/threat-research/in-depth-analysis-of-net-malware-javaupdtr.html)
 [^81]: [TrendMicro DarkComet Sept 2014](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)
 [^82]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
 [^83]: [Prevx Carberp March 2011](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
 [^84]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^85]: [SecureWorks BRONZE STARLIGHT Ransomware Operations June 2022](https://www.secureworks.com/research/bronze-starlight-ransomware-operations-use-hui-loader)
 [^86]: [Kaspersky ShrinkLocker 2024](https://securelist.com/ransomware-abuses-bitlocker/112643/)
 [^87]: [Splunk ShrinkLocker 2024](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
 [^88]: [ESET Ebury Oct 2017](https://www.welivesecurity.com/2017/10/30/windigo-ebury-update-2/)
 [^89]: [Zscaler BlindEagle DEC 2025](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)
 [^90]: [Medium Metamorfo Apr 2020](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
 [^91]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
 [^92]: [Cisco H1N1 Part 2](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)
 [^93]: [SANS Conficker](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)
 [^94]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
 [^95]: [Google Cloud BOLDMOVE 2023](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)
 [^96]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
 [^97]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
 [^98]: [Picus Qilin MAR 2025](https://www.picussecurity.com/resource/blog/qilin-ransomware)
 [^99]: [Halcyon Qilin.B OCT 2024](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
 [^100]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
 [^101]: [SentinelOne Qilin NOV 2022](https://www.sentinelone.com/anthology/agenda-qilin/)
 [^102]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
 [^103]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
 [^104]: [Unit42 Agrius 2023](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
 [^105]: [Cybereason Clop Dec 2020](https://www.cybereason.com/blog/cybereason-vs.-clop-ransomware)
 [^106]: [CISA SPAWNCHIMERA RESURGE February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)
 [^107]: [Picus Security UNC5221 Ivanti May 2025](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)
 [^108]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)
 [^109]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
 [^110]: [Dragos EKANS](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)
 [^111]: [FireEye Ransomware Feb 2020](https://www.fireeye.com/blog/threat-research/2020/02/ransomware-against-machine-learning-to-disrupt-industrial-production.html)
