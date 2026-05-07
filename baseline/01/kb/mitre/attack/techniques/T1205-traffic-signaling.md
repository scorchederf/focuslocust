---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1205
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/tactic/persistence
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1205-traffic-signaling
tactic:
    - Command And Control
    - Persistence
    - Stealth
platforms:
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may use traffic signaling to hide open ports or other malicious functionality used for persistence or command and control. Traffic signaling involves the use of a magic value or sequence that must be sent to a system to trigger a special response, such as opening a closed port or executing a malicious task. This may take the form of sending a series of packets with certain characteristics before a port will be opened that the adversary can use for command and control. Usually this series of packets consists of attempted connections to a predefined sequence of closed ports (i.e. [[kb/mitre/attack/techniques/T1205.001-port-knocking|Port Knocking]]), but can involve unusual flags, specific strings, or other unique characteristics. After the sequence is completed, opening a port may be accomplished by the host-based firewall, but could also be implemented by custom software.<br><br>Adversaries may also communicate with an already open port, but the service listening on that port will only respond to commands or trigger other malicious functionality if passed the appropriate magic value(s).<br><br>The observation of the signal packets to trigger the communication can be conducted through different methods. One means, originally implemented by Cd00r [^5] , is to use the libpcap libraries to sniff for the packets in question. Another method leverages raw sockets, which enables the malware to use ports that are already open for use by other programs.<br><br>On network devices, adversaries may use crafted packets to enable [[kb/mitre/attack/techniques/T1556.004-network-device-authentication|Network Device Authentication]] for standard services offered by the device such as telnet.  Such signaling may also be used to open a closed service port such as telnet, or to trigger module modification of malware implants on the device, adding, removing, or changing malicious capabilities.  Adversaries may use crafted packets to attempt to connect to one or more (open or closed) ports, but may also attempt to connect to a router interface, broadcast, and network address IP on the same port in order to achieve their goals and objectives.[^4] [^3] [^6]   To enable this traffic signaling on embedded devices, adversaries must first achieve and leverage [[kb/mitre/attack/techniques/T1601.001-patch-system-image|Patch System Image]] due to the monolithic nature of the architecture.<br><br>Adversaries may also use the Wake-on-LAN feature to turn on powered off systems. Wake-on-LAN is a hardware feature that allows a powered down system to be powered on, or woken up, by sending a magic packet to it. Once the system is powered on, it may become a target for lateral movement.[^1] [^2] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos can intercept the first client to server packet in the 3-way TCP handshake to determine if the packet contains the correct unique value for a specific Uroburos implant. If the value does not match, the packet and the rest of the TCP session are passed to the legitimate listening application.[^1]  |
| [S0220](https://attack.mitre.org/software/S0220) | Chaos | Chaos provides a reverse shell is triggered upon receipt of a packet with a special string, sent to any port.[^1]  |
| [S0221](https://attack.mitre.org/software/S0221) | Umbreon | Umbreon provides additional access using its backdoor Espeon, providing a reverse shell upon receipt of a special packet.[^1]  |
| [S0430](https://attack.mitre.org/software/S0430) | Winnti for Linux | Winnti for Linux has used a passive listener, capable of identifying a specific magic value before executing tasking, as a secondary command and control (C2) mechanism.[^1]  |
| [S0446](https://attack.mitre.org/software/S0446) | Ryuk | Ryuk has used Wake-on-Lan to power on turned off systems for lateral movement.[^1]  |
| [S0519](https://attack.mitre.org/software/S0519) | SYNful Knock | SYNful Knock can be sent instructions via special packets to change its functionality. Code for new functionality can be included in these messages.[^1]  |
| [S0587](https://attack.mitre.org/software/S0587) | Penquin | Penquin will connect to C2 only after sniffing a "magic packet" value in TCP or UDP packets matching specific conditions.[^2] [^1]  |
| [S0641](https://attack.mitre.org/software/S0641) | Kobalos | Kobalos is triggered by an incoming TCP connection to a legitimate service from a specific source port.[^1] [^2]   |
| [S0664](https://attack.mitre.org/software/S0664) | Pandora | Pandora can identify if incoming HTTP traffic contains a token and if so it will intercept the traffic and process the received command.[^1]  |
| [S1114](https://attack.mitre.org/software/S1114) | ZIPLINE | ZIPLINE can identify a specific string in intercepted network traffic, `SSH-2.0-OpenSSH_0.3xx.`, to trigger its command functionality.[^1]  |
| [S1118](https://attack.mitre.org/software/S1118) | BUSHWALK | BUSHWALK can modify the `DSUserAgentCap.pm` Perl module on Ivanti Connect Secure VPNs and either activate or deactivate depending on the value of the user agent in incoming HTTP requests.[^1]  |
| [S1201](https://attack.mitre.org/software/S1201) | TRANSLATEXT | TRANSLATEXT has redirected clients to legitimate Gmail, Naver or Kakao pages if the clients connect with no parameters.[^1]   |
| [S1203](https://attack.mitre.org/software/S1203) | J-magic | J-magic can monitor TCP traffic for packets containing one of five different predefined parameters and will spawn a reverse shell if one of the parameters and the proper response string to a subsequent challenge is received.[^1]  |
| [S1219](https://attack.mitre.org/software/S1219) | REPTILE | The REPTILE reverse shell component can listen for a specialized packet in TCP, UDP, or ICMP for activation.[^1] [^2]  |
| [S1228](https://attack.mitre.org/software/S1228) | PUBLOAD | PUBLOAD has utilized a magic value in C2 communications and only executes in memory when response packets match specific values of 17 03 03.[^1] [^2] [^3] [^4] [^5]   PUBLOAD has also used magic bytes consisting of 46 77 4d.[^1]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has utilized a magic value in C2 communications and only executes in memory when response packets match specific values.[^1] [^2] [^3]  |
| [S9011](https://attack.mitre.org/software/S9011) | BRUSHFIRE | BRUSHFIRE has monitored inbound VPN traffic to compromised appliances until specific inbound packets contain a specific magic string/pattern instead of external beaconing.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | Mitigation of some variants of this technique could be achieved through the use of stateful firewalls, depending upon how it is implemented. |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Disable Wake-on-LAN if it is not needed within an environment. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1205.002-socket-filters\|T1205.002]] | Socket Filters |
| [[kb/mitre/attack/techniques/T1205.001-port-knocking\|T1205.001]] | Port Knocking |

 [^1]: [Bleeping Computer - Ryuk WoL](https://www.bleepingcomputer.com/news/security/ryuk-ransomware-uses-wake-on-lan-to-encrypt-offline-devices/)
 [^2]: [AMD Magic Packet](https://www.amd.com/system/files/TechDocs/20213.pdf)
 [^3]: [Mandiant - Synful Knock](https://cloud.google.com/blog/topics/threat-intelligence/synful-knock-acis/)
 [^4]: [Cisco Synful Knock Evolution](https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices)
 [^5]: [Hartrell cd00r 2002](https://www.giac.org/paper/gcih/342/handle-cd00r-invisible-backdoor/103631)
 [^6]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)
 [^7]: [Mandiant Cutting Edge January 2024](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)
 [^8]: [Mandiant Cutting Edge Part 3 February 2024](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
 [^9]: [Kaspersky Turla Penquin December 2014](https://securelist.com/the-penquin-turla-2/67962/)
 [^10]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
 [^11]: [Chronicle Winnti for Linux May 2019](https://medium.com/chronicle-blog/winnti-more-than-just-windows-and-gates-e4f03436031a)
 [^12]: [Chaos Stolen Backdoor](http://gosecure.net/2018/02/14/chaos-stolen-backdoor-rising/)
 [^13]: [Umbreon Trend Micro](https://blog.trendmicro.com/trendlabs-security-intelligence/pokemon-themed-umbreon-linux-rootkit-hits-x86-arm-systems/?_ga=2.180041126.367598458.1505420282-1759340220.1502477046)
 [^14]: [ESET Kobalos Feb 2021](https://www.welivesecurity.com/2021/02/02/kobalos-complex-linux-threat-high-performance-computing-infrastructure/)
 [^15]: [ESET Kobalos Jan 2021](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
 [^16]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
 [^17]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
 [^18]: [Mandiant Fortinet Zero Day](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
 [^19]: [Lumen J-Magic JAN 2025](https://blog.lumen.com/the-j-magic-show-magic-packets-and-where-to-find-them/)
 [^20]: [Picus Security UNC5221 Ivanti May 2025](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)
 [^21]: [CSIRT CTI MUSTANG PANDA PUBLOAD TONESHELL JAN 2024](https://csirt-cti.net/2024/01/23/stately-taurus-targets-myanmar/)
 [^22]: [IBM MUSTANG PANDA PUBLOAD CLAIMLOADER JUNE 2025](https://www.ibm.com/think/x-force/hive0154-mustang-panda-shifts-focus-tibetan-community-deploy-pubload-backdoor)
 [^23]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
 [^24]: [2022 November_TrendMicro_Earth Preta_Toneshell_Pubload](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
 [^25]: [PaloAlto MUSTANG PANDA PUBLOAD MARCH 2024](https://unit42.paloaltonetworks.com/chinese-apts-target-asean-entities/)
 [^26]: [Zscaler Kimsuky TRANSLATEXT](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)
 [^27]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^28]: [Trend Micro Mustang Panda Earth Preta Toneshell February 2025](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)
 [^29]: [Trend Micro Mustang Panda Earth Preta TONESHELL June 2023](https://www.trendmicro.com/en_us/research/23/f/behind-the-scenes-unveiling-the-hidden-workings-of-earth-preta.html)
