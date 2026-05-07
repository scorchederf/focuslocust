---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1014
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1014-rootkit
tactic:
    - Stealth
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may use rootkits to hide the presence of programs, files, network connections, services, drivers, and other system components. Rootkits are programs that hide the existence of malware by intercepting/hooking and modifying operating system API calls that supply system information. [^3]  <br><br>Rootkits or rootkit enabling functionality may reside at the user or kernel level in the operating system or lower, to include a hypervisor or [[kb/mitre/attack/techniques/T1542.001-system-firmware|System Firmware]]. [^4]  Rootkits have been seen for Windows, Linux, and Mac OS X systems. [^1]  [^2] <br><br>Rootkits that reside or modify boot sectors are known as [[kb/mitre/attack/techniques/T1542.003-bootkit|Bootkit]]s and specifically target the boot process of the operating system.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0009](https://attack.mitre.org/software/S0009) | Hikit | Hikit is a [[kb/mitre/attack/techniques/T1014-rootkit\|Rootkit]] that has been used by Axiom.[^1]  [^2]   |
| [S0012](https://attack.mitre.org/software/S0012) | PoisonIvy | PoisonIvy starts a rootkit from a malicious file dropped to disk.[^1]  |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos can use its kernel module to prevent its host components from being listed by the targeted system's OS and to mediate requests between user mode and concealed components.[^2] [^1]  |
| [S0027](https://attack.mitre.org/software/S0027) | Zeroaccess | Zeroaccess is a kernel-mode rootkit.[^1]  |
| [[kb/mitre/attack/software/S0040-htran\|S0040]] | HTRAN | [[kb/mitre/attack/software/S0040-htran\|HTRAN]] can install a rootkit to hide network connections from the host OS.[^1]  |
| [S0047](https://attack.mitre.org/software/S0047) | Hacking Team UEFI Rootkit | Hacking Team UEFI Rootkit is a UEFI BIOS rootkit developed by the company Hacking Team to persist remote access software on some targeted systems.[^1]  |
| [S0135](https://attack.mitre.org/software/S0135) | HIDEDRV | HIDEDRV is a rootkit that hides certain operating system artifacts.[^1]  |
| [S0221](https://attack.mitre.org/software/S0221) | Umbreon | Umbreon hides from defenders by hooking libc function calls, hiding artifacts that would reveal its presence, such as the user account it creates to provide access and undermining strace, a tool often used to identify malware.[^1]  |
| [S0377](https://attack.mitre.org/software/S0377) | Ebury | Ebury acts as a user land rootkit using the SSH service.[^2] [^1]  |
| [S0394](https://attack.mitre.org/software/S0394) | HiddenWasp | HiddenWasp uses a rootkit to hook and implement functions on the system.[^1]  |
| [S0397](https://attack.mitre.org/software/S0397) | LoJax | LoJax is a UEFI BIOS rootkit deployed to persist remote access software on some targeted systems.[^1]  |
| [S0430](https://attack.mitre.org/software/S0430) | Winnti for Linux | Winnti for Linux has used a modified copy of the open-source userland rootkit Azazel, named libxselinux.so, to hide the malware's operations and network activity.[^1]  |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay has included a rootkit to evade defenses.[^1] 	 |
| [S0468](https://attack.mitre.org/software/S0468) | Skidmap | Skidmap is a kernel-mode rootkit that has the ability to hook system calls to hide specific files and fake network and CPU-related statistics to make the CPU load of the infected machine always appear low.[^1]  |
| [S0484](https://attack.mitre.org/software/S0484) | Carberp | Carberp has used user mode rootkit techniques to remain hidden on the system.[^1]  |
| [S0502](https://attack.mitre.org/software/S0502) | Drovorub | Drovorub has used a kernel module rootkit to hide processes, files, executables, and network artifacts from user space view.[^1]  |
| [S0572](https://attack.mitre.org/software/S0572) | Caterpillar WebShell | Caterpillar WebShell has a module to use a rootkit on a system.[^1]   |
| [S0601](https://attack.mitre.org/software/S0601) | Hildegard | Hildegard has modified /etc/ld.so.preload to overwrite readdir() and readdir64().[^1]  |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet uses a Windows rootkit to mask its binaries and other relevant files.[^1]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT can include a rootkit to hide processes, files, and startup.[^1]  |
| [S1105](https://attack.mitre.org/software/S1105) | COATHANGER | COATHANGER hooks or replaces multiple legitimate processes and other functions on victim devices.[^1]  |
| [S1186](https://attack.mitre.org/software/S1186) | Line Dancer | Line Dancer can hook both the crash dump process and the Autehntication, Authorization, and Accounting (AAA) functions on compromised machines to evade forensic analysis and authentication mechanisms.[^1]  |
| [S1219](https://attack.mitre.org/software/S1219) | REPTILE | REPTILE has the ability to hook kernel functions and modify functions data to achieve rootkit functionality such as hiding processes and network connections.[^1]  |
| [S1220](https://attack.mitre.org/software/S1220) | MEDUSA | MEDUSA is a rootkit with command execution and credential logging capabilities.[^1] <br> |

 [^1]: [CrowdStrike Linux Rootkit](https://www.crowdstrike.com/blog/http-iframe-injecting-linux-rootkit/)
 [^2]: [BlackHat Mac OSX Rootkit](http://www.blackhat.com/docs/asia-14/materials/Tsai/WP-Asia-14-Tsai-You-Cant-See-Me-A-Mac-OS-X-Rootkit-Uses-The-Tricks-You-Havent-Known-Yet.pdf)
 [^3]: [Symantec Windows Rootkits](https://www.symantec.com/avcenter/reference/windows.rootkit.overview.pdf)
 [^4]: [Wikipedia Rootkit](https://en.wikipedia.org/wiki/Rootkit)
 [^5]: [ESET Ebury May 2024](https://web-assets.esetstatic.com/wls/en/papers/white-papers/ebury-is-alive-but-unseen.pdf)
 [^6]: [ESET Ebury Oct 2017](https://www.welivesecurity.com/2017/10/30/windigo-ebury-update-2/)
 [^7]: [Prevx Carberp March 2011](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
 [^8]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^9]: [NSA/FBI Drovorub August 2020](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)
 [^10]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)
 [^11]: [ESET Sednit Part 3](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part3.pdf)
 [^12]: [Trend Micro Skidmap](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)
 [^13]: [Umbreon Trend Micro](https://blog.trendmicro.com/trendlabs-security-intelligence/pokemon-themed-umbreon-linux-rootkit-hits-x86-arm-systems/?_ga=2.180041126.367598458.1505420282-1759340220.1502477046)
 [^14]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^15]: [NCSC-NL COATHANGER Feb 2024](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)
 [^16]: [TrendMicro Hacking Team UEFI](http://blog.trendmicro.com/trendlabs-security-intelligence/hacking-team-uses-uefi-bios-rootkit-to-keep-rcs-9-agent-in-target-systems/)
 [^17]: [Intezer HiddenWasp Map 2019](https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/)
 [^18]: [Unit 42 Hildegard Malware](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
 [^19]: [Cisco ArcaneDoor 2024](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
 [^20]: [FireEye Hikit Rootkit](https://web.archive.org/web/20190216180458/https://www.fireeye.com/blog/threat-research/2012/08/hikit-rootkit-advanced-persistent-attack-techniques-part-1.html)
 [^21]: [FireEye HIKIT Rootkit Part 2](https://web.archive.org/web/20210920172620/https://www.fireeye.com/blog/threat-research/2012/08/hikit-rootkit-advanced-persistent-attack-techniques-part-2.html)
 [^22]: [Google Cloud Mandiant UNC3886 2024](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
 [^23]: [Chronicle Winnti for Linux May 2019](https://medium.com/chronicle-blog/winnti-more-than-just-windows-and-gates-e4f03436031a)
 [^24]: [Sophos ZeroAccess](https://sophosnews.files.wordpress.com/2012/04/zeroaccess2.pdf)
 [^25]: [ESET LoJax Sept 2018](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)
 [^26]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^27]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)
 [^28]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
 [^29]: [ClearSky Lebanese Cedar Jan 2021](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
 [^30]: [Symantec Darkmoon Aug 2005](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)
