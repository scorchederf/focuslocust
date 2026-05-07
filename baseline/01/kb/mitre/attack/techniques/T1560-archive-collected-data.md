---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1560
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/collection
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1560-archive-collected-data
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

An adversary may compress and/or encrypt data that is collected prior to exfiltration. Compressing the data can help to obfuscate the collected data and minimize the amount of data sent over the network.[^1]  Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less conspicuous upon inspection by a defender.<br><br>Both compression and encryption are done prior to exfiltration, and can be performed using a utility, 3rd party library, or custom method.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0010](https://attack.mitre.org/software/S0010) | Lurid | Lurid can compress data before sending it.[^1]  |
| [S0045](https://attack.mitre.org/software/S0045) | ADVSTORESHELL | ADVSTORESHELL encrypts with the 3DES algorithm and a hardcoded key prior to exfiltration.[^1]  |
| [S0091](https://attack.mitre.org/software/S0091) | Epic | Epic encrypts collected data using a public key framework before sending it over the C2 channel.[^1]  Some variants encrypt the collected data with AES and encode it with base64 before transmitting it to the C2 server.[^2]  |
| [S0093](https://attack.mitre.org/software/S0093) | Backdoor.Oldrea | Backdoor.Oldrea writes collected data to a temporary file in an encrypted form before exfiltration to a C2 server.[^1]  |
| [S0113](https://attack.mitre.org/software/S0113) | Prikormka | After collecting documents from removable media, Prikormka compresses the collected files, and encrypts it with Blowfish.[^1]  |
| [S0187](https://attack.mitre.org/software/S0187) | Daserf | Daserf hides collected data in password-protected .rar archives.[^1]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE has the ability to compress archived screenshots.[^1]  |
| [S0249](https://attack.mitre.org/software/S0249) | Gold Dragon | Gold Dragon encrypts data using Base64 before being sent to the command and control server.[^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | Zebrocy  has used a method similar to RC4 as well as AES for encryption and hexadecimal for encoding data before exfiltration. [^1] [^2] [^3]   |
| [S0253](https://attack.mitre.org/software/S0253) | RunningRAT | RunningRAT contains code to compress files.[^1]  |
| [S0257](https://attack.mitre.org/software/S0257) | VERMIN | VERMIN encrypts the collected files using 3-DES.[^1]  |
| [S0267](https://attack.mitre.org/software/S0267) | FELIXROOT | FELIXROOT encrypts collected data with AES and Base64 and then sends it to the C2 server.[^1]  |
| [S0279](https://attack.mitre.org/software/S0279) | Proton | Proton zips up files before exfiltrating them.[^1]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla can encrypt data with 3DES before sending it over to a C2 server.[^1]  |
| [S0343](https://attack.mitre.org/software/S0343) | Exaramel for Windows | Exaramel for Windows automatically encrypts files before sending them to the C2 server.[^1]   |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | KONNI has encrypted data and files prior to exfiltration.[^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] can ZIP directories on the target system.[^1]  |
| [S0375](https://attack.mitre.org/software/S0375) | Remexi | Remexi encrypts and adds all gathered browser data into files for upload to C2.[^1]  |
| [S0395](https://attack.mitre.org/software/S0395) | LightNeuron | LightNeuron contains a function to encrypt and store emails that it collects.[^1]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete stores zipped files with profile data from installed web browsers.[^1]   |
| [[kb/mitre/attack/software/S0445-shimratreporter\|S0445]] | ShimRatReporter | [[kb/mitre/attack/software/S0445-shimratreporter\|ShimRatReporter]] used LZ compression to compress initial reconnaissance reports before sending to the C2.[^1] 	 |
| [S0454](https://attack.mitre.org/software/S0454) | Cadelspy | Cadelspy has the ability to compress stolen data into a .cab file.[^1]  |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has used ZIP to compress data gathered on a compromised host.[^1]  |
| [S0487](https://attack.mitre.org/software/S0487) | Kessel | Kessel can RC4-encrypt credentials before sending to the C2.[^1] 	 |
| [S0515](https://attack.mitre.org/software/S0515) | WellMail | WellMail can archive files on the compromised host.[^1]  |
| [S0517](https://attack.mitre.org/software/S0517) | Pillowmint | Pillowmint has encrypted stolen credit card information with AES and further encoded it with Base64.[^1] 	 |
| [[kb/mitre/attack/software/S0521-bloodhound\|S0521]] | BloodHound | [[kb/mitre/attack/software/S0521-bloodhound\|BloodHound]] can compress data collected by its SharpHound ingestor into a ZIP file to be written to disk.[^2] [^1]  |
| [S0567](https://attack.mitre.org/software/S0567) | Dtrack | Dtrack packs collected data into a password protected archive.[^1]  |
| [S0586](https://attack.mitre.org/software/S0586) | TAINTEDSCRIBE | TAINTEDSCRIBE has used `FileReadZipSend` to compress a file and send to C2.[^1]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed has compressed collected data before exfiltration.[^1]  |
| [S0657](https://attack.mitre.org/software/S0657) | BLUELIGHT | BLUELIGHT can zip files before exfiltration.[^1]  |
| [S0658](https://attack.mitre.org/software/S0658) | XCSSET | XCSSET will compress entire `~/Desktop` folders excluding all `.git` folders, but only if the total data size is under 200MB.[^1]  |
| [S0667](https://attack.mitre.org/software/S0667) | Chrommme | Chrommme can encrypt and store on disk collected data before exfiltration.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar has encrypted data before sending it to the server.[^1]  |
| [S1012](https://attack.mitre.org/software/S1012) | PowerLess | PowerLess can encrypt browser database files prior to exfiltration.[^1]  |
| [S1039](https://attack.mitre.org/software/S1039) | Bumblebee | Bumblebee can compress data stolen from the Registry and volume shadow copies prior to exfiltration.[^1]  |
| [S1101](https://attack.mitre.org/software/S1101) | LoFiSe | LoFiSe can collect files into password-protected ZIP-archives for exfiltration.[^1]  |
| [S1140](https://attack.mitre.org/software/S1140) | Spica | Spica can archive collected documents for exfiltration.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer archives collected system information in a text f ile, `System info.txt`, prior to exfiltration.[^1]  |
| [S1196](https://attack.mitre.org/software/S1196) | Troll Stealer | Troll Stealer compresses stolen data prior to exfiltration.[^1]  |
| [S1206](https://attack.mitre.org/software/S1206) | JumbledPath | JumbledPath can compress and encrypt exfiltrated packet captures from targeted devices.[^1]  |
| [S9032](https://attack.mitre.org/software/S9032) | MuddyViper | MuddyViper has archived collected web browser data into a file named CacheDump.zip.[^1]         |
| [S9036](https://attack.mitre.org/software/S9036) | LP-Notes | LP-Notes has encrypted collected credentials using AES-CBC from the CNG API and the key ED15C8344B45DAED1E0578F8BC1A32411812C61F4CB45D89B107287DE0E09FFC<br>and the initialization vector 91A4E6F6D51DAEE773A8F00279792578.[^1]   |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | System scans can be performed to identify unauthorized archival utilities. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1560.001-archive-via-utility\|T1560.001]] | Archive via Utility |
| [[kb/mitre/attack/techniques/T1560.003-archive-via-custom-method\|T1560.003]] | Archive via Custom Method |
| [[kb/mitre/attack/techniques/T1560.002-archive-via-library\|T1560.002]] | Archive via Library |

 [^1]: [DOJ GRU Indictment Jul 2018](https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf)
 [^2]: [Wikipedia File Header Signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)
 [^3]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^4]: [ESET TeleBots Oct 2018](https://www.welivesecurity.com/2018/10/11/new-telebots-backdoor-linking-industroyer-notpetya/)
 [^5]: [CISA MAR-10288834-2.v1  TAINTEDSCRIBE MAY 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
 [^6]: [Kaspersky ToddyCat Check Logs October 2023](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
 [^7]: [Trend Micro Black Basta October 2022](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
 [^8]: [GitHub Bloodhound](https://github.com/BloodHoundAD/BloodHound)
 [^9]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
 [^10]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^11]: [Cybereason Bumblebee August 2022](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)
 [^12]: [CISA WellMail July 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)
 [^13]: [ESET_MuddyWater_Dec2025](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
 [^14]: [Symantec Chafer Dec 2015](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)
 [^15]: [Google TAG COLDRIVER January 2024](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/)
 [^16]: [ESET LightNeuron May 2019](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
 [^17]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
 [^18]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
 [^19]: [FOX-IT May 2016 Mofang](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
 [^20]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
 [^21]: [McAfee Gold Dragon](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
 [^22]: [Malwarebytes Konni Aug 2021](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
 [^23]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
 [^24]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
 [^25]: [Cybereason PowerLess February 2022](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)
 [^26]: [Kaspersky Turla](https://securelist.com/the-epic-turla-operation/65545/)
 [^27]: [Kaspersky Turla Aug 2014](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)
 [^28]: [ESET ForSSHe December 2018](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
 [^29]: [Securelist Sofacy Feb 2018](https://securelist.com/a-slice-of-2017-sofacy-activity/83930/)
 [^30]: [ESET Zebrocy Nov 2018](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
 [^31]: [CISA Zebrocy Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)
 [^32]: [Villeneuve 2011](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_dissecting-lurid-apt.pdf)
 [^33]: [KISA Operation Muzabi](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
 [^34]: [Cisco Salt Typhoon FEB 2025](https://blog.talosintelligence.com/salt-typhoon-analysis/)
 [^35]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
 [^36]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
 [^37]: [FireEye FELIXROOT July 2018](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)
 [^38]: [Securelist Remexi Jan 2019](https://securelist.com/chafer-used-remexi-malware/89538/)
 [^39]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^40]: [Talos Agent Tesla Oct 2018](https://blog.talosintelligence.com/2018/10/old-dog-new-tricks-analysing-new-rtf_15.html)
 [^41]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)
 [^42]: [Symantec Tick Apr 2016](https://www.symantec.com/connect/blogs/tick-cyberespionage-group-zeros-japan)
 [^43]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)
 [^44]: [Trustwave Pillowmint June 2020](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
 [^45]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^46]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
 [^47]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
