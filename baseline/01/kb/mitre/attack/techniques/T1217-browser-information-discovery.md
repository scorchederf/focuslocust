---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1217
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1217-browser-information-discovery
tactic:
    - Discovery
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may enumerate information about browsers to learn more about compromised environments. Data saved by browsers (such as bookmarks, accounts, and browsing history) may reveal a variety of personal information about users (e.g., banking sites, relationships/interests, social media, etc.) as well as details about internal network resources such as servers, tools/dashboards, or other related infrastructure.[^2] <br><br>Browser information may also highlight additional targets after an adversary has access to valid credentials, especially [[kb/mitre/attack/techniques/T1552.001-credentials-in-files|Credentials In Files]] associated with logins cached by a browser.<br><br>Specific storage locations vary based on platform and/or application, but browser information is typically stored in local files and databases (e.g., `%APPDATA%/Google/Chrome`).[^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0079](https://attack.mitre.org/software/S0079) | MobileOrder | MobileOrder has a command to upload to its C2 server victim browser bookmarks.[^1]  |
| [S0274](https://attack.mitre.org/software/S0274) | Calisto | Calisto collects information on bookmarks from Google Chrome.[^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] has the ability to gather browser data such as bookmarks and visited sites.[^1]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete retrieves the user profile data (e.g., browsers) from Chrome and Firefox browsers.[^1]   |
| [S0567](https://attack.mitre.org/software/S0567) | Dtrack | Dtrack can retrieve browser history.[^1] [^2]  |
| [S0673](https://attack.mitre.org/software/S0673) | DarkWatchman | DarkWatchman can retrieve browser history.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar can retrieve browser history and database files.[^2] [^1]   |
| [S1012](https://attack.mitre.org/software/S1012) | PowerLess | PowerLess has a browser info stealer module that can read Chrome and Edge browser database files.[^1]  |
| [S1042](https://attack.mitre.org/software/S1042) | SUGARDUMP | SUGARDUMP has collected browser bookmark and history information.[^1]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can collect the contents of the `%USERPROFILE%\AppData\Local\Google\Chrome\User Data\LocalState` file.[^1]   |
| [S1122](https://attack.mitre.org/software/S1122) | Mispadu | Mispadu can monitor browser activity for online banking actions and display full-screen overlay images to block user access to the intended site or present additional data fields.[^1] [^2]  |
| [S1153](https://attack.mitre.org/software/S1153) | Cuckoo Stealer | Cuckoo Stealer can collect bookmarks, cookies, and history from Safari.[^1]  |
| [S1185](https://attack.mitre.org/software/S1185) | LightSpy | To collect data on the host's Wi-Fi connection history, LightSpy reads the `/Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist` file. It also utilizes Apple's `CWWiFiClient` API to scan for nearby Wi-Fi networks and obtain data on the SSID, security type, and RSSI (signal strength) values.[^1]  |
| [S1196](https://attack.mitre.org/software/S1196) | Troll Stealer | Troll Stealer collects information from Chromium-based browsers and Firefox such as cookies, history, downloads, and extensions.[^1] [^2]  |
| [S1213](https://attack.mitre.org/software/S1213) | Lumma Stealer | Lumma Stealer has identified and gathered information from two-factor authentication extensions for multiple browsers.[^1]  |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer can collect information from browsers and browser extensions.[^1]  |
| [S1246](https://attack.mitre.org/software/S1246) | BeaverTail | BeaverTail has searched the victim device for browser extensions including those commonly associated with cryptocurrency wallets.[^1] [^2] [^3] [^4] [^5] [^6] [^7]  |
| [S9010](https://attack.mitre.org/software/S9010) | GlassWorm | GlassWorm has searched browser data for cookies, history, login databases, and cryptocurrency wallets.[^1]  |

 [^1]: [Chrome Roaming Profiles](https://support.google.com/chrome/a/answer/7349337)
 [^2]: [Kaspersky Autofill](https://www.kaspersky.com/blog/browser-data-theft/27871/)
 [^3]: [Securelist Calisto July 2018](https://securelist.com/calisto-trojan-for-macos/86543/)
 [^4]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
 [^5]: [Threatpost Lizar May 2021](https://threatpost.com/fin7-backdoor-ethical-hacking-tool/166194/)
 [^6]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^7]: [Segurança Informática URSA Sophisticated Loader 2020](https://seguranca-informatica.pt/threat-analysis-the-emergent-ursa-trojan-impacts-many-countries-using-a-sophisticated-loader/)
 [^8]: [SCILabs Malteiro 2021](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)
 [^9]: [Esentire ContagiousInterview BeaverTail InvisibleFerret November 2024](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
 [^10]: [Recorded Future Contagious Inteview BeaverTail InvisibleFerret OtterCookie February 2025](https://www.recordedfuture.com/research/inside-the-scam-north-koreas-it-worker-threat)
 [^11]: [Socket BeaverTail XORIndex HexEval Contagious Interview July 2025](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
 [^12]: [Socket HexEval BeaverTail Contagious Interview June 2025](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
 [^13]: [ESET Contagious Interview BeaverTail InvisibleFerret February 2025](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
 [^14]: [PaloAlto ContagiousInterview BeaverTail InvisibleFerret November 2023](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
 [^15]: [PaloAlto Unit42 ContagiousInterview BeaverTail InvisibileFerret October 2024](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
 [^16]: [Cybereason PowerLess February 2022](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)
 [^17]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)
 [^18]: [CyberBit Dtrack](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
 [^19]: [Prevailion DarkWatchman 2021](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
 [^20]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^21]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^22]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
 [^23]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
 [^24]: [Mandiant UNC3890 Aug 2022](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)
 [^25]: [Socket GlassWorm January 2026](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
 [^26]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
 [^27]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
 [^28]: [Scarlet Mimic Jan 2016](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)
 [^29]: [Cybereason LumaStealer Undated](https://www.cybereason.com/blog/threat-analysis-rise-of-lummastealer)
 [^30]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
