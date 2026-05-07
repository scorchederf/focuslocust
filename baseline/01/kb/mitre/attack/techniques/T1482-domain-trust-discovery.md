---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1482
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1482-domain-trust-discovery
tactic:
    - Discovery
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to gather information on domain trust relationships that may be used to identify lateral movement opportunities in Windows multi-domain/forest environments. Domain trusts provide a mechanism for a domain to allow access to resources based on the authentication procedures of another domain.[^3]  Domain trusts allow the users of the trusted domain to access resources in the trusting domain. The information discovered may help the adversary conduct [[kb/mitre/attack/techniques/T1134.005-sid-history-injection|SID-History Injection]], [[kb/mitre/attack/techniques/T1550.003-pass-the-ticket|Pass the Ticket]], and [[kb/mitre/attack/techniques/T1558.003-kerberoasting|Kerberoasting]].[^2] [^5]  Domain trusts can be enumerated using the `DSEnumerateDomainTrusts()` Win32 API call, .NET methods, and LDAP.[^5]  The Windows utility [[kb/mitre/attack/software/S0359-nltest|Nltest]] is known to be used by adversaries to enumerate domain trusts.[^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0105-dsquery\|S0105]] | dsquery | [[kb/mitre/attack/software/S0105-dsquery\|dsquery]] can be used to gather information on domain trusts with `dsquery * -filter "(objectClass=trustedDomain)" -attr *`.[^1]  |
| [[kb/mitre/attack/software/S0194-powersploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] has modules such as `Get-NetDomainTrust` and `Get-NetForestTrust` to enumerate domain and forest trusts.[^1] [^2]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot can gather information about domain trusts by utilizing [[kb/mitre/attack/software/S0359-nltest\|Nltest]].[^1] [^2]  |
| [[kb/mitre/attack/software/S0359-nltest\|S0359]] | Nltest | [[kb/mitre/attack/software/S0359-nltest\|Nltest]] may be used to enumerate trusted domains by using commands such as `nltest /domain_trusts`.[^1] [^2]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] has modules for enumerating domain trusts.[^1]  |
| [[kb/mitre/attack/software/S0378-poshc2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] has modules for enumerating domain trusts.[^1]  |
| [S0483](https://attack.mitre.org/software/S0483) | IcedID | IcedID used [[kb/mitre/attack/software/S0359-nltest\|Nltest]] during initial discovery.[^1] [^2]  |
| [[kb/mitre/attack/software/S0521-bloodhound\|S0521]] | BloodHound | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] has the ability to map domain trusts and identify misconfigurations for potential abuse.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can use [[kb/mitre/attack/software/S0359-nltest\|Nltest]] tools to obtain information about the domain.[^1] [^2]  |
| [[kb/mitre/attack/software/S0552-adfind\|S0552]] | AdFind | [[kb/mitre/attack/software/S0552-adfind\|AdFind]] can gather information about organizational units (OUs) and domain trusts from Active Directory.[^1] [^4] [^2] [^3]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can run `nltest /domain_trusts /all_trusts` for domain trust discovery.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can use LDAP queries and `nltest /domain_trusts` for domain trust discovery.[^1] [^2]  |
| [[kb/mitre/attack/software/S1071-rubeus\|S1071]] | Rubeus | [[kb/mitre/attack/software/S1071-rubeus\|Rubeus]] can gather information about domain trusts.[^2] [^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can use `nltest.exe /domain_trusts` to discover domain trust relationships on a compromised machine.[^1]  |
| [S1124](https://attack.mitre.org/software/S1124) | SocGholish | SocGholish can profile compromised systems to identify domain trust relationships.[^1] [^2]  |
| [S1145](https://attack.mitre.org/software/S1145) | Pikabot | Pikabot will gather information concerning the Windows Domain the victim machine is a member of during execution.[^1]  |
| [S1146](https://attack.mitre.org/software/S1146) | MgBot | MgBot includes modules for collecting information on local domain users and permissions.[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP can identify Active Directory information and related items.[^1]  |
| [S1160](https://attack.mitre.org/software/S1160) | Latrodectus | Latrodectus can run `C:\Windows\System32\cmd.exe /c nltest /domain_trusts` to discover domain trusts.[^2] [^1]  |
| [S9035](https://attack.mitre.org/software/S9035) | LAMEHUG | LAMEHUG can gather Active Directory domain information.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Employ network segmentation for sensitive domains.[^1] . |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Map the trusts within existing domains/forests and keep trust relationships to a minimum. |

 [^1]: [Microsoft Operation Wilysupply](https://www.microsoft.com/security/blog/2017/05/04/windows-defender-atp-thwarts-operation-wilysupply-software-supply-chain-cyberattack/)
 [^2]: [AdSecurity Forging Trust Tickets](https://adsecurity.org/?p=1588)
 [^3]: [Microsoft Trusts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc759554(v=ws.10))
 [^4]: [Microsoft GetAllTrustRelationships](https://docs.microsoft.com/en-us/dotnet/api/system.directoryservices.activedirectory.domain.getalltrustrelationships?redirectedfrom=MSDN&view=netframework-4.7.2#System_DirectoryServices_ActiveDirectory_Domain_GetAllTrustRelationships)
 [^5]: [Harmj0y Domain Trusts](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)
 [^6]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^7]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^8]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
 [^9]: [DFIR_Sodinokibi_Ransomware](https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/)
 [^10]: [DFIR_Quantum_Ransomware](https://thedfirreport.com/2022/04/25/quantum-ransomware/)
 [^11]: [Elastic Pikabot 2024](https://www.elastic.co/security-labs/pikabot-i-choose-you)
 [^12]: [Red Canary Hospital Thwarted Ryuk October 2020](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)
 [^13]: [FireEye Ryuk and Trickbot January 2019](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)
 [^14]: [Symantec Bumblebee June 2022](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)
 [^15]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)
 [^16]: [DFIR Ryuk 2 Hour Speed Run November 2020](https://thedfirreport.com/2020/11/05/ryuk-speed-run-2-hours-to-ransom/)
 [^17]: [DFIR Ryuk's Return October 2020](https://thedfirreport.com/2020/10/08/ryuks-return/)
 [^18]: [SocGholish-update](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)
 [^19]: [Red Canary SocGholish March 2024](https://redcanary.com/threat-detection-report/threats/socgholish/)
 [^20]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
 [^21]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
 [^22]: [Nltest Manual](https://ss64.com/nt/nltest.html)
 [^23]: [Fortinet TrickBot](https://www.fortinet.com/blog/threat-research/trickbot-s-new-reconnaissance-plugin.html)
 [^24]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^25]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^26]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
 [^27]: [CrowdStrike BloodHound April 2018](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)
 [^28]: [Bitsight Latrodectus June 2024](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
 [^29]: [Elastic Latrodectus May 2024](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
 [^30]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
 [^31]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^32]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)
 [^33]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)
 [^34]: [PowerSploit Documentation](http://powersploit.readthedocs.io)
 [^35]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
