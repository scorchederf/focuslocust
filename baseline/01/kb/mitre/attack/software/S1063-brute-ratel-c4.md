---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S1063
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S1063-brute-ratel-c4
---

## Description

[[kb/mitre/attack/software/S1063-brute-ratel-c4|Brute Ratel C4]] is a commercial red-teaming and adversarial attack simulation tool that first appeared in December 2020. [[kb/mitre/attack/software/S1063-brute-ratel-c4|Brute Ratel C4]] was specifically designed to avoid detection by endpoint detection and response (EDR) and antivirus (AV) capabilities, and deploys agents called badgers to enable arbitrary command execution for lateral movement, privilege escalation, and persistence. In September 2022, a cracked version of [[kb/mitre/attack/software/S1063-brute-ratel-c4|Brute Ratel C4]] was leaked in the cybercriminal underground, leading to its use by threat actors.[^2] [^3] [^1] [^5] [^4] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1005-data-from-local-system\|T1005]] | Data from Local System | <br>[[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has the ability to upload files from a compromised system.[^1]  |
| [[kb/mitre/attack/techniques/T1021-remote-services\|T1021]] | Remote Services | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has the ability to use RPC for lateral movement.[^1]  |
| [[kb/mitre/attack/techniques/T1021.002-smb-windows-admin-shares\|T1021.002]] | SMB/Windows Admin Shares | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has the ability to use SMB to pivot in compromised networks.[^3] [^1] [^2]  |
| [[kb/mitre/attack/techniques/T1021.006-windows-remote-management\|T1021.006]] | Windows Remote Management | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can use WinRM for pivoting.[^1]  |
| [[kb/mitre/attack/techniques/T1027-obfuscated-files-or-information\|T1027]] | Obfuscated Files or Information | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has used encrypted payload files and maintains an encrypted configuration structure in memory.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1027.007-dynamic-api-resolution\|T1027.007]] | Dynamic API Resolution | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can call and dynamically resolve hashed APIs.[^1]  |
| [[kb/mitre/attack/techniques/T1036.005-match-legitimate-resource-name-or-location\|T1036.005]] | Match Legitimate Resource Name or Location | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has used a payload file named OneDrive.update to appear benign.[^1]  |
| [[kb/mitre/attack/techniques/T1036.008-masquerade-file-type\|T1036.008]] | Masquerade File Type | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has used Microsoft Word icons to hide malicious LNK files.[^1]  |
| [[kb/mitre/attack/techniques/T1046-network-service-discovery\|T1046]] | Network Service Discovery | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can conduct port scanning against targeted systems.[^1]  |
| [[kb/mitre/attack/techniques/T1047-windows-management-instrumentation\|T1047]] | Windows Management Instrumentation | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can use WMI to move laterally.[^1]  |
| [[kb/mitre/attack/techniques/T1055.002-portable-executable-injection\|T1055.002]] | Portable Executable Injection | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has injected Latrodectus into the Explorer.exe process on comrpomised hosts.[^1]  |
| [[kb/mitre/attack/techniques/T1057-process-discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can enumerate all processes and locate specific process IDs (PIDs).[^1]  |
| [[kb/mitre/attack/techniques/T1059.003-windows-command-shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can use cmd.exe for execution.[^1]  |
| [[kb/mitre/attack/techniques/T1069.002-domain-groups\|T1069.002]] | Domain Groups | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can use `net group` for discovery on targeted domains.[^1]  |
| [[kb/mitre/attack/techniques/T1071.001-web-protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can use HTTPS and HTTPS for C2 communication.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1071.004-dns\|T1071.004]] | DNS | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can use DNS over HTTPS for C2.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1087.002-domain-account\|T1087.002]] | Domain Account | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can use LDAP queries, `net group "Domain Admins" /domain` and `net user /domain` for discovery.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1095-non-application-layer-protocol\|T1095]] | Non-Application Layer Protocol | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has the ability to use TCP for external C2.[^1]  |
| [[kb/mitre/attack/techniques/T1102-web-service\|T1102]] | Web Service | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can use legitimate websites for external C2 channels including Slack, Discord, and MS Teams.[^1]  |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | <br>[[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can download files to compromised hosts.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1106-native-api\|T1106]] | Native API | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can call multiple Windows APIs for execution, to share memory, and defense evasion.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1113-screen-capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can take screenshots on compromised hosts.[^1]  |
| [[kb/mitre/attack/techniques/T1140-deobfuscate-decode-files-or-information\|T1140]] | Deobfuscate/Decode Files or Information | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has the ability to deobfuscate its payload prior to execution.[^1]  |
| [[kb/mitre/attack/techniques/T1204.002-malicious-file\|T1204.002]] | Malicious File | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has gained execution through users opening malicious documents.[^1]  |
| [[kb/mitre/attack/techniques/T1482-domain-trust-discovery\|T1482]] | Domain Trust Discovery | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can use LDAP queries and `nltest /domain_trusts` for domain trust discovery.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1497.003-time-based-checks\|T1497.003]] | Time Based Checks | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can call `NtDelayExecution` to pause execution.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1518.001-security-software-discovery\|T1518.001]] | Security Software Discovery | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can detect EDR userland hooks.[^1]  |
| [[kb/mitre/attack/techniques/T1558.003-kerberoasting\|T1558.003]] | Kerberoasting | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can decode Kerberos 5 tickets and convert it to hashcat format for subsequent cracking.[^1]  |
| [[kb/mitre/attack/techniques/T1569.002-service-execution\|T1569.002]] | Service Execution | <br>[[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can create Windows system services for execution.[^1]  |
| [[kb/mitre/attack/techniques/T1572-protocol-tunneling\|T1572]] | Protocol Tunneling | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can use DNS over HTTPS for C2.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1574.001-dll\|T1574.001]] | DLL | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has used search order hijacking to load a malicious payload DLL as a dependency to a benign application packaged in the same ISO.[^1]  [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has loaded a malicious DLL by spoofing the name of the legitimate Version.DLL and placing it in the same folder as the digitally-signed Microsoft binary OneDriveUpdater.exe.[^1]  |
| [[kb/mitre/attack/techniques/T1620-reflective-code-loading\|T1620]] | Reflective Code Loading | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has used reflective loading to execute malicious DLLs.[^1]  |
| [[kb/mitre/attack/techniques/T1685-disable-or-modify-tools\|T1685]] | Disable or Modify Tools | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has the ability to hide memory artifacts and to patch Event Tracing for Windows (ETW) and the Anti Malware Scan Interface (AMSI).[^2] [^1]  |

 [^1]: [MDSec Brute Ratel August 2022](https://www.mdsec.co.uk/2022/08/part-3-how-i-met-your-beacon-brute-ratel/)
 [^2]: [Dark Vortex Brute Ratel C4](https://bruteratel.com/)
 [^3]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^4]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
 [^5]: [SANS Brute Ratel October 2022](https://www.sans.org/blog/cracked-brute-ratel-c4-framework-proliferates-across-the-cybercriminal-underground/)
 [^6]: [Rapid7 Fake W2 July 2024](https://www.rapid7.com/blog/post/2024/07/24/malware-campaign-lures-users-with-fake-w2-form/)
