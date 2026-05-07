---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1115
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/collection
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1115-clipboard-data
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

Adversaries may collect data stored in the clipboard from users copying information within or between applications. <br><br>For example, on Windows adversaries can access clipboard data by using `clip.exe` or `Get-Clipboard`.[^4] [^3] [^1]  Additionally, adversaries may monitor then replace users’ clipboard with their data (e.g., [[kb/mitre/attack/techniques/T1565.002-transmitted-data-manipulation|Transmitted Data Manipulation]]).[^2] <br><br>macOS and Linux also have commands, such as `pbpaste`, to grab clipboard contents.[^5] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0004](https://attack.mitre.org/software/S0004) | TinyZBot | TinyZBot contains functionality to collect information from the clipboard.[^1]  |
| [S0044](https://attack.mitre.org/software/S0044) | JHUHUGIT | A JHUHUGIT variant accesses a screenshot saved in the clipboard and converts it to a JPG image.[^1]  |
| [S0050](https://attack.mitre.org/software/S0050) | CosmicDuke | CosmicDuke copies and exfiltrates the clipboard contents every 30 seconds.[^1]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM collects data from the clipboard.[^1] [^2]  |
| [S0170](https://attack.mitre.org/software/S0170) | Helminth | The executable version of Helminth has a module to log clipboard contents.[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can extract clipboard data from a compromised host.[^1]  |
| [[kb/mitre/attack/software/S0250-koadic\|S0250]] | Koadic | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can retrieve the current content of the user clipboard.[^1]  |
| [S0253](https://attack.mitre.org/software/S0253) | RunningRAT | RunningRAT contains code to open and copy data from the clipboard.[^1]  |
| [S0257](https://attack.mitre.org/software/S0257) | VERMIN | VERMIN collects data stored in the clipboard.[^1]  |
| [S0261](https://attack.mitre.org/software/S0261) | Catchamas | Catchamas steals data stored in the clipboard.[^1]  |
| [S0282](https://attack.mitre.org/software/S0282) | MacSpy | MacSpy can steal clipboard contents.[^1]  |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT can capture clipboard data.[^1]  |
| [S0330](https://attack.mitre.org/software/S0330) | Zeus Panda | Zeus Panda can hook GetClipboardData function to watch for clipboard pastes to collect.[^1]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla can steal data from the victim’s clipboard.[^1] [^2] [^3] [^4]  |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] steals and modifies data from the clipboard.[^1] [^2]  |
| [S0334](https://attack.mitre.org/software/S0334) | DarkComet | DarkComet can steal data from the clipboard.[^1]  |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | KONNI had a feature to steal data from the clipboard.[^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can harvest clipboard data on both Windows and macOS systems.[^1]  |
| [S0373](https://attack.mitre.org/software/S0373) | Astaroth | Astaroth collects information from the clipboard by using the OpenClipboard() and GetClipboardData() libraries. [^1]  |
| [S0375](https://attack.mitre.org/software/S0375) | Remexi | Remexi collects text from the clipboard.[^1]  |
| [S0381](https://attack.mitre.org/software/S0381) | FlawedAmmyy | FlawedAmmyy can collect clipboard data.[^1]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete hijacks the clipboard data by creating an overlapped window that listens to keyboard events.[^1] [^2]   |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor has a plugin that collects data stored in the Windows clipboard by using the OpenClipboard and GetClipboardData APIs.[^1]  |
| [S0454](https://attack.mitre.org/software/S0454) | Cadelspy | Cadelspy has the ability to steal data from the clipboard.[^1]  |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo has a function to hijack data from the clipboard by monitoring the contents of the clipboard and replacing the cryptocurrency wallet with the attacker's.[^1] [^2]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to steal data from the clipboard of an infected host.[^1] <br> |
| [S0530](https://attack.mitre.org/software/S0530) | Melcoz | Melcoz can monitor content saved to the clipboard.[^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can capture clipboard data from a compromised host.[^1]  |
| [S0569](https://attack.mitre.org/software/S0569) | Explosive | Explosive has a function to use the OpenClipboard wrapper.[^1]   |
| [S0652](https://attack.mitre.org/software/S0652) | MarkiRAT | MarkiRAT can capture clipboard content.[^1]  |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling has the ability to capture and store clipboard data.[^1] [^2]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can monitor Clipboard text and can use `System.Windows.Forms.Clipboard.GetText()` to collect data from the clipboard.[^1]    |
| [S1066](https://attack.mitre.org/software/S1066) | DarkTortilla | DarkTortilla can download a clipboard information stealer module.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate starts a thread on execution that captures clipboard data and logs it to a predefined log file.[^1] [^2]  |
| [S1122](https://attack.mitre.org/software/S1122) | Mispadu | Mispadu has the ability to capture and replace Bitcoin wallet data in the clipboard on a compromised host.[^1]  |
| [S1146](https://attack.mitre.org/software/S1146) | MgBot | MgBot can capture clipboard data.[^1] [^2]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP can capture content from the clipboard.[^1]  |
| [S1207](https://attack.mitre.org/software/S1207) | XLoader | XLoader can collect data stored in the victim's clipboard.[^2] [^1]  |
| [S1226](https://attack.mitre.org/software/S1226) | BOOKWORM | BOOKWORM has used its KBLogger.dll module to steal data saved to the clipboard. [^1]  |
| [S1233](https://attack.mitre.org/software/S1233) | PAKLOG | PAKLOG has monitored and extracted clipboard contents.[^1]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has stolen data from the clipboard using the Python project “pyperclip”.[^1] [^2] [^4]  InvisibleFerret has also captured clipboard contents during copy and paste operations.[^3]  |

 [^1]: [CISA_AA21_200B](https://www.cisa.gov/uscert/ncas/alerts/aa21-200b)
 [^2]: [mining_ruby_reversinglabs](https://blog.reversinglabs.com/blog/mining-for-malicious-ruby-gems)
 [^3]: [clip_win_server](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/clip)
 [^4]: [MSDN Clipboard](https://msdn.microsoft.com/en-us/library/ms649012)
 [^5]: [Operating with EmPyre](https://medium.com/rvrsh3ll/operating-with-empyre-ea764eda3363)
 [^6]: [Talos Agent Tesla Oct 2018](https://blog.talosintelligence.com/2018/10/old-dog-new-tricks-analysing-new-rtf_15.html)
 [^7]: [Fortinet Agent Tesla April 2018](https://www.fortinet.com/blog/threat-research/analysis-of-new-agent-tesla-spyware-variant.html)
 [^8]: [Fortinet Agent Tesla June 2017](https://www.fortinet.com/blog/threat-research/in-depth-analysis-of-net-malware-javaupdtr.html)
 [^9]: [Bitdefender Agent Tesla April 2020](https://labs.bitdefender.com/2020/04/oil-gas-spearphishing-campaigns-drop-agent-tesla-spyware-in-advance-of-historic-opec-deal/)
 [^10]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
 [^11]: [Unit42 Redaman January 2019](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
 [^12]: [Github_SILENTTRINITY](https://github.com/byt3bl33d3r/SILENTTRINITY)
 [^13]: [Malwarebytes DarkComet March 2018](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
 [^14]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
 [^15]: [Cylance Cleaver](https://web.archive.org/web/20200302085133/https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance_Operation_Cleaver_Report.pdf)
 [^16]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^17]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^18]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)
 [^19]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^20]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
 [^21]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^22]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
 [^23]: [Securelist Remexi Jan 2019](https://securelist.com/chafer-used-remexi-malware/89538/)
 [^24]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)
 [^25]: [Symantec Chafer Dec 2015](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)
 [^26]: [Zscaler PAKLOG CorkLog SplatCloak Splatdropper April 2025](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
 [^27]: [Github Koadic](https://github.com/offsecginger/koadic)
 [^28]: [F-Secure Cosmicduke](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)
 [^29]: [Netskope XLoader 2022](https://www.netskope.com/blog/new-formbook-campaign-delivered-through-phishing-emails)
 [^30]: [Google XLoader 2017](https://cloud.google.com/blog/topics/threat-intelligence/formbook-malware-distribution-campaigns/)
 [^31]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^32]: [Talent-Jump Clambling February 2020](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)
 [^33]: [Secureworks DarkTortilla Aug 2022](https://www.secureworks.com/research/darktortilla-malware-analysis)
 [^34]: [Fortinet Metamorfo Feb 2020](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)
 [^35]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
 [^36]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^37]: [Securelist Machete Aug 2014](https://securelist.com/el-machete/66108/)
 [^38]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)
 [^39]: [Volexity InkySquid RokRAT August 2021](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)
 [^40]: [ESET EvasivePanda 2023](https://www.welivesecurity.com/2023/04/26/evasive-panda-apt-group-malware-updates-popular-chinese-software/)
 [^41]: [Symantec Daggerfly 2023](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
 [^42]: [IBM Grandoreiro April 2020](https://securityintelligence.com/posts/grandoreiro-malware-now-targeting-banks-in-spain/)
 [^43]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)
 [^44]: [Symantec Catchamas April 2018](https://web.archive.org/web/20190508165711/https://www-west.symantec.com/content/symantec/english/en/security-center/writeup.html/2018-040209-1742-99)
 [^45]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
 [^46]: [CheckPoint Volatile Cedar March 2015](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)
 [^47]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^48]: [Rapid7 BlackBasta 2024](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
 [^49]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
 [^50]: [Securelist Brazilian Banking Malware July 2020](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)
 [^51]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
 [^52]: [ESET Security Mispadu Facebook Ads 2019](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)
 [^53]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
 [^54]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
 [^55]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^56]: [Zscaler ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
 [^57]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^58]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
 [^59]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^60]: [Unit42 Bookworm Nov2015](https://unit42.paloaltonetworks.com/bookworm-trojan-a-model-of-modular-architecture/)
