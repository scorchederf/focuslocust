---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1046
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/discovery
    - attack/type/technique
    - platform/containers
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1046-network-service-discovery
tactic:
    - Discovery
platforms:
    - Containers
    - IaaS
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information include port, vulnerability, and/or wordlist scans using tools that are brought onto a system.[^2]    <br><br>Within cloud environments, adversaries may attempt to discover services running on other cloud hosts. Additionally, if the cloud environment is connected to a on-premises environment, adversaries may be able to identify services running on non-cloud systems as well.<br><br>Within macOS environments, adversaries may use the native Bonjour application to discover services running on other macOS hosts within a network. The Bonjour mDNSResponder daemon automatically registers and advertises a host’s registered services on the network. For example, adversaries can use a mDNS query (such as `dns-sd -B _ssh._tcp .`) to find other systems broadcasting the ssh service.[^1] [^3] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0020](https://attack.mitre.org/software/S0020) | China Chopper | China Chopper's server component can spider authentication portals.[^1]  |
| [S0061](https://attack.mitre.org/software/S0061) | HDoor | HDoor scans to identify open ports on the victim.[^1]  |
| [S0089](https://attack.mitre.org/software/S0089) | BlackEnergy | BlackEnergy has conducted port scans on a host.[^1]  |
| [S0093](https://attack.mitre.org/software/S0093) | Backdoor.Oldrea | Backdoor.Oldrea can use a network scanning module to identify ICS-related ports.[^1]  |
| [S0117](https://attack.mitre.org/software/S0117) | XTunnel | XTunnel is capable of probing the network for open ports.[^1]  |
| [S0125](https://attack.mitre.org/software/S0125) | Remsec | Remsec has a plugin that can perform ARP scanning as well as port scanning.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can perform port scans from an infected host.[^2] [^1] [^3]  |
| [[kb/mitre/attack/software/S0192-pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] has a built-in module for port scanning.[^1]  |
| [S0233](https://attack.mitre.org/software/S0233) | MURKYTOP | MURKYTOP has the capability to scan for open ports on hosts in a connected network.[^1]  |
| [[kb/mitre/attack/software/S0250-koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can scan for open TCP ports on the target network.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can scan the network for open ports and vulnerable instances of RDP and SMB protocols.[^1]  |
| [S0341](https://attack.mitre.org/software/S0341) | Xbash | Xbash can perform port scanning of TCP and UDP ports.[^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can perform port scans from an infected host.[^1]  |
| [S0374](https://attack.mitre.org/software/S0374) | SpeakUp | SpeakUp checks for availability of specific ports on servers.[^1]  |
| [[kb/mitre/attack/software/S0378-poshc2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can perform port scans from an infected host.[^1]  |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell can launch port scans.[^2] [^1]   |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can scan for systems that are vulnerable to the EternalBlue exploit.[^1] [^2] 	 |
| [S0532](https://attack.mitre.org/software/S0532) | Lucifer | Lucifer can scan for open ports including TCP ports 135 and 1433.[^1]  |
| [S0572](https://attack.mitre.org/software/S0572) | Caterpillar WebShell | Caterpillar WebShell has a module to use a port scanner on a system.[^1]   |
| [S0583](https://attack.mitre.org/software/S0583) | Pysa | Pysa can perform network reconnaissance using the Advanced Port Scanner tool.[^1]  |
| [[kb/mitre/attack/software/S0590-nbtscan\|S0590]] | NBTscan | [[kb/mitre/attack/software/S0590-nbtscan\|NBTscan]] can be used to scan IP networks.[^1] [^2]  |
| [S0598](https://attack.mitre.org/software/S0598) | P.A.S. Webshell | P.A.S. Webshell can scan networks for open ports and listening services.[^1]  |
| [S0601](https://attack.mitre.org/software/S0601) | Hildegard | Hildegard has used masscan to look for kubelets in the internal Kubernetes network.[^1]  |
| [S0604](https://attack.mitre.org/software/S0604) | Industroyer | Industroyer uses a custom port scanner to map out a network.[^1]  |
| [S0608](https://attack.mitre.org/software/S0608) | Conficker | Conficker scans for other machines to infect.[^1]  |
| [[kb/mitre/attack/software/S0683-peirates\|S0683]] | Peirates | [[kb/mitre/attack/software/S0683-peirates\|Peirates]] can initiate a port scan against a given IP address.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can scan for open ports on a compromised machine.[^1]  |
| [S0698](https://attack.mitre.org/software/S0698) | HermeticWizard | HermeticWizard has the ability to scan ports on a compromised network.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can conduct port scanning against targeted systems.[^1]  |
| [S1073](https://attack.mitre.org/software/S1073) | Royal | Royal can scan the network interfaces of targeted systems.[^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can check for open ports on a computer by establishing a TCP connection.[^1]  |
| [[kb/mitre/attack/software/S1144-frp\|S1144]] | FRP | As part of load balancing [[kb/mitre/attack/software/S1144-frp\|FRP]] can set `healthCheck.type = "tcp"` or `healthCheck.type = "http"` to check service status on specific hosts with TCPing or an HTTP request.[^1]  |
| [S1146](https://attack.mitre.org/software/S1146) | MgBot | MgBot includes modules for performing HTTP and server service scans.[^1]  |
| [S1180](https://attack.mitre.org/software/S1180) | BlackByte Ransomware | BlackByte Ransomware identifies remote systems via active directory queries for hostnames prior to launching remote ransomware payloads.[^1]  |
| [S1185](https://attack.mitre.org/software/S1185) | LightSpy | To collect data on the host's Wi-Fi connection history, LightSpy reads the `/Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist file`.It also utilizes Apple's CWWiFiClient API to scan for nearby Wi-Fi networks and obtain data on the SSID, security type, and RSSI (signal strength) values.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Ensure proper network segmentation is followed to protect critical servers and devices. |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Use network intrusion detection/prevention systems to detect and prevent remote service scans. |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Ensure that unnecessary ports and services are closed to prevent risk of discovery and potential exploitation. |

 [^1]: [apple doco bonjour description](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Introduction.html)
 [^2]: [CISA AR21-126A FIVEHANDS May 2021](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
 [^3]: [macOS APT Activity Bradley](https://themittenmac.com/what-does-apt-activity-look-like-on-macos/)
 [^4]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)
 [^5]: [Gigamon Berserk Bear October 2021](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)
 [^6]: [ESET Industroyer](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
 [^7]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^8]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^9]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)
 [^10]: [Cybereason Royal December 2022](https://www.cybereason.com/blog/royal-ransomware-analysis)
 [^11]: [CheckPoint SpeakUp Feb 2019](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)
 [^12]: [Securelist BlackEnergy Nov 2014](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
 [^13]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
 [^14]: [Debian nbtscan Nov 2019](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)
 [^15]: [SecTools nbtscan June 2003](https://sectools.org/tool/nbtscan/)
 [^16]: [Peirates GitHub](https://github.com/inguardians/peirates)
 [^17]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
 [^18]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)
 [^19]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
 [^20]: [Github Koadic](https://github.com/offsecginger/koadic)
 [^21]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
 [^22]: [FRP GitHub](https://github.com/fatedier/frp)
 [^23]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^24]: [Trustwave BlackByte 2021](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
 [^25]: [Unit42 Xbash Sept 2018](https://researchcenter.paloaltonetworks.com/2018/09/unit42-xbash-combines-botnet-ransomware-coinmining-worm-targets-linux-windows/)
 [^26]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
 [^27]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
 [^28]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^29]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^30]: [ANSSI Sandworm January 2021](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
 [^31]: [Invincea XTunnel](https://www.invincea.com/2016/07/tunnel-of-gov-dnc-hack-and-the-russian-xtunnel/)
 [^32]: [ESET Hermetic Wizard March 2022](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
 [^33]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
 [^34]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
 [^35]: [SANS Conficker](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)
 [^36]: [Baumgartner Naikon 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
 [^37]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^38]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)
 [^39]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
 [^40]: [Unit 42 Lucifer June 2020](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
 [^41]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
 [^42]: [CERT-FR PYSA April 2020](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)
