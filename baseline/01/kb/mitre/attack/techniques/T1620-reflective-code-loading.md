---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1620
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/stealth
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1620-reflective-code-loading
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

Adversaries may reflectively load code into a process in order to conceal the execution of malicious payloads. Reflective loading involves allocating then executing payloads directly within the memory of the process, vice creating a thread or process backed by a file path on disk (e.g., [[kb/mitre/attack/techniques/T1129-shared-modules|Shared Modules]]).<br><br>Reflectively loaded payloads may be compiled binaries, anonymous files (only present in RAM), or just snubs of fileless executable code (ex: position-independent shellcode).[^8] [^2] [^7] [^1] [^3]  For example, the `Assembly.Load()` method executed by [[kb/mitre/attack/techniques/T1059.001-powershell|PowerShell]] may be abused to load raw code into the running process.[^5] <br><br>Reflective code injection is very similar to [[kb/mitre/attack/techniques/T1055-process-injection|Process Injection]] except that the “injection” loads code into the processes’ own memory instead of that of a separate process. Reflective loading may evade process-based detections since the execution of the arbitrary code may be masked within a legitimate or otherwise benign process. Reflectively loading payloads directly into memory may also avoid creating files or other artifacts on disk, while also enabling malware to keep these payloads encrypted (or otherwise obfuscated) until execution.[^7] [^1] [^6] [^4] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has loaded its payload into memory.[^1] [^2] [^3] [^4] [^5]  |
| [S0022](https://attack.mitre.org/software/S0022) | Uroburos | Uroburos has the ability to load new modules directly into memory using its `Load Modules Mem` command.[^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike's `execute-assembly` command can run a .NET executable within the memory of a sacrificial process by loading the CLR.[^1]  |
| [[kb/mitre/attack/software/S0194-powersploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] reflectively loads a Windows PE file into a process.[^1] [^2]  |
| [S0367](https://attack.mitre.org/software/S0367) | Emotet | Emotet has reflectively loaded payloads into memory.[^1]  |
| [S0447](https://attack.mitre.org/software/S0447) | Lokibot | Lokibot has reflectively loaded the decoded DLL into memory.[^1]   |
| [S0595](https://attack.mitre.org/software/S0595) | ThiefQuest | ThiefQuest uses various API functions such as `NSCreateObjectFileImageFromMemory` to load and link in-memory payloads.[^1]  |
| [S0625](https://attack.mitre.org/software/S0625) | Cuba | Cuba loaded the payload into memory using PowerShell.[^1]   |
| [S0661](https://attack.mitre.org/software/S0661) | FoggyWeb | FoggyWeb's loader has reflectively loaded .NET-based assembly/payloads into memory.[^1]  |
| [S0666](https://attack.mitre.org/software/S0666) | Gelsemium | Gelsemium can use custom shellcode to map embedded DLLs into memory.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar has used the Reflective DLL injection module from Github to inject itself into a process’s memory.[^1]   |
| [S0689](https://attack.mitre.org/software/S0689) | WhisperGate | WhisperGate's downloader can reverse its third stage file bytes and reflectively load the file as a .NET assembly.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can run a .NET executable within the memory of a sacrificial process by loading the CLR.[^1]    |
| [[kb/mitre/attack/software/S0695-donut\|S0695]] | Donut | [[kb/mitre/attack/software/S0695-donut\|Donut]] can generate code modules that enable in-memory execution of VBScript, JScript, EXE, DLL, and dotNET payloads.[^1]  |
| [S1022](https://attack.mitre.org/software/S1022) | IceApple | IceApple can use reflective code loading to load .NET assemblies into `MSExchangeOWAAppPool` on targeted Exchange servers.[^1]  |
| [S1059](https://attack.mitre.org/software/S1059) | metaMain | metaMain has reflectively loaded a DLL to read, decrypt, and load an orchestrator file.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] has used reflective loading to execute malicious DLLs.[^1]  |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can copy a large byte array of 64-bit shellcode into process memory and execute it with a call to `CreateThread`.[^1]  |
| [S1085](https://attack.mitre.org/software/S1085) | Sardonic | Sardonic has a plugin system that can load specially made DLLs into memory and execute their functions.[^1] [^2]  |
| [S1143](https://attack.mitre.org/software/S1143) | LunarLoader | LunarLoader can use reflective loading to decrypt and run malicious executables in a new thread.[^1]  |
| [S1145](https://attack.mitre.org/software/S1145) | Pikabot | Pikabot reflectively loads stored, previously encrypted components of the PE file into memory of the currently executing process to avoid writing content to disk on the executing machine.[^1]  |
| [S1213](https://attack.mitre.org/software/S1213) | Lumma Stealer | Lumma Stealer has used reflective loading techniques to load content into memory during execution.[^2] [^1]  |
| [S9001](https://attack.mitre.org/software/S9001) | SystemBC | SystemBC has downloaded a text file into memory and set the area of memory via the VirtualProtect call. Then, SystemBC has executed the file via the CreateThread call.[^1]  |
| [S9011](https://attack.mitre.org/software/S9011) | BRUSHFIRE | BRUSHFIRE has executed its commands within memory and is not saved on disk.[^1] [^2]  |
| [S9032](https://attack.mitre.org/software/S9032) | MuddyViper | MuddyViper has reflectively loaded the decrypted HackBrowserData tool in a new thread.[^1]        |
| [S9033](https://attack.mitre.org/software/S9033) | Fooder | Fooder has reflectively loaded a payload into memory.[^1]  |

 [^1]: [00sec Droppers](https://0x00sec.org/t/super-stealthy-droppers/3715)
 [^2]: [S1 Custom Shellcode Tool](https://www.sentinelone.com/blog/building-a-custom-tool-for-shellcode-analysis/)
 [^3]: [Mandiant BYOL](https://www.mandiant.com/resources/bring-your-own-land-novel-red-teaming-technique)
 [^4]: [S1 Old Rat New Tricks](https://www.sentinelone.com/blog/teaching-an-old-rat-new-tricks/)
 [^5]: [Microsoft AssemblyLoad](https://learn.microsoft.com/dotnet/api/system.reflection.assembly.load)
 [^6]: [Intezer ACBackdoor](https://intezer.com/acbackdoor-analysis-of-a-new-multiplatform-backdoor/)
 [^7]: [Stuart ELF Memory](https://magisterquis.github.io/2018/03/31/in-memory-only-elf-execution.html)
 [^8]: [Introducing Donut](https://thewover.github.io/Introducing-Donut/)
 [^9]: [Gigamon BADHATCH Jul 2019](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)
 [^10]: [RecordedFuture WhisperGate Jan 2022](https://www.recordedfuture.com/research/whispergate-malware-corrupts-computers-ukraine)
 [^11]: [Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
 [^12]: [Github_SILENTTRINITY](https://github.com/byt3bl33d3r/SILENTTRINITY)
 [^13]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)
 [^14]: [PowerSploit Documentation](http://powersploit.readthedocs.io)
 [^15]: [Talos Lokibot Jan 2021](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)
 [^16]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^17]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
 [^18]: [EclecticIQ Mustang Panda PlugX](https://blog.eclecticiq.com/mustang-panda-apt-group-uses-european-commission-themed-lure-to-deliver-plugx-malware)
 [^19]: [Google Threat Intelligence Group MUSTANG PANDA PLUGX August 2025](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)
 [^20]: [Sophos PlugX September 2022](https://www.secureworks.com/blog/bronze-president-targets-russian-speakers-with-updated-plugx)
 [^21]: [Sophos Mustang Panda PLUGX](https://www.secureworks.com/blog/bronze-president-targets-government-officials)
 [^22]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^23]: [McAfee Cuba April 2021](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
 [^24]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
 [^25]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^26]: [TrumanKroll_SYSTEMBCServer_Jan2024](https://www.kroll.com/en/publications/cyber/inside-the-systembc-malware-server)
 [^27]: [MDSec Brute Ratel August 2022](https://www.mdsec.co.uk/2022/08/part-3-how-i-met-your-beacon-brute-ratel/)
 [^28]: [CrowdStrike IceApple May 2022](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)
 [^29]: [Elastic Pikabot 2024](https://www.elastic.co/security-labs/pikabot-i-choose-you)
 [^30]: [Donut Github](https://github.com/TheWover/donut)
 [^31]: [Binary Defense Emotes Wi-Fi Spreader](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
 [^32]: [Fortinet LummaStealer 2024](https://www.fortinet.com/blog/threat-research/lumma-variant-on-youtube)
 [^33]: [Netskope LummaStealer 2025](https://www.netskope.com/blog/lumma-stealer-fake-captchas-new-techniques-to-evade-detection)
 [^34]: [SekoiaBourhis_DiceLoader_Feb2024](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)
 [^35]: [Bitdefender Sardonic Aug 2021](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
 [^36]: [Symantec FIN8 Jul 2023](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)
 [^37]: [wardle evilquest partii](https://objective-see.com/blog/blog_0x60.html)
 [^38]: [MSTIC FoggyWeb September 2021](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
 [^39]: [Google UNC5221 Ivanti April 2025](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)
 [^40]: [Picus Security UNC5221 Ivanti May 2025](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)
 [^41]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
