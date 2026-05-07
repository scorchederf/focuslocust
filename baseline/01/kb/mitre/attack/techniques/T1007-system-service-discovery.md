---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1007
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1007-system-service-discovery
tactic:
    - Discovery
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may try to gather information about registered local system services. Adversaries may obtain information about services using tools as well as OS utility commands such as `sc query`, `tasklist /svc`, `systemctl --type=service`, and `net start`. Adversaries may also gather information about schedule tasks via commands such as `schtasks` on Windows or `crontab -l` on Linux and macOS.[^2] [^3] [^4] [^1] <br><br>Adversaries may use the information from [[kb/mitre/attack/techniques/T1007-system-service-discovery|System Service Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0015](https://attack.mitre.org/software/S0015) | Ixeshe | Ixeshe can list running services.[^1]  |
| [S0018](https://attack.mitre.org/software/S0018) | Sykipot | Sykipot may use `net start` to display running services.[^1]  |
| [S0024](https://attack.mitre.org/software/S0024) | Dyre | Dyre has the ability to identify running services on a compromised host.[^1]  |
| [[kb/mitre/attack/software/S0039-net\|S0039]] | Net | The `net start` command can be used in [[kb/mitre/attack/software/S0039-net\|Net]] to find information about Windows services.[^1]  |
| [S0049](https://attack.mitre.org/software/S0049) | GeminiDuke | GeminiDuke collects information on programs and services on the victim that are configured to automatically run at startup.[^1]  |
| [[kb/mitre/attack/software/S0057-tasklist\|S0057]] | Tasklist | [[kb/mitre/attack/software/S0057-tasklist\|Tasklist]] can be used to discover services running on a system.[^1]  |
| [S0081](https://attack.mitre.org/software/S0081) | Elise | Elise executes `net start` after initial communication is made to the remote server.[^1]  |
| [S0082](https://attack.mitre.org/software/S0082) | Emissary | Emissary has the capability to execute the command `net start` to interact with services.[^1]  |
| [S0085](https://attack.mitre.org/software/S0085) | S-Type | S-Type runs the command `net start` on a victim.[^1]  |
| [S0086](https://attack.mitre.org/software/S0086) | ZLib | ZLib has the ability to discover and manipulate Windows services.[^1]  |
| [S0091](https://attack.mitre.org/software/S0091) | Epic | Epic uses the `tasklist /svc` command to list the services on the system.[^1]  |
| [S0127](https://attack.mitre.org/software/S0127) | BBSRAT | BBSRAT can query service configuration information.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can enumerate services on compromised hosts.[^1]  |
| [S0180](https://attack.mitre.org/software/S0180) | Volgmer | Volgmer queries the system to identify existing services.[^1]  |
| [S0201](https://attack.mitre.org/software/S0201) | JPIN | JPIN can list running services.[^1]  |
| [S0203](https://attack.mitre.org/software/S0203) | Hydraq | Hydraq creates a backdoor through which remote attackers can monitor services.[^1] [^2]  |
| [S0219](https://attack.mitre.org/software/S0219) | WINERACK | WINERACK can enumerate services.[^1]  |
| [S0236](https://attack.mitre.org/software/S0236) | Kwampirs | Kwampirs collects a list of running services with the command `tasklist /svc`.[^1]  |
| [S0237](https://attack.mitre.org/software/S0237) | GravityRAT | GravityRAT has a feature to list the available services on the system.[^1]  |
| [S0241](https://attack.mitre.org/software/S0241) | RATANKBA | RATANKBA uses `tasklist /svc` to display running tasks.[^1]  |
| [S0242](https://attack.mitre.org/software/S0242) | SynAck | SynAck enumerates all running services.[^1] [^2]  |
| [S0244](https://attack.mitre.org/software/S0244) | Comnie | Comnie runs the command: `net start >> %TEMP%\info.dat` on a victim.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can obtain running services on the victim.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot collects a list of install programs and services on the system’s machine.[^1]  |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT can list local services.[^1]  |
| [S0342](https://attack.mitre.org/software/S0342) | GreyEnergy | GreyEnergy enumerates all Windows services.[^1]  |
| [[kb/mitre/attack/software/S0378-poshc2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can enumerate service and service permission information.[^1]  |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has gathered information about running services.[^1]  |
| [S0398](https://attack.mitre.org/software/S0398) | HyperBro | HyperBro can list all services and their configurations.[^1]  |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell can check the services on the system.[^1]   |
| [S0431](https://attack.mitre.org/software/S0431) | HotCroissant | HotCroissant has the ability to retrieve a list of services on the infected host.[^1]  |
| [S0496](https://attack.mitre.org/software/S0496) | REvil | REvil can enumerate active services.[^1]  |
| [S0533](https://attack.mitre.org/software/S0533) | SLOTHFULMEDIA | SLOTHFULMEDIA has the capability to enumerate services.[^1]  |
| [S0559](https://attack.mitre.org/software/S0559) | SUNBURST | SUNBURST collected a list of service names that were hashed using a FNV-1a + XOR algorithm to check against similarly-hashed hardcoded blocklists.[^1]  |
| [S0570](https://attack.mitre.org/software/S0570) | BitPaymer | BitPaymer can enumerate existing Windows services on the host that are configured to run as LocalSystem.[^1]  |
| [S0572](https://attack.mitre.org/software/S0572) | Caterpillar WebShell | Caterpillar WebShell can obtain a list of the services from a system.[^1]   |
| [S0582](https://attack.mitre.org/software/S0582) | LookBack | LookBack can enumerate services on the victim machine.[^1]  |
| [S0615](https://attack.mitre.org/software/S0615) | SombRAT | SombRAT can enumerate services on a victim machine.[^1]  |
| [S0625](https://attack.mitre.org/software/S0625) | Cuba | Cuba can query service status using `QueryServiceStatusEx` function.[^1]  |
| [S0629](https://attack.mitre.org/software/S0629) | RainyDay | RainyDay can create and register a service for execution.[^1]  |
| [S0638](https://attack.mitre.org/software/S0638) | Babuk | Babuk can enumerate all services running on a compromised host.[^1]  |
| [S0663](https://attack.mitre.org/software/S0663) | SysUpdate | SysUpdate can collect a list of services on a victim machine.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can search for modifiable services that could be used for privilege escalation.[^1]  |
| [S1027](https://attack.mitre.org/software/S1027) | Heyoka Backdoor | Heyoka Backdoor can check if it is running as a service on a compromised host.[^1]  |
| [S1066](https://attack.mitre.org/software/S1066) | DarkTortilla | DarkTortilla can retrieve information about a compromised system's running services.[^1]  |
| [S1070](https://attack.mitre.org/software/S1070) | Black Basta | Black Basta can check whether the service name `FAX` is present.[^1]  |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic has the ability to execute the `net start` command.[^1]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has leveraged `tasklist` to gather running services on victim host.[^1]  |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can identify specific services for termination or to be left running at execution.[^2] [^3] [^1] [^4]  |
| [S1244](https://attack.mitre.org/software/S1244) | Medusa Ransomware | Medusa Ransomware has leveraged an encoded list of services that it designates for termination.[^1] [^2] [^3]  |
| [S1247](https://attack.mitre.org/software/S1247) | Embargo | Embargo has obtained active services running on the victim’s system through the functions `OpenSCManagerW()` and `EnumServicesStatusExW()`.[^1]  |
| [S9035](https://attack.mitre.org/software/S9035) | LAMEHUG | LAMEHUG can gather service information on targeted systems.[^1] [^2]  |

 [^1]: [Aquasec Kinsing 2020](https://www.aquasec.com/blog/threat-alert-kinsing-malware-container-vulnerability/)
 [^2]: [Elastic Security Labs GOSAR 2024](https://www.elastic.co/security-labs/under-the-sadbridge-with-gosar)
 [^3]: [SentinelLabs macOS Malware 2021](https://www.sentinelone.com/labs/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
 [^4]: [Splunk Linux Gormir 2024](https://www.splunk.com/en_us/blog/security/breaking-down-linux-gomir-understanding-this-backdoors-ttps.html)
 [^5]: [TrendMicro Ursnif Mar 2015](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)
 [^6]: [AlienVault Sykipot 2011](https://www.alienvault.com/open-threat-exchange/blog/another-sykipot-sample-likely-targeting-us-federal-agencies)
 [^7]: [Palo Alto Comnie](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)
 [^8]: [Lunghi Iron Tiger Linux](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
 [^9]: [Savill 1999](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)
 [^10]: [Lotus Blossom Jun 2015](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)
 [^11]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)
 [^12]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
 [^13]: [Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
 [^14]: [Broadcom Medusa Ransomware Medusa Group March 2025](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
 [^15]: [Security Scorecard Medusa Ransomware January 2024](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
 [^16]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
 [^17]: [Microsoft Tasklist](https://technet.microsoft.com/en-us/library/bb491010.aspx)
 [^18]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
 [^19]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
 [^20]: [Palo Alto Networks BBSRAT](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)
 [^21]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
 [^22]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^23]: [US-CERT Volgmer Nov 2017](https://www.us-cert.gov/ncas/alerts/TA17-318B)
 [^24]: [Proofpoint LookBack Malware Aug 2019](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)
 [^25]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
 [^26]: [HC3 Qilin Threat Profile JUN 2024](https://www.aha.org/system/files/media/file/2024/06/tlp-clear-hc3-threat-profile-qilin-aka-agenda-ransomware-6-18-2024.pdf)
 [^27]: [Trend Micro Agenda Ransomware AUG 2022](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
 [^28]: [SentinelOne Qilin NOV 2022](https://www.sentinelone.com/anthology/agenda-qilin/)
 [^29]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
 [^30]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
 [^31]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^32]: [ESET GreyEnergy Oct 2018](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
 [^33]: [FireEye SUNBURST Backdoor December 2020](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
 [^34]: [Unit42 Emissary Panda May 2019](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)
 [^35]: [Cyble Black Basta May 2022](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
 [^36]: [Cyble Embargo Ransomware May 2024](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
 [^37]: [Symantec Trojan.Hydraq Jan 2010](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
 [^38]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
 [^39]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
 [^40]: [Intel 471 REvil March 2020](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
 [^41]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
 [^42]: [SecureList SynAck Doppelgänging May 2018](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
 [^43]: [Kaspersky Lab SynAck May 2018](https://usa.kaspersky.com/about/press-releases/2018_synack-doppelganging)
 [^44]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
 [^45]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
 [^46]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
 [^47]: [F-Secure The Dukes](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
 [^48]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)
 [^49]: [Emissary Trojan Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/)
 [^50]: [McAfee Babuk February 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
 [^51]: [Trend Micro IXESHE 2012](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
 [^52]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
 [^53]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
 [^54]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)
 [^55]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
 [^56]: [S2 Grupo TrickBot June 2017](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
 [^57]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
 [^58]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
 [^59]: [Cato LAMEHUG JUL 2025](https://www.catonetworks.com/blog/cato-ctrl-threat-research-analyzing-lamehug/)
 [^60]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
 [^61]: [Malwarebytes Dyreza November 2015](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
 [^62]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)
 [^63]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
