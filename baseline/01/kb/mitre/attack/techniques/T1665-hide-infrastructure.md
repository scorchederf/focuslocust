---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1665
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1665-hide-infrastructure
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

Adversaries may manipulate network traffic in order to hide and evade detection of their C2 infrastructure. This can be accomplished by identifying and filtering traffic from defensive tools,[^2]  masking malicious domains to obfuscate the true destination from both automated scanning tools and security researchers,[^7] [^9] [^4]  and otherwise hiding malicious artifacts to delay discovery and prolong the effectiveness of adversary infrastructure that could otherwise be identified, blocked, or taken down entirely.<br><br>C2 networks may include the use of [[kb/mitre/attack/techniques/T1090-proxy|Proxy]] or VPNs to disguise IP addresses, which can allow adversaries to blend in with normal network traffic and bypass conditional access policies or anti-abuse protections. For example, an adversary may use a virtual private cloud to spoof their IP address to closer align with a victim's IP address ranges. This may also bypass security measures relying on geolocation of the source IP address.[^10] [^8] <br><br>Adversaries may also attempt to filter network traffic in order to evade defensive tools in numerous ways, including blocking/redirecting common incident responder or security appliance user agents.[^3] [^1]  Filtering traffic based on IP and geo-fencing may also avoid automated sandboxing or researcher activity (i.e., [[kb/mitre/attack/techniques/T1497-virtualization-sandbox-evasion|Virtualization/Sandbox Evasion]]).[^2] [^3] <br><br>Hiding C2 infrastructure may also be supported by [[kb/mitre/attack/tactics/TA0042-resource-development|Resource Development]] activities such as [[kb/mitre/attack/techniques/T1583-acquire-infrastructure|Acquire Infrastructure]] and [[kb/mitre/attack/techniques/T1584-compromise-infrastructure|Compromise Infrastructure]]. For example, using widely trusted hosting services or domains such as prominent URL shortening providers or marketing services for C2 networks may enable adversaries to present benign content that later redirects victims to malicious web pages or infrastructure once specific conditions are met.[^5] [^6] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate command and control includes hard-coded domains in the malware masquerading as legitimate services such as Akamai CDN or Amazon Web Services.[^1]  |
| [S1164](https://attack.mitre.org/software/S1164) | UPSTYLE | UPSTYLE attempts to retrieve a non-existent webpage from the command and control server resulting in hidden commands sent via resulting error messages.[^1]  |
| [S1206](https://attack.mitre.org/software/S1206) | JumbledPath | JumbledPath can use a chain of jump hosts to communicate with compromised devices to obscure actor infrastructure.[^1]  |

 [^1]: [SocGholish-update](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)
 [^2]: [TA571](https://www.proofpoint.com/us/blog/threat-insight/security-brief-ta571-delivers-icedid-forked-loader)
 [^3]: [mod_rewrite](https://bluescreenofjeff.com/2016-04-12-combatting-incident-responders-with-apache-mod_rewrite/)
 [^4]: [Browser-updates](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)
 [^5]: [StarBlizzard](https://www.microsoft.com/en-us/security/blog/2023/12/07/star-blizzard-increases-sophistication-and-evasion-in-ongoing-attacks/)
 [^6]: [QR-cofense](https://cofense.com/blog/major-energy-company-targeted-in-large-qr-code-campaign/)
 [^7]: [Schema-abuse](https://www.mandiant.com/resources/blog/url-obfuscation-schema-abuse)
 [^8]: [Orange Residential Proxies](https://www.orangecyberdefense.com/global/blog/research/residential-proxies)
 [^9]: [Facad1ng](https://github.com/spyboy-productions/Facad1ng)
 [^10]: [sysdig](https://sysdig.com/content/c/pf-2023-global-cloud-threat-report?x=u_WFRi&xs=524303#page=1)
 [^11]: [Cisco Salt Typhoon FEB 2025](https://blog.talosintelligence.com/salt-typhoon-analysis/)
 [^12]: [Trellix Darkgate 2023](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
 [^13]: [Volexity UPSTYLE 2024](https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/)
