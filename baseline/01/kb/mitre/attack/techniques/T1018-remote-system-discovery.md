---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1018
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1018-remote-system-discovery
tactic:
    - Discovery
platforms:
    - ESXi
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for Lateral Movement from the current system. Functionality could exist within remote access tools to enable this, but utilities available on the operating system could also be used such as  [[kb/mitre/attack/software/S0097-ping|Ping]], `net view` using [[kb/mitre/attack/software/S0039-net|Net]], or, on ESXi servers, `esxcli network diag ping`.<br><br>Adversaries may also analyze data from local host files (ex: `C:\Windows\System32\Drivers\etc\hosts` or `/etc/hosts`) or other passive means (such as local [[kb/mitre/attack/software/S0099-arp|Arp]] cache entries) in order to discover the presence of remote systems in an environment.<br><br>Adversaries may also target discovery of network infrastructure as well as leverage [[kb/mitre/attack/techniques/T1059.008-network-device-cli|Network Device CLI]] commands on network devices to gather detailed information about systems within a network (e.g. `show cdp neighbors`, `show arp`).[^3] [^1]   <br>

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0018](https://attack.mitre.org/software/S0018) | Sykipot | Sykipot may use `net view /domain` to display hostnames of available systems on a network.[^1]  |
| [[kb/mitre/attack/software/S0039-net\|S0039]] | Net | Commands such as `net view` can be used in [[kb/mitre/attack/software/S0039-net\|Net]] to gather information about available remote systems.[^1]  |
| [S0063](https://attack.mitre.org/software/S0063) | SHOTPUT | SHOTPUT has a command to list all servers in the domain, as well as one to locate domain controllers on a domain.[^1]  |
| [S0091](https://attack.mitre.org/software/S0091) | Epic | Epic uses the `net view` command on the victim’s machine.[^1]  |
| [S0093](https://attack.mitre.org/software/S0093) | Backdoor.Oldrea | Backdoor.Oldrea can enumerate and map ICS-specific systems in victim environments.[^1]  |
| [[kb/mitre/attack/software/S0097-ping\|S0097]] | Ping | [[kb/mitre/attack/software/S0097-ping\|Ping]] can be used to identify remote systems within a network.[^1]  |
| [[kb/mitre/attack/software/S0099-arp\|S0099]] | Arp | [[kb/mitre/attack/software/S0099-arp\|Arp]] can be used to display a host's ARP cache, which may include address resolutions for remote systems.[^1] [^2]  |
| [S0125](https://attack.mitre.org/software/S0125) | Remsec | Remsec can ping or traceroute a remote host.[^1]  |
| [S0140](https://attack.mitre.org/software/S0140) | Shamoon | Shamoon scans the C-class subnet of the IPs on the victim's interfaces.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike uses the native Windows Network Enumeration APIs to interrogate and discover targets in a Windows Active Directory network.[^2] [^1] [^3]  |
| [S0165](https://attack.mitre.org/software/S0165) | OSInfo | OSInfo performs a connection test to discover remote systems in the network[^1]  |
| [S0233](https://attack.mitre.org/software/S0233) | MURKYTOP | MURKYTOP has the capability to identify remote hosts on connected networks.[^1]  |
| [S0236](https://attack.mitre.org/software/S0236) | Kwampirs | Kwampirs collects a list of available servers with the command `net view`.[^1]  |
| [S0241](https://attack.mitre.org/software/S0241) | RATANKBA | RATANKBA runs the `net view /domain` and `net view` commands.[^1]  |
| [S0244](https://attack.mitre.org/software/S0244) | Comnie | Comnie runs the `net view` command |
| [S0248](https://attack.mitre.org/software/S0248) | yty | yty uses the `net view` command for discovery.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot can enumerate computers and network devices.[^1]  |
| [S0335](https://attack.mitre.org/software/S0335) | Carbon | Carbon uses the `net view` command.[^1]  |
| [[kb/mitre/attack/software/S0359-nltest\|S0359]] | Nltest | [[kb/mitre/attack/software/S0359-nltest\|Nltest]] may be used to enumerate remote domain controllers using options such as `/dclist` and `/dsgetdc`.[^1]  |
| [S0365](https://attack.mitre.org/software/S0365) | Olympic Destroyer | Olympic Destroyer uses [[kb/mitre/attack/techniques/T1047-windows-management-instrumentation\|Windows Management Instrumentation]] to enumerate all systems in the network.[^1]  |
| [S0366](https://attack.mitre.org/software/S0366) | WannaCry | WannaCry scans its local network segment for remote systems to try to exploit and copy itself to.[^1]  |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT can identify remote hosts on connected networks.[^1]  |
| [S0428](https://attack.mitre.org/software/S0428) | PoetRAT | PoetRAT used Nmap for remote system discovery.[^1]  |
| [S0452](https://attack.mitre.org/software/S0452) | USBferry | USBferry can use `net view` to gather information about remote systems.[^1]  |
| [[kb/mitre/attack/software/S0488-crackmapexec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can discover active IP addresses, along with the machine name, within a targeted network.[^1]  |
| [[kb/mitre/attack/software/S0521-bloodhound\|S0521]] | BloodHound | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] can enumerate and collect the properties of domain computers, including domain controllers.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar can enumerate remote systems using ` Net View`.[^1]  |
| [[kb/mitre/attack/software/S0552-adfind\|S0552]] | AdFind | [[kb/mitre/attack/software/S0552-adfind\|AdFind]] has the ability to query Active Directory for computers.[^1] [^4] [^3] [^2]  |
| [S0570](https://attack.mitre.org/software/S0570) | BitPaymer | BitPaymer can use `net view` to discover remote systems.[^1]  |
| [S0575](https://attack.mitre.org/software/S0575) | Conti | <br>Conti has the ability to discover hosts on a target network.[^1]  |
| [S0586](https://attack.mitre.org/software/S0586) | TAINTEDSCRIBE | The TAINTEDSCRIBE command and execution module can perform target system enumeration.[^1]  |
| [[kb/mitre/attack/software/S0590-nbtscan\|S0590]] | NBTscan | [[kb/mitre/attack/software/S0590-nbtscan\|NBTscan]] can list NetBIOS computer names.[^1] [^2] 	 |
| [S0599](https://attack.mitre.org/software/S0599) | Kinsing | Kinsing has used a script to parse files like `/etc/hosts` and SSH `known_hosts` to discover remote systems.[^1]  |
| [S0604](https://attack.mitre.org/software/S0604) | Industroyer | Industroyer can enumerate remote computers in the compromised network.[^1]  |
| [S0646](https://attack.mitre.org/software/S0646) | SpicyOmelette | SpicyOmelette can identify payment systems, payment gateways, and ATM systems in compromised environments.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can identify remote systems through the `net view` command.[^1] [^3] [^2]  |
| [S0659](https://attack.mitre.org/software/S0659) | Diavol | Diavol can use the ARP table to find remote hosts to scan.[^1]   |
| [[kb/mitre/attack/software/S0684-roadtools\|S0684]] | ROADTools | [[kb/mitre/attack/software/S0684-roadtools\|ROADTools]] can enumerate Azure AD systems and devices.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can enumerate and collect the properties of domain computers.[^1]  |
| [S0694](https://attack.mitre.org/software/S0694) | DRATzarus | DRATzarus can search for other machines connected to compromised host and attempt to map the network.[^1]  |
| [S0696](https://attack.mitre.org/software/S0696) | Flagpro | Flagpro has been used to execute `net view` on a targeted system.[^1]   |
| [S0698](https://attack.mitre.org/software/S0698) | HermeticWizard | HermeticWizard can find machines on the local network by gathering known local IP addresses through `DNSGetCacheDataTable`, `GetIpNetTable`,`WNetOpenEnumW(RESOURCE_GLOBALNET, RESOURCETYPE_ANY)`,`NetServerEnum`,`GetTcpTable`, and `GetAdaptersAddresses.`[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can collect information about hosts on the victim network.[^1]  |
| [S1068](https://attack.mitre.org/software/S1068) | BlackCat | BlackCat can broadcasts NetBIOS Name Service (NBNC) messages to search for servers connected to compromised networks.[^1]  |
| [S1070](https://attack.mitre.org/software/S1070) | Black Basta | Black Basta can use LDAP queries to connect to AD and iterate over connected workstations.[^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can use a PowerShell object such as, `System.Net.NetworkInformation.Ping` to ping a computer.[^1]  |
| [S1146](https://attack.mitre.org/software/S1146) | MgBot | MgBot includes modules for performing ARP scans of local connected systems.[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP can use `ping` to identify remote hosts within the victim network.[^1]  |
| [S1198](https://attack.mitre.org/software/S1198) | Gomir | Gomir probes arbitrary network endpoints for TCP connectivity.[^1]  |
| [S1212](https://attack.mitre.org/software/S1212) | RansomHub | RansomHub can enumerate all accessible machines from the infected system.[^1]  |
| [S1229](https://attack.mitre.org/software/S1229) | Havoc | Havoc features a module capable of host enumeration.[^1] <br> |
| [S1242](https://attack.mitre.org/software/S1242) | Qilin | Qilin can enumerate domain-connected hosts during its discovery phase.[^2] [^1] [^3]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO can run `net view` and `net view /domain` for network discovery.[^1]  |

 [^1]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
 [^2]: [Elastic - Koadiac Detection with EQL](https://www.elastic.co/security-labs/embracing-offensive-tooling-building-detections-against-koadic-using-eql)
 [^3]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
 [^4]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
 [^5]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
 [^6]: [Roadtools](https://dirkjanm.io/introducing-roadtools-and-roadrecon-azure-ad-exploration-framework/)
 [^7]: [Crowdstrike Indrik November 2018](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
 [^8]: [Crowdstrike Qakbot October 2020](https://www.crowdstrike.com/blog/duck-hunting-with-falcon-complete-qakbot-zip-based-campaign/)
 [^9]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
 [^10]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^11]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
 [^12]: [Cybereason Bazar July 2020](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
 [^13]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
 [^14]: [Microsoft BlackCat Jun 2022](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
 [^15]: [Savill 1999](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)
 [^16]: [Check Point Black Basta October 2022](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)
 [^17]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
 [^18]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
 [^19]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
 [^20]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
 [^21]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
 [^22]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
 [^23]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
 [^24]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
 [^25]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
 [^26]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)
 [^27]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
 [^28]: [Kaspersky APT Trends Q1 2020](https://securelist.com/apt-trends-report-q1-2020/96826/)
 [^29]: [SecureWorks WannaCry Analysis](https://www.secureworks.com/research/wcry-ransomware-analysis)
 [^30]: [AlienVault Sykipot 2011](https://www.alienvault.com/open-threat-exchange/blog/another-sykipot-sample-likely-targeting-us-federal-agencies)
 [^31]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
 [^32]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
 [^33]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^34]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^35]: [CrowdStrike BloodHound April 2018](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)
 [^36]: [ClearSky Lazarus Aug 2020](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
 [^37]: [Symantec Buckeye](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
 [^38]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
 [^39]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
 [^40]: [TechNet Ping](https://technet.microsoft.com/en-us/library/bb490968.aspx)
 [^41]: [CrowdStrike Wizard Spider October 2020](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)
 [^42]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
 [^43]: [Palo Alto CVE-2015-3113 July 2015](http://researchcenter.paloaltonetworks.com/2015/07/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)
 [^44]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
 [^45]: [GovCERT Carbon May 2016](https://web.archive.org/web/20170718174931/https://www.melani.admin.ch/dam/melani/de/dokumente/2016/technical%20report%20ruag.pdf.download.pdf/Report_Ruag-Espionage-Case.pdf)
 [^46]: [Aqua Kinsing April 2020](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)
 [^47]: [Fortinet Diavol July 2021](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
 [^48]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
 [^49]: [Secureworks GOLD KINGSWOOD September 2018](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)
 [^50]: [TechNet Arp](https://technet.microsoft.com/en-us/library/bb490864.aspx)
 [^51]: [Palo Alto ARP](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-analytics-alert-reference/cortex-xdr-analytics-alert-reference/uncommon-arp-cache-listing-via-arp-exe.html)
 [^52]: [Debian nbtscan Nov 2019](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)
 [^53]: [SecTools nbtscan June 2003](https://sectools.org/tool/nbtscan/)
 [^54]: [Talos Olympic Destroyer 2018](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
 [^55]: [Nltest Manual](https://ss64.com/nt/nltest.html)
 [^56]: [Sophos Qilin MSP APR 2025](https://news.sophos.com/en-us/2025/04/01/sophos-mdr-tracks-ongoing-campaign-by-qilin-affiliates-targeting-screenconnect/)
 [^57]: [Picus Qilin MAR 2025](https://www.picussecurity.com/resource/blog/qilin-ransomware)
 [^58]: [Cisco Talos Qilin Ransomware OCT 2025](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
 [^59]: [Red Canary Hospital Thwarted Ryuk October 2020](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)
 [^60]: [Cybereason Bumblebee August 2022](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)
 [^61]: [FireEye Ryuk and Trickbot January 2019](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)
 [^62]: [FireEye FIN6 Apr 2019](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)
 [^63]: [FireEye Shamoon Nov 2016](https://web.archive.org/web/20210126065851/https://www.fireeye.com/blog/threat-research/2016/11/fireeye_respondsto.html)
 [^64]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^65]: [Gigamon Berserk Bear October 2021](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)
 [^66]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)
