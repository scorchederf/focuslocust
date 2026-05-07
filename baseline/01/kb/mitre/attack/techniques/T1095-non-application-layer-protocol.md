---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1095
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1095-non-application-layer-protocol
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

Adversaries may use an OSI non-application layer protocol for communication between host and C2 server or among infected hosts within a network. The list of possible protocols is extensive.[^6]  Specific examples include use of network layer protocols, such as the Internet Control Message Protocol (ICMP), transport layer protocols, such as the User Datagram Protocol (UDP), session layer protocols, such as Socket Secure (SOCKS), as well as redirected/tunneled protocols, such as Serial over LAN (SOL).<br><br>ICMP communication between hosts is one example.[^3]  Because ICMP is part of the Internet Protocol Suite, it is required to be implemented by all IP-compatible hosts.[^4]  However, it is not as commonly monitored as other Internet Protocols such as TCP or UDP and may be used by adversaries to hide communications.<br><br>In ESXi environments, adversaries may leverage the Virtual Machine Communication Interface (VMCI) for communication between guest virtual machines and the ESXi host. This traffic is similar to client-server communications on traditional network sockets but is localized to the physical machine running the ESXi host, meaning it does not traverse external networks (routers, switches). This results in communications that are invisible to external monitoring and standard networking tools like tcpdump, netstat, nmap, and Wireshark. By adding a VMCI backdoor to a compromised ESXi host, adversaries may persistently regain access from any guest VM to the compromised ESXi host’s backdoor, regardless of network segmentation or firewall rules in place.[^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0011](https://attack.mitre.org/software/S0011) | Taidoor | Taidoor can use TCP for C2 communications.[^1]  |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX can be configured to use raw TCP or UDP for command and control.[^1] [^2]  |
| [S0019](https://attack.mitre.org/software/S0019) | Regin | The Regin malware platform can use ICMP to communicate between infected computers.[^1]  |
| [S0021](https://attack.mitre.org/software/S0021) | Derusbi | Derusbi binds to a raw socket on a random source port between 31800 and 31900 for C2.[^1]  |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos can communicate through custom methodologies for UDP,  ICMP, and TCP that use distinct sessions to ride over the legitimate protocols.[^1]  |
| [S0032](https://attack.mitre.org/software/S0032) | gh0st RAT | gh0st RAT has used an encrypted protocol within TCP segments to communicate with the C2.[^1]  |
| [S0034](https://attack.mitre.org/software/S0034) | NETEAGLE | If NETEAGLE does not detect a proxy configured on the infected machine, it will send beacons via UDP/6000. Also, after retrieving a C2 IP address and Port Number, NETEAGLE will initiate a TCP connection to this socket. The ensuing connection is a plaintext C2 channel in which commands are specified by DWORDs.[^1]  |
| [S0043](https://attack.mitre.org/software/S0043) | BUBBLEWRAP | BUBBLEWRAP can communicate using SOCKS.[^1]  |
| [S0055](https://attack.mitre.org/software/S0055) | RARSTONE | RARSTONE uses SSL to encrypt its communication with its C2 server.[^1]  |
| [S0076](https://attack.mitre.org/software/S0076) | FakeM | Some variants of FakeM use SSL to communicate with C2 servers.[^1]  |
| [S0083](https://attack.mitre.org/software/S0083) | Misdat | Misdat network traffic communicates over a raw socket.[^1]  |
| [S0084](https://attack.mitre.org/software/S0084) | Mis-Type | Mis-Type network traffic can communicate over a raw socket.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson uses a custom TCP protocol for C2.[^1] [^2] 	  |
| [S0125](https://attack.mitre.org/software/S0125) | Remsec | Remsec is capable of using ICMP, TCP, and UDP for C2.[^1] [^2]  |
| [S0141](https://attack.mitre.org/software/S0141) | Winnti for Windows | Winnti for Windows can communicate using custom TCP.[^1]  |
| [S0149](https://attack.mitre.org/software/S0149) | MoonWind | MoonWind completes network communication via raw sockets.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can be configured to use TCP, ICMP, and UDP for C2 communications.[^1] [^2]  |
| [S0155](https://attack.mitre.org/software/S0155) | WINDSHIELD | WINDSHIELD C2 traffic can communicate via TCP raw sockets.[^1]  |
| [S0158](https://attack.mitre.org/software/S0158) | PHOREAL | PHOREAL communicates via ICMP for C2.[^1]  |
| [S0172](https://attack.mitre.org/software/S0172) | Reaver | Some Reaver variants use raw TCP for C2.[^1]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE can use TCP in C2 communications.[^1] [^2]  |
| [S0221](https://attack.mitre.org/software/S0221) | Umbreon | Umbreon provides access to the system via SSH or any other protocol that uses PAM to authenticate.[^1]  |
| [S0234](https://attack.mitre.org/software/S0234) | Bandook | Bandook has a command built in to use a raw TCP socket.[^1]   |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole has used TCP to download additional modules.[^1]  |
| [[kb/mitre/attack/software/S0262-quasarrat\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can use TCP for C2 communication.[^1]  |
| [S0268](https://attack.mitre.org/software/S0268) | Bisonal | Bisonal has used raw sockets for network communication.[^1]  |
| [S0335](https://attack.mitre.org/software/S0335) | Carbon | Carbon uses TCP and UDP for C2.[^1]  |
| [S0352](https://attack.mitre.org/software/S0352) | OSX_OCEANLOTUS.D | OSX_OCEANLOTUS.D has used a custom binary protocol over port 443 for C2 traffic.[^1]  |
| [S0394](https://attack.mitre.org/software/S0394) | HiddenWasp | HiddenWasp communicates with a simple network protocol over TCP.[^1]  |
| [S0430](https://attack.mitre.org/software/S0430) | Winnti for Linux | Winnti for Linux has used ICMP, custom TCP, and UDP in outbound communications.[^1]  |
| [S0436](https://attack.mitre.org/software/S0436) | TSCookie | TSCookie can use ICMP to receive information on the destination server.[^1]  |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo has used raw TCP for C2.[^1]   |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has used TCP in C2 communications.[^1]  |
| [S0461](https://attack.mitre.org/software/S0461) | SDBbot | SDBbot has the ability to communicate with C2 with TCP over port 443.[^1]  |
| [S0498](https://attack.mitre.org/software/S0498) | Cryptoistic | Cryptoistic can use TCP in communications with C2.[^1]  |
| [S0501](https://attack.mitre.org/software/S0501) | PipeMon | The PipeMon communication module can use a custom protocol based on TLS over TCP.[^1]  |
| [S0502](https://attack.mitre.org/software/S0502) | Drovorub | Drovorub can use TCP to communicate between its agent and client modules.[^1]  |
| [S0504](https://attack.mitre.org/software/S0504) | Anchor | Anchor has used ICMP in C2 communications.[^1]  |
| [S0515](https://attack.mitre.org/software/S0515) | WellMail | WellMail can use TCP for C2 communications.[^1]  |
| [S0556](https://attack.mitre.org/software/S0556) | Pay2Key | Pay2Key has sent its public key to the C2 server over TCP.[^1]  |
| [S0582](https://attack.mitre.org/software/S0582) | LookBack | LookBack uses a custom binary protocol over sockets for C2 communications.[^1]  |
| [S0587](https://attack.mitre.org/software/S0587) | Penquin | The Penquin C2 mechanism is based on TCP and UDP packets.[^1] [^2]  |
| [S0596](https://attack.mitre.org/software/S0596) | ShadowPad | ShadowPad has used UDP for C2 communications.[^1]  |
| [S0615](https://attack.mitre.org/software/S0615) | SombRAT | SombRAT has the ability to use TCP sockets to send data and ICMP to ping the C2 server.[^1] [^2]  |
| [S0629](https://attack.mitre.org/software/S0629) | RainyDay | RainyDay can use TCP in C2 communications.[^1]  |
| [S0630](https://attack.mitre.org/software/S0630) | Nebulae | Nebulae can use TCP in C2 communications.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot has the ability use TCP to send or receive C2 packets.[^1]  |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling has the ability to use TCP and UDP for communication.[^1]  |
| [S0662](https://attack.mitre.org/software/S0662) | RCSession | RCSession has the ability to use TCP and UDP in C2 communications.[^2] [^1]  |
| [S0666](https://attack.mitre.org/software/S0666) | Gelsemium | Gelsemium has the ability to use TCP and UDP in C2 communications.[^1]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT can communicate with its C2 server via TCP over port 5200.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar has used a raw TCP connection to communicate with the C2 server.[^1]     |
| [[kb/mitre/attack/software/S0699-mythic\|S0699]] | Mythic | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] supports WebSocket and TCP-based C2 profiles.[^1] 	 |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa has used a custom JSON-based protocol for its C&C communications.[^1]  |
| [S1029](https://attack.mitre.org/software/S1029) | AuTo Stealer | AuTo Stealer can use TCP to communicate with command and control servers.[^1]  |
| [S1031](https://attack.mitre.org/software/S1031) | PingPull |  PingPull variants have the ability to communicate with C2 servers using ICMP or TCP.[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can communicate with C2 over TCP and UDP.[^1]  |
| [S1049](https://attack.mitre.org/software/S1049) | SUGARUSH | SUGARUSH has used TCP for C2.[^1]  |
| [S1051](https://attack.mitre.org/software/S1051) | KEYPLUG | <br>KEYPLUG can use TCP and KCP (KERN Communications Protocol) over UDP for C2 communication.[^1]  |
| [S1059](https://attack.mitre.org/software/S1059) | metaMain | metaMain can establish an indirect and raw TCP socket-based connection to the C2 server.[^1] [^2]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can use raw TCP for C2.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has the ability to use TCP for external C2.[^1]  |
| [S1073](https://attack.mitre.org/software/S1073) | Royal | Royal establishes a TCP socket for C2 communication using the API `WSASocketW`.[^1]  |
| [S1078](https://attack.mitre.org/software/S1078) | RotaJakiro | RotaJakiro uses a custom binary protocol using a type, length, value format over TCP.[^1]  |
| [S1084](https://attack.mitre.org/software/S1084) | QUIETEXIT | QUIETEXIT can establish a TCP connection as part of its initial connection to the C2.[^1]  |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic can communicate with actor-controlled C2 servers by using a custom little-endian binary protocol.[^1]  |
| [S1099](https://attack.mitre.org/software/S1099) | Samurai | Samurai can use a proxy module to forward TCP packets to external hosts.[^1]  |
| [S1100](https://attack.mitre.org/software/S1100) | Ninja | Ninja can forward TCP packets between the C2 and a remote host.[^1] [^2]  |
| [S1105](https://attack.mitre.org/software/S1105) | COATHANGER | COATHANGER uses ICMP for transmitting configuration information to and from its command and control server.[^1]  |
| [S1114](https://attack.mitre.org/software/S1114) | ZIPLINE | ZIPLINE can communicate with C2 using a custom binary protocol.[^1]  |
| [S1121](https://attack.mitre.org/software/S1121) | LITTLELAMB.WOOLTEA | LITTLELAMB.WOOLTEA can function as a stand-alone backdoor communicating over the `/tmp/clientsDownload.sock` socket.[^1]  |
| [S1140](https://attack.mitre.org/software/S1140) | Spica | Spica can use JSON over WebSockets for C2 communications.[^1]  |
| [S1142](https://attack.mitre.org/software/S1142) | LunarMail | LunarMail can ping a specific C2 URL with the ID of a victim machine in the subdomain.[^1]  |
| [[kb/mitre/attack/software/S1144-frp\|S1144]] | FRP | [[kb/mitre/attack/software/S1144-frp\|FRP]] can communicate over TCP, TCP stream multiplexing, KERN Communications Protocol (KCP), QUIC, and UDP.[^1]  |
| [S1153](https://attack.mitre.org/software/S1153) | Cuckoo Stealer | Cuckoo Stealer can use sockets for communications to its C2 server.[^1]  |
| [S1163](https://attack.mitre.org/software/S1163) | SnappyTCP | SnappyTCP spawns a reverse TCP shell following an HTTP-based negotiation.[^1]  |
| [S1187](https://attack.mitre.org/software/S1187) | reGeorg | reGeorg can tunnel TCP sessions into targeted networks.[^1]  |
| [S1189](https://attack.mitre.org/software/S1189) | Neo-reGeorg | Neo-reGeorg can create multiple TCP connections for a single session.[^1]  |
| [S1200](https://attack.mitre.org/software/S1200) | StealBit | StealBit can use the Windows Socket networking library to communicate with attacker-controlled endpoints.[^1] <br> |
| [S1203](https://attack.mitre.org/software/S1203) | J-magic | J-magic can monitor incoming C2 communications sent over TCP to the compromised host.[^1]  |
| [S1204](https://attack.mitre.org/software/S1204) | cd00r | cd00r can monitor incoming C2 communications sent over TCP to the compromised host.[^2] [^1]  |
| [S1219](https://attack.mitre.org/software/S1219) | REPTILE | REPTILE can communicate using TLS over raw TCP.[^1] [^2] <br> |
| [S1221](https://attack.mitre.org/software/S1221) | MOPSLED | MOPSLED can use a custom binary protocol over TCP for C2 communication.[^1]  |
| [S1227](https://attack.mitre.org/software/S1227) | StarProxy | StarProxy has used TCP for C2 communications to target IPs or domains.  StarProxy contained code to support both UDP and TCP connections.[^1]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has utilized TCP-based reverse shells.[^1]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has established a connection with the C2 server over TCP traffic.[^2]  InvisibleFerret has also created a TCP reverse shell communicating via a socket connection over ports 1245, 80, 2245, 3001, and 5000.[^1]  |
| [S9001](https://attack.mitre.org/software/S9001) | SystemBC | SystemBC has used raw TCP on non-standard ports, such as 4044, for C2 communications and for HTTP communications, which include downloading binaries.[^2] [^1]  |
| [S9023](https://attack.mitre.org/software/S9023) | HiddenFace | HiddenFace can use a custom TCP protocol over Port 443 for C2.[^1] [^3] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Properly configure firewalls and proxies to limit outgoing traffic to only necessary ports and through proper network gateway systems. Also ensure hosts are only provisioned to communicate over authorized interfaces. |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | Filter network traffic to prevent use of protocols across the network boundary that are unnecessary.  If VMCI is not required in ESXi environments, consider restricting guest virtual machines from accessing VMCI services.[^1]  |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Periodically investigate ESXi hosts for open VMCI ports. Running the `lsof -A` command and inspecting results with a type of `SOCKET_VMCI` will reveal processes that have open VMCI ports.[^1]  |

 [^1]: [Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)
 [^2]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^3]: [Cisco Synful Knock Evolution](https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices)
 [^4]: [Microsoft ICMP](http://support.microsoft.com/KB/170292)
 [^5]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)
 [^6]: [Wikipedia OSI](http://en.wikipedia.org/wiki/List_of_network_protocols_%28OSI_model%29)
 [^7]: [FRP GitHub](https://github.com/fatedier/frp)
 [^8]: [Unit42 OceanLotus 2017](https://unit42.paloaltonetworks.com/unit42-new-improved-macos-backdoor-oceanlotus/)
 [^9]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
 [^10]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)
 [^11]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^12]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^13]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^14]: [FireEye APT32 May 2017](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
 [^15]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^16]: [Lumen J-Magic JAN 2025](https://blog.lumen.com/the-j-magic-show-magic-packets-and-where-to-find-them/)
 [^17]: [Hartrell cd00r 2002](https://www.giac.org/paper/gcih/342/handle-cd00r-invisible-backdoor/103631)
 [^18]: [JPCert BlackTech Malware September 2019](https://blogs.jpcert.or.jp/en/2019/09/tscookie-loader.html)
 [^19]: [Kaspersky ToddyCat June 2022](https://securelist.com/toddycat/106799/)
 [^20]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
 [^21]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
 [^22]: [Dell TG-3390](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)
 [^23]: [MalwareBytes SideCopy Dec 2021](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
 [^24]: [NCSC-NL COATHANGER Feb 2024](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)
 [^25]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
 [^26]: [GitHub Neo-reGeorg 2019](https://github.com/L-codes/Neo-reGeorg/blob/master/README-en.md)
 [^27]: [Aquino RARSTONE](http://blog.trendmicro.com/trendlabs-security-intelligence/rarstone-found-in-targeted-attacks/)
 [^28]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^29]: [NSA/FBI Drovorub August 2020](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)
 [^30]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^31]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^32]: [Chronicle Winnti for Linux May 2019](https://medium.com/chronicle-blog/winnti-more-than-just-windows-and-gates-e4f03436031a)
 [^33]: [SekoiaBourhis_DiceLoader_Feb2024](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)
 [^34]: [Mandiant Cutting Edge Part 2 January 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
 [^35]: [ESET HiddenFace 2024](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)
 [^36]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
 [^37]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
 [^38]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^39]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
 [^40]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
 [^41]: [Symantec Remsec IOCs](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/Symantec_Remsec_IOCs.pdf)
 [^42]: [Kaspersky ProjectSauron Full Report](https://securelist.com/files/2016/07/The-ProjectSauron-APT_research_KL.pdf)
 [^43]: [Novetta Winnti April 2015](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)
 [^44]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
 [^45]: [Intezer HiddenWasp Map 2019](https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/)
 [^46]: [CISA WellMail July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)
 [^47]: [Mythc Documentation](https://docs.mythic-c2.net/)
 [^48]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
 [^49]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)
 [^50]: [Check Point Pay2Key November 2020](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)
 [^51]: [Palo Alto Reaver Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)
 [^52]: [BlackBerry CostaRicto November 2020](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
 [^53]: [FireEye FiveHands April 2021](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
 [^54]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
 [^55]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)
 [^56]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)
 [^57]: [Google Cloud Threat Intelligence ESXi Hardening 2023](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)
 [^58]: [Gh0stRAT ATT March 2019](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
 [^59]: [Broadcom VMCI Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-virtual-machine-administration-guide-7-0/configuring-virtual-machine-hardwarevm-admin/virtual-machine-network-configurationvm-admin/serial-port-configurationvm-admin/configure-the-virtual-machine-communication-interface-firewallvm-admin.html)
 [^60]: [Kaspersky ShadowPad Aug 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
 [^61]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
 [^62]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)
 [^63]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
 [^64]: [ESET Carbon Mar 2017](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)
 [^65]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
 [^66]: [Proofpoint LookBack Malware Aug 2019](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)
 [^67]: [Talos Bisonal Mar 2020](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
 [^68]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^69]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
 [^70]: [netlab360 rotajakiro vs oceanlotus](https://blog.netlab.360.com/rotajakiro_linux_version_of_oceanlotus/)
 [^71]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
 [^72]: [Mandiant Fortinet Zero Day](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
 [^73]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^74]: [FireEye admin@338](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)
 [^75]: [PWC Sea Turtle 2023](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/tortoise-and-malwahare.html)
 [^76]: [Umbreon Trend Micro](https://blog.trendmicro.com/trendlabs-security-intelligence/pokemon-themed-umbreon-linux-rootkit-hits-x86-arm-systems/?_ga=2.180041126.367598458.1505420282-1759340220.1502477046)
 [^77]: [Fidelis Turbo](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)
 [^78]: [AhnLab_SystemBC_Apr2022](https://asec.ahnlab.com/en/33600/)
 [^79]: [SophosGnGal_SystemBC_Dec2020](https://news.sophos.com/en-us/2020/12/16/systembc/)
 [^80]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
 [^81]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^82]: [Cybereason StealBit Exfiltration Tool](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
 [^83]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
 [^84]: [Kaspersky Turla Penquin December 2014](https://securelist.com/the-penquin-turla-2/67962/)
 [^85]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
 [^86]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
 [^87]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^88]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^89]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^90]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)
 [^91]: [Google TAG COLDRIVER January 2024](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/)
 [^92]: [SentinelOne Lazarus macOS July 2020](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)
 [^93]: [Kaspersky Regin](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070305/Kaspersky_Lab_whitepaper_Regin_platform_eng.pdf)
 [^94]: [Fortinet reGeorg MAR 2019](https://www.fortiguard.com/encyclopedia/ips/47584/regeorg-http-tunnel)
 [^95]: [Mandiant APT41](https://www.mandiant.com/resources/apt41-us-state-governments)
 [^96]: [Zscaler](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)
 [^97]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
 [^98]: [Unit 42 NETWIRE April 2020](https://unit42.paloaltonetworks.com/guloader-installing-netwire-rat/)
 [^99]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^100]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^101]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^102]: [Mandiant UNC3890 Aug 2022](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)
 [^103]: [CISA MAR-10292089-1.v2 TAIDOOR August 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
 [^104]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
