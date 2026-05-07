---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1119
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1119-automated-collection
tactic:
    - Collection
platforms:
    - IaaS
    - Linux
    - macOS
    - Office Suite
    - SaaS
    - Windows
permissions required:
    - none
---

## Description

Once established within a system or network, an adversary may use automated techniques for collecting internal data. Methods for performing this technique could include use of a [[kb/mitre/attack/techniques/T1059-command-and-scripting-interpreter|Command and Scripting Interpreter]] to search for and copy information fitting set criteria such as file type, location, or name at specific time intervals. <br><br>In cloud-based environments, adversaries may also use cloud APIs, data pipelines, command line interfaces, or extract, transform, and load (ETL) services to automatically collect data.[^1]  <br><br>This functionality could also be built into remote access tools. <br><br>This technique may incorporate use of other techniques such as [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery|File and Directory Discovery]] and [[kb/mitre/attack/techniques/T1570-lateral-tool-transfer|Lateral Tool Transfer]] to identify and move files, as well as [[kb/mitre/attack/techniques/T1538-cloud-service-dashboard|Cloud Service Dashboard]] and [[kb/mitre/attack/techniques/T1619-cloud-storage-object-discovery|Cloud Storage Object Discovery]] to identify resources in cloud environments.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0090](https://attack.mitre.org/software/S0090) | Rover | Rover automatically collects files from the local system and removable drives based on a predefined list of file extensions on a regular timeframe.[^1]  |
| [S0098](https://attack.mitre.org/software/S0098) | T9000 | T9000 searches removable storage devices for files with a pre-defined list of file extensions (e.g. * .doc, *.ppt, *.xls, *.docx, *.pptx, *.xlsx). Any matching files are encrypted and written to a local user directory.[^1]  |
| [S0128](https://attack.mitre.org/software/S0128) | BADNEWS | BADNEWS monitors USB devices and copies files with certain extensions to a predefined directory.[^1]  |
| [S0136](https://attack.mitre.org/software/S0136) | USBStealer | For all non-removable drives on a victim, USBStealer executes automated collection of certain files for later exfiltration.[^1]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM monitors browsing activity and automatically captures screenshots if a victim browses to a URL matching one of a list of strings.[^1] [^2]  |
| [S0170](https://attack.mitre.org/software/S0170) | Helminth | A Helminth VBScript receives a batch script to execute a set of commands in a command prompt.[^1]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE can automatically archive collected data.[^1]  |
| [S0238](https://attack.mitre.org/software/S0238) | Proxysvc | Proxysvc automatically collects data about the victim and sends it to the control server.[^1]  |
| [S0239](https://attack.mitre.org/software/S0239) | Bankshot | Bankshot recursively generates a list of files within a directory and sends them back to the control server.[^1]  |
| [S0244](https://attack.mitre.org/software/S0244) | Comnie | Comnie executes a batch script to store discovery information in %TEMP%\info.dat and then uploads the temporarily file to the remote C2 server.[^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy scans the system and automatically collects files with the following extensions: .doc, .docx, ,.xls, .xlsx, .pdf, .pptx, .rar, .zip, .jpg, .jpeg, .bmp, .tiff, .kum, .tlg, .sbx, .cr, .hse, .hsf, and .lhz.[^1] [^2]  |
| [S0257](https://attack.mitre.org/software/S0257) | VERMIN | VERMIN saves each collected file with the automatically generated format {0:dd-MM-yyyy}.txt .[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can sort and collect specific documents as well as generate a list of all files on a newly inserted drive and store them in an encrypted file.[^1] [^2]  |
| [S0339](https://attack.mitre.org/software/S0339) | Micropsia | Micropsia executes an RAR tool to recursively archive files based on a predefined list of file extensions (*.xls, *.xlsx, *.csv, *.odt, *.doc, *.docx, *.ppt, *.pptx, *.pdf, *.mdb, *.accdb, *.accde, *.txt).[^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can automatically gather the username, domain name, machine name, and other information from a compromised system.[^1]  |
| [[kb/mitre/attack/software/S0378-poshc2\|S0378]] | PoshC2 | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains a module for recursively parsing through files and directories to gather valid credit card numbers.[^1]  |
| [S0395](https://attack.mitre.org/software/S0395) | LightNeuron | LightNeuron can be configured to automatically collect files under a specified directory.[^1]  |
| [S0428](https://attack.mitre.org/software/S0428) | PoetRAT | PoetRAT used file system monitoring to track modification and enable automatic exfiltration.[^1]  |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor has automatically collected data about the compromised system.[^1]  |
| [S0443](https://attack.mitre.org/software/S0443) | MESSAGETAP | MESSAGETAP checks two files, keyword_parm.txt and parm.txt, for instructions on how to target and save data parsed and extracted from SMS message data from the network traffic. If an SMS message contained either a phone number, IMSI number, or keyword that matched the predefined list, it is saved to a CSV file for later theft by the threat actor.[^1]  |
| [[kb/mitre/attack/software/S0445-shimratreporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-shimratreporter\|ShimRatReporter]] gathered information automatically, without instruction from a C2, related to the user and host machine that is compiled into a report and sent to the operators.[^1]  |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo has automatically collected mouse clicks, continuous screenshots on the machine, and set timers to collect the contents of the clipboard and website browsing.[^1]   |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can conduct an initial scan for Microsoft Word documents on the local system, removable media, and connected network drives, before tagging and collecting them. It can continue tagging documents to collect with follow up scans.[^1] 	 |
| [S0466](https://attack.mitre.org/software/S0466) | WindTail | WindTail can identify and add files that possess specific file extensions to an array for archiving.[^1]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to index and compress files into a send queue for exfiltration.[^1]  |
| [S0476](https://attack.mitre.org/software/S0476) | Valak | Valak can download a module to search for and build a report of harvested credential data.[^1]  |
| [S0491](https://attack.mitre.org/software/S0491) | StrongPity | StrongPity has a file searcher component that can automatically collect and archive files based on a predefined list of file extensions.[^1]  |
| [S0538](https://attack.mitre.org/software/S0538) | Crutch | Crutch can automatically monitor removable drives in a loop and copy interesting files.[^1]  |
| [S0597](https://attack.mitre.org/software/S0597) | GoldFinder | GoldFinder logged and stored information related to the route or hops a packet took from a compromised machine to a hardcoded C2 server, including the target C2 URL, HTTP response/status code, HTTP response headers and values, and data received from the C2 node.[^1]    |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed has automatically collected data from USB drives, keystrokes, and screen images before exfiltration.[^1]  |
| [[kb/mitre/attack/software/S0684-roadtools\|S0684]] | ROADTools | [[kb/mitre/attack/software/S0684-roadtools\|ROADTools]] automatically gathers data from Azure AD environments using the Azure Graph API.[^1]  |
| [[kb/mitre/attack/software/S0699-mythic\|S0699]] | Mythic | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] supports scripting of file downloads from agents.[^1] 	 |
| [S1017](https://attack.mitre.org/software/S1017) | OutSteel | OutSteel can automatically scan for and collect files with specific extensions.[^1]  |
| [S1043](https://attack.mitre.org/software/S1043) | ccf32 | ccf32 can be used to automatically collect files from a compromised host.[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | FunnyDream can monitor files for changes and automatically collect them.[^1]  |
| [S1078](https://attack.mitre.org/software/S1078) | RotaJakiro | Depending on the Linux distribution, RotaJakiro executes a set of commands to collect device information and sends the collected information to the C2 server.[^1]  |
| [[kb/mitre/attack/software/S1091-pacu\|S1091]] | Pacu | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can automatically collect data, such as CloudFormation templates, EC2 user data, AWS Inspector reports, and IAM credential reports.[^1]  |
| [S1101](https://attack.mitre.org/software/S1101) | LoFiSe | LoFiSe can collect all the files from the working directory every three hours and place them into a password-protected archive for further exfiltration.[^1]  |
| [S1109](https://attack.mitre.org/software/S1109) | PACEMAKER | PACEMAKER can enter a loop to read `/proc/` entries every 2 seconds in order to read a target application's memory.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate searches for stored credentials associated with cryptocurrency wallets and notifies the command and control server when identified.[^1]  |
| [[kb/mitre/attack/software/S1131-nppspy\|S1131]] | NPPSPY | [[kb/mitre/attack/software/S1131-nppspy\|NPPSPY]] collection is automatically recorded to a specified file on the victim machine.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer collects files and directories from victim systems based on configuration data downloaded from command and control servers.[^3] [^2] [^1]  |
| [S1183](https://attack.mitre.org/software/S1183) | StrelaStealer | StrelaStealer attempts to identify and collect mail login data from Thunderbird and Outlook following execution.[^2] [^1] [^3] [^4]  |
| [S1213](https://attack.mitre.org/software/S1213) | Lumma Stealer | Lumma Stealer has automated collection of various information including cryptocurrency wallet details.[^1]  |
| [S9008](https://attack.mitre.org/software/S9008) | Shai-Hulud | Shai-Hulud has the ability to automatically collect host data, secrets, system information, and endpoints.[^1] [^2] [^3]  |
| [S9035](https://attack.mitre.org/software/S9035) | LAMEHUG | LAMEHUG can recursively copy files from targeted directories on victim hosts.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1029-remote-data-storage\|M1029]] | Remote Data Storage | Encryption and off-system storage of sensitive information may be one way to mitigate collection of files, but may not stop an adversary from acquiring the information if an intrusion persists over a long period of time and the adversary is able to discover and access the data through other means. |
| [[kb/mitre/attack/mitigations/M1041-encrypt-sensitive-information\|M1041]] | Encrypt Sensitive Information | Encryption and off-system storage of sensitive information may be one way to mitigate collection of files, but may not stop an adversary from acquiring the information if an intrusion persists over a long period of time and the adversary is able to discover and access the data through other means. Strong passwords should be used on certain encrypted documents that use them to prevent offline cracking through [[kb/mitre/attack/techniques/T1110-brute-force\|Brute Force]] techniques. |

 [^1]: [Mandiant UNC3944 SMS Phishing 2023](https://www.mandiant.com/resources/blog/unc3944-sms-phishing-sim-swapping-ransomware)
 [^2]: [Palo Alto T9000 Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
 [^3]: [Palo Alto Rover](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)
 [^4]: [Radware Micropsia July 2018](https://www.radware.com/blog/security/2018/07/micropsia-malware/)
 [^5]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^6]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^7]: [Palo Alto Comnie](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)
 [^8]: [Roadtools](https://dirkjanm.io/introducing-roadtools-and-roadrecon-azure-ad-exploration-framework/)
 [^9]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
 [^10]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)
 [^11]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
 [^12]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
 [^13]: [McAfee GhostSecret](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
 [^14]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
 [^15]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^16]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
 [^17]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
 [^18]: [Aikido Shai-Hulud September 2025](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)
 [^19]: [Netskope Shai-Hulud November 2025](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
 [^20]: [Microsoft Shai-Hulud December 2025](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/)
 [^21]: [objective-see windtail2 jan 2019](https://objective-see.com/blog/blog_0x3D.html)
 [^22]: [ESET Sednit USBStealer 2014](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)
 [^23]: [KISA Operation Muzabi](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
 [^24]: [SentinelOne Valak June 2020](https://assets.sentinelone.com/labs/sentinel-one-valak-i)
 [^25]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
 [^26]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
 [^27]: [McAfee Bankshot](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)
 [^28]: [Mandiant Pulse Secure Zero-Day April 2021](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)
 [^29]: [Bitdefender StrongPity June 2020](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)
 [^30]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^31]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^32]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
 [^33]: [Sekoia Raccoon1 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)
 [^34]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
 [^35]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
 [^36]: [Unit42 Redaman January 2019](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
 [^37]: [MSTIC NOBELIUM Mar 2021](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
 [^38]: [Splunk LAMEHUG SEP 2025](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
 [^39]: [Nov AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
 [^40]: [Mythc Documentation](https://docs.mythic-c2.net/)
 [^41]: [Cybereason LumaStealer Undated](https://www.cybereason.com/blog/threat-analysis-rise-of-lummastealer)
 [^42]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^43]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^44]: [ESET Crutch December 2020](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)
 [^45]: [Palo Alto OilRig May 2016](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)
 [^46]: [RotaJakiro 2021 netlab360 analysis](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
 [^47]: [Huntress NPPSPY 2022](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)
 [^48]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)
 [^49]: [ESET Zebrocy Nov 2018](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
 [^50]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
 [^51]: [PaloAlto StrelaStealer 2024](https://unit42.paloaltonetworks.com/strelastealer-campaign/)
 [^52]: [DCSO StrelaStealer 2022](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)
 [^53]: [Fortgale StrelaStealer 2023](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)
 [^54]: [IBM StrelaStealer 2024](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
 [^55]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
 [^56]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^57]: [FireEye MESSAGETAP October 2019](https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html)
