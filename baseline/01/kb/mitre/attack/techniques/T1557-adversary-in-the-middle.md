---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1557
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/collection
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1557-adversary-in-the-middle
tactic:
    - Collection
    - Credential Access
platforms:
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to position themselves between two or more networked devices using an adversary-in-the-middle (AiTM) technique to support follow-on behaviors such as [[kb/mitre/attack/techniques/T1040-network-sniffing|Network Sniffing]], [[kb/mitre/attack/techniques/T1565.002-transmitted-data-manipulation|Transmitted Data Manipulation]], or replay attacks ([[kb/mitre/attack/techniques/T1212-exploitation-for-credential-access|Exploitation for Credential Access]]). By abusing features of common networking protocols that can determine the flow of network traffic (e.g. ARP, DNS, LLMNR, etc.), adversaries may force a device to communicate through an adversary controlled system so they can collect information or perform additional actions.[^7] <br><br>For example, adversaries may manipulate victim DNS settings to enable other malicious activities such as preventing/redirecting users from accessing legitimate sites and/or pushing additional malware.[^9] [^1] [^4]  Adversaries may also manipulate DNS and leverage their position in order to intercept user credentials, including access tokens ([[kb/mitre/attack/techniques/T1528-steal-application-access-token|Steal Application Access Token]]) and session cookies ([[kb/mitre/attack/techniques/T1539-steal-web-session-cookie|Steal Web Session Cookie]]).[^2] [^5]  [[kb/mitre/attack/techniques/T1689-downgrade-attack|Downgrade Attack]]s can also be used to establish an AiTM position, such as by negotiating a less secure, deprecated, or weaker version of communication protocol (SSL/TLS) or encryption algorithm.[^6] [^3] [^8] <br><br>Adversaries may also leverage the AiTM position to attempt to monitor and/or modify traffic, such as in [[kb/mitre/attack/techniques/T1565.002-transmitted-data-manipulation|Transmitted Data Manipulation]]. Adversaries can setup a position similar to AiTM to prevent traffic from flowing to the appropriate destination, potentially to impair defenses and/or in support of a [[kb/mitre/attack/techniques/T1498-network-denial-of-service|Network Denial of Service]].

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0281](https://attack.mitre.org/software/S0281) | Dok | Dok proxies web traffic to potentially monitor and alter victim HTTP(S) traffic.[^1] [^2]  |
| [[kb/mitre/attack/software/S1131-nppspy\|S1131]] | NPPSPY | [[kb/mitre/attack/software/S1131-nppspy\|NPPSPY]] opens a new network listener for the `mpnotify.exe` process that is typically contacted by the Winlogon process in Windows. A new, alternative RPC channel is set up with a malicious DLL recording plaintext credentials entered into Winlogon, effectively intercepting and redirecting the logon information.[^1]  |
| [S1188](https://attack.mitre.org/software/S1188) | Line Runner | Line Runner intercepts HTTP requests to the victim Cisco ASA, looking for a request with a 32-character, victim dependent parameter. If that parameter matches a value in the malware, a contained payload is then written to a Lua script and executed.[^1]  |
| [[kb/mitre/attack/software/S9003-evilginx2\|S9003]] | evilginx2 | [[kb/mitre/attack/software/S9003-evilginx2\|evilginx2]] has the ability to act as an adversary-in-the-middle (AiTM) relay between a legitimate website and a phished user to capture all transmitted data including usernames, passwords, authentication tokens, and session cookies and tokens.[^4] [^3] [^2] [^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Train users to be suspicious about certificate errors. Adversaries may use their own certificates in an attempt to intercept HTTPS traffic. Certificate errors may arise when the application’s certificate does not match the one expected by the host. |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Network segmentation can be used to isolate infrastructure components that do not require broad network access. This may mitigate, or at least alleviate, the scope of AiTM activity. |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that can identify traffic patterns indicative of AiTM activity can be used to mitigate activity at the network level. |
| [[kb/mitre/attack/mitigations/M1035-limit-access-to-resource-over-network\|M1035]] | Limit Access to Resource Over Network | Limit access to network infrastructure and resources that can be used to reshape traffic or otherwise produce AiTM conditions. |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | Use network appliances and host-based security software to block network traffic that is not necessary within the environment, such as legacy protocols that may be leveraged for AiTM conditions. |
| [[kb/mitre/attack/mitigations/M1041-encrypt-sensitive-information\|M1041]] | Encrypt Sensitive Information | Ensure that all wired and/or wireless traffic is encrypted appropriately. Use best practices for authentication protocols, such as Kerberos, and ensure web traffic that may contain credentials is protected by SSL/TLS. |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Disable legacy network protocols that may be used   to intercept network traffic if applicable, especially those that are not needed within an environment. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1557.004-evil-twin\|T1557.004]] | Evil Twin |
| [[kb/mitre/attack/techniques/T1557.003-dhcp-spoofing\|T1557.003]] | DHCP Spoofing |
| [[kb/mitre/attack/techniques/T1557.001-name-resolution-poisoning-and-smb-relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay |
| [[kb/mitre/attack/techniques/T1557.002-arp-cache-poisoning\|T1557.002]] | ARP Cache Poisoning |

 [^1]: [dns_changer_trojans](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/web-attack/125/how-dns-changer-trojans-direct-users-to-threats)
 [^2]: [volexity_0day_sophos_FW](https://www.volexity.com/blog/2022/06/15/driftingcloud-zero-day-sophos-firewall-exploitation-and-an-insidious-breach/)
 [^3]: [taxonomy_downgrade_att_tls](https://arxiv.org/abs/1809.05681)
 [^4]: [ad_blocker_with_miner](https://securelist.com/ad-blocker-with-miner-included/101105/)
 [^5]: [Token tactics](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)
 [^6]: [mitm_tls_downgrade_att](https://www.praetorian.com/blog/man-in-the-middle-tls-ssl-protocol-downgrade-attack/)
 [^7]: [Rapid7 MiTM Basics](https://www.rapid7.com/fundamentals/man-in-the-middle-attacks/)
 [^8]: [tlseminar_downgrade_att](https://tlseminar.github.io/downgrade-attacks/)
 [^9]: [ttint_rat](https://blog.netlab.360.com/ttint-an-iot-remote-control-trojan-spread-through-2-0-day-vulnerabilities/)
 [^10]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)
 [^11]: [CheckPoint Dok](https://blog.checkpoint.com/2017/04/27/osx-malware-catching-wants-read-https-traffic/)
 [^12]: [Sophos Evilginx MAR 2025](https://www.sophos.com/en-us/blog/stealing-user-credentials-with-evilginx)
 [^13]: [Breakdev Evilginx 3.2 AUG 2023](https://breakdev.org/evilginx-3-2/)
 [^14]: [Breakdev Evilginx 3.0 May 2023](https://breakdev.org/evilginx-3-0-evilginx-mastery/)
 [^15]: [Evilginx 2 July 2018](https://breakdev.org/evilginx-2-next-generation-of-phishing-2fa-tokens/)
 [^16]: [Huntress NPPSPY 2022](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)
 [^17]: [Cisco ArcaneDoor 2024](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
