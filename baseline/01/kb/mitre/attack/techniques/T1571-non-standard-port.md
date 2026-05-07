---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1571
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
mitre-attack: kb/mitre/attack/techniques/T1571-non-standard-port
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

Adversaries may communicate using a protocol and port pairing that are typically not associated. For example, HTTPS over port 8088[^2]  or port 587[^4]  as opposed to the traditional port 443. Adversaries may make changes to the standard port used by a protocol to bypass filtering or muddle analysis/parsing of network data.<br><br>Adversaries may also make changes to victim systems to abuse non-standard ports. For example, Registry keys and other configuration settings can be used to modify protocol and port pairings.[^3] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has used random, high-number, non-standard ports to listen for subsequent actions and C2 activities.[^1]  |
| [S0021](https://attack.mitre.org/software/S0021) | Derusbi | Derusbi has used unencrypted HTTP on port 443 for C2.[^1]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM used Port 44443 for its VNC module.[^1]  |
| [S0149](https://attack.mitre.org/software/S0149) | MoonWind | MoonWind communicates over ports 80, 443, 53, and 8080 via raw sockets instead of the protocols usually associated with the ports.[^1]  |
| [S0153](https://attack.mitre.org/software/S0153) | RedLeaves | RedLeaves can use HTTP over non-standard ports, such as 995, for C2.[^1]  |
| [S0237](https://attack.mitre.org/software/S0237) | GravityRAT | GravityRAT has used HTTP over a non-standard port, such as TCP port 46769.[^1]  |
| [S0239](https://attack.mitre.org/software/S0239) | Bankshot | Bankshot binds and listens on port 1058 for HTTP traffic while also utilizing a FakeTLS method.[^1]  |
| [S0245](https://attack.mitre.org/software/S0245) | BADCALL | BADCALL communicates on ports 443 and 8000 with a FakeTLS method.[^1]  |
| [S0246](https://attack.mitre.org/software/S0246) | HARDRAIN | HARDRAIN binds and listens on port 443 with a FakeTLS method.[^1]  |
| [[kb/mitre/attack/software/S0262-quasarrat\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can use port 4782 on the compromised host for TCP callbacks.[^1]  |
| [S0263](https://attack.mitre.org/software/S0263) | TYPEFRAME | TYPEFRAME has used ports 443, 8080, and 8443 with a FakeTLS method.[^1]  |
| [S0266](https://attack.mitre.org/software/S0266) | TrickBot | Some TrickBot samples have used HTTP over ports 447 and 8082 for C2.[^4] [^3] [^1]  Newer versions of TrickBot have been known to use a custom communication protocol which sends the data unencrypted over port 443. [^2]  |
| [S0352](https://attack.mitre.org/software/S0352) | OSX_OCEANLOTUS.D | OSX_OCEANLOTUS.D has used a custom binary protocol over TCP port 443 for C2.[^1]  |
| [S0367](https://attack.mitre.org/software/S0367) | Emotet | Emotet has used HTTP over ports such as 20, 22, 443, 7080, and 50000, in addition to using ports commonly associated with HTTP/S.[^2] [^1]  |
| [S0376](https://attack.mitre.org/software/S0376) | HOPLIGHT | HOPLIGHT has connected outbound over TCP port 443 with a FakeTLS method.[^1]  |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT has used port 1177 for HTTP C2 communications.[^1]  |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell can use ports 1985 and 1986 in HTTP/S communication.[^1]  |
| [S0428](https://attack.mitre.org/software/S0428) | PoetRAT | PoetRAT used TLS to encrypt communications over port 143[^1]  |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo has communicated with hosts over raw TCP on port 9999.[^1]   |
| [S0491](https://attack.mitre.org/software/S0491) | StrongPity | <br>StrongPity has used HTTPS over port 1402 in C2 communication.[^1]  |
| [S0493](https://attack.mitre.org/software/S0493) | GoldenSpy | GoldenSpy has used HTTP over ports 9005 and 9006 for network traffic, 9002 for C2 requests, 33666 as a WebSocket, and 8090 to download files.[^1]  |
| [S0515](https://attack.mitre.org/software/S0515) | WellMail | WellMail has been observed using TCP port 25, without using SMTP, to leverage an open port for secure command and control communications.[^1] [^2]  |
| [S0574](https://attack.mitre.org/software/S0574) | BendyBear | BendyBear has used a custom RC4 and XOR encrypted protocol over port 443 for C2.[^1]  |
| [S0687](https://attack.mitre.org/software/S0687) | Cyclops Blink | Cyclops Blink can use non-standard ports for C2 not typically associated with HTTP or HTTPS traffic.[^1]  |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa has used TCP port 5633 for C2 Communication.[^1]  |
| [S1031](https://attack.mitre.org/software/S1031) | PingPull | PingPull can use HTTPS over port 8080 for C2.[^1]  |
| [S1049](https://attack.mitre.org/software/S1049) | SUGARUSH | SUGARUSH has used port 4585 for a TCP connection to its C2.[^1]  |
| [S1078](https://attack.mitre.org/software/S1078) | RotaJakiro | RotaJakiro uses a custom binary protocol over TCP port 443.[^1]  |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic has the ability to connect with actor-controlled C2 servers using a custom binary protocol over port 443.[^1]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin will communicate via HTTP over port 8080 for command and control traffic.[^1]  |
| [S1145](https://attack.mitre.org/software/S1145) | Pikabot | Pikabot uses non-standard ports, such as 2967, 2223, and others, for HTTPS command and control communication.[^1]  |
| [[kb/mitre/attack/software/S1155-covenant\|S1155]] | Covenant | [[kb/mitre/attack/software/S1155-covenant\|Covenant]] listeners and controllers can be configured to use non-standard ports.[^1]  |
| [S1211](https://attack.mitre.org/software/S1211) | Hannotog | Hannotog uses non-standard listening ports, such as UDP 5900, for command and control purposes.[^1]  |
| [S1217](https://attack.mitre.org/software/S1217) | VIRTUALPITA | VIRTUALPITA has created listeners on hard coded TCP ports such as 2233, 7475, and 18098.[^1]  |
| [S1218](https://attack.mitre.org/software/S1218) | VIRTUALPIE | VIRTUALPIE has created listeners on hard coded TCP port 546.[^1]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has been observed utilizing HTTP communications to the C2 server over ports 1224, 2245 and 8637.[^1]  |
| [S1246](https://attack.mitre.org/software/S1246) | BeaverTail | BeaverTail has communicated with C2 IP addresses over ports 1224 or 1244.[^1] [^2] [^3]  |
| [S9001](https://attack.mitre.org/software/S9001) | SystemBC | The server component of SystemBC has used various TCP ports for C2 communication.[^1]  |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm has distributed C2 using BitTorrent’s Distributed Hash Table (DHT) network to harness a decentralized command capability.[^1]  |
| [S9023](https://attack.mitre.org/software/S9023) | HiddenFace | HiddenFace's passive mode listens on TCP 47000.[^2] [^1]  |
| [S9024](https://attack.mitre.org/software/S9024) | SPAWNCHIMERA | SPAWNCHIMERA has the ability to bind on a localhost and listen on port 8300.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Properly configure firewalls and proxies to limit outgoing traffic to only necessary ports for that particular network segment. |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. |

 [^1]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^2]: [Symantec Elfin Mar 2019](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)
 [^3]: [change_rdp_port_conti](https://x.com/TheDFIRReport/status/1498657772254240768)
 [^4]: [Fortinet Agent Tesla April 2018](https://www.fortinet.com/blog/threat-research/analysis-of-new-agent-tesla-spyware-variant.html)
 [^5]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
 [^6]: [Unit 42 PingPull Jun 2022](https://unit42.paloaltonetworks.com/pingpull-gallium/)
 [^7]: [Binary Defense Emotes Wi-Fi Spreader](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
 [^8]: [Talos Emotet Jan 2019](https://blog.talosintelligence.com/2019/01/return-of-emotet.html)
 [^9]: [Koi Glassworm InvisibleCode October 2025](https://www.koi.ai/blog/glassworm-first-self-propagating-worm-using-invisible-code-hits-openvsx-marketplace)
 [^10]: [Bitdefender StrongPity June 2020](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)
 [^11]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
 [^12]: [Trustwave GoldenSpy June 2020](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)
 [^13]: [Github Covenant](https://github.com/cobbr/Covenant)
 [^14]: [Mandiant UNC3890 Aug 2022](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)
 [^15]: [JPCERT MirrorFace JUL 2024](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
 [^16]: [Trend Micro Earth Kasha NOV 2024](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
 [^17]: [RedCanary RaspberryRobin 2022](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)
 [^18]: [CISA WellMail July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)
 [^19]: [NCSC APT29 July 2020](https://www.ncsc.gov.uk/files/Advisory-APT29-targets-COVID-19-vaccine-development-V1-1.pdf)
 [^20]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
 [^21]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)
 [^22]: [Palo Alto MoonWind March 2017](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
 [^23]: [US-CERT HARDRAIN March 2018](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-F.pdf)
 [^24]: [Elastic Pikabot 2024](https://www.elastic.co/security-labs/pikabot-i-choose-you)
 [^25]: [Unit42 OceanLotus 2017](https://unit42.paloaltonetworks.com/unit42-new-improved-macos-backdoor-oceanlotus/)
 [^26]: [TrumanKroll_SYSTEMBCServer_Jan2024](https://www.kroll.com/en/publications/cyber/inside-the-systembc-malware-server)
 [^27]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
 [^28]: [Unit42 BendyBear Feb 2021](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)
 [^29]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^30]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^31]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
 [^32]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
 [^33]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
 [^34]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^35]: [Fidelis Turbo](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)
 [^36]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
 [^37]: [netlab360 rotajakiro vs oceanlotus](https://blog.netlab.360.com/rotajakiro_linux_version_of_oceanlotus/)
 [^38]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
 [^39]: [Trend Micro Totbrick Oct 2016](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/tspy_trickload.n)
 [^40]: [Bitdefender Trickbot VNC module Whitepaper 2021](https://www.bitdefender.com/files/News/CaseStudies/study/399/Bitdefender-PR-Whitepaper-Trickbot-creat5515-en-EN.pdf)
 [^41]: [Fidelis TrickBot Oct 2016](https://www.fidelissecurity.com/threatgeek/2016/10/trickbot-we-missed-you-dyre)
 [^42]: [S2 Grupo TrickBot June 2017](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
 [^43]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)
 [^44]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
 [^45]: [JPCERT SPAWNCHIMERA Ivanti February 2025](https://blogs.jpcert.or.jp/en/2025/02/spawnchimera.html)
 [^46]: [US-CERT BADCALL](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)
 [^47]: [Sygnia VelvetAnt 2024A](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)
 [^48]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
 [^49]: [US-CERT TYPEFRAME June 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)
 [^50]: [Talos GravityRAT](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
 [^51]: [US-CERT Bankshot Dec 2017](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
 [^52]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
 [^53]: [NCSC Cyclops Blink February 2022](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
