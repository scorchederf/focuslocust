---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1123
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/collection
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1123-audio-capture
tactic:
    - Collection
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

An adversary can leverage a computer's peripheral devices (e.g., microphones and webcams) or applications (e.g., voice and video call services) to capture audio recordings for the purpose of listening into sensitive conversations to gather information.[^1] <br><br>Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture audio. Audio files may be written to disk and exfiltrated later.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0021](https://attack.mitre.org/software/S0021) | Derusbi | Derusbi is capable of performing audio captures.[^1]  |
| [S0098](https://attack.mitre.org/software/S0098) | T9000 | T9000 uses the Skype API to record audio and video calls. It writes encrypted data to `%APPDATA%\Intel\Skype`.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson can perform audio surveillance using microphones.[^1]  |
| [S0143](https://attack.mitre.org/software/S0143) | Flame | Flame can record audio using any existing hardware recording devices.[^1] [^2]  |
| [S0152](https://attack.mitre.org/software/S0152) | EvilGrab | EvilGrab has the capability to capture audio from a victim machine.[^1]  |
| [S0163](https://attack.mitre.org/software/S0163) | Janicab | Janicab captured audio and sent it out to a C2 server.[^1] [^2]  |
| [[kb/mitre/attack/software/S0192-pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can record sound with the microphone.[^1]  |
| [[kb/mitre/attack/software/S0194-powersploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Get-MicrophoneAudio` Exfiltration module can record system microphone audio.[^1] [^2]  |
| [S0213](https://attack.mitre.org/software/S0213) | DOGCALL | DOGCALL can capture microphone data from the victim's machine.[^1]  |
| [S0234](https://attack.mitre.org/software/S0234) | Bandook | Bandook has modules that are capable of capturing audio.[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT has an audio capture and eavesdropping module.[^1]  |
| [S0257](https://attack.mitre.org/software/S0257) | VERMIN | VERMIN can perform audio capture.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can record sound using input audio devices.[^1] [^2]  |
| [S0282](https://attack.mitre.org/software/S0282) | MacSpy | MacSpy can record the sounds from microphones on a computer.[^1]  |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT can capture microphone recordings.[^1]  |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can capture data from the system’s microphone.[^1] [^2]  |
| [S0334](https://attack.mitre.org/software/S0334) | DarkComet | DarkComet can listen in to victims' conversations through the system’s microphone.[^1] [^2]  |
| [S0336](https://attack.mitre.org/software/S0336) | NanoCore | NanoCore can capture audio feeds from the system.[^1] [^2]  |
| [S0338](https://attack.mitre.org/software/S0338) | Cobian RAT | Cobian RAT has a feature to perform voice recording on the victim’s machine.[^1]  |
| [S0339](https://attack.mitre.org/software/S0339) | Micropsia | Micropsia can perform microphone recording.[^1]  |
| [S0379](https://attack.mitre.org/software/S0379) | Revenge RAT | Revenge RAT has a plugin for microphone interception.[^2] [^1]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete captures audio from the computer’s microphone.[^1] [^2] [^3]  |
| [[kb/mitre/attack/software/S0434-imminent-monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a remote microphone monitoring capability.[^1] [^2]  |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor's has a plugin that is capable of recording audio using available input sound devices.[^1]  |
| [S0454](https://attack.mitre.org/software/S0454) | Cadelspy | Cadelspy has the ability to record audio from the compromised host.[^1]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to capture VoiceIP application audio on an infected host.[^1]  |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa has the ability to record audio.[^1]  |
| [S1090](https://attack.mitre.org/software/S1090) | NightClub | NightClub can load a module to leverage the LAME encoder and `mciSendStringW` to control and capture audio.[^1]  |
| [S1146](https://attack.mitre.org/software/S1146) | MgBot | MgBot can capture input and output audio streams from infected devices.[^1] [^2]  |
| [S1185](https://attack.mitre.org/software/S1185) | LightSpy | LightSpy uses Apple's built-in AVFoundation Framework library to capture and manage audio recordings then transform them to JSON blobs for exfiltration.[^1]  |

 [^1]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^2]: [Kaspersky Flame](https://securelist.com/the-flame-questions-and-answers-51/34344/)
 [^3]: [Kaspersky Flame Functionality](https://securelist.com/flame-bunny-frog-munch-and-beetlejuice-2/32855/)
 [^4]: [Securelist ScarCruft May 2019](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)
 [^5]: [EFF Manul Aug 2016](https://www.eff.org/files/2016/08/03/i-got-a-letter-from-the-government.pdf)
 [^6]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)
 [^7]: [PowerSploit Documentation](http://powersploit.readthedocs.io)
 [^8]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
 [^9]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^10]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)
 [^11]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
 [^12]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
 [^13]: [Symantec Chafer Dec 2015](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)
 [^14]: [DigiTrust NanoCore Jan 2017](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)
 [^15]: [PaloAlto NanoCore Feb 2016](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)
 [^16]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^17]: [Objective-See MacMa Nov 2021](https://objective-see.org/blog/blog_0x69.html)
 [^18]: [Palo Alto T9000 Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
 [^19]: [Securelist Machete Aug 2014](https://securelist.com/el-machete/66108/)
 [^20]: [Cylance Machete Mar 2017](https://threatvector.cylance.com/en_us/home/el-machete-malware-attacks-cut-through-latam.html)
 [^21]: [360 Machete Sep 2020](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)
 [^22]: [f-secure janicab](https://www.f-secure.com/weblog/archives/00002576.html)
 [^23]: [Janicab](https://web.archive.org/web/20230331162455/https://www.thesafemac.com/new-signed-malware-called-janicab/)
 [^24]: [Zscaler Cobian Aug 2017](https://www.zscaler.com/blogs/research/cobian-rat-backdoored-rat)
 [^25]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^26]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^27]: [Cofense RevengeRAT Feb 2019](https://web.archive.org/web/20200428173819/https://cofense.com/upgrades-delivery-support-infrastructure-revenge-rat-malware-bigger-threat/)
 [^28]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)
 [^29]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
 [^30]: [TrendMicro DarkComet Sept 2014](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)
 [^31]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
 [^32]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)
 [^33]: [Imminent Unit42 Dec2019](https://unit42.paloaltonetworks.com/imminent-monitor-a-rat-down-under/)
 [^34]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
 [^35]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)
 [^36]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
 [^37]: [Fortinet Remcos Feb 2017](https://www.fortinet.com/blog/threat-research/remcos-a-new-rat-in-the-wild-2.html)
 [^38]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^39]: [Radware Micropsia July 2018](https://www.radware.com/blog/security/2018/07/micropsia-malware/)
 [^40]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
 [^41]: [ESET EvasivePanda 2023](https://www.welivesecurity.com/2023/04/26/evasive-panda-apt-group-malware-updates-popular-chinese-software/)
 [^42]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
