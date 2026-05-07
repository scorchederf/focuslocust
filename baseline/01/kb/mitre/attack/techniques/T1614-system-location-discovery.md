---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1614
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/tactic/discovery
    - attack/type/technique
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1614-system-location-discovery
tactic:
    - Discovery
platforms:
    - IaaS
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

<br>Adversaries may gather information in an attempt to calculate the geographical location of a victim host. Adversaries may use the information from [[kb/mitre/attack/techniques/T1614-system-location-discovery|System Location Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.<br><br>Adversaries may attempt to infer the location of a system using various system checks, such as time zone, keyboard layout, and/or language settings.[^4] [^6] [^1]  Windows API functions such as `GetLocaleInfoW` can also be used to determine the locale of the host.[^4]  In cloud environments, an instance's availability zone may also be discovered by accessing the instance metadata service from the instance.[^2] [^5] <br><br>Adversaries may also attempt to infer the location of a victim host using IP addressing, such as via online geolocation IP-lookup services.[^3] [^6] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has obtained the location of the victim device by leveraging `GetSystemDefaultLCID`.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson can identify the geographical location of a victim host.[^1] 	  |
| [[kb/mitre/attack/software/S0262-quasarrat\|S0262]] | QuasarRAT | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can determine the country a victim host is located in.[^1]  |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can identify the location of targeted devices.[^1]  |
| [S0461](https://attack.mitre.org/software/S0461) | SDBbot | SDBbot can collected the country code of a compromised machine.[^1]  |
| [S0481](https://attack.mitre.org/software/S0481) | Ragnar Locker | Before executing malicious code, Ragnar Locker checks the Windows API `GetLocaleInfoW` and doesn't encrypt files if it finds a former Soviet country.[^1]  |
| [S0632](https://attack.mitre.org/software/S0632) | GrimAgent | GrimAgent can identify the country code on a compromised host.[^1]  |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman can identity the OS locale of a compromised host.[^1]  |
| [S1018](https://attack.mitre.org/software/S1018) | Saint Bot | Saint Bot has conducted system locale checks to see if the compromised host is in Russia, Ukraine, Belarus, Armenia, Kazakhstan, or Moldova.[^1] [^2]  |
| [S1025](https://attack.mitre.org/software/S1025) | Amadey | Amadey does not run any tasks or install additional malware if the victim machine is based in Russia.[^1]  |
| [S1111](https://attack.mitre.org/software/S1111) | DarkGate | DarkGate queries system locale information during execution.[^1]  Later versions of DarkGate query `GetSystemDefaultLCID` for locale information to determine if the malware is executing in Russian-speaking countries.[^2]  |
| [S1124](https://attack.mitre.org/software/S1124) | SocGholish | SocGholish can use IP-based geolocation to limit infections to victims in North America, Europe, and a small number of Asian-Pacific nations.[^1]  |
| [S1138](https://attack.mitre.org/software/S1138) | Gootloader | Gootloader  can use IP geolocation to determine if the person browsing to a compromised site is within a targeted territory such as the US, Canada, Germany, and South Korea.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer collects the `Locale Name` of the infected device via `GetUserDefaultLocaleName` to determine whether the string `ru` is included, but in analyzed samples no action is taken if present.[^1]  |
| [S1153](https://attack.mitre.org/software/S1153) | Cuckoo Stealer | Cuckoo Stealer can determine the geographical location of a victim host by checking the language.[^1] <br> |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer has gathered detailed information about victims’ systems, such as IP addresses, and geolocation.[^1] [^2] [^4]  RedLine Stealer has also checked the IP from where it was being executed and leveraged an opensource geolocation IP-lookup service. [^3]  |
| [S1245](https://attack.mitre.org/software/S1245) | InvisibleFerret | InvisibleFerret has collected the internal IP address, IP geolocation information of the infected host and sends the data to a C2 server.[^2]  InvisibleFerret has also leveraged the “pay” module to obtain region name, country, city, zip code, ISP, latitude and longitude using “  |
| [S1248](https://attack.mitre.org/software/S1248) | XORIndex Loader | XORIndex Loader can identify the geographical location of a victim host.[^1]  |
| [S1249](https://attack.mitre.org/software/S1249) | HexEval Loader | HexEval Loader has a function where the C2 endpoint can identify the geographical location of a victim host based on request headers, execution environment and runtime conditions.[^1]  |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm has leveraged geofencing logic to detect whether it is operating in a Russian associated time zone to determine whether it continues to execute.[^1]  |
| [S9019](https://attack.mitre.org/software/S9019) | PureCrypter | PureCrypter can use `kernel32!GetGeoInfo` to determine system location.[^1]  |
| [S9030](https://attack.mitre.org/software/S9030) | SameCoin | SameCoin can attempt to connect to the Israel Home Front Command site, oref.org[.]il, which is only reachable from within Israel to verify the target's location.[^1]  |
| [S9031](https://attack.mitre.org/software/S9031) | AshTag | AshTag can check geolocation on targeted systems.[^1]  |
| [S9034](https://attack.mitre.org/software/S9034) | Tsundere Botnet | Tsundere Botnet has checked the victim machine’s location by obtaining the culture name of the machine.[^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1614.001-system-language-discovery\|T1614.001]] | System Language Discovery |

 [^1]: [Bleepingcomputer RAT malware 2020](https://www.bleepingcomputer.com/news/security/new-rat-malware-gets-commands-via-discord-has-ransomware-feature/)
 [^2]: [AWS Instance Identity Documents](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html)
 [^3]: [Securelist Trasparent Tribe 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^4]: [FBI Ragnar Locker 2020](https://s3.documentcloud.org/documents/20413525/fbi-flash-indicators-of-compromise-ragnar-locker-ransomware-11192020-bc.pdf)
 [^5]: [Microsoft Azure Instance Metadata 2021](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/instance-metadata-service?tabs=windows)
 [^6]: [Sophos Geolocation 2016](https://news.sophos.com/en-us/2016/05/03/location-based-ransomware-threat-research/)
 [^7]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^8]: [SentinelOne Gootloader June 2021](https://www.sentinelone.com/labs/gootloader-initial-access-as-a-service-platform-expands-its-search-for-high-value-targets/)
 [^9]: [Eset PlugX Korplug Mustang Panda March 2022](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
 [^10]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
 [^11]: [SecureListUbiedo_Tsundere_Nov2025](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)
 [^12]: [Ensilo Darkgate 2018](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
 [^13]: [Trellix Darkgate 2023](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
 [^14]: [Secureworks Gold Prelude Profile](https://www.secureworks.com/research/threat-profiles/gold-prelude)
 [^15]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
 [^16]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)
 [^17]: [Check Point Wirte NOV 2024](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
 [^18]: [Zscaler PureCrypter JUN 2022](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
 [^19]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
 [^20]: [ESET RedLine Stealer November 2024](https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/)
 [^21]: [Kroll RedLine Stealer August 2024](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)
 [^22]: [McAfee RedLine Stealer April 2024](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/redline-stealer-a-novel-approach/)
 [^23]: [Proofpoint RedLine Stealer March 2020](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
 [^24]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
 [^25]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
 [^26]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^27]: [Malwarebytes Saint Bot April 2021](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
 [^28]: [Palo Alto Unit 42 OutSteel SaintBot February 2022 ](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
 [^29]: [Group IB GrimAgent July 2021](https://www.group-ib.com/blog/grimagent/)
 [^30]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
 [^31]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^32]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^33]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
 [^34]: [BlackBerry Amadey 2020](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
 [^35]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
