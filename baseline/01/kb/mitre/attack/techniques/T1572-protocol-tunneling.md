---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1572
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1572-protocol-tunneling
tactic:
    - Command And Control
platforms:
    - ESXi
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may tunnel network communications to and from a victim system within a separate protocol to avoid detection/network filtering and/or enable access to otherwise unreachable systems. Tunneling involves explicitly encapsulating a protocol within another. This behavior may conceal malicious traffic by blending in with existing traffic and/or provide an outer layer of encryption (similar to a VPN). Tunneling could also enable routing of network packets that would otherwise not reach their intended destination, such as SMB, RDP, or other traffic that would be filtered by network appliances or not routed over the Internet. <br><br>There are various means to encapsulate a protocol within another protocol. For example, adversaries may perform SSH tunneling (also known as SSH port forwarding), which involves forwarding arbitrary data over an encrypted SSH tunnel.[^4] [^1]  <br><br>[[kb/mitre/attack/techniques/T1572-protocol-tunneling|Protocol Tunneling]] may also be abused by adversaries during [[kb/mitre/attack/techniques/T1568-dynamic-resolution|Dynamic Resolution]]. Known as DNS over HTTPS (DoH), queries to resolve C2 infrastructure may be encapsulated within encrypted HTTPS packets.[^3]  <br><br>Adversaries may also leverage [[kb/mitre/attack/techniques/T1572-protocol-tunneling|Protocol Tunneling]] in conjunction with [[kb/mitre/attack/techniques/T1090-proxy|Proxy]] and/or [[kb/mitre/attack/techniques/T1001.003-protocol-or-service-impersonation|Protocol or Service Impersonation]] to further conceal C2 communications and infrastructure. 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos has the ability to communicate over custom communications methodologies that ride over common network protocols including raw TCP and UDP sockets, HTTP, SMTP, and DNS.[^1]  |
| [S0038](https://attack.mitre.org/software/S0038) | Duqu | Duqu uses a custom command and control protocol that communicates over commonly used ports, and is frequently encapsulated by application layer protocols.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike uses a custom command and control protocol that is encapsulated in HTTP, HTTPS, or DNS. In addition, it conducts peer-to-peer communication over Windows named pipes encapsulated in the SMB protocol. All protocols use their standard assigned ports.[^1] [^2]  |
| [S0173](https://attack.mitre.org/software/S0173) | FLIPSIDE | FLIPSIDE uses RDP to tunnel traffic from a victim environment.[^1]  |
| [[kb/mitre/attack/software/S0508-ngrok\|S0508]] | ngrok | [[kb/mitre/attack/software/S0508-ngrok\|ngrok]] can tunnel RDP and other services securely over internet connections.[^3] [^2] [^4] [^1]  |
| [S0604](https://attack.mitre.org/software/S0604) | Industroyer | Industroyer attempts to perform an HTTP CONNECT via an internal proxy to establish a tunnel.[^1]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | The QakBot proxy module can encapsulate SOCKS5 protocol within its own proxy protocol.[^1]  |
| [S0687](https://attack.mitre.org/software/S0687) | Cyclops Blink | Cyclops Blink can use DNS over HTTPS (DoH) to resolve C2 nodes.[^1]  |
| [[kb/mitre/attack/software/S0699-mythic\|S0699]] | Mythic | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] can use SOCKS proxies to tunnel traffic through another protocol.[^1]  |
| [S1015](https://attack.mitre.org/software/S1015) | Milan | Milan can use a custom protocol tunneled through DNS or HTTP.[^1]  |
| [S1020](https://attack.mitre.org/software/S1020) | Kevin | Kevin can use a custom protocol tunneled through DNS or HTTP.[^1]  |
| [S1027](https://attack.mitre.org/software/S1027) | Heyoka Backdoor | Heyoka Backdoor can use spoofed DNS requests to create a bidirectional tunnel between a compromised host and its C2 servers.[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can connect to HTTP proxies via TCP to create a tunnel to C2.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can use DNS over HTTPS for C2.[^1] [^2]  |
| [S1141](https://attack.mitre.org/software/S1141) | LunarWeb | LunarWeb can run a custom binary protocol under HTTPS for C2.[^1]  |
| [[kb/mitre/attack/software/S1144-frp\|S1144]] | FRP | [[kb/mitre/attack/software/S1144-frp\|FRP]] can tunnel SSH and Unix Domain Socket communications over TCP between external nodes and exposed resources behind firewalls or NAT.[^1]  |
| [S1187](https://attack.mitre.org/software/S1187) | reGeorg | reGeorg can tunnel TCP sessions including RDP, SSH, and SMB through HTTP.[^1] [^2] [^3]  |
| [S1189](https://attack.mitre.org/software/S1189) | Neo-reGeorg | Neo-reGeorg can tunnel data in and out of targeted networks.[^1]  |
| [S9015](https://attack.mitre.org/software/S9015) | BRICKSTORM | BRICKSTORM has utilized a SOCKS proxy to tunnel access within the victim network and exfiltrate files from internal shares, code repositories, and other endpoints.[^1] [^2] [^3] [^4] [^5] [^6] [^7]   BRICKSTORM has also leveraged Yamux for combining multiple concurrent logical streams over a single a socket.[^2] [^5] [^6]  |
| [S9023](https://attack.mitre.org/software/S9023) | HiddenFace | HiddenFace can hide its IP lookup by using DNS over HTTPS (DoH) for C2.[^1]  |
| [S9024](https://attack.mitre.org/software/S9024) | SPAWNCHIMERA | SPAWNCHIMERA has created SSH tunnels to facilitate C2 communications.[^1] [^2] [^3]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level.  |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | Consider filtering network traffic to untrusted or known bad domains and resources.  |

 [^1]: [Sygnia Abyss Locker 2025](https://www.sygnia.co/blog/abyss-locker-ransomware-attack-analysis/)
 [^2]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^3]: [BleepingComp Godlua JUL19](https://www.bleepingcomputer.com/news/security/new-godlua-malware-evades-traffic-monitoring-via-dns-over-https/)
 [^4]: [SSH Tunneling](https://www.ssh.com/ssh/tunneling)
 [^5]: [GitHub Neo-reGeorg 2019](https://github.com/L-codes/Neo-reGeorg/blob/master/README-en.md)
 [^6]: [SentinelOne Aoqin Dragon June 2022](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
 [^7]: [Fortinet reGeorg MAR 2019](https://www.fortiguard.com/encyclopedia/ips/47584/regeorg-http-tunnel)
 [^8]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)
 [^9]: [Cadet Blizzard emerges as novel threat actor](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)
 [^10]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^11]: [Symantec W32.Duqu](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)
 [^12]: [CISA SPAWNCHIMERA RESURGE February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)
 [^13]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
 [^14]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
 [^15]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^16]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
 [^17]: [Dragos Crashoverride 2017](https://dragos.com/blog/crashoverride/CrashOverride-01.pdf)
 [^18]: [FRP GitHub](https://github.com/fatedier/frp)
 [^19]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^20]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
 [^21]: [CrowdStrike BRICKSTORM WARP PANDA UNC5221 December 2025](https://www.crowdstrike.com/en-us/blog/warp-panda-cloud-threats/)
 [^22]: [CISA BRICKSTORM UNC5221 AR25-338A February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
 [^23]: [Picus Security BRICKSTORM UNC5221 October 2025](https://www.picussecurity.com/resource/blog/brickstorm-malware-unc5221-targets-tech-and-legal-sectors-in-the-united-states)
 [^24]: [NVISO BRICKSTORM April 2025](https://blog.nviso.eu/wp-content/uploads/2025/04/NVISO-BRICKSTORM-Report.pdf)
 [^25]: [Resecurity UNC5221 BRICKSTORM F5 Big-IP October 2025](https://www.resecurity.com/blog/article/f5-big-ip-source-code-leak-tied-to-state-linked-campaigns-using-brickstorm-backdoor)
 [^26]: [Google BRICKSTORM September 2025](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
 [^27]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^28]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
 [^29]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^30]: [Trend Micro Ngrok September 2020](https://www.trendmicro.com/en_us/research/20/i/analysis-of-a-convoluted-attack-chain-involving-ngrok.html)
 [^31]: [Cyware Ngrok May 2019](https://cyware.com/news/cyber-attackers-leverage-tunneling-service-to-drop-lokibot-onto-victims-systems-6f610e44)
 [^32]: [FireEye Maze May 2020](https://www.fireeye.com/blog/threat-research/2020/05/tactics-techniques-procedures-associated-with-maze-ransomware-incidents.html)
 [^33]: [MalwareBytes Ngrok February 2020](https://blog.malwarebytes.com/threat-analysis/2020/02/fraudsters-cloak-credit-card-skimmer-with-fake-content-delivery-network-ngrok-server/)
 [^34]: [Mythc Documentation](https://docs.mythic-c2.net/)
 [^35]: [Mandiant FIN5 GrrCON Oct 2016](https://www.youtube.com/watch?v=fevGZs0EQu8)
 [^36]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)
 [^37]: [Kaspersky QakBot September 2021](https://securelist.com/qakbot-technical-analysis/103931/)
 [^38]: [Trend Micro Cyclops Blink March 2022](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)
