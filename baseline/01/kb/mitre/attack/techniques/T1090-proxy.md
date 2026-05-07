---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1090
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1090-proxy
tactic:
    - Command And Control
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

Adversaries may use a connection proxy to direct network traffic between systems or act as an intermediary for network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist that enable traffic redirection through proxies or port redirection, including [[kb/mitre/attack/software/S0040-htran|HTRAN]], ZXProxy, and ZXPortMap. [^2]  Adversaries use these types of proxies to manage command and control communications, reduce the number of simultaneous outbound network connections, provide resiliency in the face of connection loss, or to ride over existing trusted communications paths between victims to avoid suspicion. Adversaries may chain together multiple proxies to further disguise the source of malicious traffic.<br><br>Adversaries can also take advantage of routing schemes in Content Delivery Networks (CDNs) to proxy command and control traffic.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0040-htran\|S0040]] | HTRAN | [[kb/mitre/attack/software/S0040-htran\|HTRAN]] can proxy TCP socket connections to obfuscate command and control infrastructure.[^1] [^2]  |
| [[kb/mitre/attack/software/S0108-netsh\|S0108]] | netsh | [[kb/mitre/attack/software/S0108-netsh\|netsh]] can be used to set up a proxy tunnel to allow remote host access to an infected host.[^1]  |
| [S0117](https://attack.mitre.org/software/S0117) | XTunnel | XTunnel relays traffic between a C2 server and a victim.[^1]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE can implement use of proxies to pivot traffic.[^1]  |
| [S0207](https://attack.mitre.org/software/S0207) | Vasport | Vasport is capable of tunneling though a proxy.[^1]  |
| [S0245](https://attack.mitre.org/software/S0245) | BADCALL | BADCALL functions as a proxy server between the victim and C2 server.[^1]  |
| [S0246](https://attack.mitre.org/software/S0246) | HARDRAIN | HARDRAIN uses the command `cmd.exe /c netsh firewall add portopening TCP 443 "adp"` and makes the victim machine function as a proxy server.[^1]  |
| [[kb/mitre/attack/software/S0262-quasarrat\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can communicate over a reverse proxy using SOCKS5.[^1] [^2]  |
| [S0263](https://attack.mitre.org/software/S0263) | TYPEFRAME | A TYPEFRAME variant can force the compromised system to function as a proxy server.[^1]  |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal | Bisonal has supported use of a proxy server.[^1]  |
| [S0273](https://attack.mitre.org/software/S0273) | Socksbot | Socksbot can start SOCKS proxy threads.[^1]  |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT can serve as a SOCKS proxy server.[^1]  |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] uses the infected hosts as SOCKS5 proxies to allow for tunneling and proxying.[^1] [^2]  |
| [S0347](https://attack.mitre.org/software/S0347) | AuditCred | AuditCred can utilize proxy for communications.[^1]  |
| [S0348](https://attack.mitre.org/software/S0348) | Cardinal RAT | Cardinal RAT can act as a reverse proxy.[^1]  |
| [S0376](https://attack.mitre.org/software/S0376) | HOPLIGHT | HOPLIGHT has multiple proxy options that mask traffic between the malware and the remote operators.[^1] 	<br> |
| [[kb/mitre/attack/software/S0378-poshc2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains modules that allow for use of proxies in command and control.[^1]  |
| [S0384](https://attack.mitre.org/software/S0384) | Dridex | Dridex contains a backconnect module for tunneling network traffic through a victim's computer. Infected computers become part of a P2P botnet that can relay C2 traffic to other infected peers.[^1] [^2]   |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has used a peer-to-peer (P2P) network for C2.[^1] [^2]  |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell can set up an HTTP or SOCKS proxy.[^2] [^1]   |
| [S0435](https://attack.mitre.org/software/S0435) | PLEAD | PLEAD has the ability to proxy network communications.[^1]  |
| [S0436](https://attack.mitre.org/software/S0436) | TSCookie | TSCookie has the ability to proxy communications with command and control (C2) servers.[^1]  |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has the ability to use a reverse SOCKS proxy module.[^1]  |
| [S0461](https://attack.mitre.org/software/S0461) | SDBbot | SDBbot has the ability to use port forwarding to establish a proxy between a target host and C2.[^1]  |
| [S0487](https://attack.mitre.org/software/S0487) | Kessel | Kessel can use a proxy during exfiltration if set in the configuration.[^1]  |
| [[kb/mitre/attack/software/S0508-ngrok\|S0508]] | ngrok | [[kb/mitre/attack/software/S0508-ngrok\|ngrok]] can be used to proxy connections to machines located behind NAT or firewalls.[^2] [^1]  |
| [S0615](https://attack.mitre.org/software/S0615) | SombRAT | SombRAT has the ability to use an embedded SOCKS proxy in C2 communications.[^1]  |
| [S0629](https://attack.mitre.org/software/S0629) | RainyDay | RainyDay can use proxy tools including boost_proxy_client for reverse proxy functionality.[^1]  |
| [S0669](https://attack.mitre.org/software/S0669) | KOCTOPUS | KOCTOPUS has deployed a modified version of Invoke-Ngrok to expose open local ports to the Internet.[^1]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT has the capability to act as a reverse proxy.[^1]  |
| [S0690](https://attack.mitre.org/software/S0690) | Green Lambert | Green Lambert can use proxies for C2 traffic.[^1] [^2]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can identify and use configured proxies in a compromised network for C2 communication.[^1]  |
| [S1051](https://attack.mitre.org/software/S1051) | KEYPLUG | KEYPLUG has used Cloudflare CDN associated infrastructure to redirect C2 communications to malicious domains.[^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can use SOCKS4 and SOCKS5 proxies to connect to actor-controlled C2 servers. BADHATCH can also emulate a reverse proxy on a compromised machine to connect with actor-controlled C2 servers.[^1]  |
| [S1099](https://attack.mitre.org/software/S1099) | Samurai | Samurai has the ability to proxy connections to specified remote IPs and ports through a a proxy module.[^1]  |
| [S1114](https://attack.mitre.org/software/S1114) | ZIPLINE | ZIPLINE can create a proxy server on compromised hosts.[^2] [^1]  |
| [S1121](https://attack.mitre.org/software/S1121) | LITTLELAMB.WOOLTEA | LITTLELAMB.WOOLTEA has the ability to function as a SOCKS proxy.[^1]  |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb has the ability to use a HTTP proxy server for C&C communications.[^1]  |
| [[kb/mitre/attack/software/S1144-frp\|S1144]] | FRP | [[kb/mitre/attack/software/S1144-frp\|FRP]] can proxy communications through a server in public IP space to local servers located behind a NAT or firewall.[^1]  |
| [S1187](https://attack.mitre.org/software/S1187) | reGeorg | reGeorg can establish an HTTP or SOCKS proxy to tunnel data in and out of a network.[^3] [^1] [^2]  |
| [S1189](https://attack.mitre.org/software/S1189) | Neo-reGeorg | Neo-reGeorg has the ability to establish a SOCKS5 proxy on a compromised web server.[^1]  |
| [S1190](https://attack.mitre.org/software/S1190) | Kapeka | Kapeka can identify system proxy settings via `WinHttpGetIEProxyConfigForCurrentUser()` during initialization and utilize these settings for subsequent command and control operations.[^1]  |
| [S1197](https://attack.mitre.org/software/S1197) | GoBear | GoBear implements SOCKS5 proxy functionality.[^1]  |
| [S1210](https://attack.mitre.org/software/S1210) | Sagerunex | Sagerunex uses several proxy configuration settings to ensure connectivity.[^1]  |
| [S1212](https://attack.mitre.org/software/S1212) | RansomHub | RansomHub can use a proxy to connect to remote SFTP servers.[^1]  |
| [S1229](https://attack.mitre.org/software/S1229) | Havoc | Havoc has the ability to route HTTP/S communications through designated proxies.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1020-ssl-tls-inspection\|M1020]] | SSL/TLS Inspection | If it is possible to inspect HTTPS traffic, the captures can be analyzed for connections that appear to be domain fronting. |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific C2 protocol used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools. [^1]  |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | Traffic to known anonymity networks and C2 infrastructure can be blocked through the use of network allow and block lists. It should be noted that this kind of blocking may be circumvented by other techniques like [[kb/mitre/attack/techniques/T1090.004-domain-fronting\|Domain Fronting]]. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1090.002-external-proxy\|T1090.002]] | External Proxy |
| [[kb/mitre/attack/techniques/T1090.003-multi-hop-proxy\|T1090.003]] | Multi-hop Proxy |
| [[kb/mitre/attack/techniques/T1090.004-domain-fronting\|T1090.004]] | Domain Fronting |
| [[kb/mitre/attack/techniques/T1090.001-internal-proxy\|T1090.001]] | Internal Proxy |

 [^1]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^2]: [Trend Micro APT Attack Tools](http://blog.trendmicro.com/trendlabs-security-intelligence/in-depth-look-apt-attack-tools-of-the-trade/)
 [^3]: [Cisco LotusBlossom 2025](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
 [^4]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
 [^5]: [Mandiant Cutting Edge Part 2 January 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
 [^6]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)
 [^7]: [Group-IB RansomHub FEB 2025](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
 [^8]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
 [^9]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
 [^10]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
 [^11]: [Operation Quantum Entanglement](https://web.archive.org/web/20210920193513/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-operation-quantum-entanglement.pdf)
 [^12]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)
 [^13]: [FRP GitHub](https://github.com/fatedier/frp)
 [^14]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)
 [^15]: [TrendMicro Lazarus Nov 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)
 [^16]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)
 [^17]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
 [^18]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
 [^19]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
 [^20]: [Zdnet Ngrok September 2018](https://www.zdnet.com/article/sly-malware-author-hides-cryptomining-botnet-behind-ever-shifting-proxy-service/)
 [^21]: [MalwareBytes Ngrok February 2020](https://blog.malwarebytes.com/threat-analysis/2020/02/fraudsters-cloak-credit-card-skimmer-with-fake-content-delivery-network-ngrok-server/)
 [^22]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
 [^23]: [GitHub Neo-reGeorg 2019](https://github.com/L-codes/Neo-reGeorg/blob/master/README-en.md)
 [^24]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)
 [^25]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^26]: [US-CERT BADCALL](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)
 [^27]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
 [^28]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
 [^29]: [Securelist fileless attacks Feb 2017](https://securelist.com/fileless-attacks-against-enterprise-networks/77403/)
 [^30]: [JPCert PLEAD Downloader June 2018](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)
 [^31]: [Dell Dridex Oct 2015](https://www.secureworks.com/research/dridex-bugat-v5-botnet-takeover-operation)
 [^32]: [Checkpoint Dridex Jan 2021](https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/)
 [^33]: [US-CERT HARDRAIN March 2018](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-F.pdf)
 [^34]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
 [^35]: [JPCert BlackTech Malware September 2019](https://blogs.jpcert.or.jp/en/2019/09/tscookie-loader.html)
 [^36]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)
 [^37]: [US-CERT TYPEFRAME June 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)
 [^38]: [Fortinet reGeorg MAR 2019](https://www.fortiguard.com/encyclopedia/ips/47584/regeorg-http-tunnel)
 [^39]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)
 [^40]: [GitHub reGeorg 2016](https://github.com/xl7dev/WebShell/tree/master/reGeorg-master)
 [^41]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
 [^42]: [Objective See Green Lambert for OSX Oct 2021](https://objective-see.com/blog/blog_0x68.html)
 [^43]: [Glitch-Cat Green Lambert ATTCK Oct 2021](https://web.archive.org/web/20211018145402/https://www.glitch-cat.com/blog/green-lambert-and-attack)
 [^44]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^45]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
 [^46]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
 [^47]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
 [^48]: [Symantec Vasport May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051606-5938-99)
 [^49]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)
 [^50]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)
 [^51]: [WithSecure Kapeka 2024](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)
 [^52]: [NJCCIC Ursnif Sept 2016](https://www.cyber.nj.gov/threat-landscape/malware/trojans/ursnif)
 [^53]: [ProofPoint Ursnif Aug 2016](https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality)
 [^54]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^55]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
 [^56]: [Crowdstrike DNC June 2016](https://www.crowdstrike.com/blog/bears-midst-intrusion-democratic-national-committee/)
 [^57]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^58]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^59]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)
