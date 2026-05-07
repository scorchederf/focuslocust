---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1040
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/tactic/discovery
    - attack/type/technique
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1040-network-sniffing
tactic:
    - Credential Access
    - Discovery
platforms:
    - IaaS
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may passively sniff network traffic to capture information about an environment, including authentication material passed over the network. Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.<br><br>Data captured via this technique may include user credentials, especially those sent over an insecure, unencrypted protocol. Techniques for name service resolution poisoning, such as [[kb/mitre/attack/techniques/T1557.001-name-resolution-poisoning-and-smb-relay|Name Resolution Poisoning and SMB Relay]], can also be used to capture credentials to websites, proxies, and internal systems by redirecting traffic to an adversary.<br><br>Network sniffing may reveal configuration details, such as running services, version numbers, and other network characteristics (e.g. IP addresses, hostnames, VLAN IDs) necessary for subsequent [[kb/mitre/attack/tactics/TA0008-lateral-movement|Lateral Movement]] and/or [[kb/mitre/attack/tactics/TA0005-stealth|Stealth]] activities. Adversaries may likely also utilize network sniffing during [[kb/mitre/attack/techniques/T1557-adversary-in-the-middle|Adversary-in-the-Middle]] (AiTM) to passively gain additional knowledge about the environment.<br><br>In cloud-based environments, adversaries may still be able to use traffic mirroring services to sniff network traffic from virtual machines. For example, AWS Traffic Mirroring, GCP Packet Mirroring, and Azure vTap allow users to define specified instances to collect traffic from and specified targets to send collected traffic to.[^1] [^3] [^5]  Often, much of this traffic will be in cleartext due to the use of TLS termination at the load balancer level to reduce the strain of encrypting and decrypting traffic.[^6] [^4]  The adversary can then use exfiltration techniques such as Transfer Data to Cloud Account in order to access the sniffed traffic.[^6] <br><br>On network devices, adversaries may perform network captures using [[kb/mitre/attack/techniques/T1059.008-network-device-cli|Network Device CLI]] commands such as `monitor capture`.[^7] [^2] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0019](https://attack.mitre.org/software/S0019) | Regin | Regin appears to have functionality to sniff for credentials passed over HTTP, SMTP, and SMB.[^1]  |
| [[kb/mitre/attack/software/S0174-responder\|S0174]] | Responder | [[kb/mitre/attack/software/S0174-responder\|Responder]] captures hashes and credentials that are sent to the system after the name services have been poisoned.[^1]  |
| [[kb/mitre/attack/software/S0357-impacket\|S0357]] | Impacket | [[kb/mitre/attack/software/S0357-impacket\|Impacket]] can be used to sniff network traffic via an interface or raw socket.[^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can be used to conduct packet captures on target hosts.[^1]  |
| [S0367](https://attack.mitre.org/software/S0367) | Emotet | Emotet has been observed to hook network APIs to monitor network traffic. [^1]  |
| [[kb/mitre/attack/software/S0378-poshc2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains a module for taking packet captures on compromised hosts.[^1]  |
| [S0443](https://attack.mitre.org/software/S0443) | MESSAGETAP | MESSAGETAP uses the libpcap library to listen to all traffic and parses network protocols starting with Ethernet and IP layers. It continues parsing protocol layers including SCTP, SCCP, and TCAP and finally extracts SMS message data and routing metadata.  [^1]  |
| [S0587](https://attack.mitre.org/software/S0587) | Penquin | Penquin can sniff network traffic to look for packets matching specific conditions.[^2] [^1]  |
| [[kb/mitre/attack/software/S0590-nbtscan\|S0590]] | NBTscan | [[kb/mitre/attack/software/S0590-nbtscan\|NBTscan]] can dump and print whole packet content.[^1] [^2] 	 |
| [S0661](https://attack.mitre.org/software/S0661) | FoggyWeb | FoggyWeb can configure custom listeners to passively monitor all incoming HTTP GET and POST requests sent to the AD FS server from the intranet/internet and intercept HTTP requests that match the custom URI patterns defined by the actor.[^1]  |
| [S1154](https://attack.mitre.org/software/S1154) | VersaMem | VersaMem hooked the Catalina application filter chain `doFilter` on compromised systems to monitor all inbound requests to the local Tomcat web server, inspecting them for parameters like passwords and follow-on Java modules.[^1]  |
| [S1186](https://attack.mitre.org/software/S1186) | Line Dancer | Line Dancer can create and exfiltrate packet captures from compromised environments.[^1]  |
| [S1203](https://attack.mitre.org/software/S1203) | J-magic | J-magic has a pcap listener function that can create an Extended Berkley Packet Filter (eBPF) on designated interfaces and ports.[^1]  |
| [S1204](https://attack.mitre.org/software/S1204) | cd00r | cd00r can use the libpcap library to monitor captured packets for specifc sequences.[^1]  |
| [S1206](https://attack.mitre.org/software/S1206) | JumbledPath | JumbledPath has the ability to perform packet capture on remote devices via actor-defined jump-hosts.[^1]  |
| [S1224](https://attack.mitre.org/software/S1224) | CASTLETAP | CASTLETAP has the ability to create a raw promiscuous socket to sniff network traffic.[^1]  |
| [S9024](https://attack.mitre.org/software/S9024) | SPAWNCHIMERA | SPAWNCHIMERA has monitored and filtered network traffic on compromised edge devices, allowing legitimate traffic to pass while redirecting attacker-controlled traffic to infrastructure under adversary control. [^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | In cloud environments, ensure that users are not granted permissions to create or modify traffic mirrors unless this is explicitly required. |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Deny direct access of broadcasts and multicast sniffing, and prevent attacks such as [[kb/mitre/attack/techniques/T1557.001-name-resolution-poisoning-and-smb-relay\|Name Resolution Poisoning and SMB Relay]] |
| [[kb/mitre/attack/mitigations/M1032-multi-factor-authentication\|M1032]] | Multi-factor Authentication | Use multi-factor authentication wherever possible. |
| [[kb/mitre/attack/mitigations/M1041-encrypt-sensitive-information\|M1041]] | Encrypt Sensitive Information | Ensure that all wired and/or wireless traffic is encrypted appropriately. Use best practices for authentication protocols, such as Kerberos, and ensure web traffic that may contain credentials is protected by SSL/TLS. |

 [^1]: [AWS Traffic Mirroring](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-how-it-works.html)
 [^2]: [capture_embedded_packet_on_software](https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-embedded-packet-capture/116045-productconfig-epc-00.html)
 [^3]: [GCP Packet Mirroring](https://cloud.google.com/vpc/docs/packet-mirroring)
 [^4]: [SpecterOps AWS Traffic Mirroring](https://posts.specterops.io/through-the-looking-glass-part-1-f539ae308512)
 [^5]: [Azure Virtual Network TAP](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-tap-overview)
 [^6]: [Rhino Security Labs AWS VPC Traffic Mirroring](https://rhinosecuritylabs.com/aws/abusing-vpc-traffic-mirroring-in-aws/)
 [^7]: [US-CERT-TA18-106A](https://www.us-cert.gov/ncas/alerts/TA18-106A)
 [^8]: [Impacket Tools](https://www.secureauth.com/labs/open-source-tools/impacket)
 [^9]: [Debian nbtscan Nov 2019](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)
 [^10]: [SecTools nbtscan June 2003](https://sectools.org/tool/nbtscan/)
 [^11]: [FireEye MESSAGETAP October 2019](https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html)
 [^12]: [Cisco Salt Typhoon FEB 2025](https://blog.talosintelligence.com/salt-typhoon-analysis/)
 [^13]: [Mandiant Fortinet Zero Day](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
 [^14]: [Kaspersky Turla Penquin December 2014](https://securelist.com/the-penquin-turla-2/67962/)
 [^15]: [Leonardo Turla Penquin May 2020](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
 [^16]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
 [^17]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^18]: [GitHub Responder](https://github.com/SpiderLabs/Responder)
 [^19]: [Google UNC5221 Ivanti January 2025](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
 [^20]: [Google UNC5221 BRICKSTORM SPAWNCHIMERA April 2024](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
 [^21]: [Trend Micro Banking Malware Jan 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/new-banking-malware-uses-network-sniffing-for-data-theft/)
 [^22]: [Hartrell cd00r 2002](https://www.giac.org/paper/gcih/342/handle-cd00r-invisible-backdoor/103631)
 [^23]: [Cisco ArcaneDoor 2024](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
 [^24]: [Lumen J-Magic JAN 2025](https://blog.lumen.com/the-j-magic-show-magic-packets-and-where-to-find-them/)
 [^25]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)
 [^26]: [Lumen Versa 2024](https://blog.lumen.com/taking-the-crossroads-the-versa-director-zero-day-exploitation/)
 [^27]: [Kaspersky Regin](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070305/Kaspersky_Lab_whitepaper_Regin_platform_eng.pdf)
