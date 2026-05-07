---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1049
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1049-system-network-connections-discovery
tactic:
    - Discovery
platforms:
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

Adversaries may attempt to get a listing of network connections to or from the compromised system they are currently accessing or from remote systems by querying for information over the network. <br><br>An adversary who gains access to a system that is part of a cloud-based environment may map out Virtual Private Clouds or Virtual Networks in order to determine what systems and services are connected. The actions performed are likely the same types of discovery techniques depending on the operating system, but the resulting information may include details about the networked cloud environment relevant to the adversary's goals. Cloud providers may have different ways in which their virtual networks operate.[^1] [^2] [^3]  Similarly, adversaries who gain access to network devices may also perform similar discovery activities to gather information about connected systems and services.<br><br>Utilities and commands that acquire this information include [[kb/mitre/attack/software/S0104-netstat|netstat]], "net use," and "net session" with [[kb/mitre/attack/software/S0039-net|Net]]. In Mac and Linux, [[kb/mitre/attack/software/S0104-netstat|netstat]] and `lsof` can be used to list current connections. `who -a` and `w` can be used to show which users are currently logged in, similar to "net session". Additionally, built-in features native to network devices and [[kb/mitre/attack/techniques/T1059.008-network-device-cli|Network Device CLI]] may be used (e.g. `show ip sockets`, `show tcp brief`).[^4]  On ESXi servers, the command `esxi network ip connection list` can be used to list active network connections.[^5] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has a module for enumerating TCP and UDP network connections and associated processes using the `netstat` command.[^1]  |
| [S0018](https://attack.mitre.org/software/S0018) | Sykipot | Sykipot may use `netstat -ano` to display active network connections.[^1]  |
| [S0038](https://attack.mitre.org/software/S0038) | Duqu | The discovery modules used with Duqu can collect information on network connections.[^1]  |
| [[kb/mitre/attack/software/S0039-net\|S0039]] | Net | Commands such as `net use` and `net session` can be used in [[kb/mitre/attack/software/S0039-net\|Net]] to gather information about network connections from a particular host.[^1]  |
| [S0063](https://attack.mitre.org/software/S0063) | SHOTPUT | SHOTPUT uses [[kb/mitre/attack/software/S0104-netstat\|netstat]] to list TCP connection status.[^1]  |
| [S0089](https://attack.mitre.org/software/S0089) | BlackEnergy | BlackEnergy has gathered information about local network connections using [[kb/mitre/attack/software/S0104-netstat\|netstat]].[^1] [^2]  |
| [S0091](https://attack.mitre.org/software/S0091) | Epic | Epic uses the `net use`, `net session`, and `netstat` commands to gather information on network connections.[^1] [^2]  |
| [S0094](https://attack.mitre.org/software/S0094) | Trojan.Karagany | Trojan.Karagany can use [[kb/mitre/attack/software/S0104-netstat\|netstat]] to collect a list of network connections.[^1]  |
| [[kb/mitre/attack/software/S0102-nbtstat\|S0102]] | nbtstat | [[kb/mitre/attack/software/S0102-nbtstat\|nbtstat]] can be used to discover current NetBIOS sessions. |
| [[kb/mitre/attack/software/S0104-netstat\|S0104]] | netstat | [[kb/mitre/attack/software/S0104-netstat\|netstat]] can be used to enumerate local network connections, including active TCP connections and other network statistics.[^1]  |
| [S0125](https://attack.mitre.org/software/S0125) | Remsec | Remsec can obtain a list of active connections and open ports.[^1]  |
| [S0153](https://attack.mitre.org/software/S0153) | RedLeaves | RedLeaves can enumerate drives and Remote Desktop sessions.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can produce a sessions report from compromised hosts.[^1]  |
| [S0165](https://attack.mitre.org/software/S0165) | OSInfo | OSInfo enumerates the current network connections similar to ` net use `.[^1]  |
| [S0180](https://attack.mitre.org/software/S0180) | Volgmer | Volgmer can gather information about TCP connection state.[^1]  |
| [S0184](https://attack.mitre.org/software/S0184) | POWRUNER | POWRUNER may collect active network connections by running `netstat -an` on a victim.[^1]  |
| [[kb/mitre/attack/software/S0192-pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] has a built-in utility command for `netstat`, can do net session through PowerView, and has an interactive shell which can be used to discover additional information.[^1]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE can capture session logon details from a compromised host.[^1]  |
| [S0236](https://attack.mitre.org/software/S0236) | Kwampirs | Kwampirs collects a list of active and listening connections by using the command `netstat -nao` as well as a list of available network mappings with `net use`.[^1]  |
| [S0237](https://attack.mitre.org/software/S0237) | GravityRAT | GravityRAT uses the `netstat` command to find open ports on the victim’s machine.[^1]  |
| [S0241](https://attack.mitre.org/software/S0241) | RATANKBA | RATANKBA uses `netstat -ano` to search for specific IP address ranges.[^1]  |
| [S0244](https://attack.mitre.org/software/S0244) | Comnie | Comnie executes the `netstat -ano` command.[^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy uses `netstat -aon` to gather network connection information.[^1]  |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT can list network connections.[^1]  |
| [S0335](https://attack.mitre.org/software/S0335) | Carbon | Carbon uses the `netstat -r` and `netstat -an` commands.[^1]  |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | KONNI has used `net session` on the victim's machine.[^1]   |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can enumerate the current network connections of a host.[^1]  |
| [S0374](https://attack.mitre.org/software/S0374) | SpeakUp | SpeakUp uses the `arp -a` command. [^1]  |
| [[kb/mitre/attack/software/S0378-poshc2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains an implementation of [[kb/mitre/attack/software/S0104-netstat\|netstat]] to enumerate TCP and UDP connections.[^1]  |
| [S0439](https://attack.mitre.org/software/S0439) | Okrum | Okrum was seen using NetSess to discover NetBIOS sessions.[^1]  |
| [S0443](https://attack.mitre.org/software/S0443) | MESSAGETAP | After loading the keyword and phone data files, MESSAGETAP begins monitoring all network connections to and from the victim server. [^1]  |
| [[kb/mitre/attack/software/S0445-shimratreporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-shimratreporter\|ShimRatReporter]] used the Windows function `GetExtendedUdpTable` to detect connected UDP endpoints.[^1]  |
| [S0449](https://attack.mitre.org/software/S0449) | Maze | Maze has used the "WNetOpenEnumW", "WNetEnumResourceW”, “WNetCloseEnum” and “WNetAddConnection2W” functions to enumerate the network resources on the infected machine.[^1]  |
| [S0452](https://attack.mitre.org/software/S0452) | USBferry | USBferry can use `netstat` and `nbtstat` to detect active network connections.[^1] 	 |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has the ability to gather TCP and UDP table status listings.[^1]  |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can use `netstat` to enumerate network connections.[^1]  |
| [[kb/mitre/attack/software/S0488-crackmapexec\|S0488]] | CrackMapExec | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can discover active sessions for a targeted system.[^1]  |
| [S0532](https://attack.mitre.org/software/S0532) | Lucifer | Lucifer can identify the IP and port numbers for all remote connections from the compromised host.[^1]  |
| [S0533](https://attack.mitre.org/software/S0533) | SLOTHFULMEDIA | SLOTHFULMEDIA can enumerate open ports on a victim machine.[^1]  |
| [S0554](https://attack.mitre.org/software/S0554) | Egregor | Egregor can enumerate all connected drives.[^1]  |
| [S0567](https://attack.mitre.org/software/S0567) | Dtrack | Dtrack can collect network and active connection information.[^1]  |
| [S0575](https://attack.mitre.org/software/S0575) | Conti | Conti can enumerate routine network connections from a compromised host.[^1]  |
| [S0579](https://attack.mitre.org/software/S0579) | Waterbear | Waterbear can use API hooks on `GetExtendedTcpTable` to retrieve a table containing a list of TCP endpoints available to the application.[^1]   |
| [S0589](https://attack.mitre.org/software/S0589) | Sibot | Sibot has retrieved a GUID associated with a present LAN connection on a compromised machine.[^1]  |
| [S0625](https://attack.mitre.org/software/S0625) | Cuba | Cuba can use the function `GetIpNetTable` to recover the last connections to the victim's machine.[^1]   |
| [[kb/mitre/attack/software/S0633-sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can collect network connection information.[^1]  |
| [S0638](https://attack.mitre.org/software/S0638) | Babuk | Babuk can use “WNetOpenEnumW” and “WNetEnumResourceW” to enumerate files in network resources for encryption.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot can use `netstat` to enumerate current network connections.[^2] [^1]  |
| [S0678](https://attack.mitre.org/software/S0678) | Torisma | Torisma can use `WTSEnumerateSessionsW` to monitor remote desktop connections.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar has a plugin to retrieve information about all active network sessions on the infected server.[^1]  |
| [S0696](https://attack.mitre.org/software/S0696) | Flagpro | Flagpro has been used to execute `netstat -ano` on a compromised host.[^1]  |
| [S1032](https://attack.mitre.org/software/S1032) | PyDCrypt | PyDCrypt has used [[kb/mitre/attack/software/S0108-netsh\|netsh]] to find RPC connections on remote machines.[^1]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can use the `GetExtendedTcpTable` function to retrieve information about established TCP connections.[^1]  |
| [S1075](https://attack.mitre.org/software/S1075) | KOPILUWAK | KOPILUWAK can use [[kb/mitre/attack/software/S0104-netstat\|netstat]], [[kb/mitre/attack/software/S0099-arp\|Arp]], and [[kb/mitre/attack/software/S0039-net\|Net]] to discover current TCP connections.[^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can execute `netstat.exe -f` on a compromised machine.[^1]  |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic has the ability to execute the `netstat` command.[^1]  |
| [[kb/mitre/attack/software/S1091-pacu\|S1091]] | Pacu | Once inside a Virtual Private Cloud, [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can attempt to identify DirectConnect, VPN, or VPC Peering.[^1]  |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb can enumerate system network connections.[^1]  |
| [[kb/mitre/attack/software/S1144-frp\|S1144]] | FRP | [[kb/mitre/attack/software/S1144-frp\|FRP]] can use a dashboard and U/I to display the status of connections from the FRP client and server.[^1]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has used several commands executed in sequence via `cmd` in a short interval to gather information on network connections.[^1]  |

 [^1]: [Amazon AWS VPC Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
 [^2]: [Microsoft Azure Virtual Network Overview](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
 [^3]: [Google VPC Overview](https://cloud.google.com/vpc/docs/vpc)
 [^4]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
 [^5]: [Sygnia ESXi Ransomware 2025](https://www.sygnia.co/blog/esxi-ransomware-ssh-tunneling-defense-strategies/)
 [^6]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
 [^7]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
 [^8]: [McAfee Babuk February 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
 [^9]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^10]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
 [^11]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)
 [^12]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
 [^13]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
 [^14]: [TechNet Netstat](https://technet.microsoft.com/en-us/library/bb490947.aspx)
 [^15]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
 [^16]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
 [^17]: [McAfee Maze March 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
 [^18]: [RATANKBA](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
 [^19]: [GovCERT Carbon May 2016](https://web.archive.org/web/20170718174931/https://www.melani.admin.ch/dam/melani/de/dokumente/2016/technical%20report%20ruag.pdf.download.pdf/Report_Ruag-Espionage-Case.pdf)
 [^20]: [McAfee Lazarus Nov 2020](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
 [^21]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
 [^22]: [Savill 1999](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)
 [^23]: [F-Secure BlackEnergy 2014](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)
 [^24]: [Securelist BlackEnergy Nov 2014](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
 [^25]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)
 [^26]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)
 [^27]: [Kaspersky Turla Aug 2014](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)
 [^28]: [Palo Alto Comnie](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)
 [^29]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)
 [^30]: [NHS Digital Egregor Nov 2020](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)
 [^31]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^32]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^33]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
 [^34]: [FireEye NETWIRE March 2019](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)
 [^35]: [Symantec Buckeye](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
 [^36]: [AlienVault Sykipot 2011](https://www.alienvault.com/open-threat-exchange/blog/another-sykipot-sample-likely-targeting-us-federal-agencies)
 [^37]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
 [^38]: [Trend Micro Waterbear December 2019](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
 [^39]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
 [^40]: [FRP GitHub](https://github.com/fatedier/frp)
 [^41]: [Symantec W32.Duqu](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)
 [^42]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
 [^43]: [Palo Alto CVE-2015-3113 July 2015](http://researchcenter.paloaltonetworks.com/2015/07/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)
 [^44]: [CarbonBlack Conti July 2020](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
 [^45]: [FireEye MESSAGETAP October 2019](https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html)
 [^46]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
 [^47]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^48]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
 [^49]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
 [^50]: [CheckPoint SpeakUp Feb 2019](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)
 [^51]: [ESET Okrum July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
 [^52]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
 [^53]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
 [^54]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
 [^55]: [NTT Security Flagpro new December 2021](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
 [^56]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
 [^57]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^58]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
 [^59]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)
 [^60]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
 [^61]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)
 [^62]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
 [^63]: [Symantec Volgmer Aug 2014](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)
 [^64]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
 [^65]: [GitHub Sliver Netstat](https://github.com/BishopFox/sliver/tree/58a56a077f0813bb312f9fa4df7453b510c3a73b/implant/sliver/netstat)
 [^66]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^67]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
