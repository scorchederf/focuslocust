---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1125
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/collection
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1125-video-capture
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

An adversary can leverage a computer's peripheral devices (e.g., integrated cameras or webcams) or applications (e.g., video call services) to capture video recordings for the purpose of gathering information. Images may also be captured from devices or applications, potentially in specified intervals, in lieu of video files.<br><br>Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture video or images. Video or image files may be written to disk and exfiltrated later. This technique differs from [[kb/mitre/attack/techniques/T1113-screen-capture|Screen Capture]] due to use of specific devices or applications for video recording rather than capturing the victim's screen.<br><br>In macOS, there are a few different malware samples that record the user's webcam such as FruitFly and Proton. [^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0021](https://attack.mitre.org/software/S0021) | Derusbi | Derusbi is capable of capturing video.[^1]  |
| [S0098](https://attack.mitre.org/software/S0098) | T9000 | T9000 uses the Skype API to record audio and video calls. It writes encrypted data to `%APPDATA%\Intel\Skype`.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson can capture webcam video on targeted systems.[^1] [^2]  |
| [S0152](https://attack.mitre.org/software/S0152) | EvilGrab | EvilGrab has the capability to capture video from a victim machine.[^1]  |
| [[kb/mitre/attack/software/S0192-pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can access a connected webcam and capture pictures.[^1]  |
| [S0234](https://attack.mitre.org/software/S0234) | Bandook | Bandook has modules that are capable of capturing video from a victim's webcam.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can remotely activate the victim’s webcam to capture content.[^1] [^2]  |
| [[kb/mitre/attack/software/S0262-quasarrat\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can perform webcam viewing.[^1] [^2]  |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar captures images from the webcam.[^1]  |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT has the capability to capture video from a webcam.[^1] [^2]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla can access the victim’s webcam and record video.[^1] [^2]  |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can access a system’s webcam and take pictures.[^1]  |
| [S0334](https://attack.mitre.org/software/S0334) | DarkComet | DarkComet can access the victim’s webcam to take pictures.[^1] [^2]  |
| [S0336](https://attack.mitre.org/software/S0336) | NanoCore | NanoCore can access the victim's webcam and capture data.[^1] [^2]  |
| [S0338](https://attack.mitre.org/software/S0338) | Cobian RAT | Cobian RAT has a feature to access the webcam on the victim’s machine.[^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can capture webcam data on Windows and macOS systems.[^1]  |
| [S0379](https://attack.mitre.org/software/S0379) | Revenge RAT | Revenge RAT has the ability to access the webcam.[^2] [^1]  |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT can access the victim's webcam.[^1] [^2]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete takes photos from the computer’s web camera.[^1] [^2] [^3]  |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell has a command to perform video device spying.[^1]   |
| [S0428](https://attack.mitre.org/software/S0428) | PoetRAT | PoetRAT has used a Python tool named Bewmac to record the webcam on compromised hosts.[^1]  |
| [[kb/mitre/attack/software/S0434-imminent-monitor\|S0434]] | Imminent Monitor | [[kb/mitre/attack/software/S0434-imminent-monitor\|Imminent Monitor]] has a remote webcam monitoring capability.[^1] [^2]  |
| [S0461](https://attack.mitre.org/software/S0461) | SDBbot | SDBbot has the ability to record video on a compromised host.[^2] [^1]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to capture webcam video.[^1]  |
| [[kb/mitre/attack/software/S0591-connectwise\|S0591]] | ConnectWise | [[kb/mitre/attack/software/S0591-connectwise\|ConnectWise]] can record video on remote hosts.[^1]  |
| [S0644](https://attack.mitre.org/software/S0644) | ObliqueRAT | ObliqueRAT can capture images from webcams on compromised hosts.[^1]  |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling can record screen content in AVI format.[^1] [^2]  |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT can access the webcam on a victim's machine.[^1] [^2]  |
| [[kb/mitre/attack/software/S1050-pcshare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-pcshare\|PcShare]] can capture camera video as part of its collection process.[^1]  |
| [[kb/mitre/attack/software/S1087-asyncrat\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can record screen content on targeted systems.[^1]  |
| [[kb/mitre/attack/software/S1209-quick-assist\|S1209]] | Quick Assist | [[kb/mitre/attack/software/S1209-quick-assist\|Quick Assist]] allows for the remote administrator to view the interactive session of the running machine, including full screen activity.[^2] [^1]  |

 [^1]: [objective-see 2017 review](https://objective-see.com/blog/blog_0x25.html)
 [^2]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^3]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^4]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)
 [^5]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^6]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^7]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^8]: [Zscaler Cobian Aug 2017](https://www.zscaler.com/blogs/research/cobian-rat-backdoored-rat)
 [^9]: [DigiTrust NanoCore Jan 2017](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)
 [^10]: [PaloAlto NanoCore Feb 2016](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)
 [^11]: [jRAT Symantec Aug 2018](https://www.symantec.com/blogs/threat-intelligence/jrat-new-anti-parsing-techniques)
 [^12]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
 [^13]: [Securelist Machete Aug 2014](https://securelist.com/el-machete/66108/)
 [^14]: [Cylance Machete Mar 2017](https://threatvector.cylance.com/en_us/home/el-machete-malware-attacks-cut-through-latam.html)
 [^15]: [360 Machete Sep 2020](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)
 [^16]: [Cofense RevengeRAT Feb 2019](https://web.archive.org/web/20200428173819/https://cofense.com/upgrades-delivery-support-infrastructure-revenge-rat-malware-bigger-threat/)
 [^17]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)
 [^18]: [TrendMicro DarkComet Sept 2014](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)
 [^19]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
 [^20]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
 [^21]: [Citizen Lab Group5](https://citizenlab.ca/2016/08/group5-syria/)
 [^22]: [DigiTrust Agent Tesla Jan 2017](https://www.digitrustgroup.com/agent-tesla-keylogger/)
 [^23]: [Talos Agent Tesla Oct 2018](https://blog.talosintelligence.com/2018/10/old-dog-new-tricks-analysing-new-rtf_15.html)
 [^24]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
 [^25]: [Imminent Unit42 Dec2019](https://unit42.paloaltonetworks.com/imminent-monitor-a-rat-down-under/)
 [^26]: [QiAnXin APT-C-36 Feb2019](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
 [^27]: [Anomali Static Kitten February 2021](https://www.anomali.com/blog/probable-iranian-cyber-actors-static-kitten-conducting-cyberespionage-campaign-targeting-uae-and-kuwait-government-agencies)
 [^28]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
 [^29]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
 [^30]: [AsyncRAT GitHub](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/blob/master/README.md)
 [^31]: [IBM TA505 April 2020](https://web.archive.org/web/20200420201624/https://securityintelligence.com/posts/ta505-continues-to-infect-networks-with-sdbbot-rat/)
 [^32]: [Proofpoint TA505 October 2019](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
 [^33]: [Microsoft Storm-1811 2024](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)
 [^34]: [Microsoft Quick Assist 2024](https://learn.microsoft.com/en-us/windows/client-management/client-tools/quick-assist)
 [^35]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)
 [^36]: [Check Point Warzone Feb 2020](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
 [^37]: [Uptycs Warzone UAC Bypass November 2020](https://www.uptycs.com/blog/warzone-rat-comes-with-uac-bypass-technique)
 [^38]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)
 [^39]: [EFF Manul Aug 2016](https://www.eff.org/files/2016/08/03/i-got-a-letter-from-the-government.pdf)
 [^40]: [Fortinet Remcos Feb 2017](https://www.fortinet.com/blog/threat-research/remcos-a-new-rat-in-the-wild-2.html)
 [^41]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^42]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^43]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
 [^44]: [Talos Oblique RAT March 2021](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
 [^45]: [Palo Alto T9000 Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
 [^46]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)
 [^47]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)
 [^48]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
