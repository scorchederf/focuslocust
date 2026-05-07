---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1008
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
mitre-attack: kb/mitre/attack/techniques/T1008-fallback-channels
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

Adversaries may use fallback or alternate communication channels if the primary channel is compromised or inaccessible in order to maintain reliable command and control and to avoid data transfer thresholds.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0017](https://attack.mitre.org/software/S0017) | BISCUIT | BISCUIT malware contains a secondary fallback command and control server that is contacted after the primary command and control server.[^2] [^1]  |
| [S0021](https://attack.mitre.org/software/S0021) | Derusbi | Derusbi uses a backup communication method with an HTTP beacon.[^1]  |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos can use up to 10 channels to communicate between implants.[^1]  |
| [S0023](https://attack.mitre.org/software/S0023) | CHOPSTICK | CHOPSTICK can switch to a new C2 channel if the current one is broken.[^1]  |
| [S0034](https://attack.mitre.org/software/S0034) | NETEAGLE | NETEAGLE will attempt to detect if the infected host is configured to a proxy. If so, NETEAGLE will send beacons via an HTTP POST request; otherwise it will send beacons via UDP/6000.[^1]  |
| [S0044](https://attack.mitre.org/software/S0044) | JHUHUGIT | JHUHUGIT tests if it can reach its C2 server by first attempting a direct connection, and if it fails, obtaining proxy settings and sending the connection through a proxy, and finally injecting code into a running browser if the proxy method fails.[^1]  |
| [S0051](https://attack.mitre.org/software/S0051) | MiniDuke | MiniDuke uses Google Search to identify C2 servers if its primary C2 method via Twitter is not working.[^1]  |
| [S0058](https://attack.mitre.org/software/S0058) | SslMM | SslMM has a hard-coded primary and backup C2 string.[^1]  |
| [S0059](https://attack.mitre.org/software/S0059) | WinMM | WinMM is usually configured with primary and backup domains for C2 communications.[^1]  |
| [S0062](https://attack.mitre.org/software/S0062) | DustySky | DustySky has two hard-coded domains for C2 servers; if the first does not respond, it will try the second.[^1]  |
| [S0084](https://attack.mitre.org/software/S0084) | Mis-Type | Mis-Type first attempts to use a Base64-encoded network protocol over a raw TCP socket for C2, and if that method fails, falls back to a secondary HTTP-based protocol to communicate to an alternate C2 server.[^1]  |
| [S0085](https://attack.mitre.org/software/S0085) | S-Type | S-Type primarily uses port 80 for C2, but falls back to ports 443 or 8080 if initial communication fails.[^1]  |
| [S0089](https://attack.mitre.org/software/S0089) | BlackEnergy | BlackEnergy has the capability to communicate over a backup channel via plus.google.com.[^1]  |
| [S0117](https://attack.mitre.org/software/S0117) | XTunnel | The C2 server used by XTunnel provides a port number to the victim to use as a fallback in case the connection closes on the currently used port.[^1]  |
| [S0211](https://attack.mitre.org/software/S0211) | Linfo | Linfo creates a backdoor through which remote attackers can change C2 servers.[^1]  |
| [S0236](https://attack.mitre.org/software/S0236) | Kwampirs | Kwampirs uses a large list of C2 servers that it cycles through until a successful connection is established.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole has been configured with several servers available for alternate C2 communications.[^1] [^2]  |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar can accept multiple URLs for C2 servers.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | TrickBot can use secondary C2 servers for communication after establishing connectivity and relaying victim information to primary C2 servers.[^1]  |
| [S0269](https://attack.mitre.org/software/S0269) | QUADAGENT | QUADAGENT uses multiple protocols (HTTPS, HTTP, DNS) for its C2 server as fallback channels if communication with one is unsuccessful.[^1]  |
| [S0348](https://attack.mitre.org/software/S0348) | Cardinal RAT | Cardinal RAT can communicate over multiple C2 host and port combinations.[^1]  |
| [S0376](https://attack.mitre.org/software/S0376) | HOPLIGHT | HOPLIGHT has multiple C2 channels in place in case one fails.[^1] 	 |
| [S0377](https://attack.mitre.org/software/S0377) | Ebury | Ebury has implemented a fallback mechanism to begin using a DGA when the attacker hasn't connected to the infected system for three days.[^1]  |
| [S0401](https://attack.mitre.org/software/S0401) | Exaramel for Linux | Exaramel for Linux can attempt to find a new C2 server if it receives an error.[^1]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete has sent data over HTTP if FTP failed, and has also used a fallback server.[^1]   |
| [S0444](https://attack.mitre.org/software/S0444) | ShimRat | ShimRat has used a secondary C2 location if the first was unavailable.[^1] 	 |
| [S0476](https://attack.mitre.org/software/S0476) | Valak | Valak can communicate over multiple C2 hosts.[^1]  |
| [S0495](https://attack.mitre.org/software/S0495) | RDAT | RDAT has used HTTP if DNS C2 communications were not functioning.[^1] 	 |
| [S0501](https://attack.mitre.org/software/S0501) | PipeMon | PipeMon can switch to an alternate C2 domain when a particular date has been reached.[^1]  |
| [S0504](https://attack.mitre.org/software/S0504) | Anchor | Anchor can use secondary C2 servers for communication after establishing connectivity and relaying victim information to primary C2 servers.[^1]  |
| [S0512](https://attack.mitre.org/software/S0512) | FatDuke | FatDuke has used several C2 servers per targeted organization.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar has the ability to use an alternative C2 server if the primary server fails.[^1]  |
| [S0538](https://attack.mitre.org/software/S0538) | Crutch | Crutch has used a hardcoded GitHub repository as a fallback channel.[^1]  |
| [S0586](https://attack.mitre.org/software/S0586) | TAINTEDSCRIBE | TAINTEDSCRIBE can randomly pick one of five hard-coded IP addresses for C2 communication; if one of the IP fails, it will wait 60 seconds and then try another IP address.[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet has the ability to generate new C2 domains.[^1]  |
| [S0610](https://attack.mitre.org/software/S0610) | SideTwist | SideTwist has primarily used port 443 for C2 but can use port 80 as a fallback.[^1]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed can use a second channel for C2 when the primary channel is in upload mode.[^1]  |
| [S0629](https://attack.mitre.org/software/S0629) | RainyDay | RainyDay has the ability to switch between TCP and HTTP for C2 if one method is not working.[^1]  |
| [S0666](https://attack.mitre.org/software/S0666) | Gelsemium | Gelsemium can use multiple domains and protocols in C2.[^1]  |
| [S0668](https://attack.mitre.org/software/S0668) | TinyTurla | TinyTurla can go through a list of C2 server IPs and will try to register with each until one responds.[^1]  |
| [S0674](https://attack.mitre.org/software/S0674) | CharmPower | CharmPower can change its C2 channel once every 360 loops by retrieving a new domain from the actors’ S3 bucket.[^1]  |
| [[kb/mitre/attack/software/S0699-mythic\|S0699]] | Mythic | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] can use a list of C2 URLs as fallback mechanisms in case one IP or domain gets blocked.[^1] 	 |
| [S1019](https://attack.mitre.org/software/S1019) | Shark | Shark can update its configuration to use a different C2 server.[^1]  |
| [S1020](https://attack.mitre.org/software/S1020) | Kevin | Kevin can assign hard-coded fallback domains for C2.[^1]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee can use backup C2 servers if the primary server fails.[^1]  |
| [S1084](https://attack.mitre.org/software/S1084) | QUIETEXIT | QUIETEXIT can attempt to connect to a second hard-coded C2 if the first hard-coded C2 address fails.[^1]  |
| [S1172](https://attack.mitre.org/software/S1172) | OilBooster | OilBooster can use a backup channel to request a new refresh token from its C2 server after 10 consecutive unsuccessful connections to the primary OneDrive C2 server.[^1]  |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm has utilized Google Calendar as backup C2.[^1] [^2]  |
| [S9023](https://attack.mitre.org/software/S9023) | HiddenFace | HiddenFace can use active and passive C2 modes that use different encryption algorithms and backdoor commands.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific protocol used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools. [^1]  |

 [^1]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^2]: [ESET Sednit Part 1](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part1.pdf)
 [^3]: [Symantec Linfo May 2012](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)
 [^4]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
 [^5]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
 [^6]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^7]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^8]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
 [^9]: [ESET Ebury Oct 2017](https://www.welivesecurity.com/2017/10/30/windigo-ebury-update-2/)
 [^10]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)
 [^11]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
 [^12]: [Cyberreason Anchor December 2019](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
 [^13]: [Unit 42 Valak July 2020](https://unit42.paloaltonetworks.com/valak-evolution/)
 [^14]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
 [^15]: [ESET Dukes October 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
 [^16]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
 [^17]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)
 [^18]: [ClearSky Siamesekitten August 2021](https://www.clearskysec.com/siamesekitten/)
 [^19]: [Securelist MiniDuke Feb 2013](https://web.archive.org/web/20170630181406/https://cdn.securelist.com/files/2014/07/themysteryofthepdf0-dayassemblermicrobackdoor.pdf)
 [^20]: [Proofpoint Bumblebee April 2022](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
 [^21]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
 [^22]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
 [^23]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^24]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
 [^25]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
 [^26]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
 [^27]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^28]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^29]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^30]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
 [^31]: [Check Point APT34 April 2021](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
 [^32]: [Koi Glassworm InvisibleCode October 2025](https://www.koi.ai/blog/glassworm-first-self-propagating-worm-using-invisible-code-hits-openvsx-marketplace)
 [^33]: [Koi GlassWorm Rust December 2025](https://www.koi.ai/blog/glassworm-goes-native-same-infrastructure-hardened-delivery)
 [^34]: [DustySky](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
 [^35]: [Talos TinyTurla September 2021](https://blog.talosintelligence.com/2021/09/tinyturla.html)
 [^36]: [Kaspersky Lyceum October 2021](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
 [^37]: [Fidelis Turbo](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)
 [^38]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^39]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
 [^40]: [ESET Crutch December 2020](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)
 [^41]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
 [^42]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
 [^43]: [Unit42 RDAT July 2020](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)
 [^44]: [Unit 42 QUADAGENT July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)
 [^45]: [Symantec Orangeworm April 2018](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
 [^46]: [ESET OilRig Downloaders DEC 2023](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
 [^47]: [ESET PipeMon May 2020](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
 [^48]: [Mythc Documentation](https://docs.mythic-c2.net/)
 [^49]: [Securelist BlackEnergy Nov 2014](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
